# 6.7.2018

# listojen käsittelyn apuvälineitä
# sorted(), it.sort()
it = [1,2,3,4,7,6,5]
st = sorted(it) # tekee uuden listan, joka on sortattu
it.sort() # järjestää tämän vanhan listan -> it on sortattu
st = sorted(it, reverse = True)

# sorted toimii kaikille sekvensseille, joiden alkiot voidaa lukea yksitellen, 
# it.sort() toimii vain listoille

mjt = ["yksi", "kaksi", "kolme", "nelkku", "viisi"]
print(sorted(mjt)) # aakkosjärjestykseen, tulos sortattuna, mutta mjt ei ole muuttunut
for w in sorted(mjt):
    print(w)

print(mjt)
# sort on stabiili --> jos lajittelussa ovat saman arvoiset niin pysyvät samassa järjestyksessä kuin olivat ennen
mjt = sorted(mjt) # aakkosjärjestykseen
print(mjt)
mjt = sorted(mjt, key=len) # pituusjärjestykseen
# [len(mjt[0]), len(mjt[1]), ...]
# sorted , key= voi olla mikä tahansa funktio, joka ottaa yhden parametrin ja palauttaa jotain
print(mjt)
mjt = ["yksi", "kaksi", "kolme", "nelkku", "viisi"]
def pitJaAkkVert(mj):
    return[len(mj), mj] # palauttaa kaksiosaisen tuloksen
    # jos åalauttaa tuplen, niin   return (len(mj), mj)   
    # ja listalle                  return [len(mj), mj]
print(sorted(mjt, key=pitJaAkkVert))
# lajittelutuloksessa voi olla pitkiäkin tuloslistoja, joista aina verrataan vasemmanpuoleista ensin keskenään, sitten tokaa keskenään, jne.

# [1,2] lista
# (1,2) tuple (tuple on "lista" jota ei voi muuttaa)
# tuple = "monikko" ?
# map()   muuntaa arvoja

#pit on lista, jossa on merkkijonojen pituudet
pit = list(map(len, mjt))
print(pit)

# listan karsinta ->  filter()
def alkaaKoolla(mj):
    return mj[0]=="k"

k_alkuiset = tuple(filter(alkaaKoolla, mjt))
print(k_alkuiset)

#lambda -funktio
k_alk = tuple(filter(lambda x: x[0]=="k", mjt))
# lambdafunktiolla ei ole nimeä, sisältö vastaa samaa kuin 
# def: lambda(x):
#   return x[0]=="k"

# lambdan notaatio sallii useitakin parametreja, mutta sortissa ja filterissä odotetaan funktiota, ojka ottaa vain yhden parametrin


it = [1,2,3,4,7,6,5]
print(list(reversed(it))) # listan kääntö (reversed pitää vielä muuttaa takaisin listaksi)

mjt = ["yksi", "kaksi", "kolme", "nelkku", "viisi"]
# enumerate() jos haluaa käydä joukon läpi niin että tietää sekä indeksin että alkion
for idx, arvo in enumerate(mjt):
    print("indeksi:", idx, "arvo:", arvo)

# enumerate tuottaa tupleja (pareja, joissa ekana on indeksi ja tokana arvo)
# (0, "yksi")
# (1, "kaksi") jne.
i,j,k = (1,2,3) # laillinen sijoitus: i=1; j=2; k=3

# zip() viittaa vetoketjuun (zipper) liitetään vuoron perään
ft = [1.5, 3.4, 2.2, 6.1, 1.1]
yhd = list(zip(mjt, ft,it)) # yhdistää listat listaksi tupleja
print (yhd)
# zip -objektia voi iteroida, mutta tulostukseen se pitää muuttaa listaksi

# merkkijonojen join -funktio
print(" ".join(mjt)) # loppuun ei tule välilyöntiä, mutta merkkijonojen välissä on " "
print(" ".join(map(str, ft))) # ft:n arvot mapataan merkkijonoiksi str()-funktiolla ja joinataan toisiinsa, välissä on " "

# tiedostojen käsittelyä


# omia
lista1 = [1, 2, 3]
# lisa2 = lista1 --> ,olemmat osoittavat samaan olioon, joten toisen muutaminen muuttaa molempia!
lista2 = [] + lista1 # tyhjään listaa lisätään alkuperäinen lista
lista1[1] = 5
print(lista1) #[1, 5, 3]
print(lista2) #[1, 2, 3]

