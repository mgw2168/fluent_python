from math import hypot

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return hypot(self.x, self.y)

    # 将对象以字符串的形式表示，有助于阅读
    # %r 用于repre方法，%s用于str方法
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)


v1 = Vector(1, 3)
v2 = Vector(3, 4)
print(v1 + v2)
print(abs(v2))
print(abs(v2 * 10))


