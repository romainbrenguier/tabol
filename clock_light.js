var words = 
  [
      "beurre", "jus", "kiwi", "lame", "mûre", "pamplemousse",
      "pomme de terre", "soupe", "arête",  "frite", "jambon", "os", "poulet", "purée", "radis", "restaurant", "sole", "animal", "bébés", "bouche", "cage", "câlin", "caresse", "cochon d’Inde", "foin", 
"graines", "hamster", "lapin", "maison", "nez", "œil", "oreille", "patte", "toit", "yeux", "légume", 
"abeille", "agneau", "aile", "âne", "arbre", "bain", "barque", "bassin", "bébé", "bec", "bête", "bœuf", "botte de foin", "boue", 
"bouquet", "bourgeon", "branche", "caillou", "campagne", "car", "champ", "chariot", "chat", "cheminée", "cheval", "chèvre", "chien", "cochon", "colline", "coq", "coquelicot", "crapaud", "cygne", 
"départ", "dindon", "escargot", "étang", "ferme", "fermier", "feuille", "flamme", "fleur", "fontaine", "fumée", "grain", "graine", "grenouille", "griffe", "guêpe", "herbe", "hérisson", "insecte", "jardin", "mare", "marguerite", "miel", "morceau de pain", "mouche", "mouton", "oie", "oiseau", "pierre", "pigeon", "plante", "plume", "poney", "poule", "poussin", "prairie", "rat", "rivière", "route", "tortue", "tracteur", "tulipe", "vache", "vétérinaire", "aigle", "animaux", "aquarium", "bêtes", "cerf", "chouette", "cigogne", "crocodile", "dauphin", "éléphant", "girafe", "hibou", "hippopotame", "kangourou", "lion", "loup", "ours", "panda", "panthère", "perroquet", "phoque", "renard", "requin", "rhinocéros", "singe", "tigre", "zèbre"
 "abricot", "ail", "aliment", "ananas", "banane", "bifteck", "café", "carotte", "cerise", "chocolat", "chou", "citron", "citrouille", "clémentine", "concombre", "coquillage", "corbeille", "crabe", "crevette", "endive", "farine", "fraise", "framboise", "fromage", "fruit", "gâteau", "haricot", "huile", "légume", "marchand", "melon", "monnaie", "navet", "noisette", "noix", "nourriture", "oignon", "orange", "panier", "pâtes", "pêche", "persil", "petit pois", "poire", "poireau", "pomme", "pomme de terre", "prix", "prune", "queue", "raisin", "riz", "salade", "sucre", "thé", "tomate", "viande", "vin",
"baleine"
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
