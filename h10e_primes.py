from timeit import default_timer as timer

def toka(n, primes):
    talletusvali = 500
    tulostusvali = 500
    lkm = len(primes)
    ed_lkm = lkm
    if len(primes) > 0:
        alku = max(primes)+2
    else:
        primes = [2 , 3]
        alku = 5
    edAika = timer()
    ed_i = alku
    n = 30379397+1000
    for i in range(alku, n, 2) :
        prime = True
        #if i % tulostusvali == 0: # parittomat luvut ei napsahda
        #    tulostusvali = talletusvali // 2
        #    print(i, "lkm:", lkm, sep="\t", end="\r")  # aika(a, b),
        # jos primes olisi järjestyksessä, niin ei tarvitsisi käydä läpi kaikkia primes -lukuja
        # vaan voisi lopettaa "puolivälissä" -> x pow 2:ssa ?
        stopper = i**0.5
        #stopperPrime = False
        for j in primes:
            if i % j == 0:
                prime = False  # not prime
                break
            if j > stopper:
            #    stopperPrime = True
                break
            #if j > i/2:
            #    break # potential prime
        if prime:
            #if not stopperPrime:
            #    print("\t\t\t\t", "Prime <> StopperPrime", i)  
            lkm += 1
            primes.append(i)  # .append(i) # .add(i)
            if lkm % talletusvali == 0:
                # olisi nopeampi vain lisätä tiedostoon, mutta {} ei ole järjestyksessä
                hh = timer() - edAika
                kirjoita(primes, "alkuluvut.txt", lkm,
                         lkm-ed_lkm, edAika, i-ed_i)  # välitalletus
                talletusvali = valiAika(hh, talletusvali)
                ed_lkm = lkm
                ed_i = i
                edAika = timer()
        #if stopperPrime and not prime:
        #    print("\t\t\t\t", "StopperPrime <> Prime ", i)  
    kirjoita(primes, "alkuluvut.txt", lkm-ed_lkm, edAika, i-ed_i)

tiheys = [10000000, 5000000, 2000000, 1000000,500000,250000,100000,50000,25000,10000,5000,2500,1000,500,250,100,50,25,10,5,2]

def valiAika(kulunut, vanha):
    uusi = vanha
    if kulunut > 300: # 5min = 300 s
        uusi = pienenna(vanha)
    elif kulunut < 120: # 2 min = 120 s 
        uusi = suurenna(vanha)
    return(uusi)

def pienenna(luku):
    tiheys.sort()
    i = tiheys.index(luku)
    if i>0:
        return(tiheys[i-1])
    return(luku)

def suurenna(luku):
    tiheys.sort()
    i = tiheys.index(luku)
    if i<len(tiheys)-1:
        return(tiheys[i+1])
    return(luku)


def kirjoita(primes, tiedosto, lkm, ero=0, edAika=0, i=0):  # "alkuluvut.txt"
    print("talletetaan", lkm, "alkulukua ", end="")  # ,":",primes[-10:])
    with open(tiedosto, "w", encoding="utf-8") as out:
        # jos primes ei ole set() niin ei tarvi sortata
        print(sorted(primes), file=out)  # tulostus kestää 1/10 s
    print(aika(edAika,timer()), ero, i/ero)  # lkm = len(primes)


def aika(a, b):
    s = (b-a) % 60
    m = int((b-a)//60)
    h = int(m//60)
    m = int(m % 60)
    return("{:0>2d}:{:0>2d}:{:0>5.2f}".format(h, m, s))
 

import time

if __name__ == "__main__":
    start = timer()
    vanhatiedosto = "alkuluvut.txt"  # "alkuluvut1M.txt"
    with open(vanhatiedosto, "r", encoding="utf-8") as infile:
        apu = infile.readline()
    primes = list(map(int, apu[1:-2].split(", ")))  # set() / tuple()
    print(primes[-10:])
    end = timer()
    print("luettu (", len(primes), ") kpl :", aika(start, end))
    print(time.strftime("%H:%M:%S", time.gmtime()))
    n = 10**9 # int(input("n:"))
    start = timer()
    toka(n, primes)
    end = timer()
    print("laskettu:", aika(start, end))
    print(time.strftime("%H:%M:%S", time.gmtime()))
