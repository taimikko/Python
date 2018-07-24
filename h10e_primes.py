from timeit import default_timer as timer

def toka(n, primes):
    talletusvali = 100
    tulostusvali = 1000
    lkm = len(primes)
    ed_lkm = lkm
    if len(primes) > 0:
        alku = max(primes)
    else:
        alku = 2
    a = timer()
    edAika = a
    ed_i = alku
    for i in range(alku, n):
        prime = True
        if i % tulostusvali == 0:
            b = timer()
            tulostusvali = talletusvali // 5 # valiAika(b-a, tulostusvali) 
            print(i, "lkm:", lkm, sep="\t", end="\r")  # aika(a, b),
            a = timer()
        # jos primes olisi järjestyksessä, niin ei tarvitsisi käydä läpi kaikkia primes -lukuja
        # vaan voisi lopettaa "puolivälissä"
        for j in primes:
            if i % j == 0:
                prime = False  # not prime
                break
            if j > i/2:
                break # potential prime
        if prime:
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
    kirjoita(primes, "alkuluvut.txt", lkm-ed_lkm, edAika, i-ed_i)

tiheys = [1000000,500000,250000,100000,50000,25000,10000,5000,2500,1000,500,250,100,50,25,10,5,2]

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
    if i<len(tiheys):
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
    # str(h)+":"+str(m)+":"+str(s))


import time

if __name__ == "__main__":
    start = timer()
    vanhatiedosto = "alkuluvut.txt"  # "alkuluvut1M.txt"
    with open(vanhatiedosto, "r", encoding="utf-8") as infile:
        apu = infile.readline()
    primes = list(map(int, apu[1:-3].split(", ")))  # set() / tuple()
    end = timer()
    print("luettu (", len(primes), ") kpl :", aika(start, end))
    print(time.strftime("%H:%M:%S", time.gmtime()))
    n = 10**9 # int(input("n:"))
    start = timer()
    toka(n, primes)
    # i=0
    # while True:
    #     print(str(toka(n)))
    end = timer()
    print("laskettu:", aika(start, end))
    print(time.strftime("%H:%M:%S", time.gmtime()))
