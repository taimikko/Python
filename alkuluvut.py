"""
laskee alkulukuja ja tallettaa ne oletuksena alkuluvut.txt -nimiseen tiedostoon
luvut ovat isoissa taulukoissa omilla riveillään esim.
[2, 3, 5, 7, 11, 13, 17]
[19, 23, 29, 31, 37, 41, 43]
...
laskeAlkulukuja() tekee varsinaisen laskennan, kaikki muu on koristetta kärsimättömälle
"""
from timeit import default_timer as timer
from os import rename, remove
from shutil import copyfile
import time
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

# pool = ThreadPool()
# results = pool.map(my_function, my_array)
# pool.close()
# pool.join()

TIEDOSTO = "alkuluvut.txt"

"""
def kolmas(primes, kpl):
    talletusvali = 100000
    if len(primes) == 0:
        ed = Seuranta(0, 1, TIEDOSTO)
        primes = [2, 3]
        ed.kirjoita(primes, 2, 1)
    else:
        ed = Seuranta(len(primes), max(primes), TIEDOSTO)    
    lkm = len(primes)
    luku = max(primes) 
    while lkm < kpl:
        luku += 2  # parillisia ei tarkastella
        prime = True
        stopper = luku**0.5  # i/2
        for alkuluku in primes:
            if luku % alkuluku == 0:
                prime = False  # not prime
                break
            if alkuluku > stopper:
                break  # prime
        if prime:
            lkm += 1
            primes.append(luku)  
            if lkm % talletusvali == 0:
                talletusvali = ed.kirjoita(primes, lkm, luku, talletusvali) 
            elif lkm % (talletusvali//10) == 0:
                print(luku, "lkm:", "{:11,d}".format(lkm), sep="\t", end="\r")  # tilannetiedotus

    ed.kirjoita(primes, lkm, luku, talletusvali)
"""



