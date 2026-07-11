from copy import deepcopy


from .vocabulary_data.japanese import LANGUAGE_DATA as JAPANESE_DATA
from .vocabulary_data.german import LANGUAGE_DATA as GERMAN_DATA
from .vocabulary_data.dutch import LANGUAGE_DATA as DUTCH_DATA
from .vocabulary_data.turkish import LANGUAGE_DATA as TURKISH_DATA
from .vocabulary_data.spanish import LANGUAGE_DATA as SPANISH_DATA
from .vocabulary_data.italian import LANGUAGE_DATA as ITALIAN_DATA


VOCABULARY = {
    "japanese": JAPANESE_DATA,
    "german": GERMAN_DATA,
    "dutch": DUTCH_DATA,
    "turkish": TURKISH_DATA,
    "spanish": SPANISH_DATA,
    "italian": ITALIAN_DATA,
}


EASY_MODE_PRIORITY_WORDS = [
    "bonjour",
    "au revoir",
    "s'il vous plaît",
    "merci",
    "oui",
    "non",
    "moi",
    "toi",
    "il/elle",
    "vous",
    "maison",
    "ville",
    "rue",
    "magasin",
    "voiture",
    "bus",
    "train",
    "eau",
    "pain",
    "riz",
    "viande",
    "poisson",
    "fruit",
    "café",
    "thé",
    "lait",
    "jour",
    "nuit",
    "aujourd'hui",
    "demain",
    "hier",
    "heure",
    "aller",
    "venir",
    "manger",
    "boire",
    "parler",
    "comprendre",
    "apprendre",
    "travailler",
    "dormir",
    "écrire",
    "lire",
    "bon",
    "grand",
    "petit",
    "chaud",
    "froid",
    "facile",
    "difficile",
    "enfant",
    "mère",
    "père",
    "frère",
    "soeur",
    "ami(e)",
    "femme",
    "mari",
    "travail",
    "argent",
    "livre",
    "télévision",
    "maison",
    "cuisine",
    "chambre",
    "lit",
    "table",
    "chaise",
    "porte",
    "ville",
    "rue",
    "magasin",
    "pays",
    "voyage",
    "France",
    "Angleterre",
    "voiture",
    "bus",
    "train",
    "avion",
    "transport",
    "arbre",
    "soleil",
    "montagne",
    "forêt",
    "mer",
    "temps",
    "année",
    "mois",
    "semaine",
    "jour",
    "heure",
    "minute",
    "matin",
    "soir",
    "nuit",
    "aujourd'hui",
    "demain",
    "hier",
    "quand",
    "maintenant",
    "où",
    "ici",
    "là",
    "qui",
    "quoi?",
    "pourquoi",
    "quel(le,s)",
    "ceci",
    "cela",
    "de []",
    "avec",
    "sans",
    "et",
    "ou",
    "mais",
    "parce que",
    "donc",
    "si",
    "aller",
    "venir",
    "marcher",
    "courir",
    "manger",
    "boire",
    "dormir",
    "faire",
    "travailler",
    "parler",
    "dire",
    "écouter",
    "regarder",
    "voir",
    "écrire",
    "lire",
    "acheter",
    "payer",
    "donner",
    "prendre",
    "attendre",
    "chercher",
    "trouver []",
    "comprendre",
    "apprendre",
    "avoir",
    "je veux",
    "j'ai besoin de []",
    "je peux []",
    "j'aime []",
    "je pense que []",
    "c'est",
    "il y a",
    "peut-être",
    "bon",
    "mauvais",
    "grand",
    "petit",
    "chaud",
    "froid",
    "vite",
    "lent",
    "facile",
    "difficile",
    "important",
    "propre",
    "sale",
    "près",
    "loin",
]

EASY_NOUN_GUESS_WORDS = [
    "pizza",
    "hamburger",
    "sandwich",
    "croissant",
    "baguette",
    "bonbon",
    "sushi",
    "donut",
    "glace",
    "chocolat",
    "gâteau",
    "pop-corn",
    "taco",
    "avocat",
    "ananas",
    "banane",
    "panda",
    "koala",
    "tigre",
    "zèbre",
    "girafe",
    "dauphin",
    "requin",
    "pieuvre",
    "licorne",
    "dragon",
    "robot",
    "astronaute",
    "pirate",
    "dinosaure",
    "ninja",
    "magicien",
    "super-héros",
    "trésor",
    "château",
    "fusée",
    "volcan",
    "arc-en-ciel",
    "lune",
    "étoile",
    "planète",
    "tempête",
    "nuage",
    "montagne",
    "forêt",
    "océan",
    "île",
    "désert",
    "jungle",
    "cascade",
    "parapluie",
    "ballon",
    "guitare",
    "piano",
    "caméra",
    "casque",
    "télécommande",
    "trottinette",
    "skateboard",
    "roller",
    "toboggan",
    "cerf-volant",
    "trampoline",
    "puzzle",
    "masque",
    "costume",
]

