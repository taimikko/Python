class Coupling(object):

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

    def coupling(self, in1, in2, in3, in4, in5):
        print(self.orf(self.orf3(in1, in2, in3),
                       self.xorf(in4, in5)))


class Coupling2(Coupling):

    def coupling(self, in1, in2, in3, in4, in5):
        x = self.xorf(in3, in4)
        print(self.orf(self.nandf(in1, in2), x),
              self.andf(x, in5))
