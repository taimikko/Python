import sys

def andf(a, b):
    if a == b == 1:
        return 1
    return 0

def xorf(a, b):
    if a != b and (a == 1 or b == 1):
        return 1
    return 0

def orf(a, b):
    if a == 1 or b == 1:
        return 1
    return 0

def nandf(a, b):
    if not andf(a, b):
        return 1
    return 0

def coupling1(a,b,c,d,e):
    print(orf(orf(andf(a,b),c), xorf(d,e)))

def coupling2(a,b,c,d,e):
    x = xorf(c, d)
    print(orf(nandf(a, b), x), andf(x, e))

def main():
    try:
        a = int(sys.argv[2])
        b = int(sys.argv[3])
        c = int(sys.argv[4])
        d = int(sys.argv[5])
        e = int(sys.argv[6])
        coupling1(a,b,c,d,e) if int(sys.argv[1]) == 1 else coupling2(a,b,c,d,e)
    except:
        print("virhe parametreissa.", sys.argv)

if __name__ == "__main__":
    main()

# python .\rekrytesti1.5.py 1 1 0 0 1 0
# 1
# python .\rekrytesti1.5.py 2 0 0 1 1 1
# 1 0