FUN_NOUN_GUESS_WORDS = [
    "pizza",
    "hamburger",
    "sandwich",
    "croissant",
    "baguette",
    "bonbon",
    "sushi",
    "donut",
    "glace",
    "chocolat",
    "gâteau",
    "pop-corn",
    "taco",
    "avocat",
    "ananas",
    "banane",
    "frite",
    "cookie",
    "panda",
    "koala",
    "tigre",
    "zèbre",
    "girafe",
    "dauphin",
    "requin",
    "pieuvre",
    "licorne",
    "dragon",
    "robot",
    "astronaute",
    "pirate",
    "dinosaure",
    "ninja",
    "magicien",
    "super-héros",
    "trésor",
    "château",
    "fusée",
    "volcan",
    "arc-en-ciel",
    "lune",
    "étoile",
    "planète",
    "tempête",
    "nuage",
    "montagne",
    "forêt",
    "océan",
    "île",
    "désert",
    "jungle",
    "cascade",
    "parapluie",
    "ballon",
    "guitare",
    "piano",
    "caméra",
    "casque",
    "télécommande",
    "trottinette",
    "skateboard",
    "roller",
    "toboggan",
    "cerf-volant",
    "trampoline",
    "puzzle",
    "masque",
    "costume",
    "valise",
    "miroir",
    "ampoule",
    "clé",
    "serrure",
    "montre",
    "horloge",
    "écharpe",
    "chapeau",
    "chaussette",
    "sandale",
    "ceinture",
    "coussin",
    "oreiller",
    "matelas",
    "tapis",
    "rideau",
    "placard",
    "tiroir",
    "pont",
    "tunnel",
    "phare",
    "musée",
    "cinéma",
    "stade",
    "statue",
    "taxi",
    "métro",
    "tram",
    "scooter",
    "parking",
    "football",
    "basket",
    "tennis",
    "natation",
    "chanson",
    "photo",
    "dessin",
    "peinture",
    "jouet",
    "poupée",
    "cadeau",
    "anniversaire",
    "vacances",
    "weekend",
]


def _normalize_original(value):
    return value.strip().lower()


ORIGINAL_LANGUAGE_TO_VOCAB_KEY = {
    "fr": None,
    "de": "german",
    "es": "spanish",
    "it": "italian",
    "nl": "dutch",
    "tr": "turkish",
    "ja(ro)": "japanese",
}


LOCATION_WORD_HINTS = {
    "où",
    "ici",
    "là",
    "là-bas",
    "nulle-part",
    "quelques-part",
    "partout",
    "en bas",
    "devant",
    "derrière",
    "à gauche",
    "droite (de [])",
    "l'intérieur",
    "l'exterieur",
    "tout droit",
    "dessus",
    "vers",
    "à côté",
}

YES_NO_WORDS = {"oui", "non"}

DIVERS_MODAL_HINTS = {
    "c'est",
    "ce n'est pas []",
    "il y a",
    "il n'y a pas",
    "je veux",
    "j'aime []",
    "je dois []",
    "j'ai besoin de []",
    "c'est pas la peine",
    "je vais []",
    "je connais []",
    "je sais que",
    "je peux []",
    "je pense que []",
    "présent",
    "neg. prés.",
}

CORE_MODAL_WORD_HINTS = {
    "aimer",
    "pouvoir",
}

DIVERS_INTERROGATION_HINTS = {
    "?",
    "quoi?",
    "y a t'il?",
    "pourquoi",
    "quel(le,s)",
    "quelle sorte",
}

DIVERS_CONNECTOR_HINTS = {
    "mais",
    "et",
    "ou",
    "donc",
    "puis",
    "alors",
    "parce que",
    "par example",
}

MOVEMENT_VERB_HINTS = {
    "marcher",
    "se promener",
    "aller",
    "venir",
    "partir",
    "passer",
    "entrer",
    "tourner",
    "s'asseoir",
    "sortir",
    "courir",
    "habiter à []",
}

ADJECTIVE_COLOR_SIZE_HINTS = {
    "grand",
    "petit",
    "haut",
    "bas",
    "lourd",
    "couleur",
    "bleu",
    "rouge",
    "vert",
    "jaune",
    "blanc",
    "noir",
}

ADJECTIVE_STATE_HINTS = {
    "(j'ai) faim",
    "malade",
    "fatigué",
    "content",
    "prêt",
    "interdit",
    "chaud",
    "froid",
}

QUANTITY_WORD_HINTS = {
    "combien",
    "0",
    "1",
    "2",
}

TIME_STATE_HINTS = {
    "loin",
    "près",
    "vide",
    "plein",
    "ouvert",
    "fermé",
    "nouveau",
    "bon",
    "mauvais",
}

CATEGORY_MERGE_TARGETS = {
    "Divers": "Modaux & Phrases",
}

PROTECTED_CATEGORIES_FROM_MERGE = {
    "Verbes de mouvement",
    "État",
    "Adjectifs d'état",
    "Adjectifs de description",
    "Couleurs & Taille",
    "Interrogations",
    "Connecteurs",
    "Lieux",
    "Pronoms",
}


def _normalize_easy_category_name_with_hints(category_name, original_word):
    normalized_word = _normalize_original(original_word)

    if normalized_word in CORE_MODAL_WORD_HINTS:
        return "Modaux & Phrases"

    if category_name == "Pronoms & Lieux":
        if normalized_word in LOCATION_WORD_HINTS:
            return "Lieux"
        return "Pronoms"

    if category_name in {"Temps", "Temps (suite) & État"}:
        if normalized_word in TIME_STATE_HINTS:
            return "État"
        return "Temps"

    if category_name == "Verbes d'action" and normalized_word in MOVEMENT_VERB_HINTS:
        return "Verbes de mouvement"

    if category_name in {"Adjectifs", "Adjectifs & Divers"}:
        if normalized_word in QUANTITY_WORD_HINTS:
            return "Chiffres & Quantité"
        if normalized_word in ADJECTIVE_COLOR_SIZE_HINTS:
            return "Couleurs & Taille"
        if normalized_word in ADJECTIVE_STATE_HINTS:
            return "Adjectifs d'état"
        return "Adjectifs de description"

    if category_name == "Divers":
        if normalized_word in DIVERS_MODAL_HINTS or normalized_word.startswith("je "):
            return "Modaux & Phrases"
        if normalized_word in DIVERS_INTERROGATION_HINTS or normalized_word.endswith("?"):
            return "Interrogations"
        if normalized_word in DIVERS_CONNECTOR_HINTS:
            return "Connecteurs"
        return "Divers"

    if category_name == "Chiffres & Quantité" and normalized_word in YES_NO_WORDS:
        return "Politesse"

    return category_name


