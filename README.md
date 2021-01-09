# Projet d'analyse de données sur la consommation de drogues
## Drug consumption data analysis

![alt text](https://www.pourquoidocteur.fr/media/article/thunbs/uploded_istock-817839096-1538323443-1540667498.jpg)

# Objectif de ce projet
## Le but de ce projet est d'analyser et de faire des modèles de machine learning sur le dataset "Drug consumption (quantified) Data Set" par UCI

### Le dataset analysé
Lien vers le dataset : https://archive.ics.uci.edu/ml/datasets/Drug+consumption+%28quantified%29 

Datant de 2016, il réuni des données numériques et non numériques sur 1885 personnes interrogées et classifie les consommateurs de différentes drogues en fonction de leur personnalité à travers le monde.
Au total, 32 attributs sont analysés pour chaque personne.

Chaque ligne du dataset correspond à la consommation de différentes drogues selon la personnalité et les caractéristiques d'un individu (âge, genre, origine, pays de résidence...)

### Problématique 
Ce dataset permet il de relever des résultats réalistes sur la consommation de drogue dans le monde ?

### Contenu de ce projet

Dans ce projet vous trouverez :
* Un jupyter notebook avec l'ensemble de nos analyses de données dans un 1er temps puis deux prédictions sur des algorithmes de classifications
* Un document PDF résumant en détail notre démarche, nos résultats et conclusions
* Une API du modèle avec la meilleure précision obtenue (modèle SVC) avec Flask qui permet à un utilisateur de saisir ses scores obtenus à des tests de personnalités et qui donne la prédiction suivante : **Consommateur de Cannabis** ou **Non Consommateur de Cannabis**


### Résulats

Partie 1 : Analayse du dataset
* Les âges les plus représentés dans le dataset sont les jeunes : 18 24 ans et les 25 34 ans
* Les personnes blanches sont sur représentées par rapport aux autres
* Les personnes provenant de l'Angleterre (UK) sont sur-représentés également
* Les pays de résidences souffrent aussi d'une répartition non équitable : La Nouvelle Zélande, l'Australie, l'Irlande et le Canada sont vraiment présents en faible quantité par rapport aux Etats-Unis et de l'Angleterre qui représentent à eux 85% du dataset

Nous avons pu faire des liens intéressantes entre consommations de stupéfiants et personnalité notamment.
Exemples : L'alcool est le plus consommé chez les personnes ayant quitté l'école avant 16 ans et la nicotine est le plus consommé chez les personnes ayant quitté l'école à 18 ans ou encore le cannabis est moins consommé chez les personnes ayant quittél'école à 16 ans et le plus chez les personnes ayant un diplome.


Partie 2 : Modèles de classification

Modèles testés : 
* Logistic Regression 
* KNeighbors Classification
* Random Forest
* SVC
* Decision Tree

*1ere classification : prédire la consommation d'alcool d'une personne en connaissant les résultats des tests de personnalités la concernant ainsi que sa consommation d'autres substances

Meilleure précision obtenue : 0,40 avec SVC

*2ème classification : prédire la consommation de Cannabis grâce aux données sur la personnalité

Meilleure précision obtenue : 0,78 avec SVC


### Conclusion
Ainsi, ce dataset ne nous donnera pas une idée réaliste de la consommation mondiale puisque les pays du monde ne sont pas bien représentés mais plutôt une idée de la consommation aux USA et UK, et il permet aussi de faire des liens avec la personnalité qui sont réalistes.

Nous avons eu plaisir à faire ce projet, nous esperons que nos analyses vous plairont ! :grinning:






