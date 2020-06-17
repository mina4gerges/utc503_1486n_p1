class Note:

    def __init__(self, num_etudiant, code_cours, note):
        self.num_etudiant = num_etudiant
        self.code_cours = code_cours
        self.note = note
        
    def setNumEtdiant(self, num_etudiant):
        self.code = num_etudiant
    
    def getNumEtdiant(self):
        return self.num_etudiant
    
    def setCodeCours(self, code_cours):
        self.code_cours = code_cours
    
    def getCodeCours(self):
        return self.code_cours

    def setNote(self, note):
        self.note = note
    
    def getNote(self):
        return self.note
        