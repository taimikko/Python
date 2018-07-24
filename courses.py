# h5.3_Courses.py
"""
Implement a Python module "courses" that provides the following facilities for handling course data:

    A class Course with attributes code, name, minCredits and maxCredits.
    The class needs to have:
        An initialization function that receives initialization values for these attributes
        (in the same order as they were mentioned here).
            The attributes code and name are strings.
            The attributes minCredits and maxCredits are integers.
        A string conversion function that returns a string of form "code name minCredits ECTS"
        or "code name minCredits-maxCredits ECTS",
        depending on whether minCredits == maxCredits or not.
        An equality comparison function __eq__(self, other) that compares Course-objects
        bases on their names (this is similar to what was done in a lecture example regarding __lt__).
        A function __hash__(self) that returns the value self.name.__hash__().
            Without going into details, having both the __eq__ and the __hash__-function
            enables us to use Course-objects as dictionary keys or set values.
            In this question we will not really create an own implementation but just reuse
            the __hash__-function of the attribute name.
            The end result is that in terms of dictionary keys or set values,
            two Course-objects are deeed to be identical if their names are identical.
    A function readCourses(filename) that reads course information from the file specified by the parameter filename
    and creates and returns a list of Course-objects
    that describe all courses in the file (in the order they appeared).
        Inspect the file courses.txt to see how the course information is structured.
        You need to do some suitable string matching operations in order to pick out
        the essential course information.
        You do not need to worry about duplicates (whether or not the same course appears more than once).
"""


class Course:
    def __init__(self, code, name, minCredits, maxCredits):
        self.code = code
        self.name = name
        self.minCredits = int(minCredits)
        self.maxCredits = int(maxCredits)

    def __str__(self):
        if self.minCredits == self.maxCredits:
            return ("".join(self.code+" "+self.name+" "+str(self.minCredits)+" ECTS"))
        else:
            return ("".join(self.code+" "+self.name+" "+str(self.minCredits)+"-"+str(self.maxCredits)+" ECTS"))

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return self.name.__hash__()


def line2course(line):
    i = line.find(" ")
    code = line[:i]
    header = line[i+1:].split(" ECTS")
    i = header[0].rfind(" ")
    ects = header[0][i+1:].split("–") # erikoismerkki
    #ects = ects
    maxC = minC = ects[0]
    if len(ects) > 1:
        maxC = ects[1]
    name = header[0][:i]
    course = Course(code, name, minC, maxC)
    return course


def readCourses(filename):
    print("Luetaan kursseja tiedostosta ", filename)
    courses = []
    with open(filename, encoding="UTF-8") as f:
        line = f.readline()
        while line:
            if "ECTS" in line:
                courses.append(line2course(line))
            line = f.readline()
    return courses


if __name__ == "__main__":
    x = readCourses("courses.txt")
    print(x)
