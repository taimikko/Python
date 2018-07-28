from timeit import default_timer as timer

def esilaskenta(n, primes_tuple):
    potential_primes = set()
    lkm = len(primes_tuple)
    if lkm > 0:
        alku = max(primes_tuple)+1
    else:
        alku = 2
    print(alku, primes_tuple)
    a = timer()
    for i in range(alku, n):
        prime = True
        if i%100000==0:
            b = timer()
            print(i, aika(a,b), "lkm:", lkm, sep="\t")
            a = timer()
        # jos primes olisi järjestyksessä, niin ei tarvitsisi käydä läpi kaikkia primes -lukuja
        # vaan voisi lopettaa "puolivälissä"
        for j in primes_tuple:
            if i % j == 0:
                prime = False  # not prime
                break
            if j > i/2:
                break # potential prime
        if prime:
            lkm += 1
            potential_primes.add(i) # .append(i) # .add(i)
            if lkm%10000==0:
                # olisi nopeampi vain lisätä tiedostoon, mutta {} ei ole järjestyksessä
                # jatkokäsittele primes (tarkastettava eteenpäin luku/2:sta eteenpäin
                # jos on alkuluku niin siirrä primes_tupleen ja tyhjennä primes
                kirjoita(potential_primes, "alkuluvut_potential.txt", lkm) # välitalletus
            #yield(i)
    kirjoita(potential_primes, "alkuluvut_potential.txt", lkm)


def toka(n, primes):
    tiedosto = "alkuluvut_ko.txt"
    lkm = len(primes)
    if len(primes) > 0:
        alku = max(primes)+1
    else:
        alku = 2
    a = timer()
    for i in range(alku, n):
        prime = True
        if i%100000==0:
            b = timer()
            print(i, aika(a,b), "lkm:", lkm, sep="\t")
            a = timer()
        # jos priomes olisi järjestyksessä, niin ei tarvitsisi käydä läpi kaikkia primes -lukuja
        # vaan voisi lopettaa "puolivälissä"
        for j in primes:
            if i % j == 0:
                prime = False  # not prime
                break
        if prime:
            lkm += 1
            primes.add(i) # .append(i) # .add(i)
            if lkm%10000==0:
                # olisi nopeampi vain lisätä tiedostoon, mutta {} ei ole järjestyksessä
                kirjoita(primes, tiedosto, lkm) # välitalletus
            #yield(i)
    kirjoita(primes, tiedosto, lkm)

def kirjoita(primes, tiedosto, lkm): # "alkuluvut.txt"
    a=timer()
    print("talletetaan",lkm,"alkulukua ", end="") # ,":",primes[-10:])
    with open(tiedosto, "w", encoding="utf-8") as out:
        print(sorted(primes), file=out) # jos primes ei ole set() niin ei tarvi sortata
    b=timer()
    print("- talletettu", aika(a,b)) # lkm = len(primes)

def lue(vanhatiedosto, tyyppi): # tuple / set
    start = timer()
    with open(vanhatiedosto, "r", encoding="utf-8") as infile:
        apu = infile.readline()
    primes = tyyppi(map(int,apu[1:-3].split(", "))) # set() / tuple()
    end = timer()
    print("luettu (",len(primes),") kpl :", aika(start, end))
    return primes
    
def aika(a,b):
    s = (b-a)%60
    m = int((b-a)//60)
    h = int(m//60)
    m = int(m%60)
    return("{:0>2d}:{:0>2d}:{:0>8.5f}".format(h,m,s))
        #str(h)+":"+str(m)+":"+str(s))

import time

if __name__ == "__main__":
    primes = lue("alkuluvut200.txt", tuple)
    print(primes)
    n = int(input("n:"))
    start = timer()
    esilaskenta(n, sorted(primes))
    # i=0
    # while True:
    #     print(str(toka(n)))
    end = timer()
    print("laskettu:", aika(start, end))
