myArgs <- commandArgs(trailingOnly = TRUE)

# recuperation des parametres passes en argument
Fichier_CSV = myArgs[1]
Taille_des_carreaux = myArgs[2]
Rayon_de_lissage = myArgs[3]
Liste_de_quantiles = myArgs[4]
SCR = myArgs[5]
Grille = myArgs[6]
grille_lissee = myArgs[7]
RlibFolder = myArgs[8]
 
library(RcppParallel, lib.loc=RlibFolder)
library(sf, lib.loc=RlibFolder)
library(btb, lib.loc=RlibFolder) 
  
# chargement des donnees et de la grille
donnees <- read.csv(Fichier_CSV)
grilleCarreaux <- as.data.frame(st_read(Grille, 
                          stringsAsFactors = F))
                          
# Création d'un vecteur contenant la liste des quantiles
if (Liste_de_quantiles == 'NULL') {
  listeQuantiles <- NULL
} else {
  listeQuantiles <- as.numeric(strsplit(Liste_de_quantiles,";")[[1]])
}

# Lissage des variables
donnees_smooth <- kernelSmoothing(dfObservations = donnees
                              , sEPSG = SCR
                              , iCellSize = Taille_des_carreaux
                              , iBandwidth = Rayon_de_lissage
                              , dfCentroids = grilleCarreaux
                              , vQuantiles = listeQuantiles)

st_write(donnees_smooth, grille_lissee, layer = "grille_lissee")


