line = input()
rivit = ''
while line:
  rivit+=line+'\n'
  line = input()
sanat=list(rivit.split())

maxlen=0
minlen=99
for s in sanat:
  if len(s) > maxlen:
    maxlen=len(s)
  if len(s) < minlen:
    minlen=len(s)
print(sanat)
sanat2=[x for x in sanat if len(x) >= maxlen]
maxlenw = sanat2[0]
sanat2=[x for x in sanat if len(x) == minlen]
minlenw = sanat2[0]

sanat.sort()
minw=sanat[0]
maxw=sanat[-1]

print("Min length: ",minlen," (",minlenw,"), Max length: ",maxlen," (",maxlenw,"), Smallest: ",minw,", Largest: ",maxw,sep='')
#print(sanat)
#print(sanat2)
""" def getKey(item):
   return len(item)
sanat.sort(key=getKey)
minlenw=sanat[0]
minlen=len(minlenw)
maxlenw=sanat[len(sanat)-1]
maxlen=len(maxlenw)
 """

# x= list.pop(0) = list.popleft()  listan eka pois ja palutuu mjaan x

# [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]