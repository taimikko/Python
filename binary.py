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
import zipfile
import gzip

TIEDOSTO = "alku_koe2bin.txt"


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

    def kirjoita(self, primes, alkulukujaYhteensa, suurinAlkuluku=1, talletusvali=100000):
        uusiaAlkulukuja = alkulukujaYhteensa-self.lkm
        etenema = suurinAlkuluku-self.suurinAlkuluku
        print("talletetaan", "{:11,d}".format(alkulukujaYhteensa), "alkulukua ", end="")
        # 2M alkuluvun jälkeen ei toimi enää näin vaan ilmoittaa MemmoryErrorista
        # print(sorted(primes), file=out)

        if uusiaAlkulukuja > 0:
            a = timer()
            SELDOM = 10**7
            if alkulukujaYhteensa % SELDOM == 0:
                #primes.sort()  # ei tarvita einakaan yhdessä säikeessä
                # kestää ...
                with open(self.tiedosto, "w", encoding="utf-8") as out:
                    for i in range(len(primes)//SELDOM):
                        print(primes[i*SELDOM:(i+1)*SELDOM],
                              file=out, flush=True)
                # tehdään kopio varmuuden vuoksi
                backup = self.tiedosto[:-4]+"_" + str(alkulukujaYhteensa)+"_"+time.strftime("%H%M%S", time.localtime())+".txt"
                try:
                    remove(backup)
                except FileNotFoundError:
                    pass
                try:
                    copyfile(self.tiedosto, backup)
                except Exception as e:
                    print("Tiedoston varmuuskopiointi ei onnistu:",
                        self.tiedosto, backup, e)
            else:
                with open(self.tiedosto, "a", encoding="utf-8") as out:
                    print(primes[-uusiaAlkulukuja:], file=out,
                        flush=True)  # nopeampi
            print(self.kulunutAika(self.aika), uusiaAlkulukuja, "{:.3f}".format(etenema/uusiaAlkulukuja), "\ttalletus:",
                self.kulunutAika(a))  # lkm = len(primes)

        self.lkm=alkulukujaYhteensa
        self.aika=timer()
        self.suurinAlkuluku=suurinAlkuluku
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

def lueBinary(vanhatiedosto):
    print("Luetaan tiedostoa", vanhatiedosto)
    try:
        primes=[]
        with gzip.open(vanhatiedosto, "rb") as infile:
            primes = infile.read() #str(infile.read())#.split()
        primes = str(primes)[3:-2]
        primes = primes.split(", ")
        primes = list(map(int, primes))
        #print(primes[:20],"|", primes[-20:], "\n==========\n")
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


def tulostaPrimes(uusitiedosto): 
    s = Seuranta(tiedosto=uusitiedosto)
    alkulukujaYhteensa = len(primes)
    suurinAlkuluku = max(primes)
    print(uusitiedosto, "talletetaan", "{:11,d}".format(alkulukujaYhteensa), "alkulukua ", end="")

    a = timer()
    #if alkulukujaYhteensa % SELDOM == 0:
    with open(s.tiedosto, "w", encoding="utf-8") as out:
        print(primes, file=out, flush=True)
            # for i in range(len(primes)//SELDOM):
            #     print(primes[i*SELDOM:(i+1)*SELDOM],
            #             file=out, flush=True)

    # tehdään kopio varmuuden vuoksi
    backup = s.tiedosto[:-4]+"_" + str(alkulukujaYhteensa)+"_"+time.strftime("%H%M%S", time.localtime())+".txt"
    try:
        remove(backup)
    except FileNotFoundError:
        pass
    try:
        copyfile(s.tiedosto, backup)
    except Exception as e:
        print("Tiedoston varmuuskopiointi ei onnistu:",
            s.tiedosto, backup, e)

    print("suurin:",suurinAlkuluku,"\ttalletus:",s.kulunutAika(a))  


def tulostaBinary(uusitiedosto): # "w" tai "wb"
    s = Seuranta(tiedosto=uusitiedosto+".gz")
    alkulukujaYhteensa = len(primes)
    suurinAlkuluku = max(primes)
    print(s.tiedosto,"talletetaan", "{:11,d}".format(alkulukujaYhteensa), "alkulukua ", end="")

    a = timer()
    with gzip.open(s.tiedosto, "wb") as outfile:
        outfile.write(bytes(str(primes), 'UTF-8'))
    # with zipfile.ZipFile(s.tiedosto, 'w') as out:
    #     for i in range(len(primes)//SELDOM):
    #         out.writestr(primes[i*SELDOM:(i+1)*SELDOM])
    
    # tehdään kopio varmuuden vuoksi
    backup = s.tiedosto+"_" + str(alkulukujaYhteensa)+"_"+time.strftime("%H%M%S", time.localtime())+".vara"
    try:
        remove(backup)
    except FileNotFoundError:
        pass
    try:
        copyfile(s.tiedosto, backup)
    except Exception as e:
        print("Tiedoston varmuuskopiointi ei onnistu:",
            s.tiedosto, backup, e)

    print("suurin:",suurinAlkuluku,"\ttalletus:",s.kulunutAika(a))  


if __name__ == "__main__":
    print(time.strftime("%H:%M:%S", time.localtime()))
    primes=lueAiemmat("alku_koe.txt")

    print(time.strftime("%H:%M:%S", time.localtime()))
    #laskeAlkulukuja(primes, int(lkm))
    tulostaBinary("alku_koe2bin.txt")

    print(time.strftime("%H:%M:%S", time.localtime()))

    primes = lueBinary("alku_koe2bin.txt.gz")
    print(time.strftime("%H:%M:%S", time.localtime()))
    tulostaPrimes("alku_bin2txt.txt")

    print(time.strftime("%H:%M:%S", time.localtime()))