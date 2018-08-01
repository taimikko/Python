from timeit import default_timer as timer
from os import rename, remove
from shutil import copyfile
import time
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

#pool = ThreadPool()
#results = pool.map(my_function, my_array)
# pool.close() 
# pool.join()

TIEDOSTO = "alkuluvut.txt"

"""
def kolmas(primes, kpl):
    n = 10**10  # int(input("n:"))
    talletusvali = 100000 
    ed_lkm = lkm = len(primes)
    if lkm <10000000:
        exit
    alku = max(primes)+2
    edAika = timer()
    ed_i = alku
    for i in range(alku, n, 2):
        if lkm >= kpl:
            break
        prime = True
        stopper = i**0.5  # i/2
        for j in primes:
            if i % j == 0:
                prime = False  # not prime
                break
            if j > stopper:
                break  # prime
        if prime:
            lkm += 1
            primes.append(i)  # .append(i) # .add(i)
            if lkm % talletusvali == 0:
                talletusvali = kirjoita(primes, lkm,
                         lkm-ed_lkm,  i-ed_i, talletusvali)  # välitalletus
                ed_lkm = lkm
                ed_i = i
                edAika = timer()
            elif lkm % (talletusvali//10) == 0:
                print(i, "lkm:", lkm, sep="\t", end="\r")  # tilannetiedotus

    kirjoita(primes,  lkm, lkm-ed_lkm,  i-ed_i, talletusvali)
"""