_JP_REFERENCE_CATEGORY_BY_WORD = None


def _reference_category_for_word(normalized_word):
    global _JP_REFERENCE_CATEGORY_BY_WORD
    if _JP_REFERENCE_CATEGORY_BY_WORD is None:
        reference_map = {}
        for category in JAPANESE_DATA["categories"]:
            category_name = category["name"]
            for word in category["words"]:
                key = _normalize_original(word.get("original", ""))
                if not key:
                    continue
                reference_map.setdefault(
                    key,
                    _normalize_easy_category_name_with_hints(category_name, word.get("original", "")),
                )
        _JP_REFERENCE_CATEGORY_BY_WORD = reference_map

    return _JP_REFERENCE_CATEGORY_BY_WORD.get(normalized_word)


def _normalize_easy_category_name(category_name, original_word):
    normalized_word = _normalize_original(original_word)
    reference_category = _reference_category_for_word(normalized_word)
    if reference_category:
        return reference_category
    return _normalize_easy_category_name_with_hints(category_name, original_word)


def _normalized_easy_categories(categories):
    grouped_words = {}
    ordered_category_names = []

    for category in categories:
        original_name = category["name"]
        for word in category["words"]:
            normalized_name = _normalize_easy_category_name(original_name, word["original"])

            if normalized_name not in grouped_words:
                grouped_words[normalized_name] = []
                ordered_category_names.append(normalized_name)

            grouped_words[normalized_name].append(dict(word))

    normalized_categories = []
    for category_name in ordered_category_names:
        normalized_categories.append({
            "name": category_name,
            "words": grouped_words[category_name],
        })

    return normalized_categories


def _merge_tiny_categories(categories, min_size=3):
    if not categories:
        return categories

    words_by_category = {
        category["name"]: [dict(word) for word in category["words"]]
        for category in categories
    }
    ordered_names = [category["name"] for category in categories]

    def _largest_target(excluded_name):
        candidates = [
            (name, len(words_by_category[name]))
            for name in ordered_names
            if name != excluded_name and name in words_by_category
        ]
        if not candidates:
            return None
        candidates.sort(key=lambda item: item[1], reverse=True)
        return candidates[0][0]

    merged_any = True
    while merged_any:
        merged_any = False
        for name in list(ordered_names):
            if name not in words_by_category:
                continue

            if len(words_by_category[name]) >= min_size:
                continue

            if name in PROTECTED_CATEGORIES_FROM_MERGE:
                continue

            preferred_target = CATEGORY_MERGE_TARGETS.get(name)
            if preferred_target not in words_by_category:
                preferred_target = _largest_target(name)

            if not preferred_target:
                continue

            words_by_category[preferred_target].extend(words_by_category[name])
            del words_by_category[name]
            ordered_names.remove(name)
            merged_any = True

    merged_categories = []
    for name in ordered_names:
        if name in words_by_category and words_by_category[name]:
            merged_categories.append({
                "name": name,
                "words": words_by_category[name],
            })

    return merged_categories


def _easy_categories(categories, target_count=55):
    source_categories = [
        category for category in categories
        if category["name"] != "Politesse"
    ]

    words_by_key = {}
    ordered_keys = []

    for category in source_categories:
        for word in category["words"]:
            key = _normalize_original(word["original"])
            if key not in words_by_key:
                words_by_key[key] = word
                ordered_keys.append(key)

    selected_keys = []
    selected_key_set = set()

    for preferred in EASY_MODE_PRIORITY_WORDS:
        key = _normalize_original(preferred)
        if key in words_by_key and key not in selected_key_set:
            selected_keys.append(key)
            selected_key_set.add(key)

    for key in ordered_keys:
        if len(selected_keys) >= target_count:
            break
        if key not in selected_key_set:
            selected_keys.append(key)
            selected_key_set.add(key)

    easy_categories = []
    for category in source_categories:
        filtered_words = [
            dict(word)
            for word in category["words"]
            if _normalize_original(word["original"]) in selected_key_set
        ]
        if filtered_words:
            easy_categories.append({
                "name": category["name"],
                "words": filtered_words,
            })

    return easy_categories


def _is_guessable_word(original):
    if not original:
        return False

    if "[" in original or "]" in original or "?" in original:
        return False

    if original.startswith("-"):
        return False

    return True


EXCLUDED_VOCAB_CATEGORIES = {
    "Politesse",
}

LOW_VALUE_VOCAB_WORDS = {
    "?",
    "ce n'est pas []",
    "je dois []",
    "je vais []",
    "je connais []",
    "je pense que []",
    "de []",
    "ce [] ci",
    "ce [] là",
    "droite (de [])",
    "habiter à []",
    "trouver []",
    "pour []",
    "plus que []",
    "présent",
    "neg. prés.",
    "bonjour",
    "salut",
    "bonsoir",
    "bonne nuit",
    "aurevoir",
    "s'il vous plaît",
    "merci",
    "je vous en prie",
    "excusez moi",
    "pardon",
    "pas de problème",
    "comment vas tu",
    "merci, je vais bien",
    "comment vous appelez vous?",
    "je m'appele []",
    "d'où venez vous?",
    "je suis de []",
    "enchanté",
    "parlez plus lentement",
    "écrivez le",
    "donnez moi []",
    "voici",
    "bon appétit",
    "santé!",
    "n'est ce pas",
    "ne t'inquiète pas",
    "je ne sais pas, je n'ai pas compris",
    "20",
    "100",
    "1000",
    "10000",
}


