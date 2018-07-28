command="Give a command: "
illegal="Illegal command!"
usd2eur=0
eur2usd=0
line = input(command).upper().split()
while line:
  # print(line, "pituus:",len(line))
  l = len(line)
  if len(line)==1:
      if line[0]=='QUIT':
        break
      else:
        print(illegal)
  elif len(line)==2:
      usd=0;
      eur=0;
      try:
        if line[1]=='USD':
          if usd2eur==0:
            print("No USD-EUR rate defined yet!")
          else:
            usd = float(line[0])
            eur = usd2eur*usd
            print('{:f}'.format(usd),"USD =",'{:f}'.format(eur),"EUR")
        elif line[1]=='EUR':
          if eur2usd==0:
            print("No EUR-USD rate defined yet!")
          else:
            eur = float(line[0])
            usd = eur2usd*eur
            print('{:f}'.format(eur),"EUR =",'{:f}'.format(usd),"USD")
      except:
        print(illegal)
  elif len(line)==3:
    try:
      if (line[0]=='EUR') and (line[2]=='USD'):
        eur2usd=float(line[1])
      elif (line[0]=='USD') and (line[2]=='EUR'):
        usd2eur=float(line[1])
      else:
        raise
    except:
      print(illegal)
  else:
      print(illegal)
  line = input(command).upper().split()

