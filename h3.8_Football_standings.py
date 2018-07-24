"""
Football standings

Write a Python program that:

Receives a filename as a command line parameter.
The file is assumed to contain information about wins, ties, losses and goals 
scored/allowed for football teams within the same group.
Each row has the form "team\twins\tties\tlosses\tscored-allowed". 
Note how the fields are separated by tabulator characters "\t". 
E.g. the line "Germany\t1\t0\t2\t5-4" would specify that 
Germany has won 1, tied 0 and lost 2 matches, having scored 5 goals and allowed 4 goals.
Based on the read information, prints out a standings table for the teams.

Each row of the standings table gives the team name, 
number of matches played, wins, ties, losses, goals scored, 
goals allowed and the points total.

The table is sorted according to the following (slightly artificial) rules:
Primary rule: points total. Higher points come first.
Secondary rule: goal difference (scored minus allowed). 
Higher difference comes first.
Tertiary rule: number of goals scored. Higher number comes first.
Last rule: ascending alphabetical order of team names (this rule is artificial).

Calculate the points total as follows: each win gives 3 points, each tie gives 1 point and each loss gives 0 points.
The printed standings table is formatted as follows:

The team name is padded with trailing spaces, if necessary, 
so that the number of characters is equal to the longest team name in the group.
The numbers of matches, wins, ties and losses are printed using 
3 characters of width (padded with leading spaces).
The numbers of scored and allowed goals are printed in the form 
"scored-allowed" using 6 characters of width (padded with leading spaces).
The points total is printed using 3 characters of width (padded with leading spaces).
"""

import sys

class Team(object):
    __team = ""
    __wins = 0
    __ties = 0
    __losses = 0
    __scored = 0
    __allowed = 0
    __points = 0
    __numberOfMatches = 0
    __goalDifference = 0

    def __init__(self, team, wins, ties, losses, scored, allowed):
        self.__team = team
        self.__wins = wins
        self.__ties = ties
        self.__losses = losses
        self.__scored = scored
        self.__allowed = allowed
        self.__points = 3*self.__wins + self.__ties
        self.__numberOfMatches = self.__wins + self.__ties + self.__losses
        self.__goalDifference = self.__scored - self.__allowed

    def sortOrder(self):
        return (-self.__points, -self.__goalDifference, -self.__scored, self.__team)

    def __str__(self):
        return(self.__team+"\t"+str(self.__numberOfMatches)+"\t"+str(self.__wins)+"\t" +
               str(self.__ties)+"\t"+str(self.__losses)+"\t"+str(self.__scored)+"-" +
               str(self.__allowed)+"\t"+str(self.__points))

    def nimenPituus(self):
        return(len(self.__team))

    def getTeam(self, pituus):
        muoto = "{:<"+str(pituus)+"}"
        rivi = muoto.format(self.__team)
        rivi += "{0:>3}{1:>3}{2:>3}{3:>3}".format(
            self.__numberOfMatches, self.__wins, self.__ties, self.__losses)
        #rivi += muoto.format(self.__wins)
        #rivi += muoto.format(self.__ties)
        #rivi += muoto.format(self.__losses)

        rivi += "{0:>6}{1:>3}".format(str(self.__scored) +
                                      "-"+str(self.__allowed), str(self.__points))
        #rivi += muoto.format(str(self.__points))
        return rivi


def main(filename):
    liiga = []
    with open(filename, encoding='utf-8') as infile:
        for rivi in infile:
            r = rivi.split("\t")
            team = r[0]
            wins = int(r[1])
            ties = int(r[2])
            losses = int(r[3])
            scored = int(r[4].split("-")[0])
            allowed = int(r[4].split("-")[1])
            joukkue = Team(team, wins, ties, losses, scored, allowed)
            liiga.append(joukkue)
    liiga.sort(key=Team.sortOrder)
    maxPituus = max(map(Team.nimenPituus, liiga))
    for joukkue in liiga:
        print(joukkue.getTeam(maxPituus))


if __name__ == "__main__":
    main(sys.argv[1])
