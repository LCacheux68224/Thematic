myArgs <- commandArgs(trailingOnly = TRUE)

# recuperation des parametres passes en argument
Fichier_CSV = myArgs[1]
Taille_des_carreaux = myArgs[2]
Rayon_de_lissage = myArgs[3]
Liste_de_deciles = myArgs[4]
Grille = myArgs[5]
Sortie = myArgs[6]
RlibFolder = myArgs[7]

# Chargement des packages

library(sp, lib.loc=RlibFolder)
library(rgdal, lib.loc=RlibFolder)
library(Rcpp, lib.loc=RlibFolder)
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

write.csv2(file=Sortie,outputLissage )

nbColonnes = dim(donnees)[2]-2
lineString <- paste0(paste(replicate(3,"String"),collapse =","),',')
nbRealColumn <- paste0(paste(replicate(nbColonnes,"Real"),collapse =','),',')
fullLineString <- paste0(paste0(lineString,nbRealColumn),'String')

fileConn<-file(paste0(Sortie,'t'))
writeLines(c(fullLineString), fileConn)
close(fileConn)


