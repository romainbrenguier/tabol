from copy import deepcopy


VOCABULARY = {
    "japanese": {
        "display_name": "Japonais",
        "categories": [
            {
                "name": "Alimentation",
                "words": [
                    {
                        "original": "nourriture",
                        "translation": "tabemono"
                    },
                    {
                        "original": "fruit",
                        "translation": "kudamono"
                    },
                    {
                        "original": "légumes",
                        "translation": "yasai"
                    },
                    {
                        "original": "fromage",
                        "translation": "chiizu"
                    },
                    {
                        "original": "pain",
                        "translation": "pan"
                    },
                    {
                        "original": "animal",
                        "translation": "doobutsu"
                    },
                    {
                        "original": "viande",
                        "translation": "niku"
                    },
                    {
                        "original": "poisson",
                        "translation": "sakana"
                    },
                    {
                        "original": "sucre",
                        "translation": "satoo"
                    },
                    {
                        "original": "riz",
                        "translation": "kome"
                    },
                    {
                        "original": "sel",
                        "translation": "shio"
                    },
                    {
                        "original": "café",
                        "translation": "koohii"
                    },
                    {
                        "original": "thé",
                        "translation": "ocha"
                    },
                    {
                        "original": "eau",
                        "translation": "mizu"
                    },
                    {
                        "original": "lait",
                        "translation": "gyuunyuu"
                    },
                    {
                        "original": "huile",
                        "translation": "abura"
                    },
                    {
                        "original": "bière",
                        "translation": "biiru"
                    },
                    {
                        "original": "vin",
                        "translation": "wain"
                    }
                ]
            },
            {
                "name": "Corps & Objets",
                "words": [
                    {
                        "original": "travail",
                        "translation": "shigoto"
                    },
                    {
                        "original": "argent",
                        "translation": "o kane"
                    },
                    {
                        "original": "livre",
                        "translation": "hon"
                    },
                    {
                        "original": "television",
                        "translation": "terebi"
                    },
                    {
                        "original": "vêtement",
                        "translation": "yoofuku"
                    },
                    {
                        "original": "tête",
                        "translation": "atama"
                    },
                    {
                        "original": "cheveux",
                        "translation": "kami no ke"
                    },
                    {
                        "original": "oeil",
                        "translation": "me"
                    },
                    {
                        "original": "oreille",
                        "translation": "mimi"
                    },
                    {
                        "original": "nez",
                        "translation": "ha"
                    },
                    {
                        "original": "bouche",
                        "translation": "kuchi"
                    },
                    {
                        "original": "dent",
                        "translation": "ha"
                    },
                    {
                        "original": "main",
                        "translation": "te"
                    },
                    {
                        "original": "pied",
                        "translation": "ashi"
                    }
                ]
            },
            {
                "name": "Divers",
                "words": [
                    {
                        "original": "quoi?",
                        "translation": "nani"
                    },
                    {
                        "original": "rien",
                        "translation": "nanimo"
                    },
                    {
                        "original": "quelques chose",
                        "translation": "nanika"
                    },
                    {
                        "original": "tout",
                        "translation": "subete"
                    },
                    {
                        "original": "chaque",
                        "translation": "kaku"
                    },
                    {
                        "original": "?",
                        "translation": "ka"
                    },
                    {
                        "original": "il y a",
                        "translation": "arimasu"
                    },
                    {
                        "original": "il n'y a pas",
                        "translation": "arimasen"
                    },
                    {
                        "original": "y a t'il?",
                        "translation": "arimasu ka?"
                    },
                    {
                        "original": "c'est",
                        "translation": "desu"
                    },
                    {
                        "original": "ce n'est pas []",
                        "translation": "[] dewa arimasen"
                    },
                    {
                        "original": "je veux",
                        "translation": "-tai"
                    },
                    {
                        "original": "j'aime []",
                        "translation": "[] ga suki desu"
                    },
                    {
                        "original": "je dois []",
                        "translation": "[] hitsuyoo ga arimasu"
                    },
                    {
                        "original": "j'ai besoin de []",
                        "translation": "[] ga hitsuyoo"
                    },
                    {
                        "original": "c'est pas la peine",
                        "translation": "kekko desu"
                    },
                    {
                        "original": "je vais []",
                        "translation": "[] ni ikimasu"
                    },
                    {
                        "original": "je connais []",
                        "translation": "[] o shitte iru"
                    },
                    {
                        "original": "je sais que",
                        "translation": "[] o shitte imasu"
                    },
                    {
                        "original": "je peux []",
                        "translation": "[] koto ga dekimasu"
                    },
                    {
                        "original": "je pense que []",
                        "translation": "[] to omoimasu"
                    },
                    {
                        "original": "peut-être",
                        "translation": "tabun"
                    },
                    {
                        "original": "c'est possible",
                        "translation": "dekimasu"
                    },
                    {
                        "original": "mais",
                        "translation": "demo"
                    },
                    {
                        "original": "et",
                        "translation": "to"
                    },
                    {
                        "original": "ou",
                        "translation": "soretomo"
                    },
                    {
                        "original": "donc",
                        "translation": "dakara"
                    },
                    {
                        "original": "puis",
                        "translation": "sorekara"
                    },
                    {
                        "original": "alors",
                        "translation": "(sore)dewa"
                    },
                    {
                        "original": "parce que",
                        "translation": "kara"
                    },
                    {
                        "original": "par example",
                        "translation": "tatoeba"
                    },
                    {
                        "original": "pourquoi",
                        "translation": "naze"
                    },
                    {
                        "original": "quel(le,s)",
                        "translation": "dore"
                    },
                    {
                        "original": "quelle sorte",
                        "translation": "donna"
                    },
                    {
                        "original": "présent",
                        "translation": "-(i)masu"
                    },
                    {
                        "original": "neg. prés.",
                        "translation": "-(i)masen"
                    }
                ]
            },
            {
                "name": "Verbes d'action",
                "words": [
                    {
                        "original": "marcher",
                        "translation": "aruku"
                    },
                    {
                        "original": "se promener",
                        "translation": "urokku"
                    },
                    {
                        "original": "aller",
                        "translation": "iku"
                    },
                    {
                        "original": "venir",
                        "translation": "k(uru)"
                    },
                    {
                        "original": "partir",
                        "translation": "nokoshimasu"
                    },
                    {
                        "original": "attendre",
                        "translation": "matsu"
                    },
                    {
                        "original": "écrire",
                        "translation": "kaku"
                    },
                    {
                        "original": "lire",
                        "translation": "yomu"
                    },
                    {
                        "original": "commencer",
                        "translation": "hajimeru"
                    },
                    {
                        "original": "finir",
                        "translation": "owaru"
                    },
                    {
                        "original": "rester",
                        "translation": "nokoru"
                    },
                    {
                        "original": "passer",
                        "translation": "yoru"
                    },
                    {
                        "original": "entrer",
                        "translation": "hairu"
                    },
                    {
                        "original": "tourner",
                        "translation": "magaru"
                    },
                    {
                        "original": "s'asseoir",
                        "translation": "suwaru"
                    },
                    {
                        "original": "sortir",
                        "translation": "deru"
                    },
                    {
                        "original": "courir",
                        "translation": "hashiru"
                    },
                    {
                        "original": "regarder",
                        "translation": "mimasu"
                    },
                    {
                        "original": "voir",
                        "translation": "[] ga miemasu"
                    },
                    {
                        "original": "écouter",
                        "translation": "kiku"
                    },
                    {
                        "original": "boire",
                        "translation": "nomu"
                    },
                    {
                        "original": "prendre",
                        "translation": "toru"
                    },
                    {
                        "original": "acheter",
                        "translation": "kau"
                    },
                    {
                        "original": "tenir",
                        "translation": "hoji shimasu"
                    },
                    {
                        "original": "manger",
                        "translation": "tabemasu"
                    },
                    {
                        "original": "dormir",
                        "translation": "n(eru)"
                    },
                    {
                        "original": "faire",
                        "translation": "suru"
                    },
                    {
                        "original": "travailler",
                        "translation": "hataraite imasu"
                    },
                    {
                        "original": "penser",
                        "translation": "[] to omoimasu"
                    },
                    {
                        "original": "chercher",
                        "translation": "sagasu"
                    },
                    {
                        "original": "trouver []",
                        "translation": "[] ga mitsukarimasu"
                    },
                    {
                        "original": "donner",
                        "translation": "ataeru"
                    },
                    {
                        "original": "avoir",
                        "translation": "motte imasu"
                    },
                    {
                        "original": "payer",
                        "translation": "harau"
                    },
                    {
                        "original": "parler",
                        "translation": "hanasu"
                    },
                    {
                        "original": "dire",
                        "translation": "iu"
                    },
                    {
                        "original": "demander",
                        "translation": "tatomu"
                    },
                    {
                        "original": "comprendre",
                        "translation": "wakaru"
                    },
                    {
                        "original": "apprendre",
                        "translation": "manabu"
                    },
                    {
                        "original": "habiter à []",
                        "translation": "[] ni sunde imasu"
                    }
                ]
            },
            {
                "name": "Social & Famille",
                "words": [
                    {
                        "original": "enfant",
                        "translation": "kodomo"
                    },
                    {
                        "original": "garçon",
                        "translation": "otoko no ko"
                    },
                    {
                        "original": "fille",
                        "translation": "annanoko"
                    },
                    {
                        "original": "fils",
                        "translation": "musuko"
                    },
                    {
                        "original": "mère",
                        "translation": "okaasan"
                    },
                    {
                        "original": "père",
                        "translation": "otoosan"
                    },
                    {
                        "original": "frère",
                        "translation": "ani"
                    },
                    {
                        "original": "soeur",
                        "translation": "ane"
                    },
                    {
                        "original": "ami(e)",
                        "translation": "yuujin"
                    },
                    {
                        "original": "mari",
                        "translation": "otto"
                    },
                    {
                        "original": "femme",
                        "translation": "tsuma"
                    },
                    {
                        "original": "mon épouse",
                        "translation": "kanai"
                    }
                ]
            },
            {
                "name": "Pronoms & Lieux",
                "words": [
                    {
                        "original": "qui",
                        "translation": "dare"
                    },
                    {
                        "original": "personne",
                        "translation": "daremo"
                    },
                    {
                        "original": "quelqu'un",
                        "translation": "dareka"
                    },
                    {
                        "original": "tout le monde",
                        "translation": "mina"
                    },
                    {
                        "original": "humain",
                        "translation": "jin"
                    },
                    {
                        "original": "moi",
                        "translation": "watashi"
                    },
                    {
                        "original": "toi",
                        "translation": "kimi"
                    },
                    {
                        "original": "il/elle",
                        "translation": "kare/kanojo"
                    },
                    {
                        "original": "nous",
                        "translation": "ware ware"
                    },
                    {
                        "original": "vous",
                        "translation": "anata (kata)"
                    },
                    {
                        "original": "ils",
                        "translation": "karera"
                    },
                    {
                        "original": "de []",
                        "translation": "[] no"
                    },
                    {
                        "original": "ceci",
                        "translation": "kore"
                    },
                    {
                        "original": "cela",
                        "translation": "sore"
                    },
                    {
                        "original": "ce [] ci",
                        "translation": "kono"
                    },
                    {
                        "original": "ce [] là",
                        "translation": "sono []"
                    },
                    {
                        "original": "où",
                        "translation": "doko"
                    },
                    {
                        "original": "nulle-part",
                        "translation": "doko ni mo"
                    },
                    {
                        "original": "quelques-part",
                        "translation": "doko ka"
                    },
                    {
                        "original": "partout",
                        "translation": "doko ni demo"
                    },
                    {
                        "original": "ici",
                        "translation": "koko"
                    },
                    {
                        "original": "là",
                        "translation": "soko"
                    },
                    {
                        "original": "là-bas",
                        "translation": "asoko"
                    },
                    {
                        "original": "en bas",
                        "translation": "shita"
                    },
                    {
                        "original": "devant",
                        "translation": "mae"
                    },
                    {
                        "original": "derrière",
                        "translation": "ushiro"
                    },
                    {
                        "original": "à gauche",
                        "translation": "hadari"
                    },
                    {
                        "original": "droite (de [])",
                        "translation": "([] no) migi"
                    },
                    {
                        "original": "l'intérieur",
                        "translation": "uchi"
                    }
                ]
            },
            {
                "name": "Maison & Ville",
                "words": [
                    {
                        "original": "l'exterieur",
                        "translation": "soto"
                    },
                    {
                        "original": "tout droit",
                        "translation": "masugu"
                    },
                    {
                        "original": "dessus",
                        "translation": "ue"
                    },
                    {
                        "original": "vers",
                        "translation": "mukatte"
                    },
                    {
                        "original": "à côté",
                        "translation": "soba ni"
                    },
                    {
                        "original": "maison",
                        "translation": "ie"
                    },
                    {
                        "original": "cuisine",
                        "translation": "daidokoro"
                    },
                    {
                        "original": "chambre",
                        "translation": "shin shitsu"
                    },
                    {
                        "original": "lit",
                        "translation": "beddo"
                    },
                    {
                        "original": "salle de bain",
                        "translation": "toire"
                    },
                    {
                        "original": "table",
                        "translation": "teeburu"
                    },
                    {
                        "original": "chaise",
                        "translation": "isu"
                    },
                    {
                        "original": "arbre",
                        "translation": "ki"
                    },
                    {
                        "original": "soleil",
                        "translation": "taiyoo"
                    },
                    {
                        "original": "montagne",
                        "translation": "yama"
                    },
                    {
                        "original": "forêt",
                        "translation": "shinrin"
                    },
                    {
                        "original": "mer",
                        "translation": "umi"
                    },
                    {
                        "original": "ville",
                        "translation": "tokai"
                    },
                    {
                        "original": "rue",
                        "translation": "gairo"
                    },
                    {
                        "original": "magasin",
                        "translation": "omise"
                    },
                    {
                        "original": "avion",
                        "translation": "hikooki"
                    },
                    {
                        "original": "voiture",
                        "translation": "kuruma"
                    },
                    {
                        "original": "bus",
                        "translation": "basu"
                    },
                    {
                        "original": "train",
                        "translation": "densha"
                    },
                    {
                        "original": "transport",
                        "translation": "kootsuu"
                    },
                    {
                        "original": "pays",
                        "translation": "kuni"
                    },
                    {
                        "original": "France",
                        "translation": "furansu"
                    },
                    {
                        "original": "Angleterre",
                        "translation": "igirisu"
                    },
                    {
                        "original": "voyage",
                        "translation": "ryokoo"
                    }
                ]
            },
            {
                "name": "Temps",
                "words": [
                    {
                        "original": "quand",
                        "translation": "itsu"
                    },
                    {
                        "original": "temps",
                        "translation": "jikan"
                    },
                    {
                        "original": "jamais",
                        "translation": "kesshite"
                    },
                    {
                        "original": "parfois",
                        "translation": "tokidoki"
                    },
                    {
                        "original": "souvent",
                        "translation": "shibashiba"
                    },
                    {
                        "original": "toujours",
                        "translation": "tsuneni"
                    },
                    {
                        "original": "année",
                        "translation": "nen"
                    },
                    {
                        "original": "cette année",
                        "translation": "kotoshi"
                    },
                    {
                        "original": "an",
                        "translation": "toshi"
                    },
                    {
                        "original": "mois",
                        "translation": "tsuki"
                    },
                    {
                        "original": "semaine",
                        "translation": "shuu"
                    },
                    {
                        "original": "jour",
                        "translation": "nichi"
                    },
                    {
                        "original": "heure",
                        "translation": "jikan"
                    },
                    {
                        "original": "minute",
                        "translation": "fun"
                    },
                    {
                        "original": "seconde",
                        "translation": "byou"
                    },
                    {
                        "original": "avant",
                        "translation": "mae"
                    },
                    {
                        "original": "après",
                        "translation": "ato"
                    },
                    {
                        "original": "maintenant",
                        "translation": "ima"
                    },
                    {
                        "original": "après",
                        "translation": "ato no"
                    },
                    {
                        "original": "tout de suite",
                        "translation": "sugu"
                    },
                    {
                        "original": "matin",
                        "translation": "gozen"
                    },
                    {
                        "original": "après-midi",
                        "translation": "gogo"
                    }
                ]
            },
            {
                "name": "Temps (suite) & État",
                "words": [
                    {
                        "original": "soir",
                        "translation": "yuugata"
                    },
                    {
                        "original": "nuit",
                        "translation": "yoru"
                    },
                    {
                        "original": "aujourd'hui",
                        "translation": "kyoo"
                    },
                    {
                        "original": "demain",
                        "translation": "ashita"
                    },
                    {
                        "original": "hier",
                        "translation": "kinoo"
                    },
                    {
                        "original": "tôt",
                        "translation": "hayaku"
                    },
                    {
                        "original": "bientôt",
                        "translation": "sugu ni"
                    },
                    {
                        "original": "prochain",
                        "translation": "kondo no, tsugi"
                    },
                    {
                        "original": "tard",
                        "translation": "osoi"
                    },
                    {
                        "original": "dernier",
                        "translation": "saishuu"
                    },
                    {
                        "original": "déjà",
                        "translation": "moo"
                    },
                    {
                        "original": "depuis",
                        "translation": "kara, sonogo"
                    },
                    {
                        "original": "jusqu'à",
                        "translation": "made"
                    },
                    {
                        "original": "pas encore",
                        "translation": "mada"
                    },
                    {
                        "original": "de nouveau",
                        "translation": "mata"
                    },
                    {
                        "original": "comment",
                        "translation": "ikaga"
                    },
                    {
                        "original": "loin",
                        "translation": "tooi"
                    },
                    {
                        "original": "près",
                        "translation": "chikai"
                    },
                    {
                        "original": "vide",
                        "translation": "karapo"
                    },
                    {
                        "original": "plein",
                        "translation": "ippai"
                    },
                    {
                        "original": "ouvert",
                        "translation": "aitemasu"
                    },
                    {
                        "original": "fermé",
                        "translation": "heiten"
                    },
                    {
                        "original": "nouveau",
                        "translation": "atarashii"
                    },
                    {
                        "original": "bon",
                        "translation": "oishii"
                    },
                    {
                        "original": "mauvais",
                        "translation": "warui"
                    }
                ]
            },
            {
                "name": "Adjectifs",
                "words": [
                    {
                        "original": "(j'ai) faim",
                        "translation": "onaka (ga akimashita)"
                    },
                    {
                        "original": "chaud",
                        "translation": "atsui"
                    },
                    {
                        "original": "froid",
                        "translation": "samui"
                    },
                    {
                        "original": "beau",
                        "translation": "kirei"
                    },
                    {
                        "original": "bien",
                        "translation": "(yo(rosh))ii"
                    },
                    {
                        "original": "ancien",
                        "translation": "furui"
                    },
                    {
                        "original": "jeune",
                        "translation": "wakai"
                    },
                    {
                        "original": "malade",
                        "translation": "byooki"
                    },
                    {
                        "original": "vite",
                        "translation": "hayai"
                    },
                    {
                        "original": "lent",
                        "translation": "osoi"
                    },
                    {
                        "original": "célèbre",
                        "translation": "yuumei"
                    },
                    {
                        "original": "content",
                        "translation": "ureshii"
                    },
                    {
                        "original": "gentil",
                        "translation": "yasashii"
                    },
                    {
                        "original": "intéressant",
                        "translation": "omoshiroi"
                    },
                    {
                        "original": "fatigué",
                        "translation": "tsukata"
                    },
                    {
                        "original": "interdit",
                        "translation": "kinshi"
                    },
                    {
                        "original": "prêt",
                        "translation": "yooi"
                    },
                    {
                        "original": "sale",
                        "translation": "yogoreteiru"
                    },
                    {
                        "original": "propre",
                        "translation": "kirei"
                    },
                    {
                        "original": "haut",
                        "translation": "takai"
                    },
                    {
                        "original": "bas",
                        "translation": "hikui"
                    },
                    {
                        "original": "facile",
                        "translation": "kantan"
                    },
                    {
                        "original": "difficile",
                        "translation": "muzukashii"
                    },
                    {
                        "original": "important",
                        "translation": "juuyoo"
                    },
                    {
                        "original": "cher",
                        "translation": "takai"
                    }
                ]
            },
            {
                "name": "Adjectifs & Divers",
                "words": [
                    {
                        "original": "grand",
                        "translation": "ookii"
                    },
                    {
                        "original": "petit",
                        "translation": "chiisai"
                    },
                    {
                        "original": "lourd",
                        "translation": "omoi"
                    },
                    {
                        "original": "autre",
                        "translation": "hoka no"
                    },
                    {
                        "original": "different",
                        "translation": "koto"
                    },
                    {
                        "original": "comme",
                        "translation": "sonna ni"
                    },
                    {
                        "original": "comme ça",
                        "translation": "sonna ni"
                    },
                    {
                        "original": "ainsi",
                        "translation": "soo"
                    },
                    {
                        "original": "aussi",
                        "translation": "mo"
                    },
                    {
                        "original": "pour []",
                        "translation": "[] no tame"
                    },
                    {
                        "original": "avec",
                        "translation": "to"
                    },
                    {
                        "original": "sans",
                        "translation": "nashi"
                    },
                    {
                        "original": "seul",
                        "translation": "jibun"
                    },
                    {
                        "original": "ensemble",
                        "translation": "issho"
                    },
                    {
                        "original": "couleur",
                        "translation": "iro"
                    },
                    {
                        "original": "bleu",
                        "translation": "ao"
                    },
                    {
                        "original": "rouge",
                        "translation": "aka"
                    },
                    {
                        "original": "vert",
                        "translation": "midori"
                    },
                    {
                        "original": "jaune",
                        "translation": "ki iro"
                    },
                    {
                        "original": "blanc",
                        "translation": "shiro"
                    },
                    {
                        "original": "noir",
                        "translation": "kuro"
                    },
                    {
                        "original": "combien",
                        "translation": "ikutsu"
                    },
                    {
                        "original": "0",
                        "translation": "zero"
                    },
                    {
                        "original": "1",
                        "translation": "ichi"
                    },
                    {
                        "original": "2",
                        "translation": "ni"
                    }
                ]
            },
            {
                "name": "Chiffres & Quantité",
                "words": [
                    {
                        "original": "3",
                        "translation": "san"
                    },
                    {
                        "original": "4",
                        "translation": "shi"
                    },
                    {
                        "original": "5",
                        "translation": "go"
                    },
                    {
                        "original": "6",
                        "translation": "roku"
                    },
                    {
                        "original": "7",
                        "translation": "shichi"
                    },
                    {
                        "original": "8",
                        "translation": "hachi"
                    },
                    {
                        "original": "9",
                        "translation": "kyuu"
                    },
                    {
                        "original": "10",
                        "translation": "juu"
                    },
                    {
                        "original": "11",
                        "translation": "juu ichi"
                    },
                    {
                        "original": "12",
                        "translation": "juu ni"
                    },
                    {
                        "original": "20",
                        "translation": "ni juu"
                    },
                    {
                        "original": "100",
                        "translation": "hyaku"
                    },
                    {
                        "original": "1000",
                        "translation": "sen"
                    },
                    {
                        "original": "10000",
                        "translation": "man"
                    },
                    {
                        "original": "un peu",
                        "translation": "chotto, shooshoo"
                    },
                    {
                        "original": "moins",
                        "translation": "miman"
                    },
                    {
                        "original": "environ",
                        "translation": "kurai"
                    },
                    {
                        "original": "assez",
                        "translation": "juubun"
                    },
                    {
                        "original": "plus",
                        "translation": "motto"
                    },
                    {
                        "original": "plus que []",
                        "translation": "[] yori"
                    },
                    {
                        "original": "le plus",
                        "translation": "mottomo"
                    },
                    {
                        "original": "beaucoup",
                        "translation": "takusan"
                    },
                    {
                        "original": "très",
                        "translation": "totemo"
                    },
                    {
                        "original": "trop",
                        "translation": "amarinimo"
                    },
                    {
                        "original": "oui",
                        "translation": "hai"
                    }
                ]
            },
            {
                "name": "Politesse",
                "words": [
                    {
                        "original": "non",
                        "translation": "iie"
                    },
                    {
                        "original": "bienvenue",
                        "translation": "yoo koso (irasshaimashita)"
                    },
                    {
                        "original": "bonjour",
                        "translation": "konnichi wa"
                    },
                    {
                        "original": "salut",
                        "translation": "ohayoo gozaimasu"
                    },
                    {
                        "original": "comment vas tu",
                        "translation": "genki desu ka"
                    },
                    {
                        "original": "merci, je vais bien",
                        "translation": "okage samade, genki desu"
                    },
                    {
                        "original": "comment vous appelez vous?",
                        "translation": "o namae wa nan desu ka"
                    },
                    {
                        "original": "je m'appele []",
                        "translation": "[] desu"
                    },
                    {
                        "original": "d'où venez vous?",
                        "translation": "dochira kara desu ka?"
                    },
                    {
                        "original": "je suis de []",
                        "translation": "[] shusshin desu"
                    },
                    {
                        "original": "enchanté",
                        "translation": "hajimemashite"
                    },
                    {
                        "original": "bonjour",
                        "translation": "o hayoo gozaimasu"
                    },
                    {
                        "original": "bonsoir",
                        "translation": "konbanwa"
                    },
                    {
                        "original": "bonne nuit",
                        "translation": "oyasumi nasai"
                    },
                    {
                        "original": "aurevoir",
                        "translation": "sayoonara"
                    },
                    {
                        "original": "je ne comprends pas",
                        "translation": "wakarimasen"
                    },
                    {
                        "original": "parlez plus lentement",
                        "translation": "yukkuri hanashite kudasai"
                    },
                    {
                        "original": "écrivez le",
                        "translation": "kaite kudasai"
                    },
                    {
                        "original": "s'il vous plaît",
                        "translation": "onegai shimasu"
                    },
                    {
                        "original": "donnez moi []",
                        "translation": "[] o kudasai"
                    },
                    {
                        "original": "merci",
                        "translation": "arigatoo"
                    },
                    {
                        "original": "je vous en prie",
                        "translation": "doozo"
                    },
                    {
                        "original": "excusez moi",
                        "translation": "gomen nasai"
                    },
                    {
                        "original": "pardon",
                        "translation": "sumimasen"
                    },
                    {
                        "original": "pas de problème",
                        "translation": "daijoosu desu yo"
                    }
                ]
            },
            {
                "name": "Divers",
                "words": [
                    {
                        "original": "voici",
                        "translation": "doozo"
                    },
                    {
                        "original": "bon appétit",
                        "translation": "itadakimasu"
                    },
                    {
                        "original": "santé!",
                        "translation": "kanpai"
                    },
                    {
                        "original": "n'est ce pas",
                        "translation": "ne"
                    },
                    {
                        "original": "ne t'inquiète pas",
                        "translation": "shinpai shinaide"
                    },
                    {
                        "original": "je ne sais pas, je n'ai pas compris",
                        "translation": "wakarimasen"
                    }
                ]
            }
        ]
    },
    "german": {
        "display_name": "Allemand",
        "categories": [
            {
                "name": "Alimentation",
                "words": [
                    {
                        "original": "nourriture",
                        "translation": "die Nahrung"
                    },
                    {
                        "original": "rien",
                        "translation": "nichts"
                    },
                    {
                        "original": "quelque chose",
                        "translation": "etwas"
                    },
                    {
                        "original": "tout",
                        "translation": "alles"
                    },
                    {
                        "original": "pain",
                        "translation": "das Brod"
                    },
                    {
                        "original": "sel",
                        "translation": "Salz"
                    },
                    {
                        "original": "poivre",
                        "translation": ""
                    },
                    {
                        "original": "sucre",
                        "translation": "Zucker"
                    },
                    {
                        "original": "plante",
                        "translation": "Pflanze"
                    },
                    {
                        "original": "animal",
                        "translation": "Tier"
                    },
                    {
                        "original": "viande",
                        "translation": "das Fleisch"
                    },
                    {
                        "original": "poisson",
                        "translation": "Fisch"
                    },
                    {
                        "original": "fromage",
                        "translation": "der Käse"
                    },
                    {
                        "original": "verre",
                        "translation": "das Glas"
                    },
                    {
                        "original": "café",
                        "translation": "der Kaffee"
                    },
                    {
                        "original": "thé",
                        "translation": "der Tee"
                    },
                    {
                        "original": "eau",
                        "translation": "das Wasser"
                    },
                    {
                        "original": "lait",
                        "translation": "die Milch"
                    },
                    {
                        "original": "huile",
                        "translation": "öl"
                    },
                    {
                        "original": "bière",
                        "translation": "das Bier"
                    },
                    {
                        "original": "vin",
                        "translation": "Wein"
                    },
                    {
                        "original": "travail",
                        "translation": "die Arbeit"
                    },
                    {
                        "original": "argent",
                        "translation": "das Geld"
                    },
                    {
                        "original": "livre",
                        "translation": "Buch"
                    },
                    {
                        "original": "v^etement",
                        "translation": "Kleidung"
                    },
                    {
                        "original": "oui",
                        "translation": "ja"
                    },
                    {
                        "original": "non",
                        "translation": "nein"
                    },
                    {
                        "original": "si",
                        "translation": "doch"
                    },
                    {
                        "original": "d'accord",
                        "translation": "okay"
                    }
                ]
            },
            {
                "name": "Expressions & Pensée",
                "words": [
                    {
                        "original": "ne pas",
                        "translation": "nicht"
                    },
                    {
                        "original": "pas de",
                        "translation": "kein"
                    },
                    {
                        "original": "il y a",
                        "translation": "es gibt"
                    },
                    {
                        "original": "y a t'il?",
                        "translation": "gibt es"
                    },
                    {
                        "original": "j'aime",
                        "translation": "ich mag"
                    },
                    {
                        "original": "j'aimerai",
                        "translation": "ich möchte"
                    },
                    {
                        "original": "aimeriez vous",
                        "translation": "möchten Sie"
                    },
                    {
                        "original": "voulez vous",
                        "translation": "wollen Sie"
                    },
                    {
                        "original": "je dois",
                        "translation": "ich muss"
                    },
                    {
                        "original": "c'est pas la peine",
                        "translation": "es ist nicht nötig"
                    },
                    {
                        "original": "vous devez",
                        "translation": "Sie müssen"
                    },
                    {
                        "original": "je sais",
                        "translation": "ich weiss"
                    },
                    {
                        "original": "savez vous",
                        "translation": "wissen Sie"
                    },
                    {
                        "original": "je (te) connais",
                        "translation": "ich kenne (dich)"
                    },
                    {
                        "original": "connaissez vous",
                        "translation": "kennen Sie"
                    },
                    {
                        "original": "je peux",
                        "translation": "ich kann/darf"
                    },
                    {
                        "original": "vous pouvez",
                        "translation": "Sie können/dürfen"
                    },
                    {
                        "original": "je pense",
                        "translation": "ich denke"
                    },
                    {
                        "original": "je crois",
                        "translation": "ich glaube"
                    },
                    {
                        "original": "peut-être",
                        "translation": "vielleicht"
                    },
                    {
                        "original": "pas possible",
                        "translation": "unmöglich"
                    }
                ]
            },
            {
                "name": "Verbes d'action",
                "words": [
                    {
                        "original": "faire",
                        "translation": "machen"
                    },
                    {
                        "original": "penser",
                        "translation": "denken"
                    },
                    {
                        "original": "chercher",
                        "translation": "holen"
                    },
                    {
                        "original": "trouver",
                        "translation": "finden"
                    },
                    {
                        "original": "attendre",
                        "translation": "warten"
                    },
                    {
                        "original": "commencer",
                        "translation": "anfangen"
                    },
                    {
                        "original": "écrire",
                        "translation": "schreiben"
                    },
                    {
                        "original": "lire",
                        "translation": "lesen"
                    },
                    {
                        "original": "travailler",
                        "translation": "arbeiten"
                    },
                    {
                        "original": "apprendre",
                        "translation": "lernen"
                    },
                    {
                        "original": "comprendre",
                        "translation": "verstehen"
                    },
                    {
                        "original": "regarder",
                        "translation": "ansehen"
                    },
                    {
                        "original": "voir",
                        "translation": "sehen"
                    },
                    {
                        "original": "prendre",
                        "translation": "nehmen"
                    },
                    {
                        "original": "acheter",
                        "translation": "kaufen"
                    },
                    {
                        "original": "donner",
                        "translation": "geben"
                    },
                    {
                        "original": "tenir",
                        "translation": "halten"
                    },
                    {
                        "original": "manger",
                        "translation": "essen"
                    },
                    {
                        "original": "boire",
                        "translation": "trinken"
                    },
                    {
                        "original": "parler",
                        "translation": "sprechen"
                    },
                    {
                        "original": "dire",
                        "translation": "sagen"
                    },
                    {
                        "original": "marcher",
                        "translation": "gehen"
                    },
                    {
                        "original": "se promener",
                        "translation": "besichtigen"
                    },
                    {
                        "original": "aller",
                        "translation": "fahren"
                    },
                    {
                        "original": "partir",
                        "translation": "weggehen"
                    },
                    {
                        "original": "venir",
                        "translation": "kommen"
                    },
                    {
                        "original": "rester",
                        "translation": "bleiben"
                    },
                    {
                        "original": "passer",
                        "translation": "vergehen"
                    },
                    {
                        "original": "entrer",
                        "translation": "hereinkommen"
                    },
                    {
                        "original": "sortir",
                        "translation": "auskommen"
                    },
                    {
                        "original": "courir",
                        "translation": "laufen"
                    },
                    {
                        "original": "s'asseoir",
                        "translation": "setzen"
                    },
                    {
                        "original": "dormir",
                        "translation": "schlafen"
                    },
                    {
                        "original": "habiter",
                        "translation": "wohnen"
                    }
                ]
            },
            {
                "name": "Pronoms & Lieux",
                "words": [
                    {
                        "original": "qui",
                        "translation": "wer"
                    },
                    {
                        "original": "personne",
                        "translation": "niemand"
                    },
                    {
                        "original": "quelqu'un",
                        "translation": "jemand"
                    },
                    {
                        "original": "tout le monde",
                        "translation": "alle"
                    },
                    {
                        "original": "ich",
                        "translation": "bin habe"
                    },
                    {
                        "original": "du",
                        "translation": "bist hast"
                    },
                    {
                        "original": "er",
                        "translation": "ist hat"
                    },
                    {
                        "original": "es",
                        "translation": "ist hat"
                    },
                    {
                        "original": "sie",
                        "translation": "ist hat"
                    },
                    {
                        "original": "wir",
                        "translation": "sind haben"
                    },
                    {
                        "original": "ihr",
                        "translation": "seid habt"
                    },
                    {
                        "original": "sie",
                        "translation": "sind haben"
                    },
                    {
                        "original": "mon",
                        "translation": "mein"
                    },
                    {
                        "original": "ton",
                        "translation": "dein"
                    },
                    {
                        "original": "son",
                        "translation": "sein"
                    },
                    {
                        "original": "notre",
                        "translation": "unser"
                    },
                    {
                        "original": "votre",
                        "translation": "ihr"
                    },
                    {
                        "original": "leurs",
                        "translation": "ihre"
                    },
                    {
                        "original": "ceci",
                        "translation": "das"
                    },
                    {
                        "original": "de",
                        "translation": "von"
                    },
                    {
                        "original": "enfant",
                        "translation": "das Kind"
                    },
                    {
                        "original": "fils",
                        "translation": "Sohn"
                    },
                    {
                        "original": "fille",
                        "translation": "Tochter"
                    },
                    {
                        "original": "mère",
                        "translation": "die Muter"
                    },
                    {
                        "original": "père",
                        "translation": "der Vater"
                    },
                    {
                        "original": "frère",
                        "translation": "der Bruder"
                    },
                    {
                        "original": "soeur",
                        "translation": "die Schwester"
                    },
                    {
                        "original": "mari",
                        "translation": "Mann"
                    },
                    {
                        "original": "femme",
                        "translation": "Ehefrau"
                    },
                    {
                        "original": "ami(e)",
                        "translation": "freund(in)"
                    }
                ]
            },
            {
                "name": "Maison & Ville",
                "words": [
                    {
                        "original": "où",
                        "translation": "wo"
                    },
                    {
                        "original": "quelque part",
                        "translation": "irgendwo"
                    },
                    {
                        "original": "partout",
                        "translation": "überall"
                    },
                    {
                        "original": "ici",
                        "translation": "hier, da"
                    },
                    {
                        "original": "là-bas",
                        "translation": "dort"
                    },
                    {
                        "original": "vers",
                        "translation": "nach"
                    },
                    {
                        "original": "à droite",
                        "translation": "rechts"
                    },
                    {
                        "original": "à gauche",
                        "translation": "links"
                    },
                    {
                        "original": "tout droit",
                        "translation": "geradeaus"
                    },
                    {
                        "original": "devant",
                        "translation": "an, vor"
                    },
                    {
                        "original": "derrière",
                        "translation": "hinter"
                    },
                    {
                        "original": "dessous",
                        "translation": "unter"
                    },
                    {
                        "original": "dessus",
                        "translation": "über"
                    },
                    {
                        "original": "dans",
                        "translation": "in"
                    },
                    {
                        "original": "mer",
                        "translation": "das Meer"
                    },
                    {
                        "original": "soleil",
                        "translation": "die Sonne"
                    },
                    {
                        "original": "ville",
                        "translation": "die Stadt"
                    },
                    {
                        "original": "maison",
                        "translation": "das Haus"
                    },
                    {
                        "original": "magasin",
                        "translation": "das Geschäft"
                    },
                    {
                        "original": "école",
                        "translation": "Schule"
                    },
                    {
                        "original": "lit",
                        "translation": "das Bett"
                    },
                    {
                        "original": "chambre",
                        "translation": "das Zimmer"
                    },
                    {
                        "original": "salle de bain",
                        "translation": "das Bad"
                    },
                    {
                        "original": "cuisine",
                        "translation": "die Küche"
                    },
                    {
                        "original": "table",
                        "translation": "der Tisch"
                    },
                    {
                        "original": "chaise",
                        "translation": "der Stuhl"
                    },
                    {
                        "original": "avion",
                        "translation": "das Flugzeug"
                    },
                    {
                        "original": "voiture",
                        "translation": "das Auto"
                    },
                    {
                        "original": "bus",
                        "translation": "Bus"
                    },
                    {
                        "original": "train",
                        "translation": "der Zug"
                    },
                    {
                        "original": "Allemagne",
                        "translation": "Deutschland"
                    },
                    {
                        "original": "France",
                        "translation": "Frankreich"
                    }
                ]
            },
            {
                "name": "Temps",
                "words": [
                    {
                        "original": "quand",
                        "translation": "wann"
                    },
                    {
                        "original": "le temps",
                        "translation": "die Zeit"
                    },
                    {
                        "original": "jamais",
                        "translation": "nie(mals)"
                    },
                    {
                        "original": "souvent",
                        "translation": "oft"
                    },
                    {
                        "original": "toujours",
                        "translation": "immer"
                    },
                    {
                        "original": "maintenant",
                        "translation": "jetzt"
                    },
                    {
                        "original": "tout de suite",
                        "translation": "sofort, gleich"
                    },
                    {
                        "original": "avant",
                        "translation": "vor"
                    },
                    {
                        "original": "après",
                        "translation": "nach"
                    },
                    {
                        "original": "bientôt",
                        "translation": "bald"
                    },
                    {
                        "original": "tôt",
                        "translation": "früh"
                    },
                    {
                        "original": "tard",
                        "translation": "spät"
                    },
                    {
                        "original": "dernier",
                        "translation": "letzte"
                    },
                    {
                        "original": "prochain",
                        "translation": "nächste"
                    },
                    {
                        "original": "matin",
                        "translation": "morgen"
                    },
                    {
                        "original": "soir",
                        "translation": "abend"
                    },
                    {
                        "original": "nuit",
                        "translation": "nacht"
                    },
                    {
                        "original": "aujourd'hui",
                        "translation": "heute"
                    },
                    {
                        "original": "demain",
                        "translation": "morgen"
                    },
                    {
                        "original": "hier",
                        "translation": "gestern"
                    },
                    {
                        "original": "année",
                        "translation": "das Jahr"
                    },
                    {
                        "original": "mois",
                        "translation": "der Monat"
                    },
                    {
                        "original": "semaine",
                        "translation": "die Woche"
                    },
                    {
                        "original": "jour",
                        "translation": "der Tag"
                    },
                    {
                        "original": "heure",
                        "translation": "die Uhr"
                    },
                    {
                        "original": "minute",
                        "translation": "die Minute"
                    },
                    {
                        "original": "couleur",
                        "translation": "Farbe"
                    },
                    {
                        "original": "bleu",
                        "translation": "blau"
                    },
                    {
                        "original": "rouge",
                        "translation": "rot"
                    },
                    {
                        "original": "vert",
                        "translation": "grün"
                    },
                    {
                        "original": "jaune",
                        "translation": "gelb"
                    },
                    {
                        "original": "blanc",
                        "translation": "weiss"
                    },
                    {
                        "original": "noir",
                        "translation": "schwarz"
                    }
                ]
            },
            {
                "name": "Adjectifs",
                "words": [
                    {
                        "original": "comment",
                        "translation": "wie"
                    },
                    {
                        "original": "jeune",
                        "translation": "jung"
                    },
                    {
                        "original": "fatigué",
                        "translation": "müde"
                    },
                    {
                        "original": "important",
                        "translation": "bedeutend"
                    },
                    {
                        "original": "nouveau",
                        "translation": "neu"
                    },
                    {
                        "original": "ancien",
                        "translation": "alt"
                    },
                    {
                        "original": "célèbre",
                        "translation": "berühmt"
                    },
                    {
                        "original": "beau",
                        "translation": "schön"
                    },
                    {
                        "original": "mauvais",
                        "translation": "slecht"
                    },
                    {
                        "original": "gentil",
                        "translation": "nett"
                    },
                    {
                        "original": "grand",
                        "translation": "gross"
                    },
                    {
                        "original": "petit",
                        "translation": "klein"
                    },
                    {
                        "original": "loin",
                        "translation": "weit"
                    },
                    {
                        "original": "près",
                        "translation": "nah"
                    },
                    {
                        "original": "bon",
                        "translation": "gut"
                    },
                    {
                        "original": "chaud",
                        "translation": "warm"
                    },
                    {
                        "original": "froid",
                        "translation": "kalt"
                    },
                    {
                        "original": "haut",
                        "translation": "hoch"
                    },
                    {
                        "original": "interdit",
                        "translation": "verboten"
                    },
                    {
                        "original": "vite",
                        "translation": "schnell"
                    },
                    {
                        "original": "lentement",
                        "translation": "langsam"
                    },
                    {
                        "original": "vide",
                        "translation": "leer"
                    },
                    {
                        "original": "plein",
                        "translation": "voll"
                    },
                    {
                        "original": "propre",
                        "translation": "sauber"
                    },
                    {
                        "original": "sale",
                        "translation": "schmutzig"
                    },
                    {
                        "original": "difficile",
                        "translation": "schwierig"
                    },
                    {
                        "original": "facile",
                        "translation": "einfach"
                    },
                    {
                        "original": "autre",
                        "translation": "anders"
                    },
                    {
                        "original": "comme",
                        "translation": "als"
                    },
                    {
                        "original": "aussi",
                        "translation": "auch"
                    },
                    {
                        "original": "avec (moi)",
                        "translation": "mit (mir)"
                    },
                    {
                        "original": "sans (moi)",
                        "translation": "ohne (mich)"
                    },
                    {
                        "original": "seul",
                        "translation": "allein"
                    },
                    {
                        "original": "ensemble",
                        "translation": "zusammen"
                    },
                    {
                        "original": "pour (moi)",
                        "translation": "für (mich)"
                    }
                ]
            },
            {
                "name": "Chiffres & Quantité",
                "words": [
                    {
                        "original": "combien",
                        "translation": "wie viel"
                    },
                    {
                        "original": "un peu",
                        "translation": "ein bisschen"
                    },
                    {
                        "original": "beaucoup",
                        "translation": "viel"
                    },
                    {
                        "original": "moins",
                        "translation": "weninger ... als"
                    },
                    {
                        "original": "plus",
                        "translation": "mehr ... als"
                    },
                    {
                        "original": "trop",
                        "translation": "zu"
                    },
                    {
                        "original": "1",
                        "translation": "ein"
                    },
                    {
                        "original": "2",
                        "translation": "zwei"
                    },
                    {
                        "original": "3",
                        "translation": "drei"
                    },
                    {
                        "original": "4",
                        "translation": "vier"
                    },
                    {
                        "original": "5",
                        "translation": "fünf"
                    },
                    {
                        "original": "6",
                        "translation": "sechs"
                    },
                    {
                        "original": "7",
                        "translation": "sieben"
                    },
                    {
                        "original": "8",
                        "translation": "acht"
                    },
                    {
                        "original": "9",
                        "translation": "neun"
                    },
                    {
                        "original": "10",
                        "translation": "zehn"
                    },
                    {
                        "original": "11",
                        "translation": "elf"
                    },
                    {
                        "original": "12",
                        "translation": "zwolf"
                    },
                    {
                        "original": "13",
                        "translation": "dreizehn"
                    },
                    {
                        "original": "20",
                        "translation": "zwanzig"
                    },
                    {
                        "original": "30",
                        "translation": "dreizig"
                    },
                    {
                        "original": "100",
                        "translation": "hundert"
                    },
                    {
                        "original": "1000",
                        "translation": "tausend"
                    },
                    {
                        "original": "mais",
                        "translation": "aber"
                    },
                    {
                        "original": "ou",
                        "translation": "oder"
                    },
                    {
                        "original": "et",
                        "translation": "und"
                    },
                    {
                        "original": "donc",
                        "translation": "denn"
                    },
                    {
                        "original": "puis",
                        "translation": "dann"
                    },
                    {
                        "original": "pourquoi",
                        "translation": "warum"
                    },
                    {
                        "original": "parce que",
                        "translation": "weil"
                    },
                    {
                        "original": "alors",
                        "translation": "also"
                    },
                    {
                        "original": "quel(le,s)",
                        "translation": "welche(r,s)"
                    }
                ]
            },
            {
                "name": "Politesse",
                "words": [
                    {
                        "original": "bienvenu",
                        "translation": "willkommen"
                    },
                    {
                        "original": "bonjour",
                        "translation": "guten tag"
                    },
                    {
                        "original": "salut",
                        "translation": "hallo"
                    },
                    {
                        "original": "bonsoir",
                        "translation": "guten Abend"
                    },
                    {
                        "original": "bonne nuit",
                        "translation": "gute Nacht"
                    },
                    {
                        "original": "comment vas tu",
                        "translation": "wie geht's"
                    },
                    {
                        "original": "je vais bien",
                        "translation": "es geht mir gut"
                    },
                    {
                        "original": "quoi de neuf",
                        "translation": "gibt es etwas Neues"
                    },
                    {
                        "original": "au revoir",
                        "translation": "auf Wiedersehen"
                    },
                    {
                        "original": "à plus tard",
                        "translation": "bis bald"
                    },
                    {
                        "original": "s'il vous plaît",
                        "translation": "bitte"
                    },
                    {
                        "original": "merci",
                        "translation": "danke"
                    },
                    {
                        "original": "de rien",
                        "translation": "keine ursache"
                    },
                    {
                        "original": "désolé",
                        "translation": "es tut mir Lied"
                    },
                    {
                        "original": "pardon",
                        "translation": "Entschuldigung"
                    },
                    {
                        "original": "excusez moi",
                        "translation": "entschuldigen sie"
                    },
                    {
                        "original": "c'est pas grave",
                        "translation": "das macht nichts"
                    },
                    {
                        "original": "félicitations",
                        "translation": "Glückwünsche"
                    },
                    {
                        "original": "comment vous appelez vous?",
                        "translation": "wie heissen sie?"
                    },
                    {
                        "original": "enchanté",
                        "translation": "angenehm"
                    },
                    {
                        "original": "bon appétit",
                        "translation": "guten Appetit"
                    },
                    {
                        "original": "santé!",
                        "translation": "Prost"
                    },
                    {
                        "original": "c'est bon",
                        "translation": "es schmeckt"
                    },
                    {
                        "original": "l'addition",
                        "translation": "Rechnung"
                    },
                    {
                        "original": "attention",
                        "translation": "Vorsicht"
                    },
                    {
                        "original": "je ne comprend pas",
                        "translation": "ich verstehe nicht"
                    }
                ]
            }
        ]
    },
    "dutch": {
        "display_name": "Néerlandais",
        "categories": [
            {
                "name": "Alimentation",
                "words": [
                    {
                        "original": "Quoi?",
                        "translation": "wat"
                    },
                    {
                        "original": "rien",
                        "translation": "niets"
                    },
                    {
                        "original": "quelques chose",
                        "translation": "iets"
                    },
                    {
                        "original": "tout",
                        "translation": "hele"
                    },
                    {
                        "original": "chaque",
                        "translation": "elke"
                    },
                    {
                        "original": "fruit",
                        "translation": "vrucht"
                    },
                    {
                        "original": "légumes",
                        "translation": "groente"
                    },
                    {
                        "original": "fromage",
                        "translation": "kaas"
                    },
                    {
                        "original": "pain",
                        "translation": "brood"
                    },
                    {
                        "original": "poisson",
                        "translation": "vis"
                    },
                    {
                        "original": "animal",
                        "translation": "dier"
                    },
                    {
                        "original": "viande",
                        "translation": "vlees"
                    },
                    {
                        "original": "sucre",
                        "translation": "suiker"
                    },
                    {
                        "original": "sel",
                        "translation": "zout"
                    },
                    {
                        "original": "poivre",
                        "translation": "peper"
                    },
                    {
                        "original": "verre",
                        "translation": "glas"
                    },
                    {
                        "original": "café",
                        "translation": "koffie"
                    },
                    {
                        "original": "thé",
                        "translation": "thee"
                    },
                    {
                        "original": "eau",
                        "translation": "water"
                    },
                    {
                        "original": "lait",
                        "translation": "melk"
                    },
                    {
                        "original": "huile",
                        "translation": "olie"
                    },
                    {
                        "original": "bière",
                        "translation": "bier"
                    },
                    {
                        "original": "vin",
                        "translation": "wijn"
                    },
                    {
                        "original": "travail",
                        "translation": "werk"
                    },
                    {
                        "original": "argent",
                        "translation": "geld"
                    },
                    {
                        "original": "livre",
                        "translation": "het boek"
                    },
                    {
                        "original": "vetement",
                        "translation": "kleding"
                    },
                    {
                        "original": "autre",
                        "translation": "ander"
                    },
                    {
                        "original": "difference",
                        "translation": "verschil"
                    },
                    {
                        "original": "ainsi",
                        "translation": "zo"
                    },
                    {
                        "original": "comme",
                        "translation": "zoals"
                    },
                    {
                        "original": "aussi",
                        "translation": "ook"
                    },
                    {
                        "original": "pour (moi)",
                        "translation": "voor (mij)"
                    },
                    {
                        "original": "avec (moi)",
                        "translation": "met (mij)"
                    },
                    {
                        "original": "sans (moi)",
                        "translation": "zonder (mij)"
                    },
                    {
                        "original": "ensemble",
                        "translation": "samen"
                    },
                    {
                        "original": "seul",
                        "translation": "alleen"
                    }
                ]
            },
            {
                "name": "Expressions & Pensée",
                "words": [
                    {
                        "original": "il y a",
                        "translation": "er is"
                    },
                    {
                        "original": "y a t'il?",
                        "translation": "is er?"
                    },
                    {
                        "original": "c'est",
                        "translation": "het is"
                    },
                    {
                        "original": "ne pas",
                        "translation": "niet"
                    },
                    {
                        "original": "pas de",
                        "translation": "geen"
                    },
                    {
                        "original": "j'aime",
                        "translation": "ik houd van"
                    },
                    {
                        "original": "je veux",
                        "translation": "ik wil"
                    },
                    {
                        "original": "je voudrai",
                        "translation": "ik wou graag"
                    },
                    {
                        "original": "j'ai envie",
                        "translation": "ik heb zin"
                    },
                    {
                        "original": "voulez vous",
                        "translation": "wilt u"
                    },
                    {
                        "original": "il faut",
                        "translation": "het is nodig"
                    },
                    {
                        "original": "c'est pas la peine",
                        "translation": "het is niet nodig"
                    },
                    {
                        "original": "je dois",
                        "translation": "ik moet"
                    },
                    {
                        "original": "vous devez",
                        "translation": "jullie moeten"
                    },
                    {
                        "original": "j'ai besoin",
                        "translation": "ik heb .. nodig"
                    },
                    {
                        "original": "je sais",
                        "translation": "ik weet"
                    },
                    {
                        "original": "savez vous",
                        "translation": "weet u"
                    },
                    {
                        "original": "je connais",
                        "translation": "ik ken"
                    },
                    {
                        "original": "connaissez vous",
                        "translation": "kent u"
                    },
                    {
                        "original": "je peux",
                        "translation": "ik kan"
                    },
                    {
                        "original": "pouvez vous",
                        "translation": "kan u"
                    },
                    {
                        "original": "je pense que",
                        "translation": "ik denk dat"
                    },
                    {
                        "original": "je crois",
                        "translation": "ik geloof"
                    },
                    {
                        "original": "peut-être",
                        "translation": "misschien"
                    },
                    {
                        "original": "probablement",
                        "translation": "waarschijnlijk"
                    },
                    {
                        "original": "possible",
                        "translation": "mogelijk"
                    },
                    {
                        "original": "pas possible",
                        "translation": "onmogelijk"
                    },
                    {
                        "original": "couleur",
                        "translation": "kleur"
                    },
                    {
                        "original": "rouge",
                        "translation": "rod"
                    },
                    {
                        "original": "bleu",
                        "translation": "blauw"
                    },
                    {
                        "original": "blanc",
                        "translation": "witt"
                    },
                    {
                        "original": "jaune",
                        "translation": "geel"
                    },
                    {
                        "original": "vert",
                        "translation": "groen"
                    },
                    {
                        "original": "noir",
                        "translation": "zwart"
                    }
                ]
            },
            {
                "name": "Verbes d'action",
                "words": [
                    {
                        "original": "faire",
                        "translation": "doen/maken"
                    },
                    {
                        "original": "penser",
                        "translation": "denken"
                    },
                    {
                        "original": "travailler",
                        "translation": "werken"
                    },
                    {
                        "original": "chercher",
                        "translation": "opzoeken"
                    },
                    {
                        "original": "trouver",
                        "translation": "vinden"
                    },
                    {
                        "original": "marcher",
                        "translation": "lopen"
                    },
                    {
                        "original": "se promener",
                        "translation": "wandelen"
                    },
                    {
                        "original": "aller",
                        "translation": "gaan"
                    },
                    {
                        "original": "venir",
                        "translation": "komen"
                    },
                    {
                        "original": "partir",
                        "translation": "weggaan"
                    },
                    {
                        "original": "attendre",
                        "translation": "wachten"
                    },
                    {
                        "original": "écrire",
                        "translation": "schrijven"
                    },
                    {
                        "original": "lire",
                        "translation": "lezen"
                    },
                    {
                        "original": "commencer",
                        "translation": "beginnen"
                    },
                    {
                        "original": "finir",
                        "translation": "afmaken"
                    },
                    {
                        "original": "rester",
                        "translation": "blijven"
                    },
                    {
                        "original": "entrer",
                        "translation": "binnengaan"
                    },
                    {
                        "original": "tourner",
                        "translation": "afslaan"
                    },
                    {
                        "original": "s'asseoir",
                        "translation": "zitten"
                    },
                    {
                        "original": "sortir",
                        "translation": "buitengaan"
                    },
                    {
                        "original": "courir",
                        "translation": "rennen"
                    },
                    {
                        "original": "regarder",
                        "translation": "kijken"
                    },
                    {
                        "original": "voir",
                        "translation": "zien"
                    },
                    {
                        "original": "entendre",
                        "translation": "horen"
                    },
                    {
                        "original": "boire",
                        "translation": "drinken"
                    },
                    {
                        "original": "prendre",
                        "translation": "nemen"
                    },
                    {
                        "original": "acheter",
                        "translation": "kopen"
                    },
                    {
                        "original": "manger",
                        "translation": "eten"
                    },
                    {
                        "original": "tenir",
                        "translation": "houden"
                    },
                    {
                        "original": "dormir",
                        "translation": "slapen"
                    },
                    {
                        "original": "donner",
                        "translation": "geven"
                    },
                    {
                        "original": "payer",
                        "translation": "betalen"
                    },
                    {
                        "original": "parler",
                        "translation": "spreken"
                    },
                    {
                        "original": "dire",
                        "translation": "zeggen"
                    },
                    {
                        "original": "demander",
                        "translation": "vragen"
                    },
                    {
                        "original": "apprendre",
                        "translation": "leren"
                    },
                    {
                        "original": "comprendre",
                        "translation": "begrijpen"
                    },
                    {
                        "original": "habiter",
                        "translation": "wonen"
                    }
                ]
            },
            {
                "name": "Pronoms & Lieux",
                "words": [
                    {
                        "original": "Qui?",
                        "translation": "wie"
                    },
                    {
                        "original": "personne",
                        "translation": "niemand"
                    },
                    {
                        "original": "quelqu'un",
                        "translation": "iemand"
                    },
                    {
                        "original": "tout le monde",
                        "translation": "iedereen"
                    },
                    {
                        "original": "enfant",
                        "translation": "kinder"
                    },
                    {
                        "original": "fils",
                        "translation": "zoon"
                    },
                    {
                        "original": "fille",
                        "translation": "dochter"
                    },
                    {
                        "original": "mère",
                        "translation": "moeder"
                    },
                    {
                        "original": "père",
                        "translation": "vader"
                    },
                    {
                        "original": "frère",
                        "translation": "broer"
                    },
                    {
                        "original": "soeur",
                        "translation": "zuster"
                    },
                    {
                        "original": "ami(e)",
                        "translation": "vriend"
                    },
                    {
                        "original": "ma femme",
                        "translation": "mijn vrouw"
                    },
                    {
                        "original": "mon",
                        "translation": "mijn"
                    },
                    {
                        "original": "ton",
                        "translation": "je"
                    },
                    {
                        "original": "son",
                        "translation": "zijn,haar"
                    },
                    {
                        "original": "notre",
                        "translation": "onze"
                    },
                    {
                        "original": "votre",
                        "translation": "uw"
                    },
                    {
                        "original": "leurs",
                        "translation": "hun"
                    },
                    {
                        "original": "je suis",
                        "translation": "ik ben"
                    },
                    {
                        "original": "tu es",
                        "translation": "je bent"
                    },
                    {
                        "original": "il,elle est",
                        "translation": "hij,ze is"
                    },
                    {
                        "original": "nous sommes",
                        "translation": "we zijn"
                    },
                    {
                        "original": "vous êtes",
                        "translation": "u bent"
                    },
                    {
                        "original": "ils sont",
                        "translation": "zij zijn"
                    },
                    {
                        "original": "j'ai",
                        "translation": "ik heb"
                    },
                    {
                        "original": "tu as",
                        "translation": "je hebt"
                    },
                    {
                        "original": "il, elle a",
                        "translation": "hij,ze heeft"
                    },
                    {
                        "original": "nous avons",
                        "translation": "we hebben"
                    },
                    {
                        "original": "vous avez",
                        "translation": "u heeft"
                    },
                    {
                        "original": "ils ont",
                        "translation": "zij hebben"
                    },
                    {
                        "original": "de",
                        "translation": "van"
                    },
                    {
                        "original": "ceci",
                        "translation": "deze/dit"
                    },
                    {
                        "original": "cela",
                        "translation": "die/dat"
                    },
                    {
                        "original": "oui (volontier)",
                        "translation": "ja (graag)"
                    },
                    {
                        "original": "non",
                        "translation": "nee"
                    },
                    {
                        "original": "d'accord",
                        "translation": "akkoord"
                    }
                ]
            },
            {
                "name": "Maison & Ville",
                "words": [
                    {
                        "original": "Où?",
                        "translation": "waar"
                    },
                    {
                        "original": "nulle-part",
                        "translation": "norgens"
                    },
                    {
                        "original": "quelques part",
                        "translation": "ergens"
                    },
                    {
                        "original": "partout",
                        "translation": "overal"
                    },
                    {
                        "original": "ici",
                        "translation": "hier"
                    },
                    {
                        "original": "là-bas",
                        "translation": "daar"
                    },
                    {
                        "original": "dessous",
                        "translation": "onder"
                    },
                    {
                        "original": "devant",
                        "translation": "vôôr"
                    },
                    {
                        "original": "à gauche",
                        "translation": "links"
                    },
                    {
                        "original": "vers",
                        "translation": "naar"
                    },
                    {
                        "original": "derrière",
                        "translation": "achter"
                    },
                    {
                        "original": "à côté",
                        "translation": "naast"
                    },
                    {
                        "original": "à droite",
                        "translation": "rechts"
                    },
                    {
                        "original": "tout droit",
                        "translation": "rechtdoor"
                    },
                    {
                        "original": "dans",
                        "translation": "in"
                    },
                    {
                        "original": "dessus",
                        "translation": "boven"
                    },
                    {
                        "original": "à l'intérieur",
                        "translation": "binnen"
                    },
                    {
                        "original": "à l'exterieur",
                        "translation": "buiten"
                    },
                    {
                        "original": "maison",
                        "translation": "huis"
                    },
                    {
                        "original": "cuisine",
                        "translation": "koeken"
                    },
                    {
                        "original": "table",
                        "translation": "tafel"
                    },
                    {
                        "original": "chaise",
                        "translation": "stoel"
                    },
                    {
                        "original": "soleil",
                        "translation": "zon"
                    },
                    {
                        "original": "montagnes",
                        "translation": "bergen"
                    },
                    {
                        "original": "mer",
                        "translation": "zee"
                    },
                    {
                        "original": "ville",
                        "translation": "stad"
                    },
                    {
                        "original": "rue",
                        "translation": "straat/weg"
                    },
                    {
                        "original": "magasin",
                        "translation": "winkel"
                    },
                    {
                        "original": "chambre",
                        "translation": "kamer"
                    },
                    {
                        "original": "lit",
                        "translation": "bed"
                    },
                    {
                        "original": "salle de bain",
                        "translation": "badkamer"
                    },
                    {
                        "original": "avion",
                        "translation": "vligetuig"
                    },
                    {
                        "original": "voiture",
                        "translation": "wagen"
                    },
                    {
                        "original": "bus",
                        "translation": "bus"
                    },
                    {
                        "original": "train",
                        "translation": "trein"
                    },
                    {
                        "original": "voyage",
                        "translation": "reis"
                    }
                ]
            },
            {
                "name": "Temps",
                "words": [
                    {
                        "original": "Quand?",
                        "translation": "wanneer"
                    },
                    {
                        "original": "temps",
                        "translation": "tijd"
                    },
                    {
                        "original": "jamais",
                        "translation": "nooit"
                    },
                    {
                        "original": "parfois",
                        "translation": "af en toe / soms"
                    },
                    {
                        "original": "souvent",
                        "translation": "dikwijls"
                    },
                    {
                        "original": "toujours",
                        "translation": "altijd/steeds"
                    },
                    {
                        "original": "année",
                        "translation": "jaar"
                    },
                    {
                        "original": "mois",
                        "translation": "maand"
                    },
                    {
                        "original": "semaine",
                        "translation": "week"
                    },
                    {
                        "original": "jour",
                        "translation": "dag"
                    },
                    {
                        "original": "(à) .. heure",
                        "translation": "(om) .. uur"
                    },
                    {
                        "original": "minutes",
                        "translation": "minuten"
                    },
                    {
                        "original": "seconde",
                        "translation": "seconde"
                    },
                    {
                        "original": "avant",
                        "translation": "voor"
                    },
                    {
                        "original": "maintenant",
                        "translation": "nu"
                    },
                    {
                        "original": "après",
                        "translation": "na"
                    },
                    {
                        "original": "tout de suite",
                        "translation": "onmiddelijk / dadelik"
                    },
                    {
                        "original": "matin",
                        "translation": "morgen"
                    },
                    {
                        "original": "après-midi",
                        "translation": "middag"
                    },
                    {
                        "original": "soir",
                        "translation": "avond"
                    },
                    {
                        "original": "nuit",
                        "translation": "nacht"
                    },
                    {
                        "original": "hier",
                        "translation": "gisteren"
                    },
                    {
                        "original": "aujourd'hui",
                        "translation": "vandaag"
                    },
                    {
                        "original": "demain",
                        "translation": "morgen"
                    },
                    {
                        "original": "tôt",
                        "translation": "vroeg"
                    },
                    {
                        "original": "bientôt",
                        "translation": "binnenkort"
                    },
                    {
                        "original": "prochain",
                        "translation": "volgende"
                    },
                    {
                        "original": "tard",
                        "translation": "laat"
                    },
                    {
                        "original": "dernier",
                        "translation": "vorige"
                    },
                    {
                        "original": "déjà",
                        "translation": "al"
                    },
                    {
                        "original": "depuis",
                        "translation": "sinds"
                    },
                    {
                        "original": "encore",
                        "translation": "nog"
                    },
                    {
                        "original": "jusqu'à",
                        "translation": "tot"
                    },
                    {
                        "original": "de nouveau",
                        "translation": "weer"
                    },
                    {
                        "original": "toujours pas",
                        "translation": "steeds niet"
                    }
                ]
            },
            {
                "name": "Adjectifs",
                "words": [
                    {
                        "original": "Comment?",
                        "translation": "hoe"
                    },
                    {
                        "original": "grand",
                        "translation": "grot"
                    },
                    {
                        "original": "petit",
                        "translation": "klein"
                    },
                    {
                        "original": "haut",
                        "translation": "hoog"
                    },
                    {
                        "original": "bas",
                        "translation": "lag"
                    },
                    {
                        "original": "beau",
                        "translation": "mooi"
                    },
                    {
                        "original": "vide",
                        "translation": "leeg"
                    },
                    {
                        "original": "plein",
                        "translation": "vol"
                    },
                    {
                        "original": "ouvert",
                        "translation": "open"
                    },
                    {
                        "original": "fermé",
                        "translation": "gesloten"
                    },
                    {
                        "original": "près",
                        "translation": "dichtbij"
                    },
                    {
                        "original": "loin",
                        "translation": "ver"
                    },
                    {
                        "original": "chaud",
                        "translation": "warm"
                    },
                    {
                        "original": "froid",
                        "translation": "koud"
                    },
                    {
                        "original": "nouveau",
                        "translation": "nieuw"
                    },
                    {
                        "original": "ancien",
                        "translation": "oud"
                    },
                    {
                        "original": "jeune",
                        "translation": "jong"
                    },
                    {
                        "original": "fatigué",
                        "translation": "moe"
                    },
                    {
                        "original": "malade",
                        "translation": "ziek"
                    },
                    {
                        "original": "prêt",
                        "translation": "klaar"
                    },
                    {
                        "original": "propre",
                        "translation": "schoon"
                    },
                    {
                        "original": "sale",
                        "translation": "vuil"
                    },
                    {
                        "original": "lourd",
                        "translation": "zwaar"
                    },
                    {
                        "original": "bon",
                        "translation": "lekkere"
                    },
                    {
                        "original": "bien",
                        "translation": "goed"
                    },
                    {
                        "original": "mauvais",
                        "translation": "slecht"
                    },
                    {
                        "original": "gentil",
                        "translation": "aardig"
                    },
                    {
                        "original": "content",
                        "translation": "blij"
                    },
                    {
                        "original": "difficile",
                        "translation": "moeilijk"
                    },
                    {
                        "original": "facile",
                        "translation": "gemakkelijk"
                    },
                    {
                        "original": "intéressant",
                        "translation": "interessant"
                    },
                    {
                        "original": "(j'ai) faim",
                        "translation": "(ik heb) honger"
                    },
                    {
                        "original": "rapide",
                        "translation": "vlug"
                    },
                    {
                        "original": "lent",
                        "translation": "langzaam"
                    },
                    {
                        "original": "cher",
                        "translation": "duur"
                    },
                    {
                        "original": "important",
                        "translation": "belangrijk"
                    },
                    {
                        "original": "célèbre",
                        "translation": "beroemd/bekende"
                    },
                    {
                        "original": "interdit",
                        "translation": "verboden"
                    }
                ]
            },
            {
                "name": "Chiffres & Quantité",
                "words": [
                    {
                        "original": "Combien?",
                        "translation": "hoeveel"
                    },
                    {
                        "original": "un peu",
                        "translation": "een beetje / wat"
                    },
                    {
                        "original": "peu",
                        "translation": "weinig"
                    },
                    {
                        "original": "beaucoup",
                        "translation": "veel / talrijke"
                    },
                    {
                        "original": "très",
                        "translation": "heel"
                    },
                    {
                        "original": "moins",
                        "translation": "minder"
                    },
                    {
                        "original": "plus",
                        "translation": "meer"
                    },
                    {
                        "original": "presque",
                        "translation": "bijna"
                    },
                    {
                        "original": "environ",
                        "translation": "ongeveer"
                    },
                    {
                        "original": "trop",
                        "translation": "te veel"
                    },
                    {
                        "original": "assez",
                        "translation": "genoeg/nogal"
                    },
                    {
                        "original": "1",
                        "translation": "een"
                    },
                    {
                        "original": "2",
                        "translation": "twee"
                    },
                    {
                        "original": "3",
                        "translation": "drie"
                    },
                    {
                        "original": "4",
                        "translation": "vier"
                    },
                    {
                        "original": "5",
                        "translation": "vijf"
                    },
                    {
                        "original": "6",
                        "translation": "zes"
                    },
                    {
                        "original": "7",
                        "translation": "zeven"
                    },
                    {
                        "original": "8",
                        "translation": "acht"
                    },
                    {
                        "original": "9",
                        "translation": "negen"
                    },
                    {
                        "original": "10",
                        "translation": "tien"
                    },
                    {
                        "original": "11",
                        "translation": "elf"
                    },
                    {
                        "original": "12",
                        "translation": "twaalf"
                    },
                    {
                        "original": "13",
                        "translation": "dertien"
                    },
                    {
                        "original": "20",
                        "translation": "twintig"
                    },
                    {
                        "original": "30",
                        "translation": "dertig"
                    },
                    {
                        "original": "100",
                        "translation": "honderd"
                    },
                    {
                        "original": "1000",
                        "translation": "duizend"
                    },
                    {
                        "original": "mais",
                        "translation": "maar"
                    },
                    {
                        "original": "ou",
                        "translation": "of"
                    },
                    {
                        "original": "et",
                        "translation": "en"
                    },
                    {
                        "original": "donc",
                        "translation": "dus"
                    },
                    {
                        "original": "alors",
                        "translation": "dan"
                    },
                    {
                        "original": "Pourquoi?",
                        "translation": "waarom"
                    },
                    {
                        "original": "parce que",
                        "translation": "want/omdat"
                    },
                    {
                        "original": "par example",
                        "translation": "zoals"
                    },
                    {
                        "original": "Quel(le,s)?",
                        "translation": "welke"
                    }
                ]
            },
            {
                "name": "Politesse",
                "words": [
                    {
                        "original": "bonjour",
                        "translation": "goedendag"
                    },
                    {
                        "original": "salut",
                        "translation": "hallo"
                    },
                    {
                        "original": "comment vas tu",
                        "translation": "hoe gaat het (met u)?"
                    },
                    {
                        "original": "je vais bien",
                        "translation": "het gaat goed met me"
                    },
                    {
                        "original": "quoi de neuf",
                        "translation": "wat is nieuw?"
                    },
                    {
                        "original": "bonne journée",
                        "translation": "goede dag"
                    },
                    {
                        "original": "bonsoir",
                        "translation": "goedenavond"
                    },
                    {
                        "original": "bonne nuit",
                        "translation": "goedenacht"
                    },
                    {
                        "original": "aurevoir",
                        "translation": "tot ziens"
                    },
                    {
                        "original": "bienvenu",
                        "translation": "welkom"
                    },
                    {
                        "original": "s'il vous plaît",
                        "translation": "alstublieft"
                    },
                    {
                        "original": "merci (beaucoup)",
                        "translation": "dank u (wel)/ bedankt"
                    },
                    {
                        "original": "de rien",
                        "translation": "graag gedaan"
                    },
                    {
                        "original": "excusez moi",
                        "translation": "excuseert u me"
                    },
                    {
                        "original": "désolé",
                        "translation": "het spijt me"
                    },
                    {
                        "original": "c'est pas grave",
                        "translation": "het is niet erg"
                    },
                    {
                        "original": "félicitations",
                        "translation": "gefeliciteerd"
                    },
                    {
                        "original": "comment vous appelez vous?",
                        "translation": "hoe het u"
                    },
                    {
                        "original": "je m'appele",
                        "translation": "ik heet"
                    },
                    {
                        "original": "enchanté",
                        "translation": "ik ben blij u te leren kennen"
                    },
                    {
                        "original": "voici",
                        "translation": "hier is"
                    },
                    {
                        "original": "bon appétit",
                        "translation": "eet smakelijk"
                    },
                    {
                        "original": "c'était très bon",
                        "translation": "het was heel smakelijk"
                    },
                    {
                        "original": "l'addition",
                        "translation": "de rekening"
                    },
                    {
                        "original": "santé!",
                        "translation": "proost"
                    },
                    {
                        "original": "je n'ai pas compris",
                        "translation": "ik begreep niet"
                    },
                    {
                        "original": "je ne sais pas",
                        "translation": "ik weet niet"
                    },
                    {
                        "original": "attention",
                        "translation": "kijk uit"
                    }
                ]
            }
        ]
    },
    "turkish": {
        "display_name": "Turc",
        "categories": [
            {
                "name": "Alimentation",
                "words": [
                    {"original": "nourriture", "translation": "yiyecek"},
                    {"original": "fruit", "translation": "meyve"},
                    {"original": "légumes", "translation": "sebze"},
                    {"original": "pain", "translation": "ekmek"},
                    {"original": "fromage", "translation": "peynir"},
                    {"original": "viande", "translation": "et"},
                    {"original": "poisson", "translation": "balik"},
                    {"original": "sel", "translation": "tuz"},
                    {"original": "sucre", "translation": "seker"},
                    {"original": "eau", "translation": "su"},
                    {"original": "lait", "translation": "sut"},
                    {"original": "café", "translation": "kahve"},
                    {"original": "thé", "translation": "cay"},
                    {"original": "bière", "translation": "bira"},
                    {"original": "vin", "translation": "sarap"},
                    {"original": "riz", "translation": "pirinc"},
                    {"original": "huile", "translation": "yag"},
                    {"original": "animal", "translation": "hayvan"}
                ]
            },
            {
                "name": "Expressions & Pensée",
                "words": [
                    {"original": "quoi?", "translation": "ne?"},
                    {"original": "rien", "translation": "hicbir sey"},
                    {"original": "quelque chose", "translation": "bir sey"},
                    {"original": "tout", "translation": "her sey"},
                    {"original": "il y a", "translation": "var"},
                    {"original": "il n'y a pas", "translation": "yok"},
                    {"original": "c'est", "translation": "bu"},
                    {"original": "je veux", "translation": "istiyorum"},
                    {"original": "j'aime", "translation": "seviyorum"},
                    {"original": "je dois", "translation": "gerekiyor"},
                    {"original": "je peux", "translation": "yapabilirim"},
                    {"original": "je pense", "translation": "dusunuyorum"},
                    {"original": "peut-être", "translation": "belki"},
                    {"original": "et", "translation": "ve"},
                    {"original": "ou", "translation": "veya"},
                    {"original": "mais", "translation": "ama"},
                    {"original": "parce que", "translation": "cunku"},
                    {"original": "pourquoi", "translation": "neden"}
                ]
            },
            {
                "name": "Verbes d'action",
                "words": [
                    {"original": "faire", "translation": "yapmak"},
                    {"original": "aller", "translation": "gitmek"},
                    {"original": "venir", "translation": "gelmek"},
                    {"original": "partir", "translation": "ayrilmak"},
                    {"original": "attendre", "translation": "beklemek"},
                    {"original": "écrire", "translation": "yazmak"},
                    {"original": "lire", "translation": "okumak"},
                    {"original": "commencer", "translation": "baslamak"},
                    {"original": "finir", "translation": "bitirmek"},
                    {"original": "entrer", "translation": "girmek"},
                    {"original": "sortir", "translation": "cikmak"},
                    {"original": "courir", "translation": "kosmak"},
                    {"original": "voir", "translation": "gormek"},
                    {"original": "écouter", "translation": "dinlemek"},
                    {"original": "boire", "translation": "icmek"},
                    {"original": "manger", "translation": "yemek"},
                    {"original": "parler", "translation": "konusmak"},
                    {"original": "comprendre", "translation": "anlamak"}
                ]
            },
            {
                "name": "Pronoms & Lieux",
                "words": [
                    {"original": "qui", "translation": "kim"},
                    {"original": "moi", "translation": "ben"},
                    {"original": "toi", "translation": "sen"},
                    {"original": "il/elle", "translation": "o"},
                    {"original": "nous", "translation": "biz"},
                    {"original": "vous", "translation": "siz"},
                    {"original": "ils", "translation": "onlar"},
                    {"original": "ceci", "translation": "bu"},
                    {"original": "cela", "translation": "su"},
                    {"original": "où", "translation": "nerede"},
                    {"original": "ici", "translation": "burada"},
                    {"original": "là", "translation": "orada"},
                    {"original": "devant", "translation": "onunde"},
                    {"original": "derrière", "translation": "arkasinda"},
                    {"original": "à gauche", "translation": "solda"},
                    {"original": "à droite", "translation": "sagda"},
                    {"original": "dans", "translation": "icinde"},
                    {"original": "de", "translation": "-den/-dan"}
                ]
            },
            {
                "name": "Maison & Ville",
                "words": [
                    {"original": "maison", "translation": "ev"},
                    {"original": "cuisine", "translation": "mutfak"},
                    {"original": "chambre", "translation": "oda"},
                    {"original": "lit", "translation": "yatak"},
                    {"original": "salle de bain", "translation": "banyo"},
                    {"original": "table", "translation": "masa"},
                    {"original": "chaise", "translation": "sandalye"},
                    {"original": "ville", "translation": "sehir"},
                    {"original": "rue", "translation": "sokak"},
                    {"original": "magasin", "translation": "magaza"},
                    {"original": "arbre", "translation": "agac"},
                    {"original": "montagne", "translation": "dag"},
                    {"original": "mer", "translation": "deniz"},
                    {"original": "soleil", "translation": "gunes"},
                    {"original": "voiture", "translation": "araba"},
                    {"original": "bus", "translation": "otobus"},
                    {"original": "train", "translation": "tren"},
                    {"original": "voyage", "translation": "seyahat"}
                ]
            },
            {
                "name": "Temps",
                "words": [
                    {"original": "quand", "translation": "ne zaman"},
                    {"original": "temps", "translation": "zaman"},
                    {"original": "jamais", "translation": "asla"},
                    {"original": "parfois", "translation": "bazen"},
                    {"original": "souvent", "translation": "sik sik"},
                    {"original": "toujours", "translation": "her zaman"},
                    {"original": "maintenant", "translation": "simdi"},
                    {"original": "avant", "translation": "once"},
                    {"original": "après", "translation": "sonra"},
                    {"original": "matin", "translation": "sabah"},
                    {"original": "après-midi", "translation": "ogleden sonra"},
                    {"original": "soir", "translation": "aksam"},
                    {"original": "nuit", "translation": "gece"},
                    {"original": "aujourd'hui", "translation": "bugun"},
                    {"original": "demain", "translation": "yarin"},
                    {"original": "hier", "translation": "dun"},
                    {"original": "année", "translation": "yil"},
                    {"original": "mois", "translation": "ay"}
                ]
            },
            {
                "name": "Adjectifs",
                "words": [
                    {"original": "bon", "translation": "iyi"},
                    {"original": "mauvais", "translation": "kotu"},
                    {"original": "beau", "translation": "guzel"},
                    {"original": "grand", "translation": "buyuk"},
                    {"original": "petit", "translation": "kucuk"},
                    {"original": "chaud", "translation": "sicak"},
                    {"original": "froid", "translation": "soguk"},
                    {"original": "vite", "translation": "hizli"},
                    {"original": "lent", "translation": "yavas"},
                    {"original": "nouveau", "translation": "yeni"},
                    {"original": "ancien", "translation": "eski"},
                    {"original": "facile", "translation": "kolay"},
                    {"original": "difficile", "translation": "zor"},
                    {"original": "important", "translation": "onemli"},
                    {"original": "propre", "translation": "temiz"},
                    {"original": "sale", "translation": "kirli"},
                    {"original": "près", "translation": "yakin"},
                    {"original": "loin", "translation": "uzak"}
                ]
            },
            {
                "name": "Chiffres & Quantité",
                "words": [
                    {"original": "combien", "translation": "ne kadar"},
                    {"original": "un peu", "translation": "biraz"},
                    {"original": "beaucoup", "translation": "cok"},
                    {"original": "moins", "translation": "daha az"},
                    {"original": "plus", "translation": "daha cok"},
                    {"original": "très", "translation": "cok"},
                    {"original": "trop", "translation": "fazla"},
                    {"original": "0", "translation": "sifir"},
                    {"original": "1", "translation": "bir"},
                    {"original": "2", "translation": "iki"},
                    {"original": "3", "translation": "uc"},
                    {"original": "4", "translation": "dort"},
                    {"original": "5", "translation": "bes"},
                    {"original": "6", "translation": "alti"},
                    {"original": "7", "translation": "yedi"},
                    {"original": "8", "translation": "sekiz"},
                    {"original": "9", "translation": "dokuz"},
                    {"original": "10", "translation": "on"}
                ]
            },
            {
                "name": "Politesse",
                "words": [
                    {"original": "oui", "translation": "evet"},
                    {"original": "non", "translation": "hayir"},
                    {"original": "bonjour", "translation": "merhaba"},
                    {"original": "salut", "translation": "selam"},
                    {"original": "bonsoir", "translation": "iyi aksamlar"},
                    {"original": "bonne nuit", "translation": "iyi geceler"},
                    {"original": "au revoir", "translation": "hosca kal"},
                    {"original": "s'il vous plaît", "translation": "lutfen"},
                    {"original": "merci", "translation": "tesekkur ederim"},
                    {"original": "de rien", "translation": "rica ederim"},
                    {"original": "excusez-moi", "translation": "affedersiniz"},
                    {"original": "pardon", "translation": "ozur dilerim"},
                    {"original": "comment ça va?", "translation": "nasilsin?"},
                    {"original": "je vais bien", "translation": "iyiyim"},
                    {"original": "je ne comprends pas", "translation": "anlamiyorum"},
                    {"original": "parlez plus lentement", "translation": "daha yavas konusun"},
                    {"original": "comment vous appelez-vous?", "translation": "adiniz ne?"},
                    {"original": "je m'appelle []", "translation": "benim adim []"}
                ]
            },
            {
                "name": "Divers",
                "words": [
                    {"original": "enfant", "translation": "cocuk"},
                    {"original": "garçon", "translation": "erkek cocuk"},
                    {"original": "fille", "translation": "kiz cocuk"},
                    {"original": "mère", "translation": "anne"},
                    {"original": "père", "translation": "baba"},
                    {"original": "frère", "translation": "erkek kardes"},
                    {"original": "soeur", "translation": "kiz kardes"},
                    {"original": "ami(e)", "translation": "arkadas"},
                    {"original": "mari", "translation": "koca"},
                    {"original": "femme", "translation": "es"},
                    {"original": "bon appétit", "translation": "afiyet olsun"},
                    {"original": "santé!", "translation": "serefe!"}
                ]
            }
        ]
    },
    "spanish": {
        "display_name": "Espagnol",
        "categories": [
            {
                "name": "Alimentation",
                "words": [
                    {"original": "nourriture", "translation": "comida"},
                    {"original": "fruit", "translation": "fruta"},
                    {"original": "légumes", "translation": "verduras"},
                    {"original": "pain", "translation": "pan"},
                    {"original": "fromage", "translation": "queso"},
                    {"original": "viande", "translation": "carne"},
                    {"original": "poisson", "translation": "pescado"},
                    {"original": "sel", "translation": "sal"},
                    {"original": "sucre", "translation": "azucar"},
                    {"original": "eau", "translation": "agua"},
                    {"original": "lait", "translation": "leche"},
                    {"original": "café", "translation": "cafe"},
                    {"original": "thé", "translation": "te"},
                    {"original": "bière", "translation": "cerveza"},
                    {"original": "vin", "translation": "vino"},
                    {"original": "riz", "translation": "arroz"},
                    {"original": "huile", "translation": "aceite"},
                    {"original": "animal", "translation": "animal"}
                ]
            },
            {
                "name": "Expressions & Pensée",
                "words": [
                    {"original": "quoi?", "translation": "que?"},
                    {"original": "rien", "translation": "nada"},
                    {"original": "quelque chose", "translation": "algo"},
                    {"original": "tout", "translation": "todo"},
                    {"original": "il y a", "translation": "hay"},
                    {"original": "il n'y a pas", "translation": "no hay"},
                    {"original": "c'est", "translation": "es"},
                    {"original": "je veux", "translation": "quiero"},
                    {"original": "j'aime", "translation": "me gusta"},
                    {"original": "je dois", "translation": "debo"},
                    {"original": "je peux", "translation": "puedo"},
                    {"original": "je pense", "translation": "pienso"},
                    {"original": "peut-être", "translation": "quizas"},
                    {"original": "et", "translation": "y"},
                    {"original": "ou", "translation": "o"},
                    {"original": "mais", "translation": "pero"},
                    {"original": "parce que", "translation": "porque"},
                    {"original": "pourquoi", "translation": "por que"}
                ]
            },
            {
                "name": "Verbes d'action",
                "words": [
                    {"original": "faire", "translation": "hacer"},
                    {"original": "aller", "translation": "ir"},
                    {"original": "venir", "translation": "venir"},
                    {"original": "partir", "translation": "salir"},
                    {"original": "attendre", "translation": "esperar"},
                    {"original": "écrire", "translation": "escribir"},
                    {"original": "lire", "translation": "leer"},
                    {"original": "commencer", "translation": "empezar"},
                    {"original": "finir", "translation": "terminar"},
                    {"original": "entrer", "translation": "entrar"},
                    {"original": "sortir", "translation": "salir"},
                    {"original": "courir", "translation": "correr"},
                    {"original": "voir", "translation": "ver"},
                    {"original": "écouter", "translation": "escuchar"},
                    {"original": "boire", "translation": "beber"},
                    {"original": "manger", "translation": "comer"},
                    {"original": "parler", "translation": "hablar"},
                    {"original": "comprendre", "translation": "entender"}
                ]
            },
            {
                "name": "Pronoms & Lieux",
                "words": [
                    {"original": "qui", "translation": "quien"},
                    {"original": "moi", "translation": "yo"},
                    {"original": "toi", "translation": "tu"},
                    {"original": "il/elle", "translation": "el/ella"},
                    {"original": "nous", "translation": "nosotros"},
                    {"original": "vous", "translation": "vosotros/usted"},
                    {"original": "ils", "translation": "ellos"},
                    {"original": "ceci", "translation": "esto"},
                    {"original": "cela", "translation": "eso"},
                    {"original": "où", "translation": "donde"},
                    {"original": "ici", "translation": "aqui"},
                    {"original": "là", "translation": "alli"},
                    {"original": "devant", "translation": "delante"},
                    {"original": "derrière", "translation": "detras"},
                    {"original": "à gauche", "translation": "a la izquierda"},
                    {"original": "à droite", "translation": "a la derecha"},
                    {"original": "dans", "translation": "en"},
                    {"original": "de", "translation": "de"}
                ]
            },
            {
                "name": "Maison & Ville",
                "words": [
                    {"original": "maison", "translation": "casa"},
                    {"original": "cuisine", "translation": "cocina"},
                    {"original": "chambre", "translation": "habitacion"},
                    {"original": "lit", "translation": "cama"},
                    {"original": "salle de bain", "translation": "bano"},
                    {"original": "table", "translation": "mesa"},
                    {"original": "chaise", "translation": "silla"},
                    {"original": "ville", "translation": "ciudad"},
                    {"original": "rue", "translation": "calle"},
                    {"original": "magasin", "translation": "tienda"},
                    {"original": "arbre", "translation": "arbol"},
                    {"original": "montagne", "translation": "montana"},
                    {"original": "mer", "translation": "mar"},
                    {"original": "soleil", "translation": "sol"},
                    {"original": "voiture", "translation": "coche"},
                    {"original": "bus", "translation": "autobus"},
                    {"original": "train", "translation": "tren"},
                    {"original": "voyage", "translation": "viaje"}
                ]
            },
            {
                "name": "Temps",
                "words": [
                    {"original": "quand", "translation": "cuando"},
                    {"original": "temps", "translation": "tiempo"},
                    {"original": "jamais", "translation": "nunca"},
                    {"original": "parfois", "translation": "a veces"},
                    {"original": "souvent", "translation": "a menudo"},
                    {"original": "toujours", "translation": "siempre"},
                    {"original": "maintenant", "translation": "ahora"},
                    {"original": "avant", "translation": "antes"},
                    {"original": "après", "translation": "despues"},
                    {"original": "matin", "translation": "manana"},
                    {"original": "après-midi", "translation": "tarde"},
                    {"original": "soir", "translation": "noche"},
                    {"original": "nuit", "translation": "noche"},
                    {"original": "aujourd'hui", "translation": "hoy"},
                    {"original": "demain", "translation": "manana"},
                    {"original": "hier", "translation": "ayer"},
                    {"original": "année", "translation": "ano"},
                    {"original": "mois", "translation": "mes"}
                ]
            },
            {
                "name": "Adjectifs",
                "words": [
                    {"original": "bon", "translation": "bueno"},
                    {"original": "mauvais", "translation": "malo"},
                    {"original": "beau", "translation": "bonito"},
                    {"original": "grand", "translation": "grande"},
                    {"original": "petit", "translation": "pequeno"},
                    {"original": "chaud", "translation": "caliente"},
                    {"original": "froid", "translation": "frio"},
                    {"original": "vite", "translation": "rapido"},
                    {"original": "lent", "translation": "lento"},
                    {"original": "nouveau", "translation": "nuevo"},
                    {"original": "ancien", "translation": "viejo"},
                    {"original": "facile", "translation": "facil"},
                    {"original": "difficile", "translation": "dificil"},
                    {"original": "important", "translation": "importante"},
                    {"original": "propre", "translation": "limpio"},
                    {"original": "sale", "translation": "sucio"},
                    {"original": "près", "translation": "cerca"},
                    {"original": "loin", "translation": "lejos"}
                ]
            },
            {
                "name": "Chiffres & Quantité",
                "words": [
                    {"original": "combien", "translation": "cuanto"},
                    {"original": "un peu", "translation": "un poco"},
                    {"original": "beaucoup", "translation": "mucho"},
                    {"original": "moins", "translation": "menos"},
                    {"original": "plus", "translation": "mas"},
                    {"original": "très", "translation": "muy"},
                    {"original": "trop", "translation": "demasiado"},
                    {"original": "0", "translation": "cero"},
                    {"original": "1", "translation": "uno"},
                    {"original": "2", "translation": "dos"},
                    {"original": "3", "translation": "tres"},
                    {"original": "4", "translation": "cuatro"},
                    {"original": "5", "translation": "cinco"},
                    {"original": "6", "translation": "seis"},
                    {"original": "7", "translation": "siete"},
                    {"original": "8", "translation": "ocho"},
                    {"original": "9", "translation": "nueve"},
                    {"original": "10", "translation": "diez"}
                ]
            },
            {
                "name": "Politesse",
                "words": [
                    {"original": "oui", "translation": "si"},
                    {"original": "non", "translation": "no"},
                    {"original": "bonjour", "translation": "hola"},
                    {"original": "salut", "translation": "hola"},
                    {"original": "bonsoir", "translation": "buenas tardes"},
                    {"original": "bonne nuit", "translation": "buenas noches"},
                    {"original": "au revoir", "translation": "adios"},
                    {"original": "s'il vous plaît", "translation": "por favor"},
                    {"original": "merci", "translation": "gracias"},
                    {"original": "de rien", "translation": "de nada"},
                    {"original": "excusez-moi", "translation": "disculpe"},
                    {"original": "pardon", "translation": "perdon"},
                    {"original": "comment ça va?", "translation": "como estas?"},
                    {"original": "je vais bien", "translation": "estoy bien"},
                    {"original": "je ne comprends pas", "translation": "no entiendo"},
                    {"original": "parlez plus lentement", "translation": "hable mas despacio"},
                    {"original": "comment vous appelez-vous?", "translation": "como se llama?"},
                    {"original": "je m'appelle []", "translation": "me llamo []"}
                ]
            },
            {
                "name": "Divers",
                "words": [
                    {"original": "enfant", "translation": "nino/nina"},
                    {"original": "garçon", "translation": "nino"},
                    {"original": "fille", "translation": "nina"},
                    {"original": "mère", "translation": "madre"},
                    {"original": "père", "translation": "padre"},
                    {"original": "frère", "translation": "hermano"},
                    {"original": "soeur", "translation": "hermana"},
                    {"original": "ami(e)", "translation": "amigo/a"},
                    {"original": "mari", "translation": "marido"},
                    {"original": "femme", "translation": "esposa"},
                    {"original": "bon appétit", "translation": "buen provecho"},
                    {"original": "santé!", "translation": "salud!"}
                ]
            }
        ]
    },
    "italian": {
        "display_name": "Italien",
        "categories": [
            {
                "name": "Alimentation",
                "words": [
                    {"original": "nourriture", "translation": "cibo"},
                    {"original": "fruit", "translation": "frutta"},
                    {"original": "légumes", "translation": "verdure"},
                    {"original": "pain", "translation": "pane"},
                    {"original": "fromage", "translation": "formaggio"},
                    {"original": "viande", "translation": "carne"},
                    {"original": "poisson", "translation": "pesce"},
                    {"original": "sel", "translation": "sale"},
                    {"original": "sucre", "translation": "zucchero"},
                    {"original": "eau", "translation": "acqua"},
                    {"original": "lait", "translation": "latte"},
                    {"original": "café", "translation": "caffe"},
                    {"original": "thé", "translation": "te"},
                    {"original": "bière", "translation": "birra"},
                    {"original": "vin", "translation": "vino"},
                    {"original": "riz", "translation": "riso"},
                    {"original": "huile", "translation": "olio"},
                    {"original": "animal", "translation": "animale"}
                ]
            },
            {
                "name": "Expressions & Pensée",
                "words": [
                    {"original": "quoi?", "translation": "che?"},
                    {"original": "rien", "translation": "niente"},
                    {"original": "quelque chose", "translation": "qualcosa"},
                    {"original": "tout", "translation": "tutto"},
                    {"original": "il y a", "translation": "c'e"},
                    {"original": "il n'y a pas", "translation": "non c'e"},
                    {"original": "c'est", "translation": "e"},
                    {"original": "je veux", "translation": "voglio"},
                    {"original": "j'aime", "translation": "mi piace"},
                    {"original": "je dois", "translation": "devo"},
                    {"original": "je peux", "translation": "posso"},
                    {"original": "je pense", "translation": "penso"},
                    {"original": "peut-être", "translation": "forse"},
                    {"original": "et", "translation": "e"},
                    {"original": "ou", "translation": "o"},
                    {"original": "mais", "translation": "ma"},
                    {"original": "parce que", "translation": "perche"},
                    {"original": "pourquoi", "translation": "perche"}
                ]
            },
            {
                "name": "Verbes d'action",
                "words": [
                    {"original": "faire", "translation": "fare"},
                    {"original": "aller", "translation": "andare"},
                    {"original": "venir", "translation": "venire"},
                    {"original": "partir", "translation": "partire"},
                    {"original": "attendre", "translation": "aspettare"},
                    {"original": "écrire", "translation": "scrivere"},
                    {"original": "lire", "translation": "leggere"},
                    {"original": "commencer", "translation": "iniziare"},
                    {"original": "finir", "translation": "finire"},
                    {"original": "entrer", "translation": "entrare"},
                    {"original": "sortir", "translation": "uscire"},
                    {"original": "courir", "translation": "correre"},
                    {"original": "voir", "translation": "vedere"},
                    {"original": "écouter", "translation": "ascoltare"},
                    {"original": "boire", "translation": "bere"},
                    {"original": "manger", "translation": "mangiare"},
                    {"original": "parler", "translation": "parlare"},
                    {"original": "comprendre", "translation": "capire"}
                ]
            },
            {
                "name": "Pronoms & Lieux",
                "words": [
                    {"original": "qui", "translation": "chi"},
                    {"original": "moi", "translation": "io"},
                    {"original": "toi", "translation": "tu"},
                    {"original": "il/elle", "translation": "lui/lei"},
                    {"original": "nous", "translation": "noi"},
                    {"original": "vous", "translation": "voi/Lei"},
                    {"original": "ils", "translation": "loro"},
                    {"original": "ceci", "translation": "questo"},
                    {"original": "cela", "translation": "quello"},
                    {"original": "où", "translation": "dove"},
                    {"original": "ici", "translation": "qui"},
                    {"original": "là", "translation": "la"},
                    {"original": "devant", "translation": "davanti"},
                    {"original": "derrière", "translation": "dietro"},
                    {"original": "à gauche", "translation": "a sinistra"},
                    {"original": "à droite", "translation": "a destra"},
                    {"original": "dans", "translation": "in"},
                    {"original": "de", "translation": "di"}
                ]
            },
            {
                "name": "Maison & Ville",
                "words": [
                    {"original": "maison", "translation": "casa"},
                    {"original": "cuisine", "translation": "cucina"},
                    {"original": "chambre", "translation": "camera"},
                    {"original": "lit", "translation": "letto"},
                    {"original": "salle de bain", "translation": "bagno"},
                    {"original": "table", "translation": "tavolo"},
                    {"original": "chaise", "translation": "sedia"},
                    {"original": "ville", "translation": "citta"},
                    {"original": "rue", "translation": "strada"},
                    {"original": "magasin", "translation": "negozio"},
                    {"original": "arbre", "translation": "albero"},
                    {"original": "montagne", "translation": "montagna"},
                    {"original": "mer", "translation": "mare"},
                    {"original": "soleil", "translation": "sole"},
                    {"original": "voiture", "translation": "macchina"},
                    {"original": "bus", "translation": "autobus"},
                    {"original": "train", "translation": "treno"},
                    {"original": "voyage", "translation": "viaggio"}
                ]
            },
            {
                "name": "Temps",
                "words": [
                    {"original": "quand", "translation": "quando"},
                    {"original": "temps", "translation": "tempo"},
                    {"original": "jamais", "translation": "mai"},
                    {"original": "parfois", "translation": "a volte"},
                    {"original": "souvent", "translation": "spesso"},
                    {"original": "toujours", "translation": "sempre"},
                    {"original": "maintenant", "translation": "adesso"},
                    {"original": "avant", "translation": "prima"},
                    {"original": "après", "translation": "dopo"},
                    {"original": "matin", "translation": "mattina"},
                    {"original": "après-midi", "translation": "pomeriggio"},
                    {"original": "soir", "translation": "sera"},
                    {"original": "nuit", "translation": "notte"},
                    {"original": "aujourd'hui", "translation": "oggi"},
                    {"original": "demain", "translation": "domani"},
                    {"original": "hier", "translation": "ieri"},
                    {"original": "année", "translation": "anno"},
                    {"original": "mois", "translation": "mese"}
                ]
            },
            {
                "name": "Adjectifs",
                "words": [
                    {"original": "bon", "translation": "buono"},
                    {"original": "mauvais", "translation": "cattivo"},
                    {"original": "beau", "translation": "bello"},
                    {"original": "grand", "translation": "grande"},
                    {"original": "petit", "translation": "piccolo"},
                    {"original": "chaud", "translation": "caldo"},
                    {"original": "froid", "translation": "freddo"},
                    {"original": "vite", "translation": "veloce"},
                    {"original": "lent", "translation": "lento"},
                    {"original": "nouveau", "translation": "nuovo"},
                    {"original": "ancien", "translation": "vecchio"},
                    {"original": "facile", "translation": "facile"},
                    {"original": "difficile", "translation": "difficile"},
                    {"original": "important", "translation": "importante"},
                    {"original": "propre", "translation": "pulito"},
                    {"original": "sale", "translation": "sporco"},
                    {"original": "près", "translation": "vicino"},
                    {"original": "loin", "translation": "lontano"}
                ]
            },
            {
                "name": "Chiffres & Quantité",
                "words": [
                    {"original": "combien", "translation": "quanto"},
                    {"original": "un peu", "translation": "un po"},
                    {"original": "beaucoup", "translation": "molto"},
                    {"original": "moins", "translation": "meno"},
                    {"original": "plus", "translation": "piu"},
                    {"original": "très", "translation": "molto"},
                    {"original": "trop", "translation": "troppo"},
                    {"original": "0", "translation": "zero"},
                    {"original": "1", "translation": "uno"},
                    {"original": "2", "translation": "due"},
                    {"original": "3", "translation": "tre"},
                    {"original": "4", "translation": "quattro"},
                    {"original": "5", "translation": "cinque"},
                    {"original": "6", "translation": "sei"},
                    {"original": "7", "translation": "sette"},
                    {"original": "8", "translation": "otto"},
                    {"original": "9", "translation": "nove"},
                    {"original": "10", "translation": "dieci"}
                ]
            },
            {
                "name": "Politesse",
                "words": [
                    {"original": "oui", "translation": "si"},
                    {"original": "non", "translation": "no"},
                    {"original": "bonjour", "translation": "ciao"},
                    {"original": "salut", "translation": "ciao"},
                    {"original": "bonsoir", "translation": "buonasera"},
                    {"original": "bonne nuit", "translation": "buonanotte"},
                    {"original": "au revoir", "translation": "arrivederci"},
                    {"original": "s'il vous plaît", "translation": "per favore"},
                    {"original": "merci", "translation": "grazie"},
                    {"original": "de rien", "translation": "prego"},
                    {"original": "excusez-moi", "translation": "mi scusi"},
                    {"original": "pardon", "translation": "scusa"},
                    {"original": "comment ça va?", "translation": "come stai?"},
                    {"original": "je vais bien", "translation": "sto bene"},
                    {"original": "je ne comprends pas", "translation": "non capisco"},
                    {"original": "parlez plus lentement", "translation": "parli piu lentamente"},
                    {"original": "comment vous appelez-vous?", "translation": "come si chiama?"},
                    {"original": "je m'appelle []", "translation": "mi chiamo []"}
                ]
            },
            {
                "name": "Divers",
                "words": [
                    {"original": "enfant", "translation": "bambino/bambina"},
                    {"original": "garçon", "translation": "ragazzo"},
                    {"original": "fille", "translation": "ragazza"},
                    {"original": "mère", "translation": "madre"},
                    {"original": "père", "translation": "padre"},
                    {"original": "frère", "translation": "fratello"},
                    {"original": "soeur", "translation": "sorella"},
                    {"original": "ami(e)", "translation": "amico/a"},
                    {"original": "mari", "translation": "marito"},
                    {"original": "femme", "translation": "moglie"},
                    {"original": "bon appétit", "translation": "buon appetito"},
                    {"original": "santé!", "translation": "salute!"}
                ]
            }
        ]
    }
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

CATEGORY_MERGE_TARGETS = {
    "Divers": "Modaux & Phrases",
    "Interrogations": "Modaux & Phrases",
    "Connecteurs": "Modaux & Phrases",
    "Lieux": "Maison & Ville",
    "Pronoms": "Modaux & Phrases",
}


def _normalize_easy_category_name(category_name, original_word):
    normalized_word = _normalize_original(original_word)

    if category_name == "Pronoms & Lieux":
        if normalized_word in LOCATION_WORD_HINTS:
            return "Lieux"
        return "Pronoms"

    if category_name in {"Temps", "Temps (suite) & État"}:
        return "Temps & État"

    if category_name == "Adjectifs & Divers":
        return "Adjectifs"

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
    words_by_key = {}
    ordered_keys = []

    for category in categories:
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
    for category in categories:
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


def get_guess_words(categories, difficulty="normal"):
    vocab_keys = set()
    for category in categories:
        for word in category["words"]:
            vocab_keys.add(_normalize_original(word["original"]))

    if difficulty == "easy":
        priority_words = EASY_NOUN_GUESS_WORDS
        extra_words = FUN_NOUN_GUESS_WORDS
        target_count = 50
    else:
        priority_words = FUN_NOUN_GUESS_WORDS
        extra_words = []
        target_count = 120

    selected_words = []
    selected_keys = set()

    for candidate in priority_words:
        key = _normalize_original(candidate)
        if key in selected_keys or key in vocab_keys:
            continue
        if not _is_guessable_word(candidate):
            continue
        selected_words.append(candidate)
        selected_keys.add(key)
        if len(selected_words) >= target_count:
            break

    if len(selected_words) < target_count:
        for candidate in extra_words:
            key = _normalize_original(candidate)
            if key in selected_keys or key in vocab_keys:
                continue
            if not _is_guessable_word(candidate):
                continue
            selected_words.append(candidate)
            selected_keys.add(key)
            if len(selected_words) >= target_count:
                break

    return selected_words


def get_language_data(lang_code, difficulty="normal"):
    lang_data = deepcopy(VOCABULARY[lang_code])
    categories = _normalized_easy_categories(lang_data["categories"])

    if difficulty == "easy":
        categories = _easy_categories(categories, target_count=200)

    lang_data["categories"] = _merge_tiny_categories(categories, min_size=3)

    return lang_data