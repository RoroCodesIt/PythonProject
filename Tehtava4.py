import math

def main():
    rivi = input("Anna kokonaisluku: ")
    luku1 = float(rivi)
    rivi = input ("Anna toinen kokonaisluku: ")
    luku2 = float(rivi)
    rivi = input("Anna kolmas kokonaisluku: ")
    luku3 = float(rivi)
    summa = luku1 + luku2 + luku3
    tulo = luku1 * luku2 * luku3
    keski_arvo = (luku1 + luku2 + luku3) /3

    print("Kokonaislukujen summa on: ", summa)
    print("Kokonaislukujen tulo on: ", tulo)
    print("Kokonaislukujen keski-arvo on: ", keski_arvo)


main()