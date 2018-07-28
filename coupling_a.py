class Coupling(object):
    def __init__(self, in1, in2, in3, in4, in5):
        self.__in1 = in1
        self.__in2 = in2
        self.__in3 = in3
        self.__in4 = in4
        self.__in5 = in5

    def __str__(self):
        return ""+str(self.__in1) + " " + \
            str(self.__in2) + " " + str(self.__in3) + " " + \
            str(self.__in4) + " " + str(self.__in5)

    def andf(self, a, b):
        if a == b == 1:
            return 1
        return 0

    def xorf(self, a, b):
        if a != b and (a == 1 or b == 1):
            return 1
        return 0

    def orf(self, a, b):
        if a == 1 or b == 1:
            return 1
        return 0

    def orf3(self, a, b, c):
        return self.orf(self.orf(a, b), c)

    def nandf(self, a, b):
        if not self.andf(a, b):
            return 1
        return 0

class Coupling1(Coupling):
    def __init__(self, in1, in2, in3, in4, in5):
        self.__in1 = in1
        self.__in2 = in2
        self.__in3 = in3
        self.__in4 = in4
        self.__in5 = in5

    def coupling(self):
        print(self.orf(self.orf3(self.__in1, self.__in2, self.__in3),
                       self.xorf(self.__in4, self.__in5)))

class Coupling2(Coupling):
    def __init__(self, in1, in2, in3, in4, in5):
        super().__init__(in1, in2, in3, in4, in5)

    def coupling(self):
        x = self.xorf(self.__in3, self.__in4)
        print(self.orf(self.nandf(self.__in1, self.__in2), x),
              self.andf(x, self.__in5))
