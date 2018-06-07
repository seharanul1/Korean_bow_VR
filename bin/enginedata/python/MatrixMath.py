
import math
#용진

class Matrix(object):

    def __init__(self, *args):
        if len(args) == 16:
            self.m = [[args[0], args[1], args[2], args[3]],[args[4], args[5], args[6], args[7]],[args[8], args[9], args[10], args[11]],[args[12], args[13], args[14], args[15]]]
        elif len(args) == 1:
            if isinstance(args[0], Matrix):
                self.m = args[0].m
        else:
            self.m = [[1.0, 0.0, 0.0, 0.0],[0.0, 1.0, 0.0, 0.0],[0.0, 0.0, 1.0, 0.0],[0.0, 0.0, 0.0, 1.0]]
        
    
    # A + B, A += B
    def __add__(self, v):
        return Matrix(\
            self.m[0][0] + v.m[0][0], self.m[0][1] + v.m[0][1], self.m[0][2] + v.m[0][2], self.m[0][3] + v.m[0][3], \
            self.m[1][0] + v.m[1][0], self.m[1][1] + v.m[1][1], self.m[1][2] + v.m[1][2], self.m[1][3] + v.m[1][3], \
            self.m[2][0] + v.m[2][0], self.m[2][1] + v.m[2][1], self.m[2][2] + v.m[2][2], self.m[2][3] + v.m[2][3], \
            self.m[3][0] + v.m[3][0], self.m[3][1] + v.m[3][1], self.m[3][2] + v.m[3][2], self.m[3][3] + v.m[3][3])
    
    # A - B, A -= B
    def __sub__(self, v):
        return Matrix(\
            self.m[0][0] - v.m[0][0], self.m[0][1] - v.m[0][1], self.m[0][2] - v.m[0][2], self.m[0][3] - v.m[0][3], \
            self.m[1][0] - v.m[1][0], self.m[1][1] - v.m[1][1], self.m[1][2] - v.m[1][2], self.m[1][3] - v.m[1][3], \
            self.m[2][0] - v.m[2][0], self.m[2][1] - v.m[2][1], self.m[2][2] - v.m[2][2], self.m[2][3] - v.m[2][3], \
            self.m[3][0] - v.m[3][0], self.m[3][1] - v.m[3][1], self.m[3][2] - v.m[3][2], self.m[3][3] - v.m[3][3])
    
    # A * 2, A * B, A *= 2, A *= B
    def __mul__(self, v): 
        result = Matrix.Identity()
        if isinstance(v, Matrix):
            for i in range(0,4):
              for j in range(0,4):
                 result.m[i][j] = self.m[i][0] * v.m[0][j] + self.m[i][1] * v.m[1][j]+ self.m[i][2] * v.m[2][j] + self.m[i][3] * v.m[3][j];
            return result                                              
        else:
            return Matrix(\
            self.m[0][0] * v, self.m[0][1] * v, self.m[0][2] * v, self.m[0][3] * v, \
            self.m[1][0] * v, self.m[1][1] * v, self.m[1][2] * v, self.m[1][3] * v, \
            self.m[2][0] * v, self.m[2][1] * v, self.m[2][2] * v, self.m[2][3] * v, \
            self.m[3][0] * v, self.m[3][1] * v, self.m[3][2] * v, self.m[3][3] * v)

    
    # 2 * A, B * A
    def __rmul__(self, v):  
        result = Matrix.Identity()
        if isinstance(v, Matrix):
            for i in range(0,4):
              for j in range(0,4):
                 result.m[i][j] = v.m[i][0] * self.m[0][j] + v.m[i][1] * self.m[1][j]+ v.m[i][2] * self.m[2][j] + v.m[i][3] * self.m[3][j];                                                                   
            return result 
        else:
            return Matrix(\
            self.m[0][0] * v, self.m[0][1] * v, self.m[0][2] * v, self.m[0][3] * v, \
            self.m[1][0] * v, self.m[1][1] * v, self.m[1][2] * v, self.m[1][3] * v, \
            self.m[2][0] * v, self.m[2][1] * v, self.m[2][2] * v, self.m[2][3] * v, \
            self.m[3][0] * v, self.m[3][1] * v, self.m[3][2] * v, self.m[3][3] * v)
    
    # A / 2, A / B, A /= 2, A /= B
    def __truediv__(self, v):
        if isinstance(v, Matrix):
            return Matrix(\
            self.m[0][0] / v.m[0][0], self.m[0][1] / v.m[0][1], self.m[0][2] / v.m[0][2], self.m[0][3] / v.m[0][3], \
            self.m[1][0] / v.m[1][0], self.m[1][1] / v.m[1][1], self.m[1][2] / v.m[1][2], self.m[1][3] / v.m[1][3], \
            self.m[2][0] / v.m[2][0], self.m[2][1] / v.m[2][1], self.m[2][2] / v.m[2][2], self.m[2][3] / v.m[2][3], \
            self.m[3][0] / v.m[3][0], self.m[3][1] / v.m[3][1], self.m[3][2] / v.m[3][2], self.m[3][3] / v.m[3][3])
        else:
            return Matrix(\
            self.m[0][0] / v, self.m[0][1] / v, self.m[0][2] / v, self.m[0][3] / v, \
            self.m[1][0] / v, self.m[1][1] / v, self.m[1][2] / v, self.m[1][3] / v, \
            self.m[2][0] / v, self.m[2][1] / v, self.m[2][2] / v, self.m[2][3] / v, \
            self.m[3][0] / v, self.m[3][1] / v, self.m[3][2] / v, self.m[3][3] / v)
    
    # A == B
    def __eq__(self, v):
        return \
            self.m[0][0] == v.m[0][0] and self.m[0][1] == v.m[0][1] and self.m[0][2] == v.m[0][2] and self.m[0][3] == v.m[0][3] and \
            self.m[1][0] == v.m[1][0] and self.m[1][1] == v.m[1][1] and self.m[1][2] == v.m[1][2] and self.m[1][3] == v.m[1][3] and \
            self.m[2][0] == v.m[2][0] and self.m[2][1] == v.m[2][1] and self.m[2][2] == v.m[2][2] and self.m[2][3] == v.m[2][3] and \
            self.m[3][0] == v.m[3][0] and self.m[3][1] == v.m[3][1] and self.m[3][2] == v.m[3][2] and self.m[3][3] == v.m[3][3]

    # A != B
    def __ne__(self, v):
        return \
            self.m[0][0] != v.m[0][0] and self.m[0][1] != v.m[0][1] and self.m[0][2] != v.m[0][2] and self.m[0][3] != v.m[0][3] and \
            self.m[1][0] != v.m[1][0] and self.m[1][1] != v.m[1][1] and self.m[1][2] != v.m[1][2] and self.m[1][3] != v.m[1][3] and \
            self.m[2][0] != v.m[2][0] and self.m[2][1] != v.m[2][1] and self.m[2][2] != v.m[2][2] and self.m[2][3] != v.m[2][3] and \
            self.m[3][0] != v.m[3][0] and self.m[3][1] != v.m[3][1] and self.m[3][2] != v.m[3][2] and self.m[3][3] != v.m[3][3]
    
    # for print
    def __str__(self):
        return \
            str(self.m[0][0]) + ", " + str(self.m[0][1]) + ", " + str(self.m[0][2]) + ", " + str(self.m[0][3]) + \
            str(self.m[1][0]) + ", " + str(self.m[1][1]) + ", " + str(self.m[1][2]) + ", " + str(self.m[1][3]) + \
            str(self.m[2][0]) + ", " + str(self.m[2][1]) + ", " + str(self.m[2][2]) + ", " + str(self.m[2][3]) + \
            str(self.m[3][0]) + ", " + str(self.m[3][1]) + ", " + str(self.m[3][2]) + ", " + str(self.m[3][3])
    
    def Determinent(self):
        from Vector4Math import Vector4
        minor = Vector4()
        v1 = Vector4()
        v2 = Vector4()
        v3 = Vector4()
        det = float()
        
        v1.x = self.m[0][0]
        v1.y = self.m[1][0]
        v1.z = self.m[2][0]
        v1.w = self.m[3][0]
        v2.x = self.m[0][1]
        v2.y = self.m[1][1]
        v2.z = self.m[2][1]
        v2.w = self.m[3][1]
        v3.x = self.m[0][2]
        v3.y = self.m[1][2]
        v3.z = self.m[2][2]
        v3.w = self.m[3][2]
        minor = Vector4.Cross(v1, v2, v3)
        det = -(self.m[0][3] * minor.x + self.m[1][3] * minor.y + self.m[2][3] * minor.z + self.m[3][3] * minor.w)
        return det


    def DecomposeMatrix(self, destPos, destRotation, Scale):
        from Vector3Math import Vector3
        from QuaternionMath import Quaternion
        destPos.x = self.m[3][0]
        destPos.y = self.m[3][1]
        destPos.z = self.m[3][2]
        self.m[3][0] = 0
        self.m[3][1] = 0
        self.m[3][2] = 0
        Scale.x = math.sqrt(self.m[0][0] * self.m[0][0] + self.m[1][0] * self.m[1][0] + self.m[2][0] * self.m[2][0])
        Scale.y = math.sqrt(self.m[0][1] * self.m[0][1] + self.m[1][1] * self.m[1][1] + self.m[2][1] * self.m[2][1])
        Scale.z = math.sqrt(self.m[0][2] * self.m[0][2] + self.m[1][2] * self.m[1][2] + self.m[2][2] * self.m[2][2])

        if Scale.x == 0.0 or Scale.y == 0.0 or Scale.z == 0.0 :
            return false
        self.m[0][0] /= Scale.x   
        self.m[1][0] /= Scale.x   
        self.m[2][0] /= Scale.x  
        self.m[0][1] /= Scale.y   
        self.m[1][1] /= Scale.y   
        self.m[2][1] /= Scale.y  
        self.m[0][2] /= Scale.z   
 
        self.m[1][2] /= Scale.z   
        self.m[2][2] /= Scale.z   
        self.m[0][3] = 0          
        self.m[1][3] = 0         
        self.m[2][3] = 0         
        self.m[3][3] = 1
        
        Rotation = Quaternion.RotationMatrix(self)
        return True


    #static function

    def Identity():
        
        return Matrix(
		1.0, 0.0, 0.0, 0.0,\
		0.0, 1.0, 0.0, 0.0,\
		0.0, 0.0, 1.0, 0.0,\
		0.0, 0.0, 0.0, 1.0) 

    def Copy(dst , src):
        dst.m = src.m
        
        return

    def Transpose(self):
        result = Matrix.Identity()
        for i in range(0,4,1):
            for j in range(0,4,1):
                result.m[i][j] = self.m[j][i];
                Matrix.Copy(self, result);

     
    def LookAtLH(peye0, pat, pup):
        from Vector3Math import Vector3
        peye = peye0;
        result = Matrix.Identity()
        right = Vector3()
        up = Vector3() 
        vec = Vector3()
        vec= pat - peye
        vec.Normalize()
        right = Vector3.Cross(pup, vec)
        
        up = Vector3.Cross(vec, right)
        right.Normalize()
        up.Normalize()
        
        result.m[0][0] = right.x
        result.m[1][0] = right.y
        result.m[2][0] = right.z
        result.m[3][0] = -right.Dot(peye)
        
        result.m[0][1] = up.x
        result.m[1][1] = up.y
        result.m[2][1] = up.z
        result.m[3][1] = -up.Dot(peye)

        result.m[0][2] = vec.x
        result.m[1][2] = vec.y
        result.m[2][2] = vec.z
        result.m[3][2] = -vec.Dot(peye)
        
        result.m[0][3] = 0.0
        result.m[1][3] = 0.0
        result.m[2][3] = 0.0
        result.m[3][3] = 1.0
        
        return result
    
    def LookAtRH(peye, pat, pup):
        from Vector3Math import Vector3
        result = Matrix.Identity()
        right = Vector3()
        up = Vector3()
        vec = Vector3()
        vec2 = Vector3()

        vec = pat - peye
        vec.Normalize()
        right = Vector3.Cross(pup, vec)
        up = Vector3.Cross(vec, right)
        right.Normalize()
        up.Normalize()

        result.m[0][0] = -right.x
        result.m[1][0] = -right.y
        result.m[2][0] = -right.z
        result.m[3][0] = right.Dot(peye)
        
        result.m[0][1] = up.x
        result.m[1][1] = up.y
        result.m[2][1] = up.z
        result.m[3][1] = -up.Dot(peye)
        
        result.m[0][2] = -vec.x
        result.m[1][2] = -vec.y
        result.m[2][2] = -vec.z
        result.m[3][2] = vec.Dot(peye)
        
        result.m[0][3] = 0.0
        result.m[1][3] = 0.0
        result.m[2][3] = 0.0
        result.m[3][3] = 1.0
        return result
    
    def MultiplyTranspose(pm1, pm2): 
        result = pm1 * pm2
        result.Transpose()
        return result
    
    def OrthoLH(w, h, zn, zf):
        result = Matrix.Identity()
        result.m[0][0] = 2.0 / w
        result.m[1][1] = 2.0 / h
        result.m[2][2] = 1.0 / (zf - zn)
        result.m[3][2] = zn / (zn - zf)
        return result
    
    def OrthoOffCenterLH(l, r, b, t, zn, zf):
        result = Matrix.Identity()
        result.m[0][0] = 2.0 / (r - l)
        result.m[1][1] = 2.0 / (t - b)
        result.m[2][2] = 1.0 / (zf - zn)
        result.m[3][0] = -1.0 - 2.0 * l / (r - l)
        result.m[3][1] = 1.0 + 2.0 * t / (b - t)
        result.m[3][2] = zn / (zn - zf)
        return result;

    def OrthoOffCenterRH(l, r, b, t, zn, zf):
        
        result = Matrix.Identity()
        result.m[0][0] = 2.0/ (r - l)
        result.m[1][1] = 2.0 / (t - b)
        result.m[2][2] = 1.0/ (zn - zf)
        result.m[3][0] = -1.0 - 2.0 * l / (r - l)
        result.m[3][1] = 1.0 + 2.0 * t / (b - t)
        result.m[3][2] = zn / (zn - zf)
        return result
    
    def OrthoRH(w, h, zn, zf):
        result = Matrix.Identity()
        result.m[0][0] = 2.0 / w
        result.m[1][1] = 2.0 / h
        result.m[2][2] = 1.0 / (zn - zf)
        result.m[3][2] = zn / (zn - zf)
        return result
    
    def PerspectiveFovLH(fovy, aspect, zn, zf):
        result = Matrix.Identity()
        result.m[0][0] = 1.0 / (aspect * math.tan(fovy / 2.0))
        result.m[1][1] = 1.0 / math.tan(fovy / 2.0)
        result.m[2][2] = zf / (zf - zn)
        result.m[2][3] = 1.0
        result.m[3][2] = (zf * zn) / (zn - zf)
        result.m[3][3] = 0.0
        return result
    
    def PerspectiveFovRH(fovy, aspect, zn, zf):
        result = Matrix.Identity()
        result.m[0][0] = 1.0 / (aspect * math.tan(fovy / 2.0))
        result.m[1][1] = 1.0 / math.tan(fovy / 2.0)
        result.m[2][2] = zf / (zn - zf)
        result.m[2][3] = -1.0
        result.m[3][2] = (zf * zn) / (zn - zf)
        result.m[3][3] = 0.0
        return result
    
    def PerspectiveLH(w, h, zn, zf):

        result = Matrix.Identity()
        result.m[0][0] = 2.0 * zn / w
        result.m[1][1] = 2.0 * zn / h
        result.m[2][2] = zf / (zf - zn)
        result.m[3][2] = (zn * zf) / (zn - zf)
        result.m[2][3] = 1.0
        result.m[3][3] = 0.0
        return result
    
    def PerspectiveOffCenterLH(l, r, b, t, zn, zf):
        result = Matrix.Identity()
        result.m[0][0] = 2.0 * zn / (r - l)
        result.m[1][1] = -2.0 * zn / (b - t)
        result.m[2][0] = -1.0 - 2.0 * l / (r - l)
        result.m[2][1] = 1.0 + 2.0 * t / (b - t)
        result.m[2][2] = -zf / (zn - zf)
        result.m[3][2] = (zn * zf) / (zn - zf)
        result.m[2][3] = 1.0
        result.m[3][3] = 0.0
        return result
    
    def PerspectiveOffCenterRH(l, r, b, t, zn, zf):
        result = Matrix.Identity()
        result.m[0][0] = 2.0 * zn / (r - l)
        result.m[1][1] = -2.0 * zn / (b - t)
        result.m[2][0] = 1.0 + 2.0 * l / (r - l)
        result.m[2][1] = -1.0 - 2.0 * t / (b - t)
        result.m[2][2] = zf / (zn - zf)
        result.m[3][2] = (zn * zf) / (zn - zf)
        result.m[2][3] = -1.0
        result.m[3][3] = 0.0
        return result

    def PerspectiveRH(w, h, zn, zf):
        result = Matrix.Identity()
        result.m[0][0] = 2.0 * zn / w
        result.m[1][1] = 2.0 * zn / h
        result.m[2][2] = zf / (zn - zf)
        result.m[3][2] = (zn * zf) / (zn - zf)
        result.m[2][3] = -1.0
        result.m[3][3] = 0.0
        return result
    
    def Reflect(pplane):

        from PlaneMath import Plane
        result = Matrix.Identity()
        Nplane = Plane(pplane)
        Nplane.Normalize()
        result.m[0][0] = 1.0 - 2.0 * Nplane.a * Nplane.a
        result.m[0][1] = -2.0 * Nplane.a * Nplane.b
        result.m[0][2] = -2.0 * Nplane.a * Nplane.c
        result.m[1][0] = -2.0 * Nplane.a * Nplane.b
        result.m[1][1] = 1.0 - 2.0 * Nplane.b * Nplane.b
        result.m[1][2] = -2.0 * Nplane.b * Nplane.c
        result.m[2][0] = -2.0 * Nplane.c * Nplane.a
        result.m[2][1] = -2.0 * Nplane.c * Nplane.b
        result.m[2][ 2] = 1.0 - 2.0 * Nplane.c * Nplane.c
        result.m[3][0] = -2.0 * Nplane.d * Nplane.a
        result.m[3][1] = -2.0 * Nplane.d * Nplane.b
        result.m[3][2] = -2.0 * Nplane.d * Nplane.c
        return result
    
    def RotationAxis(pv, angle):
        result = Matrix.Identity()
        from Vector3Math import Vector3
        v = Vector3(pv)
        v.Normalize()
        
        cosangle = math.cos(angle)
        sinangle = math.sin(angle)
        result.m[0][0] = (1.0 - cosangle) * v.x * v.x + cosangle
        result.m[1][0] = (1.0 - cosangle) * v.x * v.y - sinangle * v.z
        result.m[2][0] = (1.0 - cosangle) * v.x * v.z + sinangle * v.y
        result.m[0][1] = (1.0 - cosangle) * v.y * v.x + sinangle * v.z
        result.m[1][1] = (1.0 - cosangle) * v.y * v.y + cosangle
        result.m[2][1] = (1.0 - cosangle) * v.y * v.z - sinangle * v.x
        result.m[0][2] = (1.0 - cosangle) * v.z * v.x - sinangle * v.y
        result.m[1][2] = (1.0 - cosangle) * v.z * v.y + sinangle * v.x
        result.m[2][2] = (1.0 - cosangle) * v.z * v.z + cosangle
        return result
    
    def RotationQuaternion(pq):
        from QuaternionMath import Quaternion
        result = Matrix.Identity()
        result.m[0][0] = 1.0 - 2.0 * (pq.y * pq.y + pq.z * pq.z)
        result.m[0][1] = 2.0 * (pq.x * pq.y + pq.z * pq.w)
        result.m[0][2] = 2.0 * (pq.x * pq.z - pq.y * pq.w)
        result.m[1][0] = 2.0 * (pq.x * pq.y - pq.z * pq.w)
        result.m[1][1] = 1.0 - 2.0 * (pq.x * pq.x + pq.z * pq.z)
        result.m[1][2] = 2.0 * (pq.y * pq.z + pq.x * pq.w)
        result.m[2][0] = 2.0 * (pq.x * pq.z + pq.y * pq.w)
        result.m[2][1] = 2.0 * (pq.y * pq.z - pq.x * pq.w)
        result.m[2][2] = 1.0 - 2.0 * (pq.x * pq.x + pq.y * pq.y)
        return result
    
    def RotationX(angle):
        result = Matrix.Identity()
        result.m[1][1] = math.cos(angle)
        result.m[2][2] = result.m[1][1]
        result.m[1][2] = math.sin(angle)
        result.m[2][1] = -result.m[1][2]
        return result

    def RotationY(angle):
        result = Matrix.Identity()
        result.m[0][0] = math.cos(angle)
        result.m[2][2] = result.m[0][0]
        result.m[2][0] = math.sin(angle)
        result.m[0][2] = -result.m[2][0]
        return result
    
    def RotationZ(angle):
        result = Matrix.Identity()
        result.m[0][0] = math.cos(angle)
        result.m[1][1] = result.m[0][0]
        result.m[0][1] = math.sin(angle)
        result.m[1][0] = -result.m[0][1]
        return result

    def RotationYawPitchRoll(yaw, pitch, roll):
        result = Matrix.Identity()
        m = Matrix.Identity()
        m = Matrix.RotationZ(roll)
        
        result = m
        m = Matrix.RotationX(pitch)
        result = result * m

        m = Matrix.RotationY(yaw)
        result = result * m

        return result
    
    def Scaling(sx, sy, sz):
        result = Matrix.Identity()
        result.m[0][0] = sx
        result.m[1][1] = sy
        result.m[2][2] = sz
        return result
    
    def Translation(sx, sy, sz):
        result = Matrix.Identity()
        result.m[3][0] = sx
        result.m[3][1] = sy
        result.m[3][2] = sz
        return result
    
    
    def Shadow(plight, pplane):
        result = Matrix.Identity()
        Nplane = Plane(pplane)
        dot = float()
        from Vector4Math import Vector4
        Nplane.Normalize()
        dot = Nplane.Dot(plight)
        result.m[0][0] = dot - Nplane.a * plight.x
        result.m[0][1] = -Nplane.a * plight.y
        result.m[0][ 2] = -Nplane.a * plight.z
        result.m[0][3] = -Nplane.a * plight.w
        result.m[1][0] = -Nplane.b * plight.x
        result.m[1][1] = dot - Nplane.b * plight.y
        result.m[1][2] = -Nplane.b * plight.z
        result.m[1][3] = -Nplane.b * plight.w
        result.m[2][0] = -Nplane.c * plight.x
        result.m[2][1] = -Nplane.c * plight.y
        result.m[2][2] = dot - Nplane.c * plight.z
        result.m[2][3] = -Nplane.c * plight.w
        result.m[3][0] = -Nplane.d * plight.x
        result.m[3][1] = -Nplane.d * plight.y
        result.m[3][2] = -Nplane.d * plight.z
        result.m[3][3] = dot - Nplane.d * plight.w
        return result
    
    
    
    def Transformation(scalingCenter, scalingRotation, 
							  scaling, rotationCenter,
							  rotation, translation):
        
        
        from Vector3Math import Vector3
        from QuaternionMath import Quaternion
        
        A = Matrix(Matrix.Translation(-scalingCenter.x , -scalingCenter.y, -scalingCenter.z))
        B = Matrix(Matrix.Scaling(scaling.x, scaling.y,scaling.z))
        C = Matrix(Matrix.RotationQuaternion(scalingRotation))
        u = Vector3(scalingCenter - rotationCenter)
        D = Matrix(Matrix.Translation(u.x, u.y, u.z))
        E = Matrix(Matrix.RotationQuaternion(rotation))
        v = Vector3(rotationCenter + translation)
        F = Matrix(Matrix.Translation(v.x, v.y , v.z))
        Ctranspose = Matrix(C)
        Ctranspose.Transpose()
        result = Matrix( A * Ctranspose * B * C * D * E * F)
        return result
    
    def AffineTransformation(scaling, rotationcenter, rotation, translation):
        from Vector3Math import Vector3
        from QuaternionMath import Quaternion
        
        result = Matrix()
        #Matrix m1, m2, m3, m4, m5;
        
        m1 = Matrix.Scaling(scaling, scaling, scaling)
        m2 = Matrix.Translation( -rotationcenter.x, -rotationcenter.y, -rotationcenter.z)
        m4 = Matrix.Translation( rotationcenter.x, rotationcenter.y, rotationcenter.z)
        m3 = Matrix.RotationQuaternion(rotation)
        m5 = Matrix.Translation( translation.x, translation.y, translation.z)
        
        return m1 * m2 * m3 * m4 * m5
    
    def CoordTransformMatrix(xaxis, yaxis, zaxis):
        from Vector3Math import Vector3
        mat = Matrix()
        mat.m[0][0] = xaxis.x
        mat.m[1][0] = xaxis.y
        mat.m[2][0] = xaxis.z
        mat.m[3][0] = 0

        mat.m[0][1] = yaxis.x
        mat.m[1][1] = yaxis.y
        mat.m[2][1] = yaxis.z
        mat.m[3][1] = 0
        
        mat.m[0][2] = zaxis.x
        mat.m[1][2] = zaxis.y
        mat.m[2][2] = zaxis.z
        mat.m[3][2] = 0

        mat.m[0][3] = 0
        mat.m[1][3] = 0
        mat.m[2][3] = 0
        mat.m[3][3] = 1
        
        return mat

    def TransformMatrix(scale, rotate, translate ):
        from Vector3Math import Vector3
        from QuaternionMath import Quaternion
        s = Matrix.Scaling(scale.x, scale.y, scale.z )
        rot = Matrix.RotationQuaternion( rotate )
        transform = s * rot  
        transform.m[3][0] = translate.x
        transform.m[3][1] = translate.y
        transform.m[3][2] = translate.z
        return transform

    def New():
        return Matrix(1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1)


#def LookAt(dir, pos):
    
#    from Vector3Math import Vector3
#    result = Matrix()
	
#    #direction 방향이 +z .. 상이 y 좌우가 x LH 방식
#    userWorldMatrix = Matrix()
#	if !Util::IsNormalToolSmall(dir.x) | !Util::IsNormalToolSmall(dir.z)):
        
#        up = Vector3(0,1,0)
#		target = Vector3(pos + dir)
#		userWorldMatrix = LookAtLH(pos, target, up)
	
#	else:
#		up = Vector3(1, 0, 0)
#		target = Vector3(pos + dir)
#        userWorldMatrix = LookAtLH(pos, target, up)
#        return userWorldMatrix


