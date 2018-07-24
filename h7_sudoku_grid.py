line = input()
i=0
for r in range(0, 19):
  if r%6==0:
    print("#####################################")
  elif r%2==0:
    print("#---+---+---#---+---+---#---+---+---#")
  else:
    rivi = ''
    for s in range(0, 37):
      if s%12==0:
        rivi+='#'
      elif s%4==0:
        rivi+='|'
      elif s%2==1:
        rivi+=' '
      else:
        rivi+=line[i]
        i+=1
    print(rivi)
