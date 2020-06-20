class Etudiant:

    def __init__(self, num, prenom, nom, niveau):
        self.num = num
        self.prenom = prenom
        self.nom = nom
        self.niveau = niveau

    def set_num_etudiant(self, num):
        self.num = num

    def get_num_etudiant(self):
        return self.num

    def set_nom_etudiant(self, nom):
        self.nom = nom

    def get_nom_etudiant(self):
        return self.nom
    
    def set_prenom_etudiant(self, prenom):
        self.nom = prenom

    def get_prenom_etudiant(self):
        return self.prenom

    def set_niveau_etudiant(self, niveau):
        self.nom = niveau

    def get_niveau_etudiant(self):
        return self.niveau
