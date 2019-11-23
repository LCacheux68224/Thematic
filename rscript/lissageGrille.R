myArgs <- commandArgs(trailingOnly = TRUE)

# recuperation des parametres passes en argument
Fichier_CSV = myArgs[1]
Taille_des_carreaux = myArgs[2]
Rayon_de_lissage = myArgs[3]
Liste_de_deciles = myArgs[4]
Grille = myArgs[5]
Sortie = myArgs[6]
RlibFolder = myArgs[7]

Sortie_CSVT = paste0(Sortie,'t')

# Chargement des packages

library(sp, lib.loc=RlibFolder)
# library(rgdal, lib.loc=RlibFolder)
# library(Rcpp, lib.loc=RlibFolder)
 
library(btb, lib.loc=RlibFolder)
library(foreign)

# chargement des donnees et de la grille
donnees <- read.csv(Fichier_CSV)
grille<- read.dbf(Grille, as.is = T)

# formatage du la liste des deciles sous forme de vecteur
if (Liste_de_deciles == 'NULL') {
    listeDeciles <- NULL
} else {
    listeDeciles <- as.numeric(strsplit(Liste_de_deciles,";")[[1]])

}

# Lissage des variables
donnees_smooth=kernelSmoothing(dfObservations = donnees,cellSize = Taille_des_carreaux, bandwidth = Rayon_de_lissage, dfCentroids = grille, vQuantiles = listeDeciles )



# recuperation du dataframe apres lissage
outputLissage = data.frame(donnees_smooth@.Data) 
# ajout des entetes de colonnes
colnames(outputLissage) <- names(donnees_smooth)
# ajout de la variable ID
outputLissage$ID <- paste(donnees_smooth$x, donnees_smooth$y,sep = "_")





write.csv(file=Sortie,outputLissage)

# Creation du fichier csvt pour le typage automatique des variables dans Qgis

# 3 premieres colonnes de type 'String'
lineString <- "String,String,String,"
# Ajout des colonnes des variables lissees de type 'Real'
nbColonnes = dim(donnees_smooth)[2]-2
realColumns <- paste0(paste(replicate(nbColonnes,"Real"),collapse =','),',')
lineString <- paste0(lineString,realColumns)
# Ajout de la colonne ID de type 'String'
lineString <- paste0(lineString,'String')

fileConn<-file(Sortie_CSVT)
writeLines(c(lineString), fileConn)
close(fileConn)


