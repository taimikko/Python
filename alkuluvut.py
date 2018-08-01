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


class Seuranta:
    def __init__(self, lkm=0, alkuluku=0, tiedosto="alkuluvut.txt", aika=timer(), talletusvali=100000):
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

    def tarkistaTulostusTaajuus(self):
        kulunut = timer() - self.aika
        if kulunut > 600:  # 5min = 300 s
            self.pienenna()
        elif kulunut < 280:  # 2 min = 120 s
            self.suurenna()
        

    def pienenna(self):
        self.tiheys.sort()
        i = self.tiheys.index(self.talletusvali)
        if i > 0:
            self.talletusvali = self.tiheys[i-1]


    def suurenna(self):
        self.tiheys.sort()
        i = self.tiheys.index(self.talletusvali)
        if i < len(self.tiheys)-1:
            self.talletusvali = self.tiheys[i+1]

    def usein(self, lkm):
        SELDOM = 10**7
        return(lkm % SELDOM > 0) #joka 10.000.000 on true

    def paivitaSeurantaparametrit(self):
        self.lkm=len(primes)
        self.aika=timer()
        self.suurinAlkuluku=max(primes)

    MILJOONA = 10**6
    def kirjoita(self, primes):
        alkulukujaYhteensa = len(primes)
        uusiaAlkulukuja = alkulukujaYhteensa-self.lkm
        etenema = max(primes)-self.suurinAlkuluku
        print("talletetaan", "{:11,d}".format(alkulukujaYhteensa), "alkulukua ", end="")
        # 2M alkuluvun jälkeen ei toimi enää näin vaan ilmoittaa MemmoryErrorista
        # print(sorted(primes), file=out)

        if uusiaAlkulukuja > 0:
            a = timer()
            if self.usein(alkulukujaYhteensa):
                with open(self.tiedosto, "a", encoding="utf-8") as out:
                    print(primes[-uusiaAlkulukuja:], file=out, flush=True)
            else:
                #primes.sort()  # ei tarvita einakaan yhdessä säikeessä
                with open(self.tiedosto, "w", encoding="utf-8") as out:
                    for i in range(len(primes)//MILJOONA):
                        print(primes[i*MILJOONA:(i+1)*MILJOONA],
                              file=out, flush=True)
                teeVarmuuskopio(self.tiedosto, alkulukujaYhteensa)
            
            print(self.kulunutAika(self.aika), uusiaAlkulukuja, "{:.3f}".format(etenema/uusiaAlkulukuja), "\ttalletus:",
                self.kulunutAika(a))  # lkm = len(primes)
        self.paivitaSeurantaparametrit()


    def kulunutAika(self, a):
        b=timer()
        s=(b-a) % 60
        m=int((b-a)//60)
        h=int(m//60)
        m=int(m % 60)
        if h == 0:
            return("{:0>2d}:{:0>5.2f}".format(m, s))
        return("{:0>2d}:{:0>2d}:{:0>5.2f}".format(h, m, s))

def teeVarmuuskopio(tiedosto, alkulukujaYhteensa):
    backup = tiedosto+"_" + str(alkulukujaYhteensa//MILJOONA)+"M_"+time.strftime("%H%M%S", time.localtime())+".txt"
    try:
        remove(backup)
    except FileNotFoundError:
        pass
    try:
        copyfile(tiedosto, backup)
    except Exception as e:
        print("Tiedoston varmuuskopiointi ei onnistu:", tiedosto, backup, e)


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
    if len(primes) == 0:
        ed = Seuranta(0, 1, TIEDOSTO)
        primes = [2, 3]
        ed.kirjoita(primes)
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
            if lkm % (ed.talletusvali//100) == 0:
                print("isoin:{:14,d}".format(luku), "lkm:{:11,d}".format(lkm), end="\r")  # tilannetiedotus
            if lkm % ed.talletusvali == 0:
                ed.kirjoita(primes) 
                ed.tarkistaTulostusTaajuus()

    ed.kirjoita(primes)



if __name__ == "__main__":
    primes=lueAiemmat(TIEDOSTO)

    #lkm=input("Montako haluat: (enter = laske 'kaikki')")
    #if lkm == None or lkm == "":
    lkm=10**11

    print(time.strftime("%H:%M:%S", time.localtime()))
 
    laskeAlkulukuja(primes, int(lkm))

    print(time.strftime("%H:%M:%S", time.localtime()))
