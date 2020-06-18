class Cours:

    def __init__(self, code, intitule, niveau):
        self.code = code
        self.intitule = intitule
        self.niveau = niveau
        
    def set_code_cours(self, code):
        self.code = code
    
    def get_code_cours(self):
        return self.code
    
    def set_intitule_cours(self, intitule):
        self.intitule = intitule
    
    def get_intitule_cours(self):
        return self.intitule

    def set_niveau_cours(self, niveau):
        self.niveau = niveau
    
    def get_niveau_cours(self):
        return self.niveau
