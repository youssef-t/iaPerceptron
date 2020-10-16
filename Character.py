
class Character:
    def __init__(self, nom, prenom, age, profession,boost):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.profession = profession
        self.boost = boost

    def __repr__(self):
        string = "nom: {}\nprenom: {}\nage: {}\nprofession: {}\nboost: {}".format(self.nom, self.prenom, self.age, self.profession,
                                self.boost)
        return string