def toka(primes, kpl):
    talletusvali = 100000 
    ed_lkm = lkm = len(primes)
    if lkm > 0:
        alku = max(primes)
    else:
        primes = [2, 3]
        alku = 3
        lkm = ed_lkm = 2
        
    edAika = timer()
    i = ed_i = alku
    ed = Seuranta(lkm, alku, TIEDOSTO)
    ed.kirjoita(primes, lkm, lkm, 2) 
    while lkm < kpl:
        i += 2 # parillisia ei tarkastella
        prime = True
        stopper = i**0.5  # i/2
        for j in primes:
            if i % j == 0:
                prime = False  # not prime
                break
            if j > stopper:
                break  # prime
        if prime:
            lkm += 1
            primes.append(i)  # .append(i) # .add(i)
            if lkm % talletusvali == 0:
                talletusvali = ed.kirjoita(primes, lkm,
                         lkm-ed_lkm, i-ed_i, talletusvali)  # välitalletus
                ed_lkm = lkm
                ed_i = i
                edAika = timer()
            elif lkm % (talletusvali//10) == 0:
                print(i, "lkm:", lkm, sep="\t", end="\r")  # tilannetiedotus

    ed.kirjoita(primes, lkm, lkm-ed_lkm, i-ed_i, talletusvali)
                         


tiheys = [10000000, 5000000, 2000000, 1000000, 500000, 250000, 100000,
          50000, 25000, 10000, 5000, 2500, 1000, 500, 250, 100, 50, 25, 10, 5, 2]


def taajuus(ed_aika, vanha):
    uusi = vanha
    kulunut = timer() - ed_aika
    if kulunut > 300:  # 5min = 300 s
        uusi = pienenna(vanha)
    elif kulunut < 120:  # 2 min = 120 s
        uusi = suurenna(vanha)
    return(uusi)


def pienenna(luku):
    tiheys.sort()
    i = tiheys.index(luku)
    if i > 0:
        return(tiheys[i-1])
    return(luku)


def suurenna(luku):
    tiheys.sort()
    i = tiheys.index(luku)
    if i < len(tiheys)-1:
        return(tiheys[i+1])
    return(luku)



class Seuranta:
    def __init__(self, lkm=0, alkuluku=0, tiedosto="alkuluvut.txt",aika=timer(), talletusvali= 1000):
        self.__lkm = lkm
        self.__alkuluku = alkuluku
        self.__aika = aika
        self.__talletusvali = talletusvali
        self.__tiedosto = tiedosto

    @property
    def tiedosto(self):
        return(self.__tiedosto)

    @property
    def lkm(self):
        return(self.__lkm)

    @lkm.setter
    def lkm(self, lkm):
        self.__lkm = lkm
    
    def getAlkuluku(self):
        return(self.__alkuluku)

    def setAlkuluku(self, alkuluku):
        self.__alkuluku = alkuluku
    
    def getAika(self):
        return(self.__aika)

    def setAika(self, aika):
        self.__aika = aika

    def getTalletusvali(self):
        return(self.__talletusvali)

    def setTalletusvali(self, talletusvali):
        self.__talletusvali = talletusvali

    suurinAlkuluku_i = property(getAlkuluku, setAlkuluku)
    aika = property(getAika, setAika)
    talletusvali = property(getTalletusvali, setTalletusvali)

    def kirjoita(self, primes, lkm, ero=0, i=0, talletusvali=100000):  
        # ed_lkm = edellisen talletuskerran alkulukujen määrä
        # ed_i = edellisellä talletuskerralla suurin alkuluku
        # talletusväli
        print("talletetaan", lkm, "alkulukua ", end="")  
        # 2M alkuluvun jälkeen ei toimi enää näin vaan ilmoittaa MemmoryErrorista
        # print(sorted(primes), file=out)  

        print( lkm, ero, i, talletusvali) 
        if ero > 0:
            a = timer()
            SELDOM = 10**6 
            if lkm % SELDOM == 0:
                primes.sort() # ei tarvita einakaan yhdessä säikeessä
                with open(self.tiedosto, "w", encoding="utf-8") as out:  # kestää ...
                    for i in range(len(primes)//SELDOM):
                        print(primes[i*SELDOM:(i+1)*SELDOM], file=out, flush=True)
            else:
                with open(self.tiedosto, "a", encoding="utf-8") as out:
                    print(primes[-ero:], file=out,
                        flush=True)  # nopeampi
            print(kulunutAika(self.aika), ero, i/ero, "\ttalletus:",
                kulunutAika(a)  # lkm = len(primes)

        # tehdään kopio varmuuden vuoksi
        backup = self.__tiedosto[:-4]+"_" + str(lkm)+"_"+time.strftime("%H%M%S", time.localtime())+".txt"
        try:
            remove(backup)
        except FileNotFoundError:
            pass
        try:
            copyfile(self.tiedosto, backup)
            #rename(tiedosto, backup)
        except Exception as e:
            print("Tiedoston varmuuskopiointi ei onnistu:", self.tiedosto, backup, e)

        #talletusvali = kirjoita(primes, lkm, lkm-ed_lkm,  i-ed_i, talletusvali) 
        ed_lkm = lkm
        ed_i = i
        

        talletusvali = taajuus(self.aika, talletusvali)
        self.aika = timer()
        return(talletusvali)

    def kulunutAika(self, a):
        b = timer()
        s = (b-a) % 60
        m = int((b-a)//60)
        h = int(m//60)
        m = int(m % 60)
        if h == 0:
            return("{:0>2d}:{:0>5.2f}".format(m, s))
        return("{:0>2d}:{:0>2d}:{:0>5.2f}".format(h, m, s))

def lueAiemmat(vanhatiedosto):
    start = timer()
    print("Luetaan tiedostoa", vanhatiedosto)
    try:
        primes = []
        with open(vanhatiedosto, "r", encoding="utf-8") as infile:
            for row in infile:
                apu = list(map(int, row[1:-2].split(", ")))
                primes.extend(apu)
    except IOError as e:
        print(" Virhe tiedoston", vanhatiedosto, "lukemisessa ", e.args, e.strerror)
        primes = []
    except MemoryError as e:
        print(" Muistivirhe tiedoston", vanhatiedosto, "lukemisessa ", e.args)
        exit
    primes.sort()
    print(" ", primes[-3:], end="")
    end = timer()
    print("\tluettu (", len(primes), ") kpl :", aika(start, end))
    return primes

if __name__ == "__main__":
    primes = lueAiemmat(TIEDOSTO)
    
    lkm = input("Montako haluat:")
    if lkm == None or lkm == "":
        lkm = 10**10
    
    print(time.strftime("%H:%M:%S", time.localtime()))
    if len(primes) >= 10000000: #yli 10M
        kolmas(primes, int(lkm))
    else:
        toka(primes, int(lkm))
    
    print(time.strftime("%H:%M:%S", time.localtime()))
