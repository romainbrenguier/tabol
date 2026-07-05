var words = [
    "stylo", "crayon", "gomme", "taille-crayon", "cahier", "trousse", "cartable", "regle", "colle", "ciseaux",
    "papier", "agenda", "dossier", "tampon", "enveloppe", "timbre", "carte", "affiche", "ticket", "badge",
    "ordinateur", "ecran", "clavier", "souris", "telephone", "tablette", "chargeur", "batterie", "prise", "cable",
    "casque", "ecouteurs", "micro", "camera", "telecommande", "lampe", "ampoule", "interrupteur", "alarme", "horloge",
    "porte", "fenetre", "mur", "sol", "plafond", "escalier", "ascenseur", "couloir", "balcon", "garage",
    "canape", "fauteuil", "tabouret", "tapis", "rideau", "coussin", "couverture", "oreiller", "matelas", "etagere",
    "placard", "tiroir", "miroir", "parapluie", "valise", "sac", "portefeuille", "cle", "serrure", "veste",
    "pantalon", "t-shirt", "pull", "manteau", "chapeau", "bonnet", "echarpe", "gant", "chaussette", "chaussure",
    "sandale", "ceinture", "pyjama", "brosse", "savon", "shampoing", "serviette", "peigne", "dentifrice", "rasoir",
    "assiette", "verre", "tasse", "bol", "fourchette", "cuillere", "couteau", "poele", "casserole", "mixeur",
    "frigo", "congelateur", "four", "micro-ondes", "grille-pain", "evier", "robinet", "eponges", "sac-poubelle", "poubelle",
    "beurre", "confiture", "biscuit", "bonbon", "yaourt", "omelette", "pizza", "hamburger", "sandwich", "salami",
    "poivre", "epice", "ketchup", "moutarde", "compote", "gateau", "cookie", "croissant", "baguette", "limonade",
    "pluie", "neige", "nuage", "vent", "orage", "eclair", "arc-en-ciel", "lune", "etoile", "ciel",
    "plage", "desert", "ile", "pont", "tunnel", "phare", "chateau", "musee", "cinema", "ecole",
    "hopital", "pharmacie", "boulangerie", "supermarche", "bibliotheque", "bureau", "usine", "stade", "parc", "statue",
    "velo", "moto", "camion", "taxi", "metro", "tram", "bateau", "scooter", "trottinette", "parking",
    "football", "basket", "tennis", "natation", "danse", "musique", "guitare", "piano", "violon", "chanson",
    "film", "serie", "photo", "dessin", "peinture", "puzzle", "jeu", "jouet", "poupee", "ballon",
    "cerf-volant", "cadeau", "fete", "anniversaire", "vacances", "weekend", "printemps", "ete", "automne", "hiver"
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
