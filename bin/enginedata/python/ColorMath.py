
import math

class Color(object):
    
    def __init__(self, *args):
        if len(args) == 4:
            self.r = args[0]
            self.g = args[1]
            self.b = args[2]
            self.a = args[3]
        elif len(args) == 1:
            if isinstance(args[0], Color):
                self.r = args[0].r
                self.g = args[0].g
                self.b = args[0].b
                self.a = args[0].a
        else:
            self.r = 0.0
            self.g = 0.0
            self.b = 0.0
            self.a = 0.0
        
    # A + B, A += B
    def __add__(self, v):
        return Color(self.r + v.r, self.g + v.g, self.b + v.b, self.a + v.a)

    # A - B, A -= B
    def __sub__(self, v):
        return Color(self.r - v.r, self.g - v.g, self.b - v.b, self.a - v.a)
    
    # A * 2, A * B, A *= 2, A *= B
    def __mul__(self, v): 
        if isinstance(v, Color):
            return Color(self.r * v.r, self.g * v.g, self.b * v.b, self.a * v.a)
        else:
            return Color(self.r * v, self.g * v, self.b * v, self.a * v)

    # 2 * A, B * A
    def __rmul__(self, v): # 
        if isinstance(v, Color):
            return Color(self.r * v.r, self.g * v.g, self.b * v.b, self.a * v.a)
        else:
            return Color(self.r * v, self.g * v, self.b * v, self.a * v)

    # A / 2, A / B, A /= 2, A /= B
    def __truediv__(self, v):
        if isinstance(v, Color):
            return Color(self.r / v.r, self.g / v.g, self.b / v.b, self.a / v.a)
        else:
            return Color(self.r / v, self.g / v, self.b / v, self.a / v)
        
    # A == B
    def __eq__(self, v):
        return self.r == v.r and self.g == v.g and self.b == v.b and self.a == v.a

    # A != B
    def __ne__(self, v):
        return self.r != v.r or self.g != v.g or self.b != v.b or self.a != v.a

    # for print
    def __str__(self):
        return str(self.r) + ", " + str(self.g) + ", " + str(self.b) + ", " + str(self.a)

    def New():
        return Color(0.0, 0.0, 0.0, 0.0)

    def Scale(self, rate):
        return Color.Scale(self, rate)

    def Scale(col, rate):
        
        result = Color.New()

        result.r = col.r * rate
        result.g = col.g * rate
        result.b = col.b * rate
        result.a = col.a * rate

        return result

    def AdjustContrast(self, weight):
        return Color.AdjustContrast(self, weight)

    def AdjustContrast(col, weight):
        result = Color.New()
        result.r = 0.5 + weight * (col.r - 0.5)
        result.g = 0.5 + weight * (col.g - 0.5)
        result.b = 0.5 + weight * (col.b - 0.5)
        result.a = pc.a
        return result


    def AdjustSaturation(self, weight):
        return Color.AdjustSaturation(self, weight)

    def AdjustSaturation(col, weight):
        result = Color.New()

        grey = col.r * 0.2125 + col.g * 0.7154 + col.b * 0.0721;
        result.r = grey + weight * (col.r - grey)
        result.g = grey + weight * (col.g - grey)
        result.b = grey + weight * (col.b - grey)
        result.a = col.a

        return result

    def FromCOLORREF(colorref):
        result = Color.New()
        f = 1.0 / 255.0

        result.r = f * int(colorref & 0xff)
        result.g = f * int((colorref >> 8) & 0xff )
        result.b = f * int((colorref >> 16) & 0xff )
        result.a = 1.0
        
        return result

    def FromARGB(argb):
        result = Color.New()
        f = 1.0 / 255.0
        result.r = f * int((argb >> 16) & 0xff)
        result.g = f * int((argb >> 8) & 0xff)
        result.b = f * int(argb & 0xff)
        result.a = f * int((argb >> 24) & 0xff)

        return result

    def MakeARGB(self):
        return Color.MakeARGB(self)


    def MakeARGB(col):
        red = 0
        green = 0
        blue = 0
        alpha = 0
        
        if col.r >= 1.0:
            red = 0xff
        else:
            if col.r <= 0.0:
                red = 0x00
            else:
                red = int(col.r * 255.0 + 0.5)

        if col.g >= 1.0:
            green = 0xff
        else:
            if col.g <= 0.0:
                green = 0x00
            else:
                green = int(col.g * 255.0 + 0.5)

        if col.b >= 1.0:
            blue = 0xff
        else:
            if col.b <= 0.0:
                blue = 0x00
            else:
                blue = int(col.b * 255.0 + 0.5)

        if col.a >= 1.0:
            alpha = 0xff
        else:
            if col.a <= 0.0:
                alpha = 0x00
            else:
                alpha = int(col.a * 255.0 + 0.5)

        return (alpha << 24) | (red << 16) | (green << 8) | blue


    def MakeCOLORREF(self):
        return Color.MakeCOLORREF(self)

    def MakeCOLORREF(col):
        red = int
        green = int
        blue = int
        
        if col.r >= 1.0:
            red = 0xff
        else:
            if col.r <= 0.0:
                red = 0x00
            else:
                red = int(col.r * 255.0 + 0.5)

        if col.g >= 1.0:
            green = 0xff
        else:
            if col.g <= 0.0:
                green = 0x00
            else:
                green = int(col.g * 255.0 + 0.5)

        if col.b >= 1.0:
            blue = 0xff
        else:
            if col.b <= 0.0:
                blue = 0x00
            else:
                blue = int(col.b * 255.0 + 0.5)

        return (blue << 16) | (green << 8) | red

    def Negative(col):

        result = Color.New()

        result.r = 1.0 - col.r
        result.g = 1.0 - col.g
        result.b = 1.0 - col.b
        result.a = col.a

        return result


    def Lerp(lhs, rhs, deltaT):
        result = Color.New()
        result.r = (1.0 - deltaT) * (lhs.r) + deltaT * (rhs.r)
        result.g = (1.0 - deltaT) * (lhs.g) + deltaT * (rhs.g)
        result.b = (1.0 - deltaT) * (lhs.b) + deltaT * (rhs.b)
        result.a = (1.0 - deltaT) * (lhs.a) + deltaT * (rhs.a)
        return result
    

    def Modulate(lhs, rhs):
        result = Color.New()
        result.r = (lhs.r) * (rhs.r)
        result.g = (lhs.g) * (rhs.g)
        result.b = (lhs.b) * (rhs.b)
        result.a = (lhs.a) * (rhs.a)
        return result


    def __str__(self):
        return str(self.r) + "," + str(self.g) + "," + str(self.b) + "," + str(self.a)

    def ToString(self):
        return str(self.r) + "," + str(self.g) + "," + str(self.b) + "," + str(self.a)

    def FromString(self, s):
        if isinstance(s, bytes):
            colorString = s.decode('utf-8')
        else:
            colorString = s.encode().decode('utf-8')
        sp = colorString.split(",")
        self.r = float(sp[0])
        self.g = float(sp[1])
        self.b = float(sp[2])
        self.a = float(sp[3])