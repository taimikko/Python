# h5.1_Jaccard_similarity.py

import sys


def read(infile):
    with open(infile, "r", encoding="UTF-8") as f:
        data = f.read()
    return data.split()


def itemize(words, k):
    items = set()
    #print("words", len(words))
    for i in range(len(words)):
        t = tuple(words[i-k+1: i+1])
        if t :
            items.add(t)
    #print("items", len(items))
    return items


def jaccardSimilarity(k, file1, file2):
    k = int(k)
    a = itemize(read(file1), k)
    b = itemize(read(file2), k)
    #print(len(a),":",a)
    #print(len(b),":",b)

    intersection = 0
    for i in a:
        if i in b:
            intersection += 1
    union = len(a) + len(b) - intersection
    jac = intersection/union
    print ("intersection", intersection)
    print ("union",union)
    return round(jac, 4)


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        j = jaccardSimilarity(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        j = jaccardSimilarity(1, "j1.txt", "j2.txt")
    print("JAC("+sys.argv[1]+"):", round(j, 4))
