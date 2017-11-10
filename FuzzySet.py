#
#  Fuzzifier module:
#  -	Membership functions of fuzzy sets
#  -	Converts crisp input to fuzzy values

class FuzzySet:
    def __init__(self, name, a, b, alpha, beta):
        self.name = name
        self.a = a
        self.b = b
        self.alpha = alpha
        self.beta = beta

    def membership(self, value):  # returns membership value in a set given a crisp value
        if self.a <= value <= self.b:  # if value inside core
            return 1
        elif value <= self.a - self.alpha or value >= self.b + self.beta:  # if value completely outside of set
            return 0
        elif self.a - self.alpha <= value and value <= self.a:  # if value less than core
            percentage = (value - self.a + self.alpha) / self.alpha
            return percentage
        elif value >= self.b and self.b + self.beta >= value:  # if value more than core
            percentage = (self.b + self.beta - value) / self.beta
            return percentage
        else:  # default return value is 0
            return 0

    def meanofmax(self):  # returns center of core
        mom = self.a + ((self.b - self.a) / 2)
        return mom




class FuzzyDimension:
    def __init__(self, name):
        self.name = name
        self.memberships = {}

    def add_membership(self, setname, tupleofmemberhips):  # ads a membership and fuzzy set to the dimension
        fuzzyset = FuzzySet(
            setname,
            tupleofmemberhips[0],
            tupleofmemberhips[1],
            tupleofmemberhips[2],
            tupleofmemberhips[3])
        self.memberships[setname] = fuzzyset

    def membership(self, setname, value):  # returns membership value of a given fuzzy set
        percentage = self.memberships[setname].membership(value)
        return percentage

    def meanofmax(self, setname):
        mom = self.memberships[setname].meanofmax()
        return mom
