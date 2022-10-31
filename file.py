from vikingsClasses import *

miguel = Saxon(20, 50)
gonzalo = Viking("Gonzalet", 30, 80)
zazo = Saxon(70,10)

lagranguerra = War()
lagranguerra.addSaxon(miguel)
lagranguerra.addSaxon(zazo)
lagranguerra.addViking(gonzalo)
lagranguerra.vikingAttack()

print(lagranguerra.saxonArmy)
print(lagranguerra.vikingArmy)
