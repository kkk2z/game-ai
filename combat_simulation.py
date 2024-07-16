import random

class Combatant:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(0, self.attack_power)
        other.health -= damage
        return damage

    def is_alive(self):
        return self.health > 0

def battle(combatant1, combatant2):
    while combatant1.is_alive() and combatant2.is_alive():
        damage = combatant1.attack(combatant2)
        print(f"{combatant1.name}が{combatant2.name}に{damage}のダメージを与えました。")
        if not combatant2.is_alive():
            return combatant1.name
        
        damage = combatant2.attack(combatant1)
        print(f"{combatant2.name}が{combatant1.name}に{damage}のダメージを与えました。")
        if not combatant1.is_alive():
            return combatant2.name
