def tulosta(rivi):
  for i in rivi:
    print(" ",i,sep="",end="")
    
apu = input().split()
oikearivi=apu[:7]
loput=apu[7:]
print("Correct numbers:",end="")
tulosta(oikearivi)
print()

rivi=loput[:7]
while rivi:
  loput=loput[7:]
  print("Ticket:",end="")
  tulosta(rivi)
  oikein=0
  osumat=""
  for luku in rivi:
    if luku in oikearivi:
      oikein +=1;
      if oikein == 1:
        osumat=": "+luku
      else:
        osumat+=" "+luku
  if oikein > 0:
    print(" (",oikein," correct",osumat,")",sep="")
  else:
    print(" (",oikein," correct)",sep="")  
  rivi=loput[:7]
  
# 1 2 3 4 5 6 7 2 4 6 8 12 23 24 1 4 8 13 21 32 33 11 12 13 14 15 16 17
#2 30 17 8 6 19 24 7 6 1 2 3 5 4 19 3 27 13 14 17 25 5 27 6 19 7 21 14 5 10 15 20 25 28 29