def _is_low_value_vocabulary_word(original, translation):
    normalized_original = _normalize_original(original)

    if not normalized_original:
        return True

    if normalized_original in LOW_VALUE_VOCAB_WORDS:
        return True

    if "[" in original or "]" in original:
        return True

    if "?" in original:
        return True

    if original.startswith("-"):
        return True

    return False


def _curated_vocabulary_categories(categories, target_count=275):
    return _curated_vocabulary_categories_with_keys(categories, target_count=target_count)


def _curated_vocabulary_categories_with_keys(categories, target_count=275, allowed_keys=None):
    curated_categories = []
    seen_keys = set()
    selected_words = 0

    for category in categories:
        if category["name"] in EXCLUDED_VOCAB_CATEGORIES:
            continue

        filtered_words = []
        for word in category["words"]:
            original = word.get("original", "")
            translation = word.get("translation", "")
            key = _normalize_original(original)

            if key in seen_keys:
                continue

            if allowed_keys is not None and key not in allowed_keys:
                continue

            if _is_low_value_vocabulary_word(original, translation):
                continue

            filtered_words.append(dict(word))
            seen_keys.add(key)
            selected_words += 1

            if selected_words >= target_count:
                break

        if filtered_words:
            curated_categories.append({
                "name": category["name"],
                "words": filtered_words,
            })

        if selected_words >= target_count:
            break

    return curated_categories


NORMAL_EXTRA_GUESS_WORDS = [
    "boussole",
    "jumelles",
    "marteau",
    "tournevis",
    "pince",
    "lampe",
    "lanterne",
    "bougie",
    "allumette",
    "batterie",
    "cable",
    "prise",
    "micro",
    "enceinte",
    "projecteur",
    "imprimante",
    "clavier",
    "souris",
    "ecran",
    "sac a dos",
    "bouteille",
    "gobelet",
    "cuillere",
    "fourchette",
    "couteau",
    "assiette",
    "poele",
    "casserole",
    "four",
    "frigo",
    "congelateur",
    "savon",
    "shampoing",
    "brosse",
    "peigne",
    "serviette",
    "valise",
    "passeport",
    "ticket",
    "carte",
    "chemin",
    "village",
    "quartier",
    "immeuble",
    "ascenseur",
    "escalier",
    "fenetre",
    "toit",
    "garage",
    "jardin",
    "pelouse",
    "fleur",
    "feuille",
    "champignon",
    "rivière",
    "lac",
    "plage",
    "vague",
    "sable",
    "neige",
    "glacier",
    "orage",
    "eclair",
    "brouillard",
    "chaleur",
    "hiver",
    "printemps",
    "ete",
    "automne",
    "calendrier",
    "agenda",
    "anniversaire",
    "vacances",
    "concert",
    "spectacle",
    "festival",
    "match",
    "tournoi",
    "medaille",
    "trophee",
    "partie",
    "manette",
    "jeu de cartes",
    "plateau",
    "des",
    "indice",
]


EASY_EXTRA_GUESS_WORDS = [
    "orange",
    "fraise",
    "pasteque",
    "pomme",
    "poire",
    "citron",
    "gateau",
    "yaourt",
    "biscuit",
    "salade",
    "poulet",
    "tortue",
    "lapin",
    "singe",
    "cheval",
    "canard",
    "papillon",
    "abeille",
    "ballon de foot",
    "velo",
    "patin",
    "cartable",
    "crayon",
    "stylo",
    "cahier",
    "carton",
    "boite",
    "bois",
    "neige",
    "arc",
]


HARD_GUESS_WORDS = [
    "nostalgie",
    "patience",
    "jalousie",
    "courage",
    "fierte",
    "honte",
    "confiance",
    "doute",
    "surprise",
    "malaise",
    "solitude",
    "liberte",
    "justice",
    "injustice",
    "egalite",
    "responsabilite",
    "curiosite",
    "creativite",
    "intuition",
    "strategie",
    "tactique",
    "discipline",
    "motivation",
    "habitude",
    "routine",
    "equilibre",
    "priorite",
    "urgence",
    "consequence",
    "cause",
    "objectif",
    "perspective",
    "vision",
    "decision",
    "choix",
    "compromis",
    "dialogue",
    "silence",
    "rumeur",
    "secret",
    "mensonge",
    "verite",
    "mystere",
    "paradoxe",
    "coincidence",
    "probabilite",
    "hypothese",
    "theorie",
    "preuve",
    "memoire",
    "oubli",
    "souvenir",
    "concentration",
    "fatigue",
    "insomnie",
    "vertige",
    "allergie",
    "infection",
    "guerison",
    "panne",
    "incident",
    "accident",
    "catastrophe",
    "crise",
    "penurie",
    "abondance",
    "inflation",
    "economie",
    "budget",
    "investissement",
    "entreprise",
    "client",
    "employe",
    "patron",
    "entrepreneur",
    "architecte",
    "ingenieur",
    "journaliste",
    "avocat",
    "juge",
    "chercheur",
    "pharmacien",
    "infirmier",
    "pilote",
    "capitaine",
    "explorateur",
    "archeologue",
    "traducteur",
    "negociation",
    "mediation",
    "cooperation",
    "competition",
    "rivalite",
    "leadership",
    "autorite",
    "influence",
    "reputation",
    "identite",
    "culture",
    "tradition",
    "rituel",
    "symbole",
    "heritage",
    "civilisation",
    "democratie",
    "diplomatie",
    "frontiere",
    "territoire",
    "alliance",
    "energie",
    "matiere",
    "gravite",
    "friction",
    "equation",
    "algorithme",
    "reseau",
    "satellite",
    "comete",
    "constellation",
    "orbite",
    "biodiversite",
    "ecosysteme",
    "pollution",
    "recyclage",
    "soutenabilite",
    "innovation",
    "prototype",
    "version",
    "compatibilite",
    "maintenance",
    "diagnostic",
    "simulation",
    "scenario",
    "interpretation",
    "imagination",
    "inspiration",
    "vocation",
    "resilience",
    "adaptation",
    "transformation",
]

