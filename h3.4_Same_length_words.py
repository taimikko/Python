"""
Same length words

Write a Python function listLenWords that:

Receives two parameters: a filename and a word length. 
The length will always be an integer.
Opens the file specified by the filename and 
return a list of all words in the file whose length equals 
the received word length parameter. 
The words should be returned in the same order as they appear in the file.
WETO's test code prints out the words returned by your function, 
inserting a line break after every 10 words.
"""
import sys

def listLenWords(filename, wordLength):
    tulos = []
    with open(filename, encoding="utf-8") as infile:
        for rivi in infile:
            for sana in rivi.split():
                if len(sana) == wordLength:
                    tulos.append(sana)
    #return " ".join(tulos)
    return tulos

if __name__=="__main__":
    s = listLenWords(sys.argv[1], int(sys.argv[2]))
    print(s)