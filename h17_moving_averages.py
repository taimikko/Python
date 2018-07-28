import sys

def movingAverages(data, m):
  n = len(data)
  #print(data, " pituus:",n)
  tulos = []
  m = int(m)
  for i in range(n):
    x = 0
    y = int(i - (m-1)/2)
    a = x if x > y else y  #max(0, i − (m-1)/2 )
    x= n-1
    y = int(i + (m - 1)/2)
    b = x if x < y else y # min((n−1),(i+(m-1)/2))
    lista = data[a:b+1]
    t = sum(lista)/len(lista)
    tulos.append(t)
    # print("[a:b] ",a,":",b,"average:",round(t,3),"lista:", lista,"sum", sum(lista), len(lista))
  return tulos

  # [1.5, 2.2, 9.7, 4.6, 2.6, 5.7, 9.2, 5.1] and the window size m = 3. 
if __name__ == "__main__":
  #filename = sys.argv[1] #averages1.txt
  #mSize = sys.argv[2]
  #with open(filename) as f:
  #  luettu = f.readlines()
  #f.closed
  luettu = []
  luettu.append(1.5)
  luettu.append(2.2)
  luettu.append(9.7)
  luettu.append(4.6)
  luettu.append(2.6)
  luettu.append(5.7)
  luettu.append(9.2)
  luettu.append(5.1)
  mSize = 3
  print("Original values:",luettu)
  #luettu = luettu.split(", ")
  tulos = movingAverages(luettu, mSize)
  
  print("Moving averages (m = ",mSize,"): ", tulos, sep="")
  #Original values: 1.5 2.2 9.7 4.6 2.6 5.7 9.2 5.1
  #Moving averages (m = 3): 1.85 4.467 5.5 5.633 4.3 5.833 6.667 7.15
