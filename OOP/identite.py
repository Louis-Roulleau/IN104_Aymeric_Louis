

class vehicule:

    def __init__(self, name, vitesse, poids):
        self.vitesse = vitesse
        self.name = name
        self.poids = poids
        print('Le vehicule %s va à la vitesse de %d km/h et pèse %d kg.', % (name),% (vitesse),% (poids))

    def getVitesse(self):
        return self.__vitesse

    def getPoids(self):
        return self.__poids

    def doubler(self, vmax):
        if self.vitesse>vmax
            printf("Ce vehicule va plus vite")
            return 1
        return 0

class voiture(vehicule):
    def __str__(self):
        return "Je suis une voiture qui roule à "+str(self.getVitesse())" km/h."
    def doubler(self):
        print("Je double mes concurrents")

class motocyclette(vehicule):
    def __str__(self):
        return "Je suis une motocylette qui pèse à "+str(self.getPoids())" kg."
    def lever(self):
        print("Je roule en Y")
