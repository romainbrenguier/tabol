var words = 
  [
    "angle", "armoire", "banc", "bureau", "cabinet", "carreau", "chaise", 
    "classe", "clé", "coin", "couloir", "dossier", "école", "écriture", 
    "entrée", "escalier", "étagère", "étude", "extérieur", "fenêtre",
    "intérieur", "lavabo", "lecture", "marche", "matelas", "maternelle", 
    "meuble", "mousse", "mur", "peluche", "placard", "plafond", "porte",
    "portemanteau", "poubelle", "radiateur", "rampe", "récréation", 
    "rentrée", "rideau", "robinet", "salle", "savon", "serrure", "serviette",
    "siège", "sieste", "silence", "sol", "sommeil", "sonnette", "sortie",
    "tableau", "tabouret", "tapis", "tiroir", "toilette", "vitre",
    "crayon", "stylo", "feutre", "taille-crayon", "pointe", "mine",
    "gomme", "dessin", "coloriage", "rayure", "peinture", "pinceau",
    "couleur", "craie", "papier", "feuille", "cahier", "carnet", "carton",
    "ciseaux", "découpage", "pliage", "pli", "colle", "affaire", "boîte",
    "casier", "caisse", "trousse", "cartable", "jouet", "jeu", "pion", "dé",
    "domino", "puzzle", "cube", "perle", "chose", "carré", "rond",
    "pâte à modeler", "tampon", "histoire", "bibliothèque", "image", "album",
    "titre", "bande dessinée", "conte", "dictionnaire", "magazine", 
    "catalogue", "page", "ligne", "mot", "enveloppe", "étiquette", "affiche",
    "alphabet", "appareil", "caméscope", "cassette", "chanson", "chiffre", 
    "contraire", "différence", "doigt", "écran", "écriture", "film", "idée",
    "instrument", "intrus", "lettre", "liste", "magnétoscope", "main", "micro",
    "modèle", "musique", "nom", "nombre", "orchestre", "ordinateur", "photo",
    "point", "poster", "pouce", "prénom", "question", "radio", "sens",
    "tambour", "télécommande", "téléphone", "télévision", "trait", "trompette",
    "voix", "xylophone",
    "attention", "camarade", "colère", "copain", "coquin", "dame", "directeur",
    "directrice", "droit", "effort", "élève", "enfant", "fatigue", "faute", 
    "gardien", "madame", "maître", "maîtresse", "mensonge", "ordre", "personne",
    "retard", "sourire",
    "arrosoir", "assiette", "balle", "bateau", "boîte", "bouchon", "bouteille",
    "bulles", "canard", "casserole", "cuillère", "cuvette", "douche",
    "entonnoir", "gouttes", "litre", "moulin", "pluie", "poisson", "pont", 
    "pot", "roue", "saladier", "seau", "tablier", "tasse", "trous", "verre",
    "anorak", "arc", "bagage", "baguette", "barbe", "bonnet", "botte", 
    "bouton", "bretelle", "cagoule", "casque", "casquette", "ceinture",
    "chapeau", "chaussette", "chausson", "chaussure", "chemise", "cigarette", 
    "col", "collant", "couronne", "cravate", "culotte", "écharpe", "épée", 
    "fée", "flèche", "fusil", "gant", "habit", "jean", "jupe", "lacet", 
    "laine", "linge", "lunettes", "magicien", "magie", "maillot", "manche", "manteau", "mouchoir", "moufle", "nœud", "paire", "pantalon", "pied", "poche", "prince", "pull-over", "pyjama", "reine", "robe", "roi", "ruban", "semelle", "soldat", "sorcière", "tache", "taille", "talon", "tissu", "tricot", "uniforme", "valise", "veste", "vêtement", 
"aiguille", "ampoule", "avion", "bois", "bout", "bricolage", "bruit", "cabane", "carton", "clou", "colle", "crochet", "élastique", "ficelle", "fil", "marionnette", "marteau", "métal", "mètre", "morceau", "moteur", "objet", "outil", "peinture", "pinceau", "planche", "plâtre", "scie", "tournevis", "vis", "voiture", "véhicule", "accident", "aéroport", "auto", "camion", "engin", "feu", "frein", "fusée", "garage", "gare", "grue", "hélicoptère", "moto", "panne", "parking", "pilote", "pneu", "quai", "train", "virage", "vitesse", "voyage", "wagon", "zigzag", "acrobate", "arrêt", "arrière", "barre", "barreau", "bord", "bras", "cerceau", "chaises", "cheville", "chute", "cœur", "corde", "corps", "côté", "cou", "coude", "cuisse", "danger", "doigts", "dos", "échasses", "échelle", "épaule", "équipe", "escabeau", "fesse", "filet", "fond", "genou", "gymnastique", "hanche", "jambes", "jeu", "mains", "milieu", "montagne", "mur d’escalade", "muscle", "numéro", "ongle", "parcours", "pas", "passerelle", "pente", "peur", "pieds", "plongeoir", "poignet", "poing", "pont de singe", "poutre d’équilibre", "prises", "rivière des crocodiles", "roulade", "saut", "serpent", "sport", "suivant", "tête", "toboggan", "tour", "trampoline", "tunnel", "ventre", "bagarre", "balançoire", "ballon", "bande", "bicyclette", "bille", "cadenas", "cage à écureuil", "cerf-volant", "château", "coup", "cour", "course", "échasse", 
"flaque", "paix", "pardon", "partie", "pédale", "pelle", "pompe", "préau", "raquette", "rayon", "récréation", "sable", "sifflet", "signe", "tas", "tricycle", "tuyau", 
"vélo", "filet", "allumette", "anniversaire", "appétit", "beurre", "coquille", "crêpes", "croûte", "dessert", "envie", "faim", "fève", "four", "galette", "gâteau", "goût", "invitation", "langue", "lèvres", "liquide", "louche", "mie", "moitié", "moule", "odeur", "œuf", "part", "pâte", "pâtisserie", "recette", "rouleau", "sel", "soif", "tarte", "tranche", "yaourt", "glaçon", "jus", "kiwi", "lame", "mûre", "noyau", "paille", "pamplemousse", "râpe",
"bassine", "cocotte", "épluchure", "légume", "pomme de terre", "rondelle", "soupe", "consommé", "potage",
"arête", "femme", "frite", "gobelet", "jambon", "os", "poulet", "purée", "radis", "restaurant", "sole", "animal", "bébés", "bouche", "cage", "câlin", "caresse", "cochon d’Inde", "foin", 
"graines", "hamster", "lapin", "maison", "nez", "œil", "oreille", "patte", "toit", "yeux", "légume", 
"abeille", "agneau", "aile", "âne", "arbre", "bain", "barque", "bassin", "bébé", "bec", "bête", "bœuf", "botte de foin", "boue", 
"bouquet", "bourgeon", "branche", "caillou", "campagne", "car", "champ", "chariot", "chat", "cheminée", "cheval", "chèvre", "chien", "cochon", "colline", "coq", "coquelicot", "crapaud", "cygne", 
"départ", "dindon", "escargot", "étang", "ferme", "fermier", "feuille", "flamme", "fleur", "fontaine", "fumée", "grain", "graine", "grenouille", "griffe", "guêpe", "herbe", "hérisson", "insecte", "jardin", "mare", "marguerite", "miel", "morceau de pain", "mouche", "mouton", "oie", "oiseau", "pierre", "pigeon", "plante", "plume", "poney", "poule", "poussin", "prairie", "rat", "rivière", "route", "tortue", "tracteur", "tulipe", "vache", "vétérinaire", "aigle", "animaux", "aquarium", "bêtes", "cerf", "chouette", "cigogne", "crocodile", "dauphin", "éléphant", "girafe", "hibou", "hippopotame", "kangourou", "lion", "loup", "ours", "panda", "panthère", "perroquet", "phoque", "renard", "requin", "rhinocéros", "singe", "tigre", "zèbre", "zoo", "épingle", "bâton", "bêtise", "bonhomme", "bottes", "canne", "cauchemar", "cri", "danse", "déguisement", "dinosaure", "drapeau", "en argent", "en or", "en rang", "fête", "figure", "géant", "gens", "grand-mère", "grand-père", "joie", "joue", "journaux", "maquillage", "masque", "monsieur", "moustache", "ogre", "princesse", "rue", "trottoir", "Noël", "boule", "cadeau", "canne à pêche", "chance", "cube", "guirlande", "humeur", "papillon", "spectacle", "surprise", "trou", "visage", "âge", "an", "année", "après-midi", "calendrier", "début", "dimanche", "été", "étoile", "fin", "heure des mamans", "heure", "hiver", "horloge", "jeudi", "jour", "journée", "lumière", "lundi", "lune", "mardi", "matin", "mercredi", "midi", "minuit", "minute", "mois", "moment", "montre", "nuit", "ombre", "pendule", "retour", "réveil", "saison", "samedi", "semaine", "soir", "soleil", "temps", "univers", "vacances", "vendredi",
"air", "arc-en-ciel", "brouillard", "ciel", "éclair", "flocon", "goutte", "hirondelle", "luge", "neige", "nuage", "orage", "ouragan", "parapluie", "parasol", "ski", "tempête", "thermomètre", "tonnerre", "traîneau", "vent", "assiette", "balai", "biscuit", "boisson", "bol", "bonbon", "céréale", "confiture", "coquetier", "couteau", "couvercle", "couvert", "cuillère", "cuisine", "cuisinière", "désordre", "dînette", "éponge", "évier", "four", "fourchette", "lait", "lave-linge", "lessive", "machine", "nappe", "pain", "pile", "plat", "plateau", "poêle", "réfrigérateur", "repas", "tartine", "torchon", "vaisselle", "argent", "aspirateur", "bague", "barrette", "bijou", "bracelet", "brosse", "cadre", "canapé", "chambre", "cheveu", "chiffon", "cil", "coffre", "coffret", "collier", "couette", "coussin", "couverture", "dent", "dentifrice", "drap", "fauteuil", "fer à repasser", "frange", "glace", "lampe", "lit", "ménage", "or", "oreiller", "parfum", "peigne", "pouf", "poupée", "poussette", "poussière", "shampoing", "sourcil", "trésor", "tube", "vase", "adulte", "album", "amour", "baiser", "bavoir", "biberon", "bisou", "caprice", "cimetière", "cousin", "cousine", "crèche", "fils", "frère", "grand-parent", "homme", "jumeau", "maman", "mari", "mariage", "mère", "papa", "parent", "père", "petit-enfant", "petit-fils", "petite-fille", "rasoir", "sœur", "ambulance", "bosse", "champignon", "dentiste", "docteur", "fièvre", "front", "gorge", "infirmier", "infirmière", "jambe", "larme", "médecin", "menton", "mine", "ordonnance", "pansement", "peau", "piqûre", "poison", "sang", "santé", "squelette", "trousse",
"araignée", "brouette", "chenille", "coccinelle", "fourmi", "herbe", "jonquille", "lézard", "pâquerette", "rangée", "râteau", "rosé", "souris", "taupe", "terrain", "terre", "terrier", "tige", "ver", "portière", "sac", "billet", "caisse", "farce", "grimace", "grotte", "pays", "regard", "ticket", "bûche", "buisson", "camp", "chasseur", "châtaigne", "chemin", "chêne", "corbeau", "écorce", "écureuil", "forêt", "gourde", "lac", "loupe", "lutin", "marron", "mûre", "moustique", "muguet", "nid", "paysage", "pin", "rocher", "sapin", "sommet", "tente", "adresse", "appartement", "ascenseur", "balcon", "boucherie", "boulanger", "boulangerie", "boutique", "bus", "caniveau", "caravane", "carrefour", "cave", "charcuterie", "cinéma", "cirque", "clin d’œil", "cloche", "clocher", "clown", "coiffeur", "colis-route", "courrier", "croix", "église", "embouteillage", "endroit", "enveloppe", "essence", "facteur", "fleuriste", "foire", "hôpital", "hôtel", "immeuble", "incendie", "laisse", "magasin", "manège", "médicament", "moineau", "monde", "monument", "ouvrier", "palais", "panneau", "paquet", "parc", "passage", "pharmacie", "pharmacien", "piscine", "place", "police", "policier", "pompier", "poste", "promenade", "quartier", "square", "timbre", "travaux", "usine", "village", "ville", "voisin", "volet", "abricot", "ail", "aliment", "ananas", "banane", "bifteck", "café", "carotte", "cerise", "chocolat", "chou", "citron", "citrouille", "clémentine", "concombre", "coquillage", "corbeille", "crabe", "crevette", "endive", "farine", "fraise", "framboise", "fromage", "fruit", "gâteau", "haricot", "huile", "légume", "marchand", "melon", "monnaie", "navet", "noisette", "noix", "nourriture", "oignon", "orange", "panier", "pâtes", "pêche", "persil", "petit pois", "poire", "poireau", "pomme", "pomme de terre", "prix", "prune", "queue", "raisin", "riz", "salade", "sucre", "thé", "tomate", "viande", "vin",
"  baleine", "bouée", "île", "jumelles", "marin", "mer", "mouette", "navire", "pêcheur", "plage", "poisson", "port", "sardine", "serviette", "vague", "voile",
    "amener", "apporter", "appuyer", "s'asseoir", "attendre", "bâiller",
    "bosser", "se coucher", "éclairer", "emmener", "emporter", "s'endormir", 
    "s ennuyer", "étudier", "fermer", "frapper", "s'installer", "se lever",
    "se presser", "se réchauffer", "rentrer", "se reposer", "rester", 
    "se réveiller", "sonner", "tricher",
    "chanter", "chercher", "choisir", "chuchoter", "coller", "colorier",
    "commencer", "comparer", "compter", "construire", "continuer", "copier", 
    "couper", "déchirer", "décoller", "décorer", "découper", "demander",
    "démolir", "se dépêcher", "dessiner", "discuter", "écouter", "effacer", 
    "entourer", "envoyer", "fouiller", "goûter", "imiter", "laisser", "mettre",
    "montrer", "peindre", "plier", "poser", "préparer", "ranger", "réciter",
    "recommencer", "remettre", "répéter", "répondre", "sentir", "souligner",
    "tailler", "se taire", "tenir", "terminer", "toucher", "trier",
    "aider", "défendre", "désobéir", "distribuer", "échanger", "s'excuser",
    "expliquer", "se fâcher", "gronder", "obéir", "obliger", "partager",
    "prêter", "priver", "promettre", "punir", "se quitter", "raconter", 
    "refuser", "séparer",
    "agiter", "s'amuser", "arroser", "attraper", "avancer", "baigner",
    "barboter", "boucher", "bouger", "déborder", "doucher", "éclabousser", 
    "essuyer", "envoyer", "flotter", "gonfler", "inonder", "jouer", "laver",
    "mélanger", "mouiller", "nager", "patauger", "pleuvoir", "plonger",
    "pousser", "pouvoir", "presser", "recevoir", "remplir", "renverser",
    "sécher", "serrer", "souffler", "tirer", "tourner", "tremper", "verser",
    "vider", "vouloir", 
    "se changer", "se chausser", "se couvrir", "se déguiser", "se déshabiller", "enlever", "s’habiller", "lacer", "porter", "ressembler",
    "arracher", "attacher", "casser", "coudre", "détruire", "s’écorcher", "enfiler", "enfoncer", "fabriquer", "mesurer", "percer", "se pincer", "réparer", "réussir", "servir", "taper", "trouer",
"s’arrêter", "atterrir", "bouder", "charger", "conduire", "démarrer", "disparaître", "donner", "écraser", "s’envoler", "garder", "se garer", "manquer", "partir", "se poser", "reculer", "rouler", "tendre", "transporter", "voler", "s’accrocher", "s’appuyer", "arriver", "se baisser", "se balancer", "bondir", "bousculer", "se cogner", "courir", "danser", "dépasser", "descendre", "écarter", "escalader", "gagner", "gêner", "glisser", "grimper", "marcher à quatre pattes", "marcher sur", "se mettre debout", "monter", "se pencher", "se percher", "perdre", "ramper", "rater", "remplacer", "respirer", "se retourner", "revenir", "sauter", "soulever", "suivre", "tomber", "transpirer", "traverser", "se bagarrer", "se battre", "se cacher", "cracher", "creuser", "crier", "se dégonfler", "se disputer", "empêcher", "galoper", "hurler", "jongler", "lancer", "pédaler", "se plaindre", "pleurer", "poursuivre", "protéger", "saigner", "se salir", "siffler", "surveiller", "traîner", "trouver", "aimer", "allumer", "avaler", "battre", "se brûler", "chauffer", "cuire", "étaler", "éteindre", "falloir", "inviter", "jeter", "lécher", "oublier", "se régaler", "remercier", "remuer", "souhaiter", "sucer", "croquer", "éplucher", "râper", "bouillir", "mixer",
"   déjeuner", "accoucher", "agacer", "appeler", "câliner", "caresser", "changer", "déranger", "s’échapper", "élever", "enfermer", "enterrer", "gratter", "grignoter", "installer", "lâcher", "mordre", "mourir", "naître", "nourrir", "s’occuper de", "se promener", "ronger", "se sauver", "soigner", "téter", "vivre", "voir",
"accompagner", "se baigner", "courir après", "couver", "donner à manger", "faire boire", "fumer", "griffer", "habiter", "piquer", "ramasser", "traire",
"déguiser", "défiler", "éclater", "essayer", "marcher", "se moquer", "plaire", "rencontrer", "ressembler à", "retourner", "rêver", "rire", "taper sur", "danser", "sauter", "chanter",
"   faire peur", "lever", "maquiller",
"   avancer", "briller", "dîner", "grandir", "retarder",
"s’abriter", "faire beau", "geler", "se mouiller", "neiger", "se tromper", "pleuvoir",
"accrocher", "balayer", "boire", "frotter", "manger", "nettoyer", "se servir", "cuisiner",
"s’allonger", "se coiffer", "hésiter", "se laver", "se maquiller", "passer", "préférer", "repasser", "se sécher", "secouer", "téléphoner",
"s’agiter", "s’appeler", "baver", "bercer", "se blottir", "consoler", "déménager", "se détester", "s’embrasser", "se marier", "offrir", "penser", "se rappeler", "se raser", "ronfler", "se serrer", "tricoter",
"aller bien", "attraper une maladie", "se blesser", "détester", "devoir", "éternuer", "se gratter", "guérir", "se moucher", "ne pas oublier", "se protéger", "recoudre", "souffrir", "tâter", "tousser", "trembler",
"cueillir", "jardiner", "se faner", "s’ouvrir", "planter", "voyager", "se doucher", "tuer",
"camper", "chasser", "s’éloigner ", "entendre", "s’envoler", "griller", "grimper", "guetter", "s’imaginer", "jeter", "lancer", "manger", "marcher", "montrer", "se mouiller", "patauger", "se percher", "se perdre", "photographier", "pique-niquer", "pleuvoir", "poser", "poursuivre", "ramasser", "regarder", "rencontrer", "se reposer", "respirer", "revoir", "rêver", "sentir", "siffler", "transpirer", "traverser", "trouver", "vivre",
"barrer", "clignoter", "se croiser", "garer", "photographier", "reconnaître", "retrouver", "revoir", "saluer", "savoir", "se toucher", "se trouver", "visiter",
"acheter", "ajouter", "coûter", "payer", "peser", "rendre", "vendre",
"se noyer", "ramer", "nager"
  ];

function nextWord() {
    var i = Math.floor(Math.random () * words.length);
    var word = words[i];
    document.getElementById('word').innerHTML = word;
}

function initializeClock(id, endtime){
    var clock = document.getElementById(id);
    var t = endtime;
    clock.innerHTML = t + ' sec.';
    var timeinterval = setInterval(function(){
	t = t - 1;
	clock.innerHTML = t + ' sec.';
	if(t<0){
	    clearInterval(timeinterval);
	    alert("Time's up");
	}
    },1000);
}

// initializeClock('clockdiv',100);
nextWord();
