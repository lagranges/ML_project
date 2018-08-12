# Kaggle Project
# Home Credit Risk

## Author
* Van Tuan LE

## Introduction
    Machine Learning project

## Structure

### download:
    Ceux qui sont téléchargés, par examples, les kernels
    
### documents:
    Les articles, livres
    
### img:
    Où se trouvent les images, par exemple les images des features importances

### input:
    Où se trouvent les raw datas
    
### data:
    Où se trouvent les fichiers *csv, *h5 des données qui sont résulats de feature engeerings.
    But: éviter refaire feature engeerings.

### logs:
     Où se trouvent les fichiers .log qui contient le résultat complet
     d'une expériementation (ce qui affichie dans la console)

### pretrained:
    Où se trouveent les fichier *.pkl, *.h5 qui contient des models entrainés
    
### submissions:
    Où se trouvent les fichiers de submissions.

### storage:
    Pour stocker n'importe quel fichiers qui n'appartient à aucun répertoire ci-déssus.
    -> aussi appelée " la poubelle"
    
### src
    * Flavien
        Où se trouve le code d'une expérimentation (nommé F_experimentation_i.py ), il contient de:
            1. Configuration: le prefix pour tous les fichiers liés par example "ensembling1_feature_engineering2"
            Note: essayer utiliser le nom du model, de la fonction feature engineering utilisés pour le prefix.
            2. Préparation de données: Lire les données en input et data
            3. Feature engineering: Feature engineering :)
            4. Modeling or Cross validation:
            5. Génération du fichier de submission.
    * Tuan
        Les fichier T_experimentation_i.py
        Pareil, un répertoire sont crées pour chacun pour éviter le conflict en pushant code.
    * models:
        Implémentation des models 
    * feature_engineering:
        Implémentation des feature engineerings
    * cross_validation:
        Implémentation des cross_validations

### ensembeling:
     Où se trouvent les fichiers *.csv qui sont utilisé pour model d'ensembeling
