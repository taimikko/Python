from timeit import default_timer as timer
import time
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

lkm = 1


def onkoAlkuluku(luku):
    prime = True
    stopper = luku**0.5  # i/2
    for alkuluku in primes:
        if luku % alkuluku == 0:
            prime = False  # not prime
            break
        if alkuluku > stopper:
            break  # prime
    if prime:
        #lkm += 1
        primes.append(luku)
        # if lkm%10000 == 0:
        # , "lkm:", "{:11,d}".format(lkm), end="\r")
        print("\t", luku, end="\r")
        # return luku


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
    iso = max(primes)  # 1147700429 # iso alkuluku
    lkm = len(primes)
    monta = 5*10**6
    luvut = [x*2+iso for x in range(monta)]
    pool = ThreadPool(4)
    print(time.strftime("%H:%M:%S", time.localtime()))

    lkm_vanha = lkm
    results = pool.map(onkoAlkuluku, luvut)
    pool.close()
    pool.join()

    SELDOM = 10**6
    primes.sort()
    with open("alku60M1.txt", "w", encoding="utf-8") as out:
        for i in range(len(primes)//SELDOM):
            print(primes[i*SELDOM:(i+1)*SELDOM],
                  file=out, flush=True)
    print("uusia alkulukuja", len(primes) - lkm_vanha)
    print(time.strftime("%H:%M:%S", time.localtime()))
