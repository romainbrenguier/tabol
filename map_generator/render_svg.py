import argparse
import math
import random

import pydantic
import yaml

def generate_fuzzy_circle(cx, cy, r, fuzz):
    """
    Generate a fuzzy circle path for SVG rendering.
    """
    points = []
    num_segments = 60  # Smoothness of the land loop
    
    for i in range(num_segments):
        angle = (i / num_segments) * 2 * math.pi
        # Apply random offset based on fuzziness factor
        offset = random.uniform(-fuzz, fuzz) if fuzz > 0 else 0
        current_r = r + offset
        
        x = cx + current_r * math.cos(angle)
        y = cy + current_r * math.sin(angle)
        points.append(f"{x:.1f},{y:.1f}")
        
    return "M " + " L ".join(points) + " Z"

def generate_square(cx, cy, r):
    """
    Generate a square path for SVG rendering.
    """
    points = [
        (cx - r, cy - r),
        (cx + r, cy - r),
        (cx + r, cy + r),
        (cx - r, cy + r)
    ]
    
    return "M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in points) + " Z"

class Region(pydantic.BaseModel):
    """
    Represents a region in the map layout.
    """
    name: str
    description: str
    position: tuple[int, int]
    area: int
    base_terrain: str

class LandFeature(pydantic.BaseModel):
    """
    Represents a land feature in the map layout.
    Integer represents percentage of the total for the map.
    """
    position: tuple[int, int]
    radius_min: int # TODO not taken into account yet, but will be used for more complex land generation
    radius_max: int
    terrain_type: str
    area: int
    label: str | None = None  # Optional label for the land
    in_region: str | None = None  # Optional region association

def distance_to_center(point: tuple[int, int], center: tuple[int, int]) -> float:
    """
    Calculate the Euclidean distance from a point to the center.
    
    Args:
        point (tuple[int, int]): The (x, y) coordinates of the point.
        center (tuple[int, int]): The (x, y) coordinates of the center.
    
    Returns:
        float: The Euclidean distance between the point and the center.
    """
    return math.sqrt((point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2)

def fill_map_with_land_features(map: list[list[str]], default_terrain: str, regions: dict[str, Region], land_features: list[LandFeature]) -> None:
    """
    Fill the map with land features based on the provided specifications.
    
    Args:
        map_width (int): Width of the map.
        map_height (int): Height of the map.
        land_features (list[LandFeature]): List of land feature specifications.
    
    Returns:
        list[dict]: List of generated land features with positions and radii.
    """
    map_height = len(map)
    map_width = len(map[0]) if map_height > 0 else 0

    for region in regions.values():
        # Calculate the region's position and size on the map
        region_width = int(math.sqrt(region.area) * min(map_width, map_height) / 100)  # Scale region size based on area percentage
        region_offset = ((region.position[0] * map_width - region_width) // 2, (region.position[1] * map_height - region_width) // 2)
        print(f"Region '{region.name}' will occupy an area of {region.area} with a width of {region_width} at offset {region_offset}.")
        # Fill the region with its base terrain
        for y in range(region_offset[1], region_offset[1] + region_width):
            for x in range(region_offset[0], region_offset[0] + region_width):
                if 0 <= x < map_width and 0 <= y < map_height:
                    map[y][x] = region.base_terrain

    borders = {str(feature): [] for feature in land_features}
    to_place = {str(feature): 0 for feature in land_features}
    first_point = {str(feature): (0, 0) for feature in land_features}

    for feature in land_features:
        # Calculate the number of features to generate based on area percentage
        region_factor = 100 if feature.in_region is None else regions[feature.in_region].area
        num_features = int(feature.area * (map_width * map_height) * region_factor / 10000)  # Adjusted for percentage of the map and region area
        region_width = 100 if feature.in_region is None else int(math.sqrt(regions[feature.in_region].area))
        region_offset = (0, 0) if feature.in_region is None else ((regions[feature.in_region].position[0] - region_width) // 2, (regions[feature.in_region].position[1] - region_width) // 2)
        first_point[str(feature)] = [(feature.position[0] * map_width + region_offset[0]) // 100, (feature.position[1] * map_height + region_offset[1]) // 100]
        borders[str(feature)] = [first_point[str(feature)]]
        to_place[str(feature)] = num_features

    while any(to_place[terrain] > 0 and len(borders[terrain]) > 0 for terrain in borders):
        # Randomly select a terrain type that still has features to place
        feature_str = random.choice([feature for feature in to_place if to_place[feature] > 0 and len(borders[feature]) > 0])
        border = borders[feature_str]
        feature = next(f for f in land_features if str(f) == feature_str)

        # Select a random point within the border and ensure it fits within the map dimensions
        on_border = random.choice(border)
        # Find adjacent points to the border point to expand the feature
        adjacent_points = [
            (on_border[0] + dx, on_border[1] + dy)
            for dx in range(-1, 2)
            for dy in range(-1, 2)
            if 0 <= on_border[0] + dx < map_width and 0 <= on_border[1] + dy < map_height
                and map[on_border[1] + dy][on_border[0] + dx] == default_terrain
                and distance_to_center((on_border[0] + dx, on_border[1] + dy), first_point[feature_str]) <= feature.radius_max
        ]
        
        if not adjacent_points:
            # remove the point from the border if no adjacent points are available
            border.remove(on_border)
            if len(border) == 0:
                print(f"No more adjacent points available for {feature}. Stopping placement. There are {to_place[feature_str]} features left to place.")
        else:
            # Randomly select an adjacent point to place the feature
            new_point = random.choice(adjacent_points)
            border.append(new_point)
            map[new_point[1]][new_point[0]] = feature.terrain_type
            to_place[feature_str] -= 1

def draw_path(start:tuple, end:tuple, map: list[list[str]], avoid: list[str]) -> list[tuple[int, int]]:
    """
    Generate a list of points making a path between two coordinates.
    """
    points = [start]
    x1, y1 = start
    x2, y2 = end

    direction = (0, 0)
    nb_attempts = 0
    while (x1 != x2 or y1 != y2) and nb_attempts < 1000:
        dx = 1 if x2 > x1 else 0 if x2 == x1 else -1
        dy = 1 if y2 > y1 else 0 if y2 == y1 else -1
        all_choices = [(dx, 0), (0, dy), (dx, dy)]
        best_choices = [choice for choice in all_choices if 0 <= x1 + choice[0] < len(map[0]) and 0 <= y1 + choice[1] < len(map) and map[y1 + choice[1]][x1 + choice[0]] not in avoid]
        new_direction = random.choice(best_choices) if best_choices else random.choice(all_choices)
        x1 += new_direction[0]
        y1 += new_direction[1]
        if new_direction != direction:
            direction = new_direction
            points.append((x1, y1))
        else:
            points[-1] = (x1, y1)  # Update the last point if continuing in the same direction
        nb_attempts += 1
    if nb_attempts >= 1000:
        print(f"Warning: Could not generate path from {start} to {end} after 1000 attempts.")
    return points

def is_adjacent_to(x: int, y: int, map: list[list[str]], terrain: list[str]) -> bool:
    if x < 0 or y < 0 or y >= len(map) or x >= len(map[0]):
        return False
    if terrain is None:
        return True
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(map[0]) and 0 <= ny < len(map):
                if map[ny][nx] in terrain:
                    return True
    return False

def place_object_on_map(obj: dict, map: list[list[str]]) -> tuple[int, int]:
    print(f"Attempting to place object {obj}.")
    pos_x, pos_y = obj["position"][0] * len(map[0]) / 100, obj["position"][1] * len(map) / 100
    if "on_terrain" in obj:
        print(f"Placing object {obj['object_type']} on terrain {obj['on_terrain']} at initial position ({pos_x}, {pos_y}).")
        nb_attempts = 0
        while (map[int(pos_y)][int(pos_x)] != obj["on_terrain"] or not is_adjacent_to(int(pos_x), int(pos_y), map, obj.get("adjacent_to"))) and nb_attempts < 100:
            pos_x = int(random.normalvariate(pos_x, 2))
            pos_y = int(random.normalvariate(pos_y, 2))
            nb_attempts += 1
        
        print(f"Object {obj['object_type']} attempted to be placed on terrain {obj['on_terrain']} at position ({pos_x}, {pos_y}) after {nb_attempts} attempts.")
        if nb_attempts >= 100:  # Prevent infinite loop
            print(f"Warning: Could not place object {obj['object_type']} on terrain {obj['on_terrain']} after 100 attempts. Placing at original position.")
    
    print(f"Object {obj['object_type']} placed at final position ({pos_x}, {pos_y}) on terrain {map[int(pos_y)][int(pos_x)]}.")
    return int(pos_x), int(pos_y)


def render_svg_from_yaml(yaml_file_path, output="map"):
    """
    Render an SVG layout from an AoE2-style YAML blueprint.
    
    Args:
        yaml_file_path (str): Path to the YAML file containing the map blueprint.
    Returns:
        str: A string containing the SVG code for the map layout.
    """
        
    # Load the blueprint
    with open(yaml_file_path, "r") as f:
        blueprint = yaml.safe_load(f)

    settings = blueprint["map_settings"]
    objects = blueprint.get("features", [])
    land = blueprint.get("land", [])
    paths = blueprint.get("paths", [])
    font_size = settings.get("font_size", 1)  # Default font size if not specified

    # Hex colors for our layout terrains
    TERRAIN_COLORS = {
        "WATER": "#3a86c8",
        "DESERT": "#e2c995",
        "GRASS": "#60a05b",
        "MOUNTAIN": "#8b8c7a",
        "FOREST": "#2e8b57",
        "ROAD": "#a0522d",
        "RIVER": "#1f78b4",
        "SWAMP": "#556b2f",
        "TUNDRA": "#d3d3d3",
    }

    w, h = settings["width"], settings["height"]

    # Initialize SVG file string with standard headers
    with open("assets.svg.xml", "r") as f:
        reusable_objects = f.read()

    svg_output = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w*10}" height="{h*10}">',
        '  <!-- Definitions for custom reusable object graphics -->',
        '  <defs>',
        reusable_objects,
        '  </defs>'
    ]

    ASSET_MAPPING = {
        "CASTLE": "castle_asset",
        "CITY": "city_asset",
        "PORT": "port_asset",
        "OUTPOST": "outpost_asset",
        "RUINS": "ruin_asset",
        "VILLAGE": "village_asset",
        "MINE": "mine_asset"
    }

    # 1. Render Base Canvas
    base_color = TERRAIN_COLORS.get(settings["base_terrain"], "#ffffff")
    svg_output.append(f'  <rect width="{w}" height="{h}" fill="{base_color}" />')


    land_features = [LandFeature(**feature) for feature in land]
    print(f"Generating {len(land_features)} land features based on the blueprint specifications.")       
    map = [[settings["base_terrain"] for _ in range(w)] for _ in range(h)]
    regions = {region["name"]: Region(**region) for region in blueprint.get("regions", [])}
    fill_map_with_land_features(map, settings["base_terrain"], regions, land_features)
    print(f"Map filled with land features successfully.")
    
    for y in range(h):
        for x in range(w):
            terrain_type = map[y][x]
            if terrain_type != settings["base_terrain"]:
                # Render the land feature as a fuzzy circle
                radius = 0.5
                path_data = generate_square(x, y, radius)
                color = TERRAIN_COLORS.get(terrain_type, "#000000")
                svg_output.append(f'  <path d="{path_data}" fill="{color}" stroke="none" />')

    for land in land_features:
        # Render the label for the land if it exists
        if land.label:
            pos_x, pos_y = land.position[0] * w / 100, land.position[1] * h / 100
            svg_output.append(f'  <text x="{pos_x}" y="{pos_y}" font-size="{font_size}" text-anchor="middle" fill="#000">{land.label}</text>')

    for path in paths:
        start_x, start_y = int(path["start"][0] * w / 100), int(path["start"][1] * h / 100)
        end_x, end_y = int(path["end"][0] * w / 100), int(path["end"][1] * h / 100)
        point_list = draw_path((start_x, start_y), (end_x, end_y), map, path.get("avoid", []))
        terrain_type = path.get("type", "ROAD")
        print(f"Rendering path from {path['start']} to {path['end']} with terrain type '{terrain_type}' and avoiding {path.get('avoid', [])}.")
        color = TERRAIN_COLORS.get(terrain_type, "#000000")
        
        svg_output.append(f'  <path d="M {start_x},{start_y} ' + ' '.join(f'L {x},{y}' for x, y in point_list[1:]) + f'" stroke="{color}" stroke-width="{path.get("width", 1)}" fill="none" />')
              
        if "label" in path:
            mid_x, mid_y = (start_x + end_x) / 2, (start_y + end_y) / 2
            svg_output.append(f'  <text x="{mid_x}" y="{mid_y}" font-size="{font_size}" text-anchor="middle" fill="#000">{path["label"]}</text>')

    # 3. Render Objects
    for obj in objects:
        pos_x, pos_y = place_object_on_map(obj, map)
        obj_type = obj["object_type"]
        label = obj.get("label", "")
        size = font_size * 2  # Size of the object icon
        asset_id = ASSET_MAPPING.get(obj_type)
        if asset_id:
            svg_output.append(f'  <svg width="{size}" height="{size}" x="{pos_x - size/2}" y="{pos_y - size/2}">')
            svg_output.append(f'  <use href="#{asset_id}" x="0" y="0"/>')
            svg_output.append(f'  </svg>')
        if label:
            svg_output.append(f'  <text x="{pos_x}" y="{pos_y - size / 2}" font-size="{font_size}" text-anchor="middle" fill="#000">{label}</text>')
            
    
    # Close file tag
    svg_output.append('</svg>')

    # Save directly to a standard web-ready vector graphic
    with open(f"{output}.svg", "w") as f:
        f.write("\n".join(svg_output))

    print(f"Vector map rendered successfully to '{output}.svg'!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Render an SVG map layout from an AoE2-style YAML blueprint.")
    parser.add_argument("yaml_file", type=str, help="Path to the YAML blueprint file")
    args = parser.parse_args()

    render_svg_from_yaml(args.yaml_file, args.yaml_file.rsplit('.', 1)[0])  # Save with the same name as the YAML file but with .svg extension