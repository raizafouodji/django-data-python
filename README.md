
Projet HATVP
============
Liste des participants au projet:
   1. Raissa Tatsa'a Fouodji
   2. Mohammad Backer Ibrahim
   3. Jahd Jabre
   4. Thibault Lefebvre
   5. Amaury Mouquet
   6. Ayoub Ouzahout
Projet disponible sur **GitHub** : https://github.com/raizafouodji/django-data-python
**Champs d'étude du jeu de données**
La Haute Autorité pour la Transparence de la Vie Publique est une institution chargée de controler la
déontologie des responsables publics et de gérer les répertoires des représentants d'intérets.
Elle met à disposition de tous les citoyens des fichiers open-data contenant des informations sur les
mouvements financiers déclarés entre responsables d'interets responsables politiques. Ces fichiers sont
librement téléchargeables sur [le site internet de la HATVP](https://www.hatvp.fr/le-repertoire/#open-data-repertoire).
Dans le cadre de ce projet, nous avons étudié et développé une application permettant de l'exploiter les
données issues d'un lot de 15 fichiers au format .CSV (15 tables accompagnées d'un fichier de documentation).

Méthodologie de traitement des données.
=======================================

La collecte des données
-----------------------
Le lot de 15 fichiers à analyser recence sous forme de tables les informations nécessaires à la compréhension
des relations entre les représentants d'intérêts et les responsables publiques lorsque sont prises des décisions
publiques. Cela permet par exemple de connaitre les organisations ayant exercées des actions de lobying auprès
de responsables politiques, avec les noms des responsables, les dates, les montants etc.
Pour rendre l'analyse et le traitement des fichiers CSV plus aisés, nous les avons transformé au format CSV.
En plus du fichier de documentation, nous avons donc travaillé sur les 15 tables suivantes:
1._informations_generales.csv
2._dirigeants.csv
3._collaborateurs.csv
4._clients.csv
5._affiliations.csv
6._niveaux_interventions.csv
7._domaines_interventions.csv
8._objets_activites.csv
9._secteurs_activites.csv
10._actions_menees.csv
11._beneficiaires.csv
12._decisions_concernees.csv
13._ministeres_aai_api.csv
14._observations.csv
15._exercices.csv

L'angle d'attaque de l'application
-------------------------
- Nous souhaitons créer une application permettant à son utilisateur de rechercher les actions de lobbying effectuées par une entreprise. Grâce a cette application, inscrire le nom de l'entreprise permettra d'obtenir toutes les informations de manière claire.

Exploration des données
-----------------------
- Nous avons analysé chaque table une par une afin de mieux comprendre les enjeux de ce jeu de données et d'établir un angle d'attaque. Suite à cette exploration nous avons décidé de nous focaliser premièrement sur le cercle d'influence d'une entreprise et enfin sur l'intéraction entre les entreprises et les ministères afin de mieux comprendre les influences dans les hautes sphères de l'état.

Construction des modèles
------------------------
- Nous avons construit 15 modèles en rapport avec les tables et leur caractéristiques.

La représentation des résultats
-------------------------------
L'utilisateur de l'application devra inscrire l'entreprise souhaité dans un input prévu à cet effet. L'input va déclencher une requête SQL qui va nous permettre d'afficher les résultat sur la page d'application.


Technologies utilisées pour la création de l'application
-------------------------------------------------------
L'application permettant l'interprétation des données a été développée avec Python 3.8 et Django 3.0
Postgres va nous permettre d'utiliser SQL
Pour le front : Bootstrap(html/css)


Difficultés rencontrées
------------------------------
Nous avons rencontré au debut du projet un difficulté pour l'importation des données sur SQLite3 dûe au temps de chargement des données. On a résolu ce problème avec POSTGRESQL. 
Nous avons également eu un problème au niveau du temps par ce que nous n'avons pas été informés à temps par l'administration afin de continuer sur le proget.

Installations requises
-------------------------------------------------------------
1. Créer un environnement virtuel python 3

2. Installer django 
    1. pip install django
3. Installer une base de donnée postgreSQL
    1. Créer un  utilisateur ,et une base de donnée.
    2. Aller dans le fichier settings.py du projetpython et remplacer ‘NAME’  par le nom de votre base de donnée,’USER’ par le nom de l’utilisateur,et 'PASSWORD' par votre password.

4. Installer l'adaptateur de base de données PostgreSQL
    1. $ pip install psycopg2
5. Installer l’extension qui transformer des ensembles de données en tableaux HTML
    1. $ pip install django_tables2
6. Installler l’extension  pour afficher ou masquer dynamiquement les colonnes à l'aide de jQuery.
    1. $ pip install django-tables2-column-shifter

7. Préparer la base de données.
    1. $ python manage.py makemigrations HATVP_app
    2. puis  migrer vos models
    3. python manage.py migrate

8. Importer les donnees en base de donnée
    1. python manage.py import

9. Créer un super-utilisateur pour accéder a la page d’administration : 
    1. python manage.py createsuperuser

10. Démarrer le serveur :
    1. python manage.py runserver