ENGLISH_GUESS_WORDS = [
    "pizza", "hamburger", "sandwich", "croissant", "baguette", "candy", "sushi", "donut",
    "ice cream", "chocolate", "cake", "popcorn", "taco", "avocado", "pineapple", "banana",
    "fries", "cookie", "panda", "koala", "tiger", "zebra", "giraffe", "dolphin", "shark",
    "octopus", "unicorn", "dragon", "robot", "astronaut", "pirate", "dinosaur", "ninja",
    "wizard", "superhero", "treasure", "castle", "rocket", "volcano", "rainbow", "moon",
    "star", "planet", "storm", "cloud", "mountain", "forest", "ocean", "island", "desert",
    "jungle", "waterfall", "umbrella", "balloon", "guitar", "piano", "camera", "headphones",
    "remote", "scooter", "skateboard", "roller skates", "slide", "kite", "trampoline", "puzzle",
    "mask", "costume", "suitcase", "mirror", "light bulb", "key", "lock", "watch", "clock",
    "scarf", "hat", "sock", "sandal", "belt", "cushion", "pillow", "mattress", "carpet",
    "curtain", "closet", "drawer", "bridge", "tunnel", "lighthouse", "museum", "cinema",
    "stadium", "statue", "taxi", "subway", "tram", "parking", "football", "basketball",
    "tennis", "swimming", "song", "photo", "drawing", "painting", "toy", "doll", "gift",
    "birthday", "vacation", "weekend", "compass", "binoculars", "hammer", "screwdriver", "pliers",
    "lamp", "lantern", "candle", "match", "battery", "cable", "socket", "microphone", "speaker",
    "projector", "printer", "keyboard", "mouse", "screen", "backpack", "bottle", "cup", "spoon",
    "fork", "knife", "plate", "pan", "pot", "oven", "fridge", "freezer", "soap", "shampoo",
    "brush", "comb", "towel", "passport", "ticket", "map", "path", "crossroad", "traffic",
    "sidewalk", "building", "garden", "fountain", "library", "bookstore", "bakery", "pharmacy",
    "hospital", "airport", "harbor", "engine", "motor", "wheel", "pedal", "battery pack",
    "ingredient", "recipe", "menu", "dessert", "breakfast", "lunch", "dinner", "snack", "spice",
    "flavor", "temperature", "shadow", "silence", "noise", "question", "answer", "idea", "memory",
    "focus", "fatigue", "allergy", "infection", "recovery", "incident", "accident", "crisis",
    "shortage", "abundance", "inflation", "economy", "budget", "investment", "company", "client",
    "employee", "boss", "entrepreneur", "architect", "engineer", "journalist", "lawyer", "judge",
    "researcher", "pharmacist", "nurse", "pilot", "captain", "explorer", "archaeologist", "translator",
    "negotiation", "mediation", "cooperation", "competition", "rivalry", "leadership", "authority",
    "influence", "reputation", "identity", "culture", "tradition", "ritual", "symbol", "heritage",
    "civilization", "democracy", "diplomacy", "border", "territory", "alliance", "energy", "matter",
    "gravity", "friction", "equation", "algorithm", "network", "satellite", "comet", "constellation",
    "orbit", "biodiversity", "ecosystem", "pollution", "recycling", "sustainability", "innovation",
    "prototype", "version", "compatibility", "maintenance", "diagnosis", "simulation", "scenario",
    "interpretation", "imagination", "inspiration", "vocation", "resilience", "adaptation", "transformation",
]


def _dedupe_preserve_order(values):
    seen = set()
    ordered = []
    for value in values:
        key = _normalize_original(value)
        if key in seen:
            continue
        seen.add(key)
        ordered.append(value)
    return ordered


# Single merged pool: keep words concrete/easy and avoid abstract hard words.
CONCRETE_GUESS_WORDS = _dedupe_preserve_order(
    ["grenouille", "ours", "chat", "chien", "bateau", "avion", "banane", "orange"]
    + EASY_NOUN_GUESS_WORDS
    + FUN_NOUN_GUESS_WORDS
)


