from itertools import zip_longest
# import itertools #zip_longest()
def yhdista(l1, l2, l3):
    # enumerate() jos haluaa käydä joukon läpi niin että tietää sekä indeksin että alkion
    # for idx, arvo in enumerate(mjt):
        # print("indeksi:", idx, "arvo:", arvo)
    # enumerate tuottaa tupleja (pareja, joissa ekana on indeksi ja tokana arvo)
    # (0, "yksi")
    # (1, "kaksi") jne.
    # i,j,k = (1,2,3) # laillinen sijoitus: i=1; j=2; k=3
    # zip() viittaa vetoketjuun (zipper) liitetään vuoron perään
    #yhd = list(zip(l1, l2, l3)) # yhdistää listat listaksi tupleja
    yhd = list(zip_longest(l1, l2, l3))
    uusi = []
    for item in yhd:
        l_item = list(item)
        uusi.append(l_item)
    print("yhdiste:",yhd)
    print("uusi:   ",uusi)
    kolmas = tuple(map(lambda a: list(a), yhd))
    print("kolmas: ",kolmas)
    a,b,c = zip(*yhd)
    print(list(a))
    print(b)
    print(c)
    x = list(zip(*[iter(yhd)]*4))
    print("x:",x)
    # x = tuple(zip(*[yhd]*4))
    # print(x)
    # print([iter(a)]*3)
    # print(list(iter(a)))


def main():
    maat=[]
    with open("countries.txt") as infile:
        for rivi in infile:
            data = rivi.split("\t")
            maa=data[0]
            maat.append(maa)
    maat.sort(key=laji)
    print("\n".join(maat))

    it = [1,2,3,4,7,6,5]
    mt = ["yksi", "kaksi", "kolme", "nelkku", "viisi"]
    ft = [1.5, 3.4, 2.2, 6.1, 1.1, 0.4]

    yhdista(it, ft, mt)

def laji(maa):
    return(-len(maa), maa)

if __name__=="__main__":
    main()
