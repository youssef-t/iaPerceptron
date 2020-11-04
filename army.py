
class Army:
    def __init__(self, chef, moral):
        self.chef = chef
        self.moral = moral

    def __repr__(self):
        string = "Chef: {}\t Army Boost: {}".format(self.chef, self.moral)
        return string

    def get_chef(self): return self.chef
    def get_moral(self): return self.moral
    def set_chef(self, chef): self.chef = chef
    def set_boost_army(self, moral): self.moral = moral

    def get_total_moral(self): return self.chef.get_boost() * self.moral

