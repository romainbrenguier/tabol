var words = 
  [
      "beurre", "jus", "kiwi", "lame", "mure", "pamplemousse",
      "pomme de terre", "soupe", "arête",  "frite", "jambon", "os", "poulet", "puree", "radis", "restaurant", "sole", "animal", "bebes", "bouche", "cage", "câlin", "caresse", "cochon d’Inde", "foin", 
"graines", "hamster", "lapin", "maison", "nez", "oeil", "oreille", "patte", "toit", "yeux", "legume", 
"abeille", "agneau", "aile", "âne", "arbre", "bain", "barque", "bassin", "bebe", "bec", "bête", "bœuf", "botte de foin", "boue", 
"bouquet", "bourgeon", "branche", "caillou", "campagne", "car", "champ", "chariot", "chat", "cheminee", "cheval", "chèvre", "chien", "cochon", "colline", "coq", "coquelicot", "crapaud", "cygne", 
"depart", "dindon", "escargot", "etang", "ferme", "fermier", "feuille", "flamme", "fleur", "fontaine", "fumee", "grain", "graine", "grenouille", "griffe", "guêpe", "herbe", "herisson", "insecte", "jardin", "mare", "marguerite", "miel", "morceau de pain", "mouche", "mouton", "oie", "oiseau", "pierre", "pigeon", "plante", "plume", "poney", "poule", "poussin", "prairie", "rat", "rivière", "route", "tortue", "tracteur", "tulipe", "vache", "veterinaire", "aigle", "animaux", "aquarium", "bêtes", "cerf", "chouette", "cigogne", "crocodile", "dauphin", "elephant", "girafe", "hibou", "hippopotame", "kangourou", "lion", "loup", "ours", "panda", "panthère", "perroquet", "phoque", "renard", "requin", "rhinoceros", "singe", "tigre", "zèbre",
 "abricot", "ail", "aliment", "ananas", "banane", "bifteck", "cafe", "carotte", "cerise", "chocolat", "chou", "citron", "citrouille", "clementine", "concombre", "coquillage", "corbeille", "crabe", "crevette", "endive", "farine", "fraise", "framboise", "fromage", "fruit", "gâteau", "haricot", "huile", "legume", "marchand", "melon", "monnaie", "navet", "noisette", "noix", "nourriture", "oignon", "orange", "panier", "pâtes", "pêche", "persil", "petit pois", "poire", "poireau", "pomme", "pomme de terre", "prix", "prune", "queue", "raisin", "riz", "salade", "sucre", "the", "tomate", "viande", "vin", "baleine" ];

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
