Mini projet 1
Le mini-projet consiste à gérer la base de données d’une université. Les données sont stockées dans quatre classes: 
Étudiant : chaque instance contient les attributs suivants: 
numéro de l’étudiant
prénom de l’étudiant 
nom de l’étudiant 
niveau de l’étudiant (cyle d’inscription A,B ou C)
Cours : chaque instance contient les attributs suivants d’un cours:
code du cours
intitulé du cours
niveau du cours (A, B ou C)
Note : chaque instance contient les informations suivante d’une note d’un étudiant, obtenues pour un
cours:
numéro de l’étudiant
code du cours
note
BD: contient 3 listes
Liste des étudiants
Liste des cours
Liste des notes


Nous souhaitons être capable de réaliser les requêtes suivantes permettant de gérer la base de données:
Ajouter un étudiant : Créer un étudiant et l’ajouter dans la BD
Supprimer un étudiant de la BD
Editer un étudiant : modifier les informations d’un étudiant (sauf l’identifiant)
Ajouter un cours : Créer un cours et l’ajouter dans la BD
Supprimer un cours  
Editer un cours : modifier les informations d’un cours (sauf l’identifiant)
Ajouter une note : créer la note (vérifier que les identifiants d’étudiant et cours existent) et l’ajouter à la BD
Supprimer une note
Éditer une note
Calculer la moyenne de la classe
Calculer la moyenne d’un étudiant
Consulter les notes d’une classe
Consulter les notes d’un étudiant

Travail demandé:
Appliquer le paradigme Objet et créer les classes, constructeurs, méthodes, etc… nécessaire pour respecter les spécifications. remarques, vous aurez en principe 4 classes, dans une première version réaliser les méthodes dans un paradigme impératif (ou fonctionnel récursif)
Dans une seconde version réaliser les méthodes: Calculer la moyenne de la classe, Calculer la moyenne d’un étudiant, Consulter les notes d’une classe et Consulter les notes d’un étudiant avec le paradigme “filter-map-reduce”

