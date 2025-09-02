import math

def laske_ympyran_ala(r):
    return math.pi * r * r

sade = float(input("Kerro ympyran sade: "))

pinta_ala = laske_ympyran_ala(sade)

print(f"Ympyran pinta-ala on: {pinta_ala:6.2f}" )




