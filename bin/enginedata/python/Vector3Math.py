import math

class Vector3(object):
    
    def __init__(self, *args):
        if len(args) == 3:
            self.x = args[0]
            self.y = args[1]
            self.z = args[2]
        elif len(args) == 1:
            if isinstance(args[0], Vector3):
                self.x = args[0].x
                self.y = args[0].y
                self.z = args[0].z
        else:
            self.x = 0.0
            self.y = 0.0
            self.z = 0.0
        
    # A + B, A += B
    def __add__(self, v):
        return Vector3(self.x + v.x, self.y + v.y, self.z + v.z)

    # A - B, A -= B
    def __sub__(self, v):
        return Vector3(self.x - v.x, self.y - v.y, self.z - v.z)
    
    # A * 2, A * B, A *= 2, A *= B
    def __mul__(self, v): 
        if isinstance(v, Vector3):
            return Vector3(self.x * v.x, self.y * v.y, self.z * v.z)
        else:
            return Vector3(self.x * v, self.y * v, self.z * v)

    # 2 * A, B * A
    def __rmul__(self, v): # 
        if isinstance(v, Vector3):
            return Vector3(self.x * v.x, self.y * v.y, self.z * v.z)
        else:
            return Vector3(self.x * v, self.y * v, self.z * v)

    # A / 2, A / B, A /= 2, A /= B
    def __truediv__(self, v):
        if isinstance(v, Vector3):
            return Vector3(self.x / v.x, self.y / v.y, self.z / v.z)
        else:
            return Vector3(self.x / v, self.y / v, self.z / v)
        
    # A == B
    def __eq__(self, v):
        return self.x == v.x and self.y == v.y and self.z == v.z

    # A != B
    def __ne__(self, v):
        return self.x != v.x or self.y != v.y or self.z != v.z

    # for print
    def __str__(self):
        return str(self.x) + ", " + str(self.y) + ", " + str(self.z)

    def New():
        return Vector3(0,0,0)

    def Zero(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def Identity(self):
        self.x = 1.0
        self.y = 1.0
        self.z = 1.0

    def Length(self):
        return math.sqrt( (self.x * self.x) + (self.y * self.y) + (self.z * self.z) )

    def LengthSq(self):
        return (self.x * self.x) + (self.y * self.y) + (self.z * self.z)

    def Normalize(self):
        norm = self.Length()

        if norm == 0.0:
            self.x = 0.0
            self.y = 0.0
            self.z = 0.0
        else:
            self.x /= norm
            self.y /= norm
            self.z /= norm

    def Scale(vec, ratio):
        vec.x *= ratio
        vec.y *= ratio
        vec.z *= ratio

    def TransformCoord(source, mat):
        from MatrixMath import Matrix
        result = Vector3.New()
        norm = mat.m[0][3] * source.x + mat.m[1][3] * source.y + mat.m[2][3] * source.z + mat.m[3][3]
        if norm != 0.0:
            result.x = (mat.m[0][0] * source.x + mat.m[1][0] * source.y + mat.m[2][0] * source.z + mat.m[3][0]) / norm
            result.y = (mat.m[0][1] * source.x + mat.m[1][1] * source.y + mat.m[2][1] * source.z + mat.m[3][1]) / norm
            result.z = (mat.m[0][2] * source.x + mat.m[1][2] * source.y + mat.m[2][2] * source.z + mat.m[3][2]) / norm
        return result

    def TransformNormal(source, mat):
        from MatrixMath import Matrix
        result = Vector3.New()
        
        result.x = mat.m[0][0] * source.x + mat.m[1][0] * source.y + mat.m[2][0] * source.z
        result.y = mat.m[0][1] * source.x + mat.m[1][1] * source.y + mat.m[2][1] * source.z
        result.z = mat.m[0][2] * source.x + mat.m[1][2] * source.y + mat.m[2][2] * source.z
        return result;

    def Cross(pv1, pv2):
        result = Vector3.New()
        result.x = (pv1.y) * (pv2.z) - (pv1.z) * (pv2.y)
        result.y = (pv1.z) * (pv2.x) - (pv1.x) * (pv2.z)
        result.z = (pv1.x) * (pv2.y) - (pv1.y) * (pv2.x)
        return result;

    def Dot(lhs, rhs):
        return (lhs.x * rhs.x) + (lhs.y * rhs.y) + (lhs.z * rhs.z);
    

    def Maximize(lhs, rhs):
        result = Vector3(lhs)

        if lhs.x < rhs.x:
            result.x = rhs.x

        if lhs.y < rhs.y:
            result.y = rhs.y

        if lhs.z < rhs.z:
            result.z = rhs.z
        return result

    def Minimize(lhs, rhs):
        result = Vector3(rhs)

        if lhs.x < rhs.x:
            result.x = lhs.x

        if lhs.y < rhs.y:
            result.y = lhs.y

        if lhs.z < rhs.z:
            result.z = lhs.z
        return result
    
    

    def Catmullrom(pv0, pv1, pv2, pv3, s):
        result = Vector3.New()
        result.x = 0.5 * (2.0 * pv1.x + (pv2.x - pv0.x) * s + (2.0 * pv0.x - 5.0 * pv1.x + 4.0 * pv2.x - pv3.x) * s * s + (pv3.x - 3.0 * pv2.x + 3.0 * pv1.x - pv0.x) * s * s * s)
        result.y = 0.5 * (2.0 * pv1.y + (pv2.y - pv0.y) * s + (2.0 * pv0.y - 5.0 * pv1.y + 4.0 * pv2.y - pv3.y) * s * s + (pv3.y - 3.0 * pv2.y + 3.0 * pv1.y - pv0.y) * s * s * s)
        result.z = 0.5 * (2.0 * pv1.z + (pv2.z - pv0.z) * s + (2.0 * pv0.z - 5.0 * pv1.z + 4.0 * pv2.z - pv3.z) * s * s + (pv3.z - 3.0 * pv2.z + 3.0 * pv1.z - pv0.z) * s * s * s)
        return result

    def Hermite(pv1, pt1, pv2, pt2, s):
        result = Vector3.New()
        
        h1 = 2.0 * s * s * s - 3.0 * s * s + 1.0
        h2 = s * s * s - 2.0 * s * s + s
        h3 = -2.0 * s * s * s + 3.0 * s * s
        h4 = s * s * s - s * s
        
        result.x = h1 * (pv1.x) + h2 * (pt1.x) + h3 * (pv2.x) + h4 * (pt2.x)
        result.y = h1 * (pv1.y) + h2 * (pt1.y) + h3 * (pv2.y) + h4 * (pt2.y)
        result.z = h1 * (pv1.z) + h2 * (pt1.z) + h3 * (pv2.z) + h4 * (pt2.z)

        return result

    def Lerp(pv1, pv2, s):
        result = Vector3.New()
        result.x = (1 - s) * (pv1.x) + s * (pv2.x)
        result.y = (1 - s) * (pv1.y) + s * (pv2.y)
        result.z = (1 - s) * (pv1.z) + s * (pv2.z)
        return result

    def BaryCentric(pv1, pv2, pv3, f, g):
        result = Vector3.New()
        result.x = (1.0 - f - g) * (pv1.x) + f * (pv2.x) + g * (pv3.x)
        result.y = (1.0 - f - g) * (pv1.y) + f * (pv2.y) + g * (pv3.y)
        result.z = (1.0 - f - g) * (pv1.z) + f * (pv2.z) + g * (pv3.z)
        return result
    
    def Transform(pv, pm):
        from MatrixMath import Matrix
        from Vector4Math import Vector4
        result = Vector4.New()
        result.x = pm.m[0][0] * pv.x + pm.m[1][0] * pv.y + pm.m[2][0] * pv.z + pm.m[3][0]
        result.y = pm.m[0][1] * pv.x + pm.m[1][1] * pv.y + pm.m[2][1] * pv.z + pm.m[3][1]
        result.z = pm.m[0][2] * pv.x + pm.m[1][2] * pv.y + pm.m[2][2] * pv.z + pm.m[3][2]
        result.w = pm.m[0][3] * pv.x + pm.m[1][3] * pv.y + pm.m[2][3] * pv.z + pm.m[3][3]
        return result

    def __str__(self):
        return str(self.x) + "," + str(self.y) + "," + str(self.z)

    def ToString(self):
        return str(self.x) + "," + str(self.y) + "," + str(self.z)

    def FromString(self, s):
        if isinstance(s, bytes):
            vectorString = s.decode('utf-8')
        else:
            vectorString = s.encode().decode('utf-8')
        sp = vectorString.split(",")
        self.x = float(sp[0])
        self.y = float(sp[1])
        self.z = float(sp[2])

#main
#v3 = Vector3(1,1,1)
#Vector3.Scale(v3, 2)
#print(str(v3))

#v3.Scale(6)
#print(str(v3))

#print(str(v3.LengthSq()))

#from MatrixMath import Matrix
#v4= Vector3(0,0,1)
#mat = Matrix()
#mat.m[0][0] = 0.5
#mat.m[0][2] = 0.5
#mat.m[2][0] = 0.5
#mat.m[2][3] = 0.5

#v5 = v4.TransformNormal(mat)
#print(str(v4))
#print(str(v5))

#v10 = Vector3(1,0,0)
#v11 = Vector3(0,1,0)

#print("cross")
#print(str(v10.Cross(v11)))

#print("vec")
#v11 = Vector3(2,2,2)
#v12 = Vector3.New()
#print(str(v11))
#v12.x = 3
#print(str(v12))
#print(str(v11))





