import math


def main ():
    rivi = input("Anna suorakulmion kanta: ")
    kanta = float(rivi)
    rivi = input("Anna suorakulmion korkeus: ")
    korkeus = float(rivi)
    pinta_ala = kanta * korkeus
    piiri = kanta + korkeus + kanta + korkeus

    print("Suorakulmion pinta-ala on:", pinta_ala, "neliometria")

    print("Suorakulmion piiri on:", piiri, "cm")
    

main()



