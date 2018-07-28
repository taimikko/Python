a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
d=int(input("d:"))
def tulosta(c,d):
    if c<d:
      for sarake in range(c,d+1):
        print("(",rivi,", ",sarake,")",end="",sep="")
    else:
      for sarake in reversed(range(d,c+1)):
        print("(",rivi,", ",sarake,")",end="",sep="") 
    print()

if a<b:
  for rivi in range(a,b+1):
    tulosta(c,d)
else:   
  for rivi in reversed(range(b,a+1)):
    tulosta(c,d)
