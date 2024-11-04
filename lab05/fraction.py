import math

class fraction:
    num = 1
    denom = 1

    def __init__(self, num, denom):
        assert denom != 0
        self.num = num
        self.denom = denom
        self.simplify()

    def simplify(self):
        # 0 is always 0/1
        if self.num == 0:
            self.denom = 1
            return
        
        # Denom is always positive
        if self.denom < 0:
            self.num = -self.num
            self.denom = -self.denom
        
        # Simplify
        gcd_ = math.gcd(self.num, self.denom)
        self.num //= gcd_
        self.denom //= gcd_

    def __add__(self, other):
        return fraction(self.num * other.denom + other.num * self.denom, self.denom * other.denom)
    
    def __sub__(self, other):
        return fraction(self.num * other.denom - other.num * self.denom, self.denom * other.denom)
    
    def __mul__(self, other):
        return fraction(self.num * other.num, self.denom * other.denom)
    
    def __truediv__(self, other):
        return fraction(self.num * other.denom, self.denom * other.num)

    def __eq__(self, other):
        return self.num == other.num and self.denom == other.denom       
        
    def __lt__(self, other):
        return self.num * other.denom < other.num * self.denom

    def __le__(self, other):
        return self.num * other.denom <= other.num * self.denom
        
    def __str__(self):
        return f'{self.num}/{self.denom}'
        


if __name__ == '__main__':
    f1 = fraction(1, 2)
    f2 = fraction(2, -3)

    print(f'f1 = {f1}')
    print(f'f2 = {f2}')
    print(f'{f1} + {f2} = {f1 + f2}')
    print(f'{f1} - {f2} = {f1 - f2}')
    print(f'{f1} * {f2} = {f1 * f2}')
    print(f'{f1} / {f2} = {f1 / f2}')
    print(f'{f1} == {f2} : {f1 == f2}')
    print(f'{f1} != {f2} : {f1 != f2}')
    print(f'{f1} < {f2} : {f1 < f2}')
    print(f'{f1} <= {f2} : {f1 <= f2}')
    print(f'{f1} > {f2} : {f1 > f2}')
    print(f'{f1} >= {f2} : {f1 >= f2}')
