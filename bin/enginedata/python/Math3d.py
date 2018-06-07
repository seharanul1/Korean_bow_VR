
from Matrix3Math import Matrix3
from ColorMath import Color
from MatrixMath import Matrix
from PlaneMath import Plane
from Vector2Math import Vector2
from Vector3Math import Vector3
from Vector4Math import Vector4
from QuaternionMath import Quaternion
from Util import Collision
from Util import Line
from Util import Polygon
from Util import MathUtil
from Util import PrimitiveMesh
from Util import EaseTypeCurve
from BoundingBoxMath import BoundingBox
from BoundingBox2DMath import BoundingBox2D
from FrustumMath import Frustum
from RectMath import Rect
from RangeMath import Range
from PointMath import Point

'''
class Vector2:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + "," + str(self.y)

    def ToString(self):
        return str(self.x) + "," + str(self.y)
        
    def FromString(self, s):
        sp = s.split(',')
        self.x = float(sp[0])
        self.y = float(sp[1])

class Vector3:
    
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return str(self.x) + "," + str(self.y) + "," + str(self.z)

    def ToString(self):
        return str(self.x) + "," + str(self.y) + "," + str(self.z)

    def FromString(self, s):
        sp = s.split(',')
        self.x = float(sp[0])
        self.y = float(sp[1])
        self.z = float(sp[2])

class Vector4:
    
    def __init__(self, x = 0, y = 0, z = 0, w = 0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __str__(self):
        return str(self.x) + "," + str(self.y) + "," + str(self.z) + "," + str(self.w)

    def ToString(self):
        return str(self.x) + "," + str(self.y) + "," + str(self.z) + "," + str(self.w)

    def FromString(self, s):
        sp = s.split(',')
        self.x = float(sp[0])
        self.y = float(sp[1])
        self.z = float(sp[2])
        self.w = float(sp[3])

class Quaternion:
    
    def __init__(self, x = 0, y = 0, z = 0, w = 0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __str__(self):
        return str(self.x) + "," + str(self.y) + "," + str(self.z) + "," + str(self.w)

    def ToString(self):
        return str(self.x) + "," + str(self.y) + "," + str(self.z) + "," + str(self.w)

    def FromString(self, s):
        sp = s.split(',')
        self.x = float(sp[0])
        self.y = float(sp[1])
        self.z = float(sp[2])
        self.w = float(sp[3])

class Color:
    
    def __init__(self, r = 0, g = 0, b = 0, a = 0):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __str__(self):
        return str(self.r) + "," + str(self.g) + "," + str(self.b) + "," + str(self.a)

    def ToString(self):
        return str(self.r) + "," + str(self.g) + "," + str(self.b) + "," + str(self.a)

    def FromString(self, s):
        sp = s.split(',')
        self.r = float(sp[0])
        self.g = float(sp[1])
        self.b = float(sp[2])
        self.a = float(sp[3])

class Plane:
    
    def __init__(self, a = 0, b = 0, c = 0, d = 0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self):
        return str(self.a) + "," + str(self.b) + "," + str(self.c) + "," + str(self.d)

    def ToString(self):
        return str(self.a) + "," + str(self.b) + "," + str(self.c) + "," + str(self.d)

    def FromString(self, s):
        sp = s.split(',')
        self.a = float(sp[0])
        self.b = float(sp[1])
        self.c = float(sp[2])
        self.d = float(sp[3])

class Matrix:

    def __init__(self, 
                 m11 = 1, m12 = 0, m13 = 0, m14 =0,
                 m21 = 0, m22 = 1, m23 = 0, m24 =0,
                 m31 = 0, m32 = 0, m33 = 1, m34 =0,
                 m41 = 0, m42 = 0, m43 = 0, m44 =1):
        self.m = [[m11, m12, m13, m14],[m21, m22, m23, m24],[m31, m32, m33, m34],[m41, m42, m43, m44]]


class Matrix3:

    def __init__(self, 
                 m11 = 1, m12 = 0, m13 = 0, 
                 m21 = 0, m22 = 1, m23 = 0, 
                 m31 = 0, m32 = 0, m33 = 1):
        self.m = [[m11, m12, m13],[m21, m22, m23],[m31, m32, m33]]
'''
