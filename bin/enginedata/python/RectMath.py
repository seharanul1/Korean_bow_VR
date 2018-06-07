import math

class Rect(object):
    
    def __init__(self, *args):
        if len(args) == 4:
            self.left = args[0]
            self.top = args[1]
            self.right = args[2]
            self.bottom = args[3]
        elif len(args) == 1:
            if isinstance(args[0], Rect):
                self.left = args[0].left
                self.top = args[0].top
                self.right = args[0].right
                self.bottom = args[0].bottom
        elif len(args) == 2:
            from Vector2Math import Vector2
            if isinstance(args[0], Vector2) and isinstance(args[1], Vector2):
                self.left = args[0].x
                self.top = args[0].y
                self.right = args[1].x
                self.bottom = args[1].y
        else:
            self.left = 0.0
            self.top = 0.0
            self.right = 0.0
            self.bottom = 0.0

    # A + B, A += B
    def __add__(self, v):
        from Vector2Math import Vector2
        if isinstance(v, Vector2):
            return self.OffsetRect(v.x, v.y)
        elif isinstance(v, Rect):
            return self.InflateRect(v)

    # A - B, A -= B
    def __sub__(self, v):
        from Vector2Math import Vector2
        if isinstance(v, Vector2):
            return self.OffsetRect(-v.x, -v.y)
        elif isinstance(v, Rect):
            return self.DeflateRect(v)

    # A & B, A &= B
    def __and__(self, v):
        if isinstance(v, Rect):
            return self.IntersectRect(v)
    
    # A | B, A |= B
    def __or__(self, v):
        if isinstance(v, Rect):
            return self.UnionRect(v)

    # A == B
    def __eq__(self, v):
        return self.EqualRect(v)

    # A != B
    def __ne__(self, v):
        return not self.EqualRect(v)

    # for print
    def __str__(self):
        return str(self.left) + ", " + str(self.top) + ", " + str(self.right) + ", " + str(self.bottom)

    def New():
        return Rect()

    def ToString(self):
        return str(self.left) + ", " + str(self.top) + ", " + str(self.right) + ", " + str(self.bottom)

    def FromString(self, s):
        if isinstance(s, bytes):
            rectString = s.decode('utf-8')
        else:
            rectString = s.encode().decode('utf-8')
        sp = rectString.split(",")
        self.left = float(sp[0])
        self.top = float(sp[1])
        self.right = float(sp[2])
        self.bottom = float(sp[3])

    def Width(self):
        return self.right - self.left

    def Height(self):
        return self.bottom - self.top

    def Size(self):
        from Vector2Math import Vector2
        return Vector2(self.Width(), self.Height())

    def TopLeft(self):
        from Vector2Math import Vector2
        return Vector2(self.left, self.top)

    def BottomRight(self):
        from Vector2Math import Vector2
        return Vector2(self.right, self.bottom)

    def CenterPofloat(self):
        from Vector2Math import Vector2
        return Vector2((self.left + self.right)*0.5, (self.top + self.bottom)*0.5)

    def SwapLeftRight(self, *args):
        if len(args) == 0:
            temp = self.left
            self.left = self.right
            self.right = temp
        elif len(args) == 1:
            if isinstance(args[0], Rect):
                self.CopyRect(args[0])
                temp = self.left
                self.left = self.right
                self.right = temp

    def IsRectEmpty(self):
        return self.right <= self.left and self.bottom <= self.top

    def IsRectNull(self):
        return self.left == 0 and self.right == 0 and self.top == 0 and self.bottom == 0

    def PtInRect(self, source):
        from Vector2Math import Vector2
        from PointMath import Point
        if isinstance(source, Vector2):
            return source.x >= self.left and source.x <= self.right and source.y >= self.top and source.y <= self.bottom
        elif isinstance(source, Point):
            return source.x >= self.left and source.x <= self.right and source.y >= self.top and source.y <= self.bottom

    def SetRect(self, *args):
        if len(args) == 2:
            from Vector2Math import Vector2
            if isinstance(args[0], Vector2) and isinstance(args[1], Vector2):
                self.left = args[0].x;
                self.top = args[0].y;
                self.right = args[1].x;
                self.bottom = args[1].y;
        elif len(args) == 4:
            self.left = args[0];
            self.top = args[1];
            self.right = args[2];
            self.bottom = args[3];

    def SetRectEmpty(self):
        self.left = 0.0
        self.right = 0.0
        self.top = 0.0
        self.bottom = 0.0

    def CopyRect(self, source):
        if isinstance(source, Rect):
            self.left = source.left
            self.top = source.top
            self.right = source.right
            self.bottom = source.bottom

    def EqualRect(self, source):
        if isinstance(source, Rect):
            return self.left == source.left and self.right == source.right and self.top == source.top and self.bottom == source.bottom

    def InflateRect(self, *args):
        if len(args) == 2:
            self.left -= args[0]
            self.top -= args[0]
            self.right += args[1]
            self.bottom += args[1]
        elif len(args) == 1:
            from Vector2Math import Vector2
            if isinstance(args[0], Vector2):
                self.left -= args[0].x
                self.top -= args[0].x
                self.right += args[0].y
                self.bottom += args[0].y
            elif isinstance(args[0], Rect):
                self.left -= args[0].left
                self.top -= args[0].top
                self.right += args[0].right
                self.bottom += args[0].bottom
        elif len(args) == 4:
            self.left -= args[0]
            self.top -= args[1]
            self.right += args[2]
            self.bottom += args[3]

    def DeflateRect(self, *args):
        if len(args) == 2:
            self.InflateRect(-args[0], -args[1])
        elif len(args) == 1:
            from Vector2Math import Vector2
            if isinstance(args[0], Vector2):
                self.InflateRect(-args[0].x, -args[0].y)
            elif isinstance(args[0], Rect):
                self.InflateRect(-args[0].left, -args[0].top, -args[0].right, -args[0].bottom)
        elif len(args) == 4:
            self.InflateRect(-args[0], -args[1], -args[2], -args[3])

    def OffsetRect(self, *args):
        if len(args) == 2:
            self.left += args[0]
            self.right += args[0]
            self.top += args[1]
            self.bottom += args[1]
        elif len(args) == 1:
            from Vector2Math import Vector2
            if isinstance(args[0], Vector2):
                self.left += args[0].x
                self.right += args[0].x
                self.top += args[0].y
                self.bottom += args[0].y

    def NormalizeRect(self):
        if self.left > self.right:
            temp = self.left
            self.left = self.right
            self.right = temp
        elif self.top > self.bottom:
            temp = self.top
            self.top = self.bottom
            self.bottom = temp

    def MoveToY(self, y):
        self.bottom = self.Height() + y
        self.top = y

    def MoveToX(self, x):
        self.right = self.Width() + x
        self.left = x

    def MoveToXY(self, *args):
        if len(args) == 2:
            self.MoveToX(args[0])
            self.MoveToY(args[1])
        elif len(args) == 1:
            from Vector2Math import Vector2
            if isinstance(args[0], Vector2):
                self.MoveToX(args[0].x)
                self.MoveToY(args[0].y)

    def IntersectRect(self, source):
        r = Rect(self)
        if r.left < source.left:
            r.left = source.left;
        if r.right > source.right:
            r.right = source.right;
        if r.top < source.top:
            r.top = source.top;
        if r.bottom > source.bottom:
            r.bottom = source.bottom;
        return r

    def UnionRect(self, source):
        r = Rect(self)
        if r.left > source.left:
            r.left = source.left;
        if r.right < source.right:
            r.right = source.right;
        if r.top > source.top:
            r.top = source.top;
        if r.bottom < source.bottom:
            r.bottom = source.bottom;
        return r

    def SubtractRect(self, source):
        r = self.IntersectRect(source)
        r2 = Rect(self)
        if not r.IsRectEmpty():
            return r2
        if r.top == self.top and r.bottom == self.bottom:
            if r2.right == r.right:
                r2.right = r.left
            elif r2.left == r.left:
                r2.left = r.right
            return r2
        elif r.left == self.left and r.right == self.right:
            if r2.bottom == r.bottom:
                r2.bottom = r.top
            elif r2.top == r.top:
                r2.top = r.bottomi
            return r2
        else:
            return r2