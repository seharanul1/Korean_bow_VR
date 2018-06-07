import math

class Vector2(object):
    
    def __init__(self, *args):
        if len(args) == 2:
            self.x = args[0]
            self.y = args[1]
        elif len(args) == 1:
            if isinstance(args[0], Vector2):
                self.x = args[0].x
                self.y = args[0].y
        else:
            self.x = 0.0
            self.y = 0.0
        
    # A + B, A += B
    def __add__(self, v):
        return Vector2(self.x + v.x, self.y + v.y)

    # A - B, A -= B
    def __sub__(self, v):
        return Vector2(self.x - v.x, self.y - v.y)
    
    # A * 2, A * B, A *= 2, A *= B
    def __mul__(self, v): 
        if isinstance(v, Vector2):
            return Vector2(self.x * v.x, self.y * v.y)
        else:
            return Vector2(self.x * v, self.y * v)

    # 2 * A, B * A
    def __rmul__(self, v): # 
        if isinstance(v, Vector2):
            return Vector2(self.x * v.x, self.y * v.y)
        else:
            return Vector2(self.x * v, self.y * v)

    # A / 2, A / B, A /= 2, A /= B
    def __truediv__(self, v):
        if isinstance(v, Vector2):
            return Vector2(self.x / v.x, self.y / v.y)
        else:
            return Vector2(self.x / v, self.y / v)
        
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
        return Vector2(0,0,0)

    def Zero(self):
        self.x = 0.0
        self.y = 0.0

    def Identity(self):
        self.x = 1.0
        self.y = 1.0

    def Length(self):
        return math.sqrt((self.x * self.x) + (self.y * self.y))

    def LengthSq(self):
        return (self.x * self.x) + (self.y * self.y)

    def Normalize(self):
        norm = self.Length()
        if norm == 0.0:
            self.x = 0.0
            self.y = 0.0
        else:
            self.x /= norm
            self.x /= norm

    def Scale(vec, ratio):
        vec.x *= ratio
        vec.y *= ratio
     
    def TransformCoord(source, sourceMatrix):
        from MatrixMath import Matrix
        result = Vector2.New()
        norm = sourceMatrix.m[0][2] * source.x + sourceMatrix.m[1][2] * source.y + sourceMatrix.m[2][2]
        
        if math.fabs(norm) >= 0.0001:
            result.x = (sourceMatrix.m[0][0] * source.x + sourceMatrix.m[1][0] * source.y + sourceMatrix.m[2][0]) / norm
            result.y = (sourceMatrix.m[0][1] * source.x + sourceMatrix.m[1][1] * source.y + sourceMatrix.m[2][1]) / norm

        return result
 
    def TransformNormal(source, sourceMatrix):
        from MatrixMath import Matrix
        result = Vector2.New()
        result.x = sourceMatrix.m[0][0] * source.x + sourceMatrix.m[1][0] * source.y
        result.y = sourceMatrix.m[0][1] * source.x + sourceMatrix.m[1][1] * source.y
        return result;
    

    def CCW(self, vec):
        return (self.x * vec.y) - ( self.y * vec.x)

    def Dot(lhs, rhs):
        return (lhs.x * rhs.x) + (lhs.y * rhs.y);


    def Maximize(lhs, rhs):
        result = Vector2(lhs)

        if lhs.x < rhs.x:
            result.x = rhs.x

        if lhs.y < rhs.y:
            result.y = rhs.y
        return result


    def Minimize(lhs, rhs):
        result = Vector2(rhs)

        if lhs.x < rhs.x:
            result.x = lhs.x

        if lhs.y < rhs.y:
            result.y = lhs.y
        return result


    def Transform(source, sourceMatrix):
        from MatrixMath import Matrix
        from Vector4Math import Vector4
        result = Vector4.New()
        result.x = sourceMatrix.m[0][0] * source.x + sourceMatrix.m[1][0] * source.y  + sourceMatrix.m[3][0]
        result.y = sourceMatrix.m[0][1] * source.x + sourceMatrix.m[1][1] * source.y  + sourceMatrix.m[3][1]
        result.z = sourceMatrix.m[0][2] * source.x + sourceMatrix.m[1][2] * source.y  + sourceMatrix.m[3][2]
        result.w = sourceMatrix.m[0][3] * source.x + sourceMatrix.m[1][3] * source.y  + sourceMatrix.m[3][3]
        return result

    def CatmullRom(v0, v1, v2, v3, weight):
        result = Vector2.New()
        result.x = 0.5 * (2.0 * v1.x + (v2.x - v0.x) * weight + (2.0 * v0.x - 5.0 * v1.x + 4.0 * v2.x - v3.x) * weight * weight +(v3.x - 3.0 * v2.x + 3.0 * v1.x - v0.x) * weight * weight * weight)
        result.y = 0.5 * (2.0 * v1.y + (v2.y - v0.y) * weight + (2.0 * v0.y - 5.0 * v1.y + 4.0 * v2.y - v3.y) * weight * weight +(v3.y - 3.0 * v2.y + 3.0 * v1.y - v0.y) * weight * weight * weight)
        return result

    def Hermite(startPoint, startToNextDelta, nextPoint, nextToNextDelta, weight):
        result = Vector2.New()

        h0 = 2.0 * weight * weight * weight - 3.0 * weight * weight + 1.0
        h1 = weight * weight * weight - 2.0 * weight * weight + weight
        h2 = -2.0 * weight * weight * weight + 3.0 * weight * weight
        h3 = weight * weight * weight - weight * weight
        result.x = h0 * (startPoint.x) + h1 * (startToNextDelta.x) + h2 * (nextPoint.x) + h3 * (nextToNextDelta.x)
        result.y = h0 * (startPoint.y) + h1 * (startToNextDelta.y) + h2 * (nextPoint.y) + h3 * (nextToNextDelta.y)
        return result

    def Lerp(lhs, rhs, deltaT):
        result = Vector2.New()
        result.x = (1.0 - deltaT) * (lhs.x) + deltaT * (rhs.x)
        result.y = (1.0 - deltaT) * (lhs.y) + deltaT * (rhs.y);
        return result;

    def BaryCentric(trianglePoint0, trianglePoint1, trianglePoint2, p1Weight, p2Weight):
        result = Vector2.New()
        result.x = (1.0 - p1Weight - p2Weight) * (trianglePoint0.x) + p1Weight * (trianglePoint1.x) + p2Weight * (trianglePoint2.x)
        result.y = (1.0 - p1Weight - p2Weight) * (trianglePoint0.y) + p1Weight * (trianglePoint1.y) + p2Weight * (trianglePoint2.y)
        return result


    def __str__(self):
        return str(self.x) + "," + str(self.y)

    def ToString(self):
        return str(self.x) + "," + str(self.y)

    def FromString(self, s):
        if isinstance(s, bytes):
            vectorString = s.decode('utf-8')
        else:
            vectorString = s.encode().decode('utf-8')
        sp = vectorString.split(",")
        self.x = float(sp[0])
        self.y = float(sp[1])
