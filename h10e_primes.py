from timeit import default_timer as timer
from os import rename, remove
from shutil import copyfile
import time
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

#pool = ThreadPool()
#results = pool.map(my_function, my_array)


def toka(primes, kpl):
    n = 10**10  # int(input("n:"))
    talletusvali = 100000 
    ed_lkm = lkm = len(primes)
    if lkm > 0:
        alku = max(primes)+2
    else:
        primes = [2, 3]
        alku = 5
        lkm = ed_lkm = 2
        kirjoita(primes, "alkuluvut.txt", lkm, lkm, timer(), 2) 
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
                hh = timer() - edAika
                kirjoita(primes, "alkuluvut.txt", lkm,
                         lkm-ed_lkm, edAika, i-ed_i)  # välitalletus
                talletusvali = valiAika(hh, talletusvali)
                ed_lkm = lkm
                ed_i = i
                edAika = timer()
            elif lkm % (talletusvali//10) == 0:
                print(i, "lkm:", lkm, sep="\t", end="\r")  # tilannetiedotus

    kirjoita(primes, "alkuluvut.txt", lkm-ed_lkm, edAika, i-ed_i)


tiheys = [10000000, 5000000, 2000000, 1000000, 500000, 250000, 100000,
          50000, 25000, 10000, 5000, 2500, 1000, 500, 250, 100, 50, 25, 10, 5, 2]


def valiAika(kulunut, vanha):
    uusi = vanha
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


def kirjoita(primes, tiedosto, lkm, ero=0, edAika=0, i=0):  # "alkuluvut.txt"
    print("talletetaan", lkm, "alkulukua ", end="")  # ,":",primes[-10:])
    # 2M alkuluvun jälkeen ei toimi enää näin vaan ilmoittaa MemmoryErrorista
    # print(sorted(primes), file=out)  # tulostus kestää 1/10 s

    a = timer()
    SELDOM = 10**7 
    if lkm % SELDOM == 0:
        # primes.sort() # mahdetaanko tarvita
        with open(tiedosto, "w", encoding="utf-8") as out:  # kestää 30 sek
            for i in range(len(primes)//SELDOM):
                print(primes[i*SELDOM:(i+1)*SELDOM], file=out, flush=True)
    else:
        with open(tiedosto, "a", encoding="utf-8") as out:
            print(primes[-ero:], file=out,
                  flush=True)  # tulostus kestää 1/10 s
    print(aika(edAika, timer()), ero, i/ero, "\ttalletus:",
          aika(a, timer()))  # lkm = len(primes)

    backup = tiedosto[:-4]+"_" + \
        str(lkm)+"_"+time.strftime("%H%M%S", time.gmtime())+".txt"
    try:
        remove(backup)
    except FileNotFoundError:
        pass
    try:
        copyfile(tiedosto, backup)
        #rename(tiedosto, backup)
    except Exception as e:
        print("Tiedoston varmuuskopiointi ei onnistu:", tiedosto, backup, e)


def aika(a, b):
    s = (b-a) % 60
    m = int((b-a)//60)
    h = int(m//60)
    m = int(m % 60)
    return("{:0>2d}:{:0>2d}:{:0>5.2f}".format(h, m, s))


if __name__ == "__main__":
    vanhatiedosto = "alkuluvut.txt"  # "alkuluvut1M.txt"
    start = timer()
    print("Luetaan aiempia lukuja tiedostosta", vanhatiedosto, end="")
    try:
        primes = []
        with open(vanhatiedosto, "r", encoding="utf-8") as infile:
            for row in infile:
                apu = list(map(int, row[1:-2].split(", ")))
                primes.extend(apu)
    except Exception as e:
        print(" Virhe tiedoston", vanhatiedosto, "lukemisessa ", e.args)
        primes = []
    primes.sort()
    print(" ", primes[-3:], end="")
    end = timer()
    print("\tluettu (", len(primes), ") kpl :", aika(start, end))
    lkm = input("Montako haluat:")
    print(time.strftime("%H:%M:%S", time.gmtime()))
    start = timer()
    toka(primes, int(lkm))
    end = timer()
    print("laskettu:", aika(start, end))
    print(time.strftime("%H:%M:%S", time.gmtime()))
