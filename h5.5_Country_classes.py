"""
 Country classes

Write Python code where you define two classes Country and Countries that have the following properties:

    Class Country
        Stores the name, population and area of a country. Name is a string, 
        population is an integer and area is a floating point number.
        Has an initializing function that allows to create a new Country-object in the form 
            Country(name, population, area). E.g. country = Country("Finland", 5259250, 130558) 
            would make a Country-object country that represents Finland.
            The data used in this question expresses area as square miles (1 square mile ≈ 2.59 km2). 
            This detail has no significance in terms of how you should implement your answer; 
            keep the original area numbers as such.
        Stores the name, population and area in attributes name, population and area.
            E.g. if country represents Finland as in the example above, then country.name is "Finland", country.population is 5259250 and country.area is 130558.0.
    Class Countries
        Stores information about countries.
        Has an initializing function that takes a counry data filename as a parameter 
        and reads and stores information about the countries described in the country data file.
            The country data file contains rows of form "countryName\tpopulation\tarea\n", 
            where \t is a tabulator character and \n is a newline.
            E.g. countries = Countries("countries.txt") would create a Countries-object countries 
            that stores information about all countries described in the file countries.txt.
        Has a member function size that returns the number of countries the corresponding 
        Countries-object has information about.
            E.g. if countries was a Countries-object created as above, then countries.size() 
            would return the number of countries that the input file countries.txt described 
            (and countries then stored in itself).
        Has a member function listByArea that returns a list of Country-objects 
        that describes all countries that the corresponding Countries-object has information about. 
        The list is sorted according to the countries' area, in descending order: 
        first is the largest country, then the next-largest, and so on.
            This function is called in the form countries.listByArea().
"""


class Country:
    def __init__(self, name, population, area):
        try:
            self.name = str(name)
            self.population = int(population)
            self.area = float(area)
        except:
            pass

    def __str__(self):
        return (self.name + "\t" + str(self.population) + "\t" + str(self.area))


class Countries:
    def __init__(self, filename):
        self.countries = {}
        with open(filename, encoding="UTF-8") as infile:
            for row in infile:
                data = row[:-1].split("\t")
                country = Country(data[0], data[1], data[2])
                self.countries[data[0]] = country

    def size(self):
        return(len(self.countries))

    def listByArea(self):
        for c in sorted(self.countries, key=lambda x: (-self.countries[x].area)):
            yield self.countries[c]


if __name__ == "__main__":
    countries = Countries("OmaCountries.txt")
    print("Size:", countries.size())
    for country in countries.listByArea():
        print(country)