# Keep only concrete English words (trim abstract tail), plus concrete replacements.
ENGLISH_CONCRETE_GUESS_WORDS = _dedupe_preserve_order([
    "frog", "bear", "cat", "dog", "boat", "airplane", "banana", "orange",
    "pizza", "hamburger", "sandwich", "croissant", "baguette", "candy", "sushi", "donut",
    "ice cream", "chocolate", "cake", "popcorn", "taco", "avocado", "pineapple", "banana",
    "fries", "cookie", "panda", "koala", "tiger", "zebra", "giraffe", "dolphin", "shark",
    "octopus", "unicorn", "dragon", "robot", "astronaut", "pirate", "dinosaur", "ninja",
    "wizard", "superhero", "treasure", "castle", "rocket", "volcano", "rainbow", "moon",
    "star", "planet", "storm", "cloud", "mountain", "forest", "ocean", "island", "desert",
    "jungle", "waterfall", "umbrella", "balloon", "guitar", "piano", "camera", "headphones",
    "remote", "scooter", "skateboard", "roller skates", "slide", "kite", "trampoline", "puzzle",
    "mask", "costume", "suitcase", "mirror", "light bulb", "key", "lock", "watch", "clock",
    "scarf", "hat", "sock", "sandal", "belt", "cushion", "pillow", "mattress", "carpet",
    "curtain", "closet", "drawer", "bridge", "tunnel", "lighthouse", "museum", "cinema",
    "stadium", "statue", "taxi", "subway", "tram", "parking", "football", "basketball",
    "tennis", "swimming", "song", "photo", "drawing", "painting", "toy", "doll", "gift",
    "birthday", "vacation", "weekend", "compass", "binoculars", "hammer", "screwdriver", "pliers",
    "lamp", "lantern", "candle", "match", "battery", "cable", "socket", "microphone", "speaker",
    "projector", "printer", "keyboard", "mouse", "screen", "backpack", "bottle", "cup", "spoon",
    "fork", "knife", "plate", "pan", "pot", "oven", "fridge", "freezer", "soap", "shampoo",
    "brush", "comb", "towel", "passport", "ticket", "map", "path", "crossroad", "traffic",
    "sidewalk", "building", "garden", "fountain", "library", "bookstore", "bakery", "pharmacy",
    "hospital", "airport", "harbor", "engine", "motor", "wheel", "pedal", "battery pack",
])


GERMAN_CONCRETE_GUESS_WORDS = _dedupe_preserve_order([
    "frosch", "baer", "katze", "hund", "boot", "flugzeug", "banane", "orange", "pizza", "hamburger",
    "sandwich", "croissant", "bonbon", "sushi", "donut", "eis", "schokolade", "kuchen", "popcorn", "taco",
    "ananas", "keks", "panda", "koala", "tiger", "zebra", "giraffe", "delfin", "hai", "krake",
    "einhorn", "drache", "roboter", "astronaut", "pirat", "dinosaurier", "ninja", "zauberer", "superheld", "schatz",
    "schloss", "rakete", "vulkan", "regenbogen", "mond", "stern", "planet", "wolke", "berg", "wald",
    "ozean", "insel", "wueste", "dschungel", "wasserfall", "regenschirm", "ballon", "gitarre", "klavier", "kamera",
    "koffer", "spiegel", "schluessel", "uhr", "hut", "socke", "guertel", "kissen", "teppich", "bruecke",
    "tunnel", "museum", "kino", "stadion", "statue", "taxi", "fussball", "basketball", "tennis", "foto",
    "zeichnung", "spielzeug", "puppe", "geschenk", "kompass", "hammer", "schraubenzieher", "lampe", "kerze", "batterie",
    "mikrofon", "lautsprecher", "rucksack", "flasche", "tasse", "loeffel", "gabel", "messer", "teller", "pfanne",
    "topf", "ofen", "kuehlschrank", "seife", "shampoo", "buerste", "kamm", "handtuch", "pass", "ticket",
    "karte", "garten", "bibliothek", "baeckerei", "apotheke", "krankenhaus", "flughafen", "hafen", "motor", "rad",
])

SPANISH_CONCRETE_GUESS_WORDS = _dedupe_preserve_order([
    "rana", "oso", "gato", "perro", "barco", "avion", "banana", "naranja", "pizza", "hamburguesa",
    "sandwich", "croissant", "caramelo", "sushi", "dona", "helado", "chocolate", "pastel", "palomitas", "taco",
    "pina", "galleta", "panda", "koala", "tigre", "cebra", "jirafa", "delfin", "tiburon", "pulpo",
    "unicornio", "dragon", "robot", "astronauta", "pirata", "dinosaurio", "ninja", "mago", "superheroe", "tesoro",
    "castillo", "cohete", "volcan", "arcoiris", "luna", "estrella", "planeta", "nube", "montana", "bosque",
    "oceano", "isla", "desierto", "jungla", "cascada", "paraguas", "globo", "guitarra", "piano", "camara",
    "maleta", "espejo", "llave", "reloj", "sombrero", "calcetin", "cinturon", "cojin", "alfombra", "puente",
    "tunel", "museo", "cine", "estadio", "estatua", "taxi", "futbol", "baloncesto", "tenis", "foto",
    "dibujo", "juguete", "muneca", "regalo", "brujula", "martillo", "destornillador", "lampara", "vela", "bateria",
    "microfono", "altavoz", "mochila", "botella", "taza", "cuchara", "tenedor", "cuchillo", "plato", "sarten",
    "olla", "horno", "nevera", "jabon", "champu", "cepillo", "peine", "toalla", "pasaporte", "billete",
    "mapa", "jardin", "biblioteca", "panaderia", "farmacia", "hospital", "aeropuerto", "puerto", "motor", "rueda",
])

