myArgs <- commandArgs(trailingOnly = TRUE)

# 'c:/users/lionel/appdata/local/temp/tmptya3_n/output.csv', '1000', '15000', 'NULL', 27572, u'C:/Users/lionel/Desktop/QGIS/batch/output1.shp', 'C:/Users/lionel/Documents/configQgis/Wien/qgisconfig/python/plugins/BeyondTheBorder/rlib'

# recuperation des parametres passes en argument
Fichier_CSV = myArgs[1]
Taille_des_carreaux = as.numeric(myArgs[2])
Rayon_de_lissage = as.numeric(myArgs[3])
Liste_de_deciles = myArgs[4]
SCR = myArgs[5]
grille_lissee = myArgs[6]
RlibFolder = myArgs[7]

# verification et chargement des packages 

# verification et chargement des packages

library(sp, lib.loc=RlibFolder)
library(rgdal, lib.loc=RlibFolder)
library(Rcpp, lib.loc=RlibFolder)
library(btb, lib.loc=RlibFolder)

# chargement des donnees et de la grille
donnees <- read.csv(Fichier_CSV)

# formatage du la liste des deciles sous forme de vecteur
if (Liste_de_deciles == 'NULL') {
    listeDeciles <- NULL
} else {
    listeDeciles <- as.numeric(strsplit(Liste_de_deciles,";")[[1]])
}

# Lissage des variables
donnees_smooth=kernelSmoothing(dfObservations = donnees,cellSize = Taille_des_carreaux, bandwidth = Rayon_de_lissage , vQuantiles = listeDeciles )

# Creation du fond de carte et enregistrement en shapefile
grille=smoothingToGrid(donnees_smooth,as.character(SCR))
writeOGR(grille, grille_lissee, "grille", driver = "GPKG")
