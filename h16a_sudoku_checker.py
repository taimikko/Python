def haeRivit(lista):
  rivit=[]
  for line in lista:
    rivi = list(filter(isNumber, line)) # poistaa riviltä kaikki merkit, jotka eivät ole numeroita
    rivi = list(map(toNumber,rivi)) # '1' -> 1
    if len(rivi)>0:
       rivit.append(rivi)
  return(rivit)
  
def check(errStr, lista):
  ill=""
  for i in range(len(lista)):
    l = lista[i]
    for luku in range(1,10): # etsitään lukuja 1-9
      if luku not in l:
        if ill=="":
          ill = errStr
        ill += " "+str(1+i)
        break; # riittää että löytyi virheellinen rivi/sarake, ei tarvi enää tutkia
  return ill  
  
def checkGrid(errStr, lista):
  ill=""
  for i in range(len(lista)):
    grid = lista[i]
    for j in range(len(grid)):
      subGrid = grid[j]
      for luku in range(1,10): # etsitään lukuja 1-9
        if luku not in subGrid:
          if ill=="":
            ill = errStr
          ill += " ["+str(1+i)+", "+str(1+j)+"]"
          break; # riittää että löytyi virheellinen rivi/sarake, ei tarvi etää tutkia
  return ill  
  
def makeSubGrids(rivit):
  allGrids=[]
  for x in range(3):
    grids = []
    for y in range(3):
      subGrid = []
      for x1 in range(3):
        for y1 in range(3):
          rivi = rivit[3*x+x1]
          luku = rivi[3*y+y1]
          subGrid.append(luku)
      grids.append(subGrid)
    allGrids.append(grids)
  return(allGrids)

def checkSudoku(lista):
  rivit=haeRivit(lista)
  illRows = check("Illegal rows:", rivit)

  sarakkeet = [list(a) for a in zip(*rivit)]
  illCols = check("Illegal columns:", sarakkeet)
  
  subGrids = makeSubGrids(rivit)  
  illSubs = checkGrid("Illegal subgrids:", subGrids)
  #print("rivit:",rivit)
  #print("sarakkeet:",sarakkeet)
  #print("subGrids:",allGrids)

  if illRows:
    print(illRows)
  if len(illCols)>0:
    print(illCols)
  if (illSubs != ""):
    print(illSubs)
  if not (illRows+illCols+illSubs):
    print("The sudoku solution is legal")

def isNumber(n):
  try:
    int(n)
    return True
  except:
    return False

def toNumber(n):
  try:
    i=int(n)
    return i
  except:
    return 
