from timeit import default_timer as timer
import time
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
 
def onkoAlkuluku(luku):
    stopper = luku**0.5  # i/2
    # if (luku//1000)%10==0:
    #     print("\t",luku,end="\r")
    for alkuluku in primes:
        if luku % alkuluku == 0:
            break # not prime
        if alkuluku > stopper:
            return luku # prime
    else:
        return luku # prime

def tarkasta1000(luku):
    tulos = []
    #for i in range(0, 1000, 2):
    for i in range(0, 1000):
        a = luku +i
        if onkoAlkuluku(a) != None:
            tulos.append(a)
            if ((a)//1000)%10==0:
                print("\t",a,end="\r")
    return tulos

def lueAiemmat(vanhatiedosto):
    print("Luetaan tiedostoa", vanhatiedosto)
    try:
        primes = []
        with open(vanhatiedosto, "r", encoding="utf-8") as infile:
            for row in infile:
                apu = list(map(int, row[1:-2].split(", ")))
                primes.extend(apu)
    except IOError as e:
        print(" Virhe tiedoston", vanhatiedosto,
              "lukemisessa ", e.args, e.strerror)
        primes = []
    except MemoryError as e:
        print(" Muistivirhe tiedoston", vanhatiedosto, "lukemisessa ", e.args)
        exit
    primes.sort()
    print(" ", primes[-3:], end="")
    print("\tluettu (", len(primes), ") kpl")
    return primes


if __name__ == "__main__":
    primes = lueAiemmat("alku60M.txt")
    iso = max(primes)+2  # 1147700429 # iso alkuluku
    lkm_vanha = lkm = len(primes)
    print(lkm_vanha)
    klontti = 1000
    monta = (10*10**6)//klontti
    
    luvut = [x*klontti+iso for x in range(monta)]
    print(len(luvut))
    #print(luvut)
    #a=input("keskeytetäänkö")
    pool = ThreadPool(4)
    print(time.strftime("%H:%M:%S", time.localtime()))
    
    # results = list(filter(lambda x: x != None, pool.map(onkoAlkuluku, luvut)))
    results =  pool.map(tarkasta1000, luvut)
    pool.close()
    pool.join()

    SELDOM = 10**6
    primes.sort()
    with open("alku60M1.txt", "w", encoding="utf-8") as out:
        for i in range(len(primes)//SELDOM):
            print(primes[i*SELDOM:(i+1)*SELDOM],
                  file=out, flush=True)
    print("uusia alkulukuja", len(primes) - lkm_vanha, len(primes), lkm_vanha)
    print(time.strftime("%H:%M:%S", time.localtime()))

    flat_result = [item for sublist in results for item in sublist]

    print(flat_result[-3:])
    with open("alku60M1.txt", "a", encoding="utf-8") as out:
        print("[uudet]", file=out, flush=True)
        print(flat_result, file=out, flush=True)
    print("uusia alkulukuja", len(flat_result))
