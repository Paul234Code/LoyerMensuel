class Personne(object):
    # classe personne et son construteur
    def __init__(self, prenom, nom, age, profession):
        self.prenom = prenom
        self.nom = nom
        self.age = age
        self.profession = profession

    def getPrenom(self):
        return self.prenom

    def getNom(self):
        return self.nom

    def getAge(self):
        return self.age

    def getProfession(self):
        return self.profession

    # les setteurs
    def setPrenom(self, prenom):
        self.prenom = prenom

    def setNom(self, nom):
        self.nom = nom

    def setAge(self, age):
        self.age = age

    def setProfession(self, profession):
        self.profession = profession


