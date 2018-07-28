from timeit import default_timer as timer

n=int(input("n:"))
k=int(input("k:"))
primes=[]

def main():
  for i in range(2, n):
    prime= True
    for j in primes:
      if i%j==0:
        prime = False # not prime
        break
    if prime:
      primes.append(i)
  #print(primes)
  for i in range(0, len(primes), k):
    if i==0:
      print(primes[i], end="")
    else:
      print("",primes[i], end="")
  print()

start = timer()
main()
end = timer()
print("aika:", end - start)

