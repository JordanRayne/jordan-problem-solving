class Character:
    def __init__(self, name, health, attack, defence):
        self.name = name

        self.health = max(0, min(100, health))
        self.attack = attack
        self.defence = defence

    def info(self):
        return f"Character: {self.name} | HP: {self.health} | ATK: {self.attack} | DEF: {self.defence}"

    def take_damage(self, amount):

        effective_damage = max(0, amount - self.defence)
        self.health -= effective_damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} took {effective_damage} damage!")

    def heal(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100
        print(f"{self.name} healed for {amount} points!")




hero = Character("Knight", 100, 20, 10)
villain = Character("Goblin", 50, 15, 2)


print(hero.info())
print(villain.info())


hero.take_damage(25)
villain.take_damage(20)


hero.heal(10)
villain.heal(50)


print("\nFinal Stats:")
print(hero.info())
print(villain.info())
