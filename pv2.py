#29.6.2018

luku = None # None vastaa nullia, ei viittaa mihinkään
arvo = 1; # float(input())
if (luku is None) or (luku > arvo):  # is,  and,  or
    luku = arvo

# iStep = 1 if a < b else -1           Pythonissa
# iStep = (a < b) ? 1 : -1             Muissa kielissä
# voi käyttää esim for-silmukassa
# for i in range(a, b + iStep), iStep): # jos iStep on negat. niin mennään ylhäältä alas 

print("#####################################")
print("#"*(4*9+1)) # sama tulos kuin edelleisellä rivillä

# geany editor
# atom editor

#funktion sisällä voi viitata globaaliin muuttujaan global etusanalla


def lisaa(x):
    #global y  #toimii ilman globaliakin
    print("lisaa(",x,"):",x+y)
y=1
lisaa(2)
 
import paketti # tiedostosta paketti.py
paketti.funktio() # kutsuttaessa viitattava paketin nimen kautta

# vaihtoehtoisesti

from paketti import funktio() 
    funktio() # jolloin käyttö helpompaa
 

# import samalla suorittaa importoitavan tiedoston jos seillä on suoritettavaa koodia!
# voidaan estää käytämällä __name__ :a
# if __name__ == "__main__":
# suorituksessa olevan ohjelman nimi on __main__
# jos moduli on importattu niin __main__ on importoidun modulin nimi (kun sitä suoritetaan)

# jos funktio ei palauta mitään niin sen palautusarvo on None
