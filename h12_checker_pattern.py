r=int(input("r:"))
c=int(input("c:"))
h=int(input("h:"))
w=int(input("w:"))
musta=False;
black="#"
white=" "
for rivi in range(0,r):
  tulos=''
  for sarake in range(0, c): 
    for lev in range(0, w):
      if musta:
        tulos+=black
      else:
        tulos+=white
    musta = not musta
  for kork in range(0,h):
    print(tulos)
  if c%2==0:
    musta = not musta

              