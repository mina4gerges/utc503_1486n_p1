class Etudiant:

    def __init__(self, num, prenom, nom, niveau):
        self.num = num
        self.prenom = prenom
        self.nom = nom
        self.niveau = niveau
        
    def setNumEtudiant(self, num):
        self.num = num
    
    def getNumEtudiant(self):
        return self.num
    
    def setNomEtudiant(self, nom):
        self.nom = nom
    
    def getNomEtudiant(self):
        return self.nom
    
    def setPrenomEtudiant(self, prenom):
        self.nom = prenom
    
    def getPrenomEtudiant(self):
        return self.prenom
    
    def setNiveauEtudiant(self, niveau):
        self.nom = niveau
    
    def getNiveauEtudiant(self):
        return self.niveau
        