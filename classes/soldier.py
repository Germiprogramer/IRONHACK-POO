class Soldier():
    def __init__(self, health, strength):
        self.strength = strength
        self.health = health
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage