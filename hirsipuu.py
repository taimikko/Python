infile = open("sanat.txt")
sanat = infile.read()  # lukee koko tiedoston sisällön merkkijonoon
infile.close()
# sitten sama fiksummin

with open("sanat.txt") as infile:
    sanat = infile.read()
# ylläoleva takaa että tiedosto suljetaan, kun with -silmuksasta poistutaan

import sys
# sys.argv on lista komentoparametreista [0] = ohjeman nimi, [1] eka parametri, jne
with open(sys.argv[1], encoding="utf-8") as infile: # utf-8:lla saadaan ääkköset oikein, kun tiedosto on linuxista
    sanat = infile.read()

arvauskertoja = int(sys.argv[2])
#print(sanat[:100])  # tulostetaan 100 ekaa merkkiä
sanat = sanat.split(',')
# strip() poistaa alusta ja lopusta tyhjät
sanat = list(map(lambda mj: mj.strip().lower(), sanat))

#print(sanat[:10])  # tulostetaan 10 ekaa sanaa
import random
# random:ista löytyy monia funktioita satunnaisuuden käsittelyyn
sanaidx = random.randint(0, len(sanat)-1) # hakee satunnaisen indeksinumeron annetulta väliltä
#print(sanat[sanaidx]) #tulostaa satunnaisen sanan

sana = random.choice(sanat) # palauttaa satunnaisen sanan listasta
#print(sana)

nykysana = ["_"]*len(sana)
# print(" ".join(nykysana)) # kirjaimet joinattu toisiinsa tyhjällä merkkijonolla erotettuna

arvauksia = 0
arvauksiaJaljella = arvauskertoja
while arvauksiaJaljella>0 and ("_" in nykysana):
    print("Arvaus:", " ".join(nykysana))
    arvaus = input("Anna ("+str(arvauksia+1)+".) kirjain:")
    if len(arvaus) != 1:
        print("Anna vain yksi kirjain.")
    else:
        arvauksia +=1
        oikein = False
        for i, k in enumerate(nykysana):
            if nykysana[i] == "_" and arvaus == sana[i]:
                nykysana[i] = sana[i]
                oikein = True
                # oikein arvattu
            else:
                pass # väärin arvattu
        if not oikein:
            print("Väärin arvattu.")
            arvauksiaJaljella -= 1
    if not "_" in nykysana:
        break

if "_" in nykysana:
    print("Hävisit. sana oli:", sana)
else:
    print("Voitit! Onneksi olkoon!")
