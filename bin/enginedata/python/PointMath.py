import math

class Point(object):
    
    def __init__(self, *args):
        if len(args) == 2:
            self.x = args[0]
            self.y = args[1]
        elif len(args) == 1:
            if isinstance(args[0], Point):
                self.x = args[0].x
                self.y = args[0].y
        else:
            self.x = 0.0
            self.y = 0.0
        
    # A + B, A += B
    def __add__(self, v):
        return Point(self.x + v.x, self.y + v.y)

    # A - B, A -= B
    def __sub__(self, v):
        return Point(self.x - v.x, self.y - v.y)
    
    # A * 2, A * B, A *= 2, A *= B
    def __mul__(self, v): 
        if isinstance(v, Point):
            return Point(self.x * v.x, self.y * v.y)
        else:
            return Point(self.x * v, self.y * v)

    # 2 * A, B * A
    def __rmul__(self, v): # 
        if isinstance(v, Point):
            return Point(self.x * v.x, self.y * v.y)
        else:
            return Point(self.x * v, self.y * v)

    # A / 2, A / B, A /= 2, A /= B
    def __truediv__(self, v):
        if isinstance(v, Point):
            return Point(self.x / v.x, self.y / v.y)
        else:
            return Point(self.x / v, self.y / v)
        
    # A == B
    def __eq__(self, v):
        return self.x == v.x and self.y == v.y

    # A != B
    def __ne__(self, v):
        return self.x != v.x or self.y != v.y

    # for print
    def __str__(self):
        return str(self.x) + ", " + str(self.y)

    def New():
        return Point(0,0,0)

    def ToString(self):
        return str(self.x) + "," + str(self.y)

    def FromString(self, s):
        if isinstance(s, bytes):
            pointString = s.decode('utf-8')
        else:
            pointString = s.encode().decode('utf-8')
        sp = pointString.split(",")
        self.x = float(sp[0])
        self.y = float(sp[1])
