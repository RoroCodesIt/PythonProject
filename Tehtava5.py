import math

#Annetaan vakioarvot

leiviska_naulaa = 20
naula_luotia = 32
luoti_grammoina = 13.3

#Kysytään käyttäjältä määrät

leiviskat = float(input("Anna leiviskat: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))

#Muunnetaan kaikki massa luodeiksi
luodit_yhteensa = (leiviskat * leiviska_naulaa * naula_luotia + naula * naula_luotia + luoti)

#Muunnetaan luodit grammoiksi
grammat_yhteensa = luodit_yhteensa * luoti_grammoina

#Erotellaan kokonaiset kilogrammat ja loppugrammat

kilogrammat = int(grammat_yhteensa // 1000)
grammat = grammat_yhteensa % 1000

#Tulostetaan tulos

print("\nMassa nykymittojen mukaan: ")
print(f"{kilogrammat} kilogrammaa ja {grammat: .2f} grammaa.")