ITALIAN_CONCRETE_GUESS_WORDS = _dedupe_preserve_order([
    "rana", "orso", "gatto", "cane", "barca", "aereo", "banana", "arancia", "pizza", "hamburger",
    "panino", "croissant", "caramella", "sushi", "donut", "gelato", "cioccolato", "torta", "popcorn", "taco",
    "ananas", "biscotto", "panda", "koala", "tigre", "zebra", "giraffa", "delfino", "squalo", "polpo",
    "unicorno", "drago", "robot", "astronauta", "pirata", "dinosauro", "ninja", "mago", "supereroe", "tesoro",
    "castello", "razzo", "vulcano", "arcobaleno", "luna", "stella", "pianeta", "nuvola", "montagna", "foresta",
    "oceano", "isola", "deserto", "giungla", "cascata", "ombrello", "palloncino", "chitarra", "pianoforte", "fotocamera",
    "valigia", "specchio", "chiave", "orologio", "cappello", "calzino", "cintura", "cuscino", "tappeto", "ponte",
    "tunnel", "museo", "cinema", "stadio", "statua", "taxi", "calcio", "pallacanestro", "tennis", "foto",
    "disegno", "giocattolo", "bambola", "regalo", "bussola", "martello", "cacciavite", "lampada", "candela", "batteria",
    "microfono", "altoparlante", "zaino", "bottiglia", "tazza", "cucchiaio", "forchetta", "coltello", "piatto", "padella",
    "pentola", "forno", "frigorifero", "sapone", "shampoo", "spazzola", "pettine", "asciugamano", "passaporto", "biglietto",
    "mappa", "giardino", "biblioteca", "panetteria", "farmacia", "ospedale", "aeroporto", "porto", "motore", "ruota",
])

DUTCH_CONCRETE_GUESS_WORDS = _dedupe_preserve_order([
    "kikker", "beer", "kat", "hond", "boot", "vliegtuig", "banaan", "sinaasappel", "pizza", "hamburger",
    "sandwich", "croissant", "snoep", "sushi", "donut", "ijs", "chocolade", "taart", "popcorn", "taco",
    "ananas", "koekje", "panda", "koala", "tijger", "zebra", "giraf", "dolfijn", "haai", "inktvis",
    "eenhoorn", "draak", "robot", "astronaut", "piraat", "dinosaurus", "ninja", "tovenaar", "superheld", "schat",
    "kasteel", "raket", "vulkaan", "regenboog", "maan", "ster", "planeet", "wolk", "berg", "bos",
    "oceaan", "eiland", "woestijn", "jungle", "waterval", "paraplu", "ballon", "gitaar", "piano", "camera",
    "koffer", "spiegel", "sleutel", "horloge", "hoed", "sok", "riem", "kussen", "tapijt", "brug",
    "tunnel", "museum", "bioscoop", "stadion", "standbeeld", "taxi", "voetbal", "basketbal", "tennis", "foto",
    "tekening", "speelgoed", "pop", "cadeau", "kompas", "hamer", "schroevendraaier", "lamp", "kaars", "batterij",
    "microfoon", "luidspreker", "rugzak", "fles", "kop", "lepel", "vork", "mes", "bord", "pan",
    "pot", "oven", "koelkast", "zeep", "shampoo", "borstel", "kam", "handdoek", "paspoort", "ticket",
    "kaart", "tuin", "bibliotheek", "bakkerij", "apotheek", "ziekenhuis", "luchthaven", "haven", "motor", "wiel",
])

TURKISH_CONCRETE_GUESS_WORDS = _dedupe_preserve_order([
    "kurbaga", "ayi", "kedi", "kopek", "tekne", "ucak", "muz", "portakal", "pizza", "hamburger",
    "sandvic", "kruvasan", "seker", "sushi", "donut", "dondurma", "cikolata", "pasta", "patlamis misir", "taco",
    "ananas", "kurabiye", "panda", "koala", "kaplan", "zebra", "zurafa", "yunus", "kopekbaligi", "ahtapot",
    "tekboynuz", "ejderha", "robot", "astronot", "korsan", "dinozor", "ninja", "buyucu", "super kahraman", "hazine",
    "sato", "roket", "volkan", "gokkusagi", "ay", "yildiz", "gezegen", "bulut", "dag", "orman",
    "okyanus", "ada", "col", "jungla", "selale", "semsiye", "balon", "gitar", "piyano", "kamera",
    "valiz", "ayna", "anahtar", "saat", "sapka", "corap", "kemer", "yastik", "hali", "kopru",
    "tunel", "muze", "sinema", "stadyum", "heykel", "taksi", "futbol", "basketbol", "tenis", "fotograf",
    "cizim", "oyuncak", "bebek", "hediye", "pusula", "cekic", "tornavida", "lamba", "mum", "pil",
    "mikrofon", "hoparlor", "sirt cantasi", "sise", "fincan", "kasik", "catal", "bicak", "tabak", "tava",
    "tencere", "firin", "buzdolabi", "sabun", "sampuan", "firca", "tarak", "havlu", "pasaport", "bilet",
    "harita", "bahce", "kutuphane", "pastane", "eczane", "hastane", "havalimani", "liman", "motor", "tekerlek",
])

