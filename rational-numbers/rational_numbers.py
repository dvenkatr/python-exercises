from __future__ import division


class Rational:
    def __init__(self, x, y):
        if y == 0:
            raise ValueError("This number is infinite")
        if y < 0:
            x = -x
            y = abs(y)
        if x == 0:
            self.numer = 0
            self.denom = 1
        else:
            if abs(x) > abs(y):
                smaller = abs(y)
            else:
                smaller = abs(x)
            hcf = 1
            for i in range(1, smaller + 1):
                if (x % i == 0) and (y % i == 0):
                    hcf = i
            self.numer = x // hcf
            self.denom = y // hcf

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational((self.numer * other.denom + other.numer * self.denom), (self.denom * other.denom))
        
    def __sub__(self, other):
        return Rational((self.numer * other.denom - other.numer * self.denom), (self.denom * other.denom))

    def __mul__(self, other):
        return Rational((self.numer * other.numer), (self.denom * other.denom))

    def __truediv__(self, other):
        if(other.numer * self.denom == 0):
            raise ValueError("Cannot divide numbers")
        else:
            return Rational((self.numer * other.denom), (other.numer * self.denom))
            
    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if(power < 0):
            power = abs(power)
            return Rational((self.denom**power), (self.numer**power))
        else:
            return Rational((self.numer**power), (self.denom**power))

    def __rpow__(self, base):
            return (base**self.numer) ** (1/self.denom)
        

