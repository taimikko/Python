from timeit import default_timer as timer

def toka(primes, kpl):
    n = 10**10 # int(input("n:"))
    #n = 30379397+1000
    talletusvali = 500
    ed_lkm = lkm = len(primes)
    if lkm > 0:
        alku = max(primes)+2
    else:
        primes = [2 , 3]
        alku = 5
        lkm = ed_lkm = 2
    edAika = timer()
    ed_i = alku
    for i in range(alku, n, 2) :
        if lkm >= kpl:
            break
        prime = True
        stopper = i**0.5 # i/2
        for j in primes:
            if i % j == 0:
                prime = False  # not prime
                break
            if j > stopper:
                break # prime
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
    try:
        with open(vanhatiedosto, "r", encoding="utf-8") as infile:
            apu = infile.readline()
        primes = list(map(int, apu[1:-2].split(", ")))  # set() / tuple()        
    except:
        primes = [2, 3]
    print(primes[-10:])
    end = timer()
    print("luettu (", len(primes), ") kpl :", aika(start, end))
    lkm = input("Montako haluat:")
    print(time.strftime("%H:%M:%S", time.gmtime()))
    start = timer()
    toka(primes, int(lkm))
    end = timer()
    print("laskettu:", aika(start, end))
    print(time.strftime("%H:%M:%S", time.gmtime()))
