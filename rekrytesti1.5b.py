import sys
from coupling import Coupling1, Coupling2

def check(s):
    try:
        i = int(s)
        if 0 <= i <= 1:
            return i
        else:
            raise  ValueError('Luvun ('+s+') pitää olla 0 tai 1')
    except:
        raise #ValueError('Vain 0 ja 1 käyvät parametriksi:'+s)

def main():
    try:
        if len(sys.argv) != 7:
            raise Exception("Parametreja on väärä määrä.")
        a = check(sys.argv[2])
        b = check(sys.argv[3])
        c = check(sys.argv[4])
        d = check(sys.argv[5])
        e = check(sys.argv[6])
        if int(sys.argv[1]) == 1:
            co = Coupling1()
        else:
            co = Coupling2()
        co.coupling(a, b, c, d, e)
    except Exception as e:
        print("virhe parametreissa.", e.args)


if __name__ == "__main__":
    main()

# python .\rekrytesti1.5b.py 1 1 0 0 1 0
# 1
# python .\rekrytesti1.5b.py 2 0 0 1 1 1
# 1 0
