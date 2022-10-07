class Duck:
    def __init__(self, species="Common Duck", migratory=True):
        self.species = species
        self.migratory = migratory

    def fly(self):
        return "Fly like an eagle, into the future!"

    def walk(self):
        return "waddle, waddle, waddle"

    def talk(self):
        return "quack, quack, quack"
