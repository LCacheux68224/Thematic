myArgs <- commandArgs(trailingOnly = TRUE)

# recuperation des parametres passes en argument
Fichier_CSV = myArgs[1]
Taille_des_carreaux = as.numeric(myArgs[2])
Rayon_de_lissage = as.numeric(myArgs[3])
listeQuantiles = myArgs[4]
SCR = myArgs[5]
grille_lissee = myArgs[6]
RlibFolder = myArgs[7]


library(RcppParallel, lib.loc=RlibFolder)
# fileConn<-file('c:/temp/log.txt')
# writeLines(c(log), fileConn)
# close(fileConn)

library(sf, lib.loc=RlibFolder)
library(btb, lib.loc=RlibFolder)



# chargement des donnees et de la grille
donnees <- read.csv(Fichier_CSV)

# Création d'un vecteur contenant la liste des quantiles
if (listeQuantiles == 'NULL') {
  listeQuantiles <- NULL
} else {
  listeQuantiles <- as.numeric(strsplit(listeQuantiles,";")[[1]])
}

# Lissage des variables
donnees_smooth=kernelSmoothing(dfObservations = donnees,
                               sEPSG = SCR,
                               iCellSize = Taille_des_carreaux,
                               iBandwidth = Rayon_de_lissage,
                               vQuantiles = listeQuantiles)
                           
st_write(donnees_smooth, grille_lissee, layer = "grille_lissee")


