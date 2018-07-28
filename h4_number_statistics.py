line = input()
luvut = []
while line:
  luku=float(line)
  luvut.append(luku)
  # You should do something with the input in this part.
  # The below line tries to read the next input line: it should
  # remain as the last line of the while-loop.
  line = input()
# Here the input has ended. Now it is time to compute and print results.
lkm = len(luvut)
minimi = min(luvut)
maksimi = max(luvut)
summa = sum(luvut)
ka= summa/lkm
print("Minimum ",minimi,", maximum ", maksimi,", sum ", summa, " and mean ",ka,sep='')
