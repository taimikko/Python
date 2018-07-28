from timeit import default_timer as timer


def eka():
    return
    primes = []
    for i in range(2, n):
        prime = True
        for j in primes:
            if i % j == 0:
                prime = False  # not prime
                break
        if prime:
            primes.append(i)
    # print(primes)
    """
    for i in range(0, len(primes), k):
        if i==0:
        print(primes[i], end="")
        else:
        print("",primes[i], end="")
    print()
    """


def toka(n):
    # len(str(n))-1
    raja = 99*n//100
    primes = [] # set()
    for i in range(2, n):
        prime = True
        for j in primes:
            if i % j == 0:
                prime = False  # not prime
                break
        if prime:
            primes.append(i) # .add(i)
            #yield(i)
    print("yhteensa:",len(primes),":",primes[-10:])
    with open("alkuluvut.txt", "w", encoding="utf-8") as out:
        print(primes, file=out)
    print("valmis")



if __name__ == "__main__":
    n = int(input("n:"))
    #k = int(input("k:"))
    # start = timer()
    # eka()
    # end = timer()
    # print("eka:", end - start)
    start = timer()
    toka(n)
    # i=0
    # while True:
    #     print(str(toka(n)))
    end = timer()
    print("toka:", end - start)
