n=int(input("n:")) #"n:"))
primes=[]

""" vanhatiedosto = "alkuluvut.txt"  # "alkuluvut1M.txt"
with open(vanhatiedosto, "r", encoding="utf-8") as infile:
    apu = infile.readline()
primes2test = list(map(int, apu[1:-3].split(", ")))  # set() / tuple()
 """
for i in range(2, n):
  prime= True
  raja = i/2
  for j in primes:
    if i%j==0:
      prime = False # not prime
      break
    if j > raja:
        break # prime =True
  if prime:
    primes.append(i)
#print(primes)
alku=len(primes) -100
if alku < 0:
    alku = 0
for i in range(alku, len(primes)):
  if i==0:
    print(primes[i], end="")
  else:
    print("",primes[i], end="")
  if i%10==0:
    print()
print()