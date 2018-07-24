def stringSearch(s,t,c): #string, text, case
  if not c: # not case sensitive
    t = t.lower()
    s = s.lower()
  text = t.splitlines()
  #print(text)
  #print(s)
  #print(c)
  result=[]
  row=-1
  pos=0
  for rivi in text:
      p=0
      row+=1
      res = []
      while True:
        try:
          pos = rivi.index(s,p)
          res.append(row+1)
          res.append(pos+1)
          #print(res)
          result.append(res)
          res = []
          p = pos + len(s)
        except ValueError:
          break
  #print(result)
  return result
         

if __name__ == "__main__":
  mjono = "smith"
  texti = "Mr Smith is a blacksmith.\nThe Smithsonian Institution is in Washington D.C."
  print( stringSearch(mjono, texti, True) )
  print( stringSearch(mjono, texti, False))

  texti = "sometimes pain assists to this end for example a man on a mission\nis worried with business cares and has not slept well\nof late one evening he has a severe toothache which\ndemands his entire attention as the pain is relieved he\ndrops off into a quiet sleep and forgets his troubles on mississippi" 
  mjono = "issi"
  print( stringSearch(mjono, texti, True) )
  mjono = "he"
  print( stringSearch(mjono, texti, True) )