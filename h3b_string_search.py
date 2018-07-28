def stringSearch(s,t,c): #string, text, case
  result=[]
  row=0
  pos=0
  text = t.split("\n")
  for r in text:
      p=0
      r = []
      while True:
        try:
          pos = text.index(s,p)
          r.append(row,pos)
          result.append(r)
          p = pos + len(s)
        except ValueError:
          break
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