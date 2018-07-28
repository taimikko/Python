line=input("h:")
while line:
  h=int(line)           # 5
  puolivali = ((h-1)/2) # 2
  s=input("s:")
  for kork in range(0,h): # 0..4
    di=''
    if kork <= puolivali:
      pos=kork            # 0, 1, 2
    else:
      pos = h-kork-1      # 1, 0

    for lev in range(0,h):
        if (lev==puolivali-pos) or (lev==puolivali+pos):
          di+=s
        else:
          di+=" "
 
    for lkm in range(0, n):
      print(di," ",end="", sep="")
    print()
  line=input("h:")