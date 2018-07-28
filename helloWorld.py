x = 4
y = 5
print(x+y)
mj = 'Tämäkin on "merkkijono".\nSiinä voi olla \'hipsuja\'.'
print(mj)
pi = 3.142
print(pi)
z = x
print(id(x), id(z))  # kommentti
print("x=", x, "z=", z)
z = 1
print(id(x), id(z))  # pilkulla erotetut arvot tulostetaan pilkulla erotettuna
print("x=", x, "z=", z)
print("x=", x, "z=", z, sep="-->")
print(5/98)  # normaali jakolasku
print(5//98)  # kokonaislukujakolasku
print(13 % 8)  # modulo = jakojäännös 5
print(2**3)  # 2 potenssiin 3
print(100**0.5)  # 100 potenssiin puoli = neliöjuuri -> 10 (0.5)
# kokonaisluvut voi olla mielivaltaisen suuria
x = 99999999999999999999999999999999999999999999999999999999999999999999999999
y = 88888888888888888888888888888888888888888888888888888888888888888888888888
print(x*y)
# liukuluvut on kuitenkin rajallisia
x = x+0.5
print(x*y)

# for i in sekvenssi/iteroitava
#range(mistä, mihin, step)
for i in range(0, 6, 2):
    # kaikkien rivien pitää olla yhtä paljon sisennetty
    j = i
    # vaikka i:tä muutettaisiin täällä niin se menee seuraavalla kierroksella taas range:n mukaan
    while j < 6:  # lohkon perässä on kaksoispiste
        # str():llä muutetaan numero merkkijonoksi, jonka voi yhdistää plussalla
        print("i,j", str(i)+","+str(j))
        j += 1  # pythonissa ei ole j++:aa
# puolipisteellä voi pythonissa yhdistää useita eri lauseita samalle riville
#x = 1;y = 2;z = 3

# pythonin taulukot: listan käsite kattaa taulukon
it = [4, 5, 'kuusi', 7]
print(it)  # taulukko osaa muuntaa itsensä merkkijonoksi joka näyttää taulukolta
for arvo in it:
    print(arvo)
print("------")
for i in range(0, len(it)):
    print(it[i])

t10 = [0] * 10  # vastaa javan taulukkoa t=[10]
print(t10, type(t10))

it.append("kaheksan")
it.append([1, 2, 3])
print(it)

del it[0]
del it[len(it)-1]
print(it)

while len(t10) > 0:
    del(t10[0])
    print(t10)

it.insert(2, 'kaks')
print(it)

nimi = "m"
#nimi = input("Anna nimesi:")
print("Hei", nimi)

# True ja False kirjoitetaan isolla alkukirjaimella
taulu = []
while True:
    rivi = input("Anna luku (tai lopeta): ")
    if rivi == "lopeta":
        break
    try:
        luku = float(rivi)
        taulu.append(luku)
    except:
        print("Anna luku tai kirjoita 'lopeta'")
print(taulu)
summa = 0
s = 0
try:
    for arvo in taulu:
        # tyypin muunnos tai tulkinta kokonaisluvuksi/desimaalilluvuksi
        summa += int(arvo)
        s += float(arvo)
except ValueError as virhe:  # ValueError
    print("tuli virhe (ValueError):", virhe)
print("summa=", summa)

pii = 3.14159
x = round(pii, 3)
print(pii, x)

i = 2
# and ja or kirjoitetaan
if i > 1 and i < 10:
    print(i)

if i < 4 or i > 10:
    print(i)

# it then else if ...
if i > 10:
    print("eka")
elif i == 5:
    print("toka")
else:
    print("kolmas")


# merkkijono  käyttäytyy kuin taulukko, jota ei voi muuttaa
mj = "neljä"
#mj[1] = "e"
print(mj[1], mj)

mj="4 5 6"
k=mj.split(sep=" ")
print(k)

