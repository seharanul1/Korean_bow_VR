import math

class Vector4(object):
    
    def __init__(self, *args):
        if len(args) == 4:
            self.x = args[0]
            self.y = args[1]
            self.z = args[2]
            self.w = args[3]
        elif len(args) == 1:
            if isinstance(args[0], Vector4):
                self.x = args[0].x
                self.y = args[0].y
                self.z = args[0].z
                self.w = args[0].w
        else:
            self.x = 0.0
            self.y = 0.0
            self.z = 0.0
            self.w = 0.0
        
    # A + B, A += B
    def __add__(self, v):
        return Vector4(self.x + v.x, self.y + v.y, self.z + v.z, self.w + v.w)

    # A - B, A -= B
    def __sub__(self, v):
        return Vector4(self.x - v.x, self.y - v.y, self.z - v.z, self.w - v.w)
    
    # A * 2, A * B, A *= 2, A *= B
    def __mul__(self, v): 
        if isinstance(v, Vector4):
            return Vector4(self.x * v.x, self.y * v.y, self.z * v.z, self.w * v.w)
        else:
            return Vector4(self.x * v, self.y * v, self.z * v, self.w * v)

    # 2 * A, B * A
    def __rmul__(self, v): # 
        if isinstance(v, Vector4):
            return Vector4(self.x * v.x, self.y * v.y, self.z * v.z, self.w * v.w)
        else:
            return Vector4(self.x * v, self.y * v, self.z * v, self.w * v)

    # A / 2, A / B, A /= 2, A /= B
    def __truediv__(self, v):
        if isinstance(v, Vector4):
            return Vector4(self.x / v.x, self.y / v.y, self.z / v.z, self.w / v.w)
        else:
            return Vector4(self.x / v, self.y / v, self.z / v, self.w / v)
        
    # A == B
    def __eq__(self, v):
        return self.x == v.x and self.y == v.y and self.z == v.z and self.w == v.w

    # A != B
    def __ne__(self, v):
        return self.x != v.x or self.y != v.y or self.z != v.z or self.w != v.w

    # for print
    def __str__(self):
        return str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ", " + str(self.w)

    def New():
        return Vector4(0,0,0)

    def Zero(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.w = 0.0

    def Identity(self):
        self.x = 1.0
        self.y = 1.0
        self.z = 1.0
        self.w = 1.0

    def Length(self):
        return math.sqrt( (self.x * self.x) + (self.y * self.y) + (self.z * self.z) + (self.w * self.w) )


    def LengthSq(self):
        return (self.x * self.x) + (self.y * self.y) + (self.z * self.z) + (self.w * self.w)

    def Normalize(self):
        norm = self.Length()

        if norm == 0.0:
            self.x = 0.0
            self.y = 0.0
            self.z = 0.0
            self.w = 0.0
        else:
            self.x /= norm
            self.x /= norm
            self.y /= norm
            self.w /= norm

    def Scale(vec, ratio):
        vec.x *= ratio
        vec.y *= ratio
        vec.z *= ratio
        vec.w *= ratio

    def TransformCoord(source, sourceMatrix):
        from MatrixMath import Matrix
        result = Vector4.New()

        norm = sourceMatrix.m[0][3] * source.x + sourceMatrix.m[1][3] * source.y +sourceMatrix.m[2][3] * source.z + sourceMatrix.m[3][3]
        if norm != 0.0 :
            result.x = ((sourceMatrix.m[0][0] * source.x + sourceMatrix.m[1][0] * source.y + sourceMatrix.m[2][0] * source.z + sourceMatrix.m[3][0]) / norm )
            result.y = ((sourceMatrix.m[0][1] * source.x + sourceMatrix.m[1][1] * source.y + sourceMatrix.m[2][1] * source.z + sourceMatrix.m[3][1]) / norm )
            result.z = ((sourceMatrix.m[0][2] * source.x + sourceMatrix.m[1][2] * source.y + sourceMatrix.m[2][2] * source.z + sourceMatrix.m[3][2]) / norm )

        return result

    def TransformNormal(source, sourceMatrix):
        from MatrixMath import Matrix
        result = Vector4.New()

        result.x = (sourceMatrix.m[0][0] * source.x + sourceMatrix.m[1][0] * source.y + sourceMatrix.m[2][0] * source.z)
        result.y = (sourceMatrix.m[0][1] * source.x + sourceMatrix.m[1][1] * source.y + sourceMatrix.m[2][1] * source.z)
        result.z = (sourceMatrix.m[0][2] * source.x + sourceMatrix.m[1][2] * source.y + sourceMatrix.m[2][2] * source.z)

        return result;

    def Dot(pv1, pv2):
        return pv1.x * pv2.x + pv1.y * pv2.y + pv1.z * pv2.z + pv1.w * pv2.w;

    def Maximize(lhs, rhs):
        result = Vector4(lhs)

        if lhs.x < rhs.x:
            result.x = rhs.x

        if lhs.y < rhs.y:
            result.y = rhs.y

        if lhs.z < rhs.z:
            result.z = rhs.z

        if lhs.w < rhs.w:
            result.z = rhs.w

        return result

    def Minimize(lhs, rhs):
        result = Vector4(rhs)

        if lhs.x < rhs.x:
            result.x = lhs.x

        if lhs.y < rhs.y:
            result.y = lhs.y

        if lhs.z < rhs.z:
            result.z = lhs.z

        if lhs.w < rhs.w:
            result.w = lhs.w

        return result

    
    def CatmullRom(pv0, pv1, pv2, pv3, weight):
        result = Vector4.New()

        result.x = 0.5 * (2.0 * pv1.x + (pv2.x - pv0.x) * weight + (2.0 * pv0.x - 5.0 * pv1.x + 4.0 * pv2.x - pv3.x) * weight * weight + (pv3.x - 3.0 * pv2.x + 3.0 * pv1.x - pv0.x) * weight * weight * weight)
        result.y = 0.5 * (2.0 * pv1.y + (pv2.y - pv0.y) * weight + (2.0 * pv0.y - 5.0 * pv1.y + 4.0 * pv2.y - pv3.y) * weight * weight + (pv3.y - 3.0 * pv2.y + 3.0 * pv1.y - pv0.y) * weight * weight * weight)
        result.z = 0.5 * (2.0 * pv1.z + (pv2.z - pv0.z) * weight + (2.0 * pv0.z - 5.0 * pv1.z + 4.0 * pv2.z - pv3.z) * weight * weight + (pv3.z - 3.0 * pv2.z + 3.0 * pv1.z - pv0.z) * weight * weight * weight)
        result.w = 0.5 * (2.0 * pv1.w + (pv2.w - pv0.w) * weight + (2.0 * pv0.w - 5.0 * pv1.w + 4.0 * pv2.w - pv3.w) * weight * weight + (pv3.w - 3.0 * pv2.w + 3.0 * pv1.w - pv0.w) * weight * weight * weight)

        return result


    def Hermite(startPoint, startToNextDelta, nextPoint, nextToNextDelta, weight):
        result = Vector4.New()
            
        h1 = 2.0 * weight * weight * weight - 3.0 * weight * weight + 1.0
        h2 = weight * weight * weight - 2.0 * weight * weight + weight
        h3 = -2.0 * weight * weight * weight + 3.0 * weight * weight
        h4 = weight * weight * weight - weight * weight
        
        result.x = h1 * (startPoint.x) + h2 * (startToNextDelta.x) + h3 * (nextPoint.x) + h4 * (nextToNextDelta.x)
        result.y = h1 * (startPoint.y) + h2 * (startToNextDelta.y) + h3 * (nextPoint.y) + h4 * (nextToNextDelta.y)
        result.z = h1 * (startPoint.z) + h2 * (startToNextDelta.z) + h3 * (nextPoint.z) + h4 * (nextToNextDelta.z)
        result.w = h1 * (startPoint.w) + h2 * (startToNextDelta.w) + h3 * (nextPoint.w) + h4 * (nextToNextDelta.w)
        
        return result;


    def Lerp(lhs, rhs, deltaT):
        result = Vector4.New()

        result.x = (1.0 - deltaT) * (lhs.x) + deltaT * (rhs.x)
        result.y = (1.0 - deltaT) * (lhs.y) + deltaT * (rhs.y)
        result.z = (1.0 - deltaT) * (lhs.z) + deltaT * (rhs.z)
        result.w = (1.0 - deltaT) * (lhs.w) + deltaT * (rhs.w)

        return result;


    def BaryCentric(trianglePoint0, trianglePoint1, trianglePoint2, p1Weight, p2Weight):
        result = Vector4.New()

        result.x = (1.0 - f - g) * (trianglePoint0.x) + p1Weight * (trianglePoint1.x) + p2Weight * (trianglePoint2.x)
        result.y = (1.0 - f - g) * (trianglePoint0.y) + p1Weight * (trianglePoint1.y) + p2Weight * (trianglePoint2.y)
        result.z = (1.0 - f - g) * (trianglePoint0.z) + p1Weight * (trianglePoint1.z) + p2Weight * (trianglePoint2.z)
        result.w = (1.0 - f - g) * (trianglePoint0.w) + p1Weight * (trianglePoint1.w) + p2Weight * (trianglePoint2.w)

        return result


    def Cross(pv1, pv2, pv3):
        result = Vector4.New()

        result.x = pv1.y * (pv2.z * pv3.w - pv3.z * pv2.w) - pv1.z * (pv2.y * pv3.w - pv3.y * pv2.w) + pv1.w * (pv2.y * pv3.z - pv2.z * pv3.y)
        result.y = -(pv1.x * (pv2.z * pv3.w - pv3.z * pv2.w) - pv1.z * (pv2.x * pv3.w - pv3.x * pv2.w) + pv1.w * (pv2.x * pv3.z - pv3.x * pv2.z))
        result.z = pv1.x * (pv2.y * pv3.w - pv3.y * pv2.w) - pv1.y * (pv2.x * pv3.w - pv3.x * pv2.w) + pv1.w * (pv2.x * pv3.y - pv3.x * pv2.y)
        result.w = -(pv1.x * (pv2.y * pv3.z - pv3.y * pv2.z) - pv1.y * (pv2.x * pv3.z - pv3.x * pv2.z) + pv1.z * (pv2.x * pv3.y - pv3.x * pv2.y))

        return result


    def Transform(source, sourceMatrix):
        from MatrixMath import Matrix
        result = Vector4.New()

        result.x = sourceMatrix.m[0][0] * source.x + sourceMatrix.m[1][0] * source.y + sourceMatrix.m[2][0] * source.z + sourceMatrix.m[3][0] * source.w
        result.y = sourceMatrix.m[0][1] * source.x + sourceMatrix.m[1][1] * source.y + sourceMatrix.m[2][1] * source.z + sourceMatrix.m[3][1] * source.w
        result.z = sourceMatrix.m[0][2] * source.x + sourceMatrix.m[1][2] * source.y + sourceMatrix.m[2][2] * source.z + sourceMatrix.m[3][2] * source.w
        result.w = sourceMatrix.m[0][3] * source.x + sourceMatrix.m[1][3] * source.y + sourceMatrix.m[2][3] * source.z + sourceMatrix.m[3][3] * source.w

        return result;



    def __str__(self):
        return str(self.x) + "," + str(self.y) + "," + str(self.z) + "," + str(self.w)

    def ToString(self):
        return str(self.x) + "," + str(self.y) + "," + str(self.z) + "," + str(self.w)

    def FromString(self, s):
        if isinstance(s, bytes):
            vectorString = s.decode('utf-8')
        else:
            vectorString = s.encode().decode('utf-8')
        sp = vectorString.split(",")
        self.x = float(sp[0])
        self.y = float(sp[1])
        self.z = float(sp[2])
        self.w = float(sp[3])