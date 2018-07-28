# Guessing types
line = input()
while line:
    sanat = line.split()
    tulos = ""
    for sana in sanat:
        tyyppi = "=str"
        try:
            f = float(sana)
            tyyppi = "=float"
            i = int(sana)
            tyyppi = "=int"
        except:
            pass
        if tulos >"":
            tulos+=" "
        tulos+=sana+tyyppi
    print(tulos)
    line = input()
