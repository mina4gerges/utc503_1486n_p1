class Cours:

    def __init__(self, code, intitule, niveau):
        self.code = code
        self.intitule = intitule
        self.niveau = niveau
        
    def setCodeCours(self, code):
        self.code = code
    
    def getCodeCours(self):
        return self.code
    
    def setIntituleCours(self, intitule):
        self.intitule = intitule
    
    def getIntituleCours(self):
        return self.intitule

    def setNiveauCours(self, niveau):
        self.nom = niveau
    
    def getNiveauCours(self):
        return self.niveau
        