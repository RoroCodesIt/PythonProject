import random

#Kolmenumeroinen koodi (numerot välillä 0-9)

kolmenumero_koodi = ""
for _ in range(3):
    kolmenumero_koodi += str(random.randint(0, 9))


nelinumero_koodi = ""
for _ in range(4):
    nelinumero_koodi += str(random.randint(1, 6))

#Tulostetaan koodit

print("Kolmenumeroisen lukon koodi: ", kolmenumero_koodi)
print("Nelinumeroisen lukon koodi: ", nelinumero_koodi)



