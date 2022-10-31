import random

class Soldier():
    def __init__(self, health, strength):
        self.strength = strength
        self.health = health
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def attack(self):
        return super().attack()

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health >0:
            return("{} has received {} points of damage".format(self.name, damage))
        else:
            return("{} has died in act of combat".format(self.name))
    
    def battleCry(self):
        return "Odin Owns You All"

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def attack(self):
        return super().attack()
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health >0:
            return("A Saxon has received {} points of damage".format(damage))
        else:
            return("A Saxon has died in combat")

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def saxonAttack(self):
        try:
            viking = self.vikingArmy[random.randint(0,len(self.vikingArmy)-1)]
            saxon = self.saxonArmy[random.randint(0,len(self.saxonArmy)-1)]
        except:
            pass
        viking.receiveDamage(saxon.strength)
        if viking.health < 0:
            self.vikingArmy.remove(viking)

    def vikingAttack(self):
        try:
            viking = self.vikingArmy[random.randint(0,len(self.vikingArmy)-1)]
            saxon = self.saxonArmy[random.randint(0,len(self.saxonArmy)-1)]
        except:
            pass
        saxon.receiveDamage(viking.strength)
        if saxon.health < 0:
            self.saxonArmy.remove(saxon)

    def showstatus(self):
        if len(self.saxonArmy) == 0:
            print("Vikings have won the war of the century!")
        elif len(self.vikingArmy) == 0:
            print("Saxons have fought for their lives and survive another day...")ç
        else:
            print("Vikings and Saxons are still in the thick of battle.")


    



    
    
    