JAPANESE_ROMAJI_CONCRETE_GUESS_WORDS = _dedupe_preserve_order([
    "kaeru", "kuma", "neko", "inu", "fune", "hikooki", "banana", "orenji", "pizza", "hamburger",
    "sandoicchi", "kurowassan", "ame", "sushi", "donatsu", "aisukurimu", "chokoreeto", "keeki", "poppukoon", "takosu",
    "ananasu", "kukkii", "panda", "koara", "tora", "zebra", "kirin", "iruka", "same", "tako",
    "yunikoon", "doragon", "robotto", "asutoronauto", "kaizoku", "kyooryuu", "ninja", "majutsushi", "suupaa hiiroo", "takara",
    "shiro", "roketto", "kazan", "niji", "tsuki", "hoshi", "wakusei", "kumo", "yama", "mori",
    "umi", "shima", "sabaku", "jyanguru", "taki", "kasa", "fuusen", "gitaa", "piano", "kamera",
    "suutukeesu", "kagami", "kagi", "tokei", "booshi", "kutsushita", "beruto", "kusshon", "juutan", "hashi",
    "tonneru", "hakubutsukan", "eigakan", "sutajiamu", "zou", "takushii", "sakaa booru", "basuketto booru", "tenisu", "shashin",
    "e", "omocha", "ningyoo", "purezento", "rashinban", "kanazuchi", "doraibaa", "ranpu", "roosoku", "denchi",
    "maiku", "supiikaa", "ryukkusakku", "botoru", "kappu", "supuun", "fooku", "naifu", "osara", "furai pan",
    "nabe", "oobun", "reizooko", "sekken", "shanpuu", "burashi", "kushi", "taoru", "pasupooto", "chiketto",
    "chizu", "niwa", "toshokan", "panya", "yakkyoku", "byooin", "kuukoo", "minato", "enjin", "sharin",
])


LANGUAGE_CONCRETE_GUESS_POOLS = {
    "fr": CONCRETE_GUESS_WORDS,
    "french": CONCRETE_GUESS_WORDS,
    "en": ENGLISH_CONCRETE_GUESS_WORDS,
    "english": ENGLISH_CONCRETE_GUESS_WORDS,
    "de": GERMAN_CONCRETE_GUESS_WORDS,
    "german": GERMAN_CONCRETE_GUESS_WORDS,
    "es": SPANISH_CONCRETE_GUESS_WORDS,
    "spanish": SPANISH_CONCRETE_GUESS_WORDS,
    "it": ITALIAN_CONCRETE_GUESS_WORDS,
    "italian": ITALIAN_CONCRETE_GUESS_WORDS,
    "nl": DUTCH_CONCRETE_GUESS_WORDS,
    "dutch": DUTCH_CONCRETE_GUESS_WORDS,
    "tr": TURKISH_CONCRETE_GUESS_WORDS,
    "turkish": TURKISH_CONCRETE_GUESS_WORDS,
    "ja(ro)": JAPANESE_ROMAJI_CONCRETE_GUESS_WORDS,
    "japanese": JAPANESE_ROMAJI_CONCRETE_GUESS_WORDS,
}


VERB_LIKE_GUESS_WORDS = {
    "aller", "venir", "manger", "boire", "parler", "comprendre", "apprendre",
    "travailler", "dormir", "ecrire", "lire", "marcher", "courir", "faire",
    "donner", "prendre", "chercher", "trouver", "payer", "aimer", "pouvoir",
    "to go", "to come", "to eat", "to drink", "to speak", "to understand",
    "to learn", "to work", "to sleep", "to write", "to read", "to walk",
    "to run", "to do", "to give", "to take", "to search", "to find", "to pay",
}


def _is_preferred_guess_word(word):
    key = _normalize_original(word)
    if not _is_guessable_word(word):
        return False
    if key in VERB_LIKE_GUESS_WORDS:
        return False
    if key.startswith("je "):
        return False
    return True


def get_guess_words(categories, difficulty="normal", original_language="fr"):
    normalized_original_language = str(original_language).strip().lower() if original_language else ""
    priority_words = LANGUAGE_CONCRETE_GUESS_POOLS.get(
        normalized_original_language,
        CONCRETE_GUESS_WORDS,
    )

    # Difficulty is intentionally ignored: one merged easy/concrete list for all modes.
    target_count = 130

    vocab_keys = set()
    vocab_translation_keys = set()
    for category in categories:
        for word in category["words"]:
            vocab_keys.add(_normalize_original(word.get("original", "")))
            vocab_translation_keys.add(_normalize_original(word.get("translation", "")))

    selected_words = []
    selected_keys = set()

    for candidate in priority_words:
        key = _normalize_original(candidate)
        if key in selected_keys:
            continue
        if key in vocab_keys:
            continue
        if key in vocab_translation_keys:
            continue
        if not _is_preferred_guess_word(candidate):
            continue

        selected_words.append(candidate)
        selected_keys.add(key)
        if len(selected_words) >= target_count:
            break

    return selected_words


def _uniform_categories_with_japanese_reference(lang_code, categories):
    if lang_code == "japanese":
        return categories

    translations_by_original = {}
    for category in categories:
        for word in category["words"]:
            original = word["original"].strip()
            key = _normalize_original(original)
            translation = word.get("translation", "")

            # Keep first non-empty translation when duplicates exist.
            if key not in translations_by_original or (
                not translations_by_original[key] and translation
            ):
                translations_by_original[key] = translation

    reference_categories = VOCABULARY["japanese"]["categories"]
    harmonized_categories = []

    for reference_category in reference_categories:
        harmonized_words = []
        for reference_word in reference_category["words"]:
            original = reference_word["original"]
            key = _normalize_original(original)
            translation = translations_by_original.get(key, "")
            if not translation:
                translation = f"[{original}]"
            harmonized_words.append({
                "original": original,
                "translation": translation,
            })

        harmonized_categories.append({
            "name": reference_category["name"],
            "words": harmonized_words,
        })

    return harmonized_categories


def get_language_data(lang_code, difficulty="normal"):
    lang_data = deepcopy(VOCABULARY[lang_code])
    categories = lang_data["categories"]
    categories = _normalized_easy_categories(categories)
    categories = _curated_vocabulary_categories_with_keys(
        categories,
        target_count=275,
    )

    lang_data["categories"] = _merge_tiny_categories(categories, min_size=3)

    return lang_data