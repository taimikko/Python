class Person:
  def __init__(self, name="", age=0, height=0, weight=0):
    # Using two leading underscores leads into name mangling.
    # E.g. the reference self.__name is ok here inside the class
    # definition, but a reference of form p.__name with some
    # Person-object p in outside code would fail.
    self.__name = name
    self.__age = age
    self.__height = height
    self.__weight = weight
  
  def bmi(self):
    return self.__weight/((self.__height/100) ** 2)
  
  def __str__(self):
    return ("Name is {:s}\n"
            "Age is {:d}\n"
            "Height is {:.1f}\n"
            "Weight is {:.1f}\n"
            "BMI is {:.2f}").format(
            self.__name, self.__age, self.__height, self.__weight, self.bmi())
  
  def __setattr__(self, attr, val):
    if attr not in self.__dict__:
      print("Attribute", attr, "is new!")
    object.__setattr__(self, attr, val)
 # The getter for height: this simply returns the __height attribute.
  def getHeight(self):
    return self.__height

  # The setter for height: this sets the received parameter into the __height
  # attribute. The function also prints a message if the height is negative.
  def setHeight(self, height):
    if height < 0:
      print("Height is negative!")
    self.__height = height
  
  # Now define "height" as an attribute that can be accessed with
  # the getter getHeight and the setter setHeight.
  height = property(getHeight, setHeight)

  # The @property decorator below has the effect of defining the following
  # function as a setter for an attribute with that function's name (here "height").
  @property
  def weight(self):
    return self.__weight

  # The decorator above has the same effect as if we had included the line
  #   height = property(height)
  # here (without indentation).

  # A decorator of form @name.setter defines that the following function
  # is a setter for the attribute "name" (here "height"). The function
  # has to have the same name as the corresponding attribute (again, "height").
  # A separate definition for the attribute "height" itself is not needed.
  @weight.setter
  def weight(self, weight):
    if weight < 0:
      print("Weight is negative!")
    self.__weight = weight

tc = Person(weight=67, name="Tom Cruise", age=56, height=170)
dt = Person("Donald Trump", 72, 188, 105)
putin = Person("Vladimir Putin", 65, 168, 71)

print(dir(tc))
print(tc)
tc.setHeight(-25)
print("New height:", tc.height)

tc.weight = -67
print("New weight:", tc.weight)

# The following line gives an error because the "weight" attribute cannot be used as a function.
#tc.weight(-25)

