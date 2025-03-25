# Base class for a superhero
class Superhero:
    def __init__(self, name, superpower, alias, weakness):
        self.name = name
        self.superpower = superpower
        self.alias = alias
        self.weakness = weakness

    def use_power(self):
        return f"{self.name} uses their incredible {self.superpower} to save the day!"

    def reveal_identity(self):
        return f"The superhero is actually {self.alias} in disguise!"

# Subclass for a sidekick, inheriting from Superhero
class Sidekick(Superhero):
    def __init__(self, name, superpower, alias, weakness, mentor):
        super().__init__(name, superpower, alias, weakness)
        self.mentor = mentor

    def assist_hero(self):
        return f"{self.name}, the loyal sidekick of {self.mentor}, assists with {self.superpower}!"

# Example objects
hero = Superhero("Captain Thunder", "lightning control", "Ethan Sparks", "water")
sidekick = Sidekick("Flashbolt", "superspeed", "Liam Swift", "ice", "Captain Thunder")

# Using methods
print(hero.use_power())
print(hero.reveal_identity())
print(sidekick.use_power())
print(sidekick.assist_hero())
