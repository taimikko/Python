a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
d=int(input("d:"))
pit = len(str(b*d))+1
formatstr='{:'+str(pit)+'}'
tulos=formatstr.format(" ")
for sarake in range(a,b+1):
  tulos+=formatstr.format(sarake)
print(tulos)
for rivi in range (c,d+1):
  tulos=formatstr.format(rivi)
  for sarake in range(a,b+1):
    tulos+=formatstr.format(rivi*sarake)
  print(tulos)    
