s=float(input())
i=float(input())
n=int(input())
p=int(input())
for year in range(0, n+1):
  #k = format(s,"#."+str(p)+"f")
  k=round(s,p)
  print("Year "+str(year)+":", k)
  s+=((i/100)*s)