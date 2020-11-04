
class Character:
    def __init__(self, nom, prenom, age, profession, boost):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.profession = profession
        self.boost = float(boost)

    def __repr__(self):
        string = "nom: {}\tprenom: {}\tage: {}\tprofession: {}\tboost: {}".format(self.nom, self.prenom, self.age, self.profession,
                                self.boost)
        return string

    def get_nom(self): return self.nom
    def get_prenom(self): return self.prenom
    def get_age(self): return self.age
    def get_profession(self): return self.profession
    def get_boost(self): return self.boost
    def set_nom(self, nom): self.nom = nom
    def set_prenom(self,prenom): self.prenom = prenom
    def set_age(self,age): self.age = age
    def set_profession(self,profession): self.profession = profession
    def set_boost(self,boost): self.boost = boost
