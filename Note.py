class Note:

    def __init__(self, num_etudiant, code_cours, note):
        self.num_etudiant = num_etudiant
        self.code_cours = code_cours
        self.note = note
        
    def get_num_etudiant(self):
        return self.num_etudiant
    
    def set_code_cours(self, code_cours):
        self.code_cours = code_cours
    
    def get_code_cours(self):
        return self.code_cours

    def set_note(self, note):
        self.note = note
    
    def get_note(self):
        return self.note
