import sys
import random

with open(sys.argv[1], encoding="utf-8") as infile:
    sanat = infile.read() #.split(",") # luetaan koko tiedosto kerralla
    
with open(sys.argv[1], encoding="utf-8") as infile:
    # sanat = infile.read() #.split(",")
    sanat = infile.readlines() # kukin rivi omana taulukon alkiona

with open(sys.argv[1], encoding="utf-8") as infile:
    for rivi in infile:
        print(rivi)

with open(sys.argv[1], encoding="utf-8") as infile:
    for rivi in infile:
        for sana in rivi.split():
            print(sana)