class Seuranta:
    def __init__(self, lkm=0, alkuluku=0, tiedosto="alkuluvut.txt", aika=timer(), talletusvali=1000):
        self.__lkm = lkm
        self.__alkuluku = alkuluku
        self.__aika = aika
        self.__talletusvali = talletusvali
        self.__tiedosto = tiedosto
        self.tiheys = [10000000, 5000000, 2000000, 1000000, 500000, 250000, 100000,
          50000, 25000, 10000, 5000, 2500, 1000, 500, 250, 100, 50, 25, 10, 5, 2]

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

    suurinAlkuluku = property(getAlkuluku, setAlkuluku)
    aika = property(getAika, setAika)
    talletusvali = property(getTalletusvali, setTalletusvali)

    def taajuus(self, vanha):
        uusi = vanha
        kulunut = timer() - self.aika
        if kulunut > 300:  # 5min = 300 s
            uusi = self.pienenna(vanha)
        elif kulunut < 120:  # 2 min = 120 s
            uusi = self.suurenna(vanha)
        return(uusi)


    def pienenna(self, luku):
        self.tiheys.sort()
        i = self.tiheys.index(luku)
        if i > 0:
            return(self.tiheys[i-1])
        return(luku)


    def suurenna(self, luku):
        self.tiheys.sort()
        i = self.tiheys.index(luku)
        if i < len(self.tiheys)-1:
            return(self.tiheys[i+1])
        return(luku)


    def kirjoita(self, primes, alkulukujaYhteensa, suurinAlkulku=1, talletusvali=100000):
        uusiaAlkulukuja = alkulukujaYhteensa-self.lkm
        etenema = suurinAlkulku-self.suurinAlkuluku
        print("talletetaan", "{:11,d}".format(alkulukujaYhteensa), "alkulukua ", end="")
        # 2M alkuluvun jälkeen ei toimi enää näin vaan ilmoittaa MemmoryErrorista
        # print(sorted(primes), file=out)

        if uusiaAlkulukuja > 0:
            a = timer()
            SELDOM = 10**6
            if alkulukujaYhteensa % SELDOM == 0:
                primes.sort()  # ei tarvita einakaan yhdessä säikeessä
                # kestää ...
                with open(self.tiedosto, "w", encoding="utf-8") as out:
                    for i in range(len(primes)//SELDOM):
                        print(primes[i*SELDOM:(i+1)*SELDOM],
                              file=out, flush=True)
            else:
                with open(self.tiedosto, "a", encoding="utf-8") as out:
                    print(primes[-uusiaAlkulukuja:], file=out,
                        flush=True)  # nopeampi
            print(self.kulunutAika(self.aika), uusiaAlkulukuja, "{:.3f}".format(etenema/uusiaAlkulukuja), "\ttalletus:",
                self.kulunutAika(a))  # lkm = len(primes)

        # tehdään kopio varmuuden vuoksi
        backup = self.tiedosto[:-4]+"_" + str(alkulukujaYhteensa)+"_"+time.strftime("%H%M%S", time.localtime())+".txt"

        try:
            remove(backup)
        except FileNotFoundError:
            pass
        try:
            copyfile(self.tiedosto, backup)
            # rename(tiedosto, backup)
        except Exception as e:
            print("Tiedoston varmuuskopiointi ei onnistu:",
                  self.tiedosto, backup, e)

        talletusvali=self.taajuus(talletusvali)
        self.lkm=alkulukujaYhteensa
        self.aika=timer()
        self.suurinAlkuluku=suurinAlkulku
        return(talletusvali)

    def kulunutAika(self, a):
        b=timer()
        s=(b-a) % 60
        m=int((b-a)//60)
        h=int(m//60)
        m=int(m % 60)
        if h == 0:
            return("{:0>2d}:{:0>5.2f}".format(m, s))
        return("{:0>2d}:{:0>2d}:{:0>5.2f}".format(h, m, s))

def lueAiemmat(vanhatiedosto):
    print("Luetaan tiedostoa", vanhatiedosto)
    try:
        primes=[]
        with open(vanhatiedosto, "r", encoding="utf-8") as infile:
            for row in infile:
                apu=list(map(int, row[1:-2].split(", ")))
                primes.extend(apu)
    except IOError as e:
        print(" Virhe tiedoston", vanhatiedosto,
              "lukemisessa ", e.args, e.strerror)
        primes=[]
    except MemoryError as e:
        print(" Muistivirhe tiedoston", vanhatiedosto, "lukemisessa ", e.args)
        exit
    primes.sort()
    print(" ", primes[-3:], end="")
    print("\tluettu (", len(primes), ") kpl")
    return primes

def laskeAlkulukuja(primes, kpl):
    talletusvali = 100000
    if len(primes) == 0:
        ed = Seuranta(0, 1, TIEDOSTO)
        primes = [2, 3]
        ed.kirjoita(primes, 2, 1)
    else:
        ed = Seuranta(len(primes), max(primes), TIEDOSTO)    
    lkm = len(primes)
    luku = max(primes) 
    while lkm < kpl:
        luku += 2  # parillisia ei tarkastella
        prime = True
        stopper = luku**0.5  # i/2
        for alkuluku in primes:
            if luku % alkuluku == 0:
                prime = False  # not prime
                break
            if alkuluku > stopper:
                break  # prime
        if prime:
            lkm += 1
            primes.append(luku)  
            if lkm % talletusvali == 0:
                talletusvali = ed.kirjoita(primes, lkm, luku, talletusvali) 
            elif lkm % (talletusvali//10) == 0:
                print("isoin:{:14,d}".format(luku), "lkm:{:11,d}".format(lkm), end="\r")  # tilannetiedotus

    ed.kirjoita(primes, lkm, luku, talletusvali)



if __name__ == "__main__":
    primes=lueAiemmat(TIEDOSTO)

    lkm=input("Montako haluat: (enter = laske 'kaikki')")
    if lkm == None or lkm == "":
        lkm=10**10

    print(time.strftime("%H:%M:%S", time.localtime()))
    # if len(primes) >= 10000000:  # yli 10M
    #     kolmas(primes, int(lkm))
    # else:
    laskeAlkulukuja(primes, int(lkm))

    print(time.strftime("%H:%M:%S", time.localtime()))
