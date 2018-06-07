import math

class Plane(object):
    
    def __init__(self, *args):
        if len(args) == 4:
            self.a = args[0]
            self.b = args[1]
            self.c = args[2]
            self.d = args[3]
        elif len(args) == 1:
            if isinstance(args[0], Plane):
                self.a = args[0].a
                self.b = args[0].b
                self.c = args[0].c
                self.d = args[0].d
        else:
            self.a = 0.0
            self.b = 0.0
            self.c = 0.0
            self.d = 0.0
        
    # A + B, A += B
    def __add__(self, v):
        return Plane(self.a + v.a, self.b + v.b, self.c + v.c, self.d + v.d)

    # A - B, A -= B
    def __sub__(self, v):
        return Plane(self.a - v.a, self.b - v.b, self.c - v.c, self.d - v.d)
        
    # A == B
    def __eq__(self, v):
        return self.a == v.a and self.b == v.b and self.c == v.c and self.d == v.d

    # A != B
    def __ne__(self, v):
        return self.a != v.a or self.b != v.b or self.c != v.c or self.d != v.d

    # for print
    def __str__(self):
        return str(self.a) + ", " + str(self.b) + ", " + str(self.c) + ", " + str(self.d)

    def New():
        return Plane(0.0, 0.0, 0.0, 0.0)

    def Zero(self):
        self.a = 0.0
        self.b = 0.0
        self.c = 0.0
        self.d = 0.0

    def Length(self):
        return math.sqrt( (self.a * self.a) + (self.b * self.b) + (self.c * self.c) + (self.d * self.d) )
    
    def Normalize(self):
        norm = math.sqrtf(self.a * self.a + self.b * self.b + self.c * self.c);

        if norm != 0.0:
            self.a /= norm
            self.b /= norm
            self.c /= norm
            self.d /= norm
        else:
            self.Zero()

    def Transform(self, mat):
        return Plane.Transform(self, mat)

    def Transform(plane, mat):
        from MatrixMath import Matrix
        result = Plane.New()
        result.a = mat.m[0][0] * plane.a + mat.m[1][0] * plane.b + mat.m[2][0] * plane.c + mat.m[3][0] * plane.d
        result.b = mat.m[0][1] * plane.a + mat.m[1][1] * plane.b + mat.m[2][1] * plane.c + mat.m[3][1] * plane.d
        result.c = mat.m[0][2] * plane.a + mat.m[1][2] * plane.b + mat.m[2][2] * plane.c + mat.m[3][2] * plane.d
        result.d = mat.m[0][3] * plane.a + mat.m[1][3] * plane.b + mat.m[2][3] * plane.c + mat.m[3][3] * plane.d
        return result

    def TransformPlane(self, mat):
        Plane.TransformPlane(self, mat)

    def TransformPlane(plane, mat):
        from Vector3Math import Vector3
        from Vector4Math import Vector4
        from MatrixMath import Matrix
        o = Vector4(plane.a * plane.d, plane.b * plane.d, plane.c * plane.d, 1.0)
        n = (plane.a , plane.b , plane.c , 0.0)
        o.Transform(mat)
        
        mati = Matrix(mat)
        mati.Inverse()
        mat.Transpose()

        n.Transform(mati)

        on = Vector3(o.x, o.y, o.z)
        nn = Vector3(n.x, n.y, n.z)

        return Plane(n.x, n.y, n.z, on.Dot(nn))



    def Dot(self, sourcePlane):
        Plane.Dot(self, sourcePlane)

    def Dot(plane, sourcePlane):
        return plane.a * sourcePlane.a + plane.b * sourcePlane.b + plane.c * sourcePlane.c + plane.d * sourcePlane.d;


    def DotCoord(self, sourcePlane):
        Plane.DotCoord(self, sourcePlane)

    def DotCoord(plane, sourcePlane):
        return ((plane.a) * (sourcePlane.x) + (plane.b) * (sourcePlane.y) + (plane.c) * (sourcePlane.z) + (plane.d));

    def DotNormal(self, sourcePlane):
        Plane.DotNormal(self, sourcePlane)

    def DotNormal(plane, sourcePlane):
        return ((plane.a) * (sourcePlane.x) + (plane.b) * (sourcePlane.y) + (plane.c) * (sourcePlane.z));

    def PlaneIntersectLine(self, p1, p2):
        from Vector3Math import Vector3

        normal = Vector3(self.a, self.b, self.c)
        direction = p2 - p1
        dotVal = Vector3.Dot(normal, direction)

        if dotVal == 0.0:
            return -1

        temp = (self.d + Vector3.Dot(normal, p1)) / dot

        result = Vector3.New()
        result.x = p1.x - temp * direction.x
        result.y = p1.y - temp * direction.y
        result.z = p1.z - temp * direction.z

        return result

    def Translation(self, pos):
        from Vector3Math import Vector3
        result = Plane.New()
        result.a = self.a
        result.b = self.b
        result.c = self.c
        result.d = -result.a * pos.x - result.b * pos.y - result.c * pos.z
        return result

    def ProjectPoint(self, point):
        from Vector3Math import Vector3
        
        dist = DistanceFromPoint(point)
        normal = Vector3(self.a, self.b, self.c)
        normal.Normalize()

        return point - dist * normal	

    def DistanceFromPoint(self, point):
        from Vector3Math import Vector3

        normal = Vector3(self.a, self.b, self.c );
        normal.Normalize();

        return point.Dot(normal) + self.d;


    def PlaneFromPointNormal(sourcePoint, sourceNormal):
        from Vector3Math import Vector3

        result = Plane.New()
        result.a = sourceNormal.x
        result.b = sourceNormal.y
        result.c = sourceNormal.z
        result.d = -Vector3.Dot(sourcePoint, sourceNormal)
        return result
    
    def PlaneFromPoints(pv1, pv2, pv3):
        from Vector3Math import Vector3
        result = Plane.New()

        edge1 = pv2 - pv1
        edge2 = pv3 - pv1
        normal = Vector3.Cross(edge1, edge2)
        normal.Normalize()
        result = Plane.PlaneFromPointNormal(pv1, normal)
        return result


    def __str__(self):
        return str(self.a) + "," + str(self.b) + "," + str(self.c) + "," + str(self.d)

    def ToString(self):
        return str(self.a) + "," + str(self.b) + "," + str(self.c) + "," + str(self.d)

    def FromString(self, s):
        if isinstance(s, bytes):
            vectorString = s.decode('utf-8')
        else:
            vectorString = s.encode().decode('utf-8')
        sp = PlaneString.split(",")
        self.a = float(sp[0])
        self.b = float(sp[1])
        self.c = float(sp[2])
        self.d = float(sp[3])