
import math
#용진

class Quaternion(object):
    
    def __init__(self, *args):
        if len(args) == 4:
            self.x = args[0]
            self.y = args[1]
            self.z = args[2]
            self.w = args[3]
        elif len(args) == 1:
            if isinstance(args[0], Quaternion):
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
        return Quaternion(self.x + v.x, self.y + v.y, self.z + v.z, self.w + v.w)

    # A - B, A -= B
    def __sub__(self, v):
        return Quaternion(self.x - v.x, self.y - v.y, self.z - v.z, self.w - v.w)
    
    # A * 2, A * B, A *= 2, A *= B
    def __mul__(self, v): 
        if isinstance(v, Quaternion):
            return Quaternion(self.x * v.x, self.y * v.y, self.z * v.z, self.w * v.w)
        else:
            return Quaternion(self.x * v, self.y * v, self.z * v, self.w * v)

    # 2 * A, B * A
    def __rmul__(self, v): # 
        if isinstance(v, Quaternion):
            return Quaternion(self.x * v.x, self.y * v.y, self.z * v.z, self.w * v.w)
        else:
            return Quaternion(self.x * v, self.y * v, self.z * v, self.w * v)

    # A / 2, A / B, A /= 2, A /= B
    def __truediv__(self, v):
        if isinstance(v, Quaternion):
            return Quaternion(self.x / v.x, self.y / v.y, self.z / v.z, self.w / v.w)
        else:
            return Quaternion(self.x / v, self.y / v, self.z / v, self.w / v)
        
    # A == B
    def __eq__(self, v):
        return self.x == v.x and self.y == v.y and self.z == v.z and self.w == v.w

    # A != B
    def __ne__(self, v):
        return self.x != v.x or self.y != v.y or self.z != v.z or self.w != v.w

    # for print
    def __str__(self):
        return str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ", " + str(self.w)
    
    
    def EulerDegreeToQuaternionFloat(Euler):
        from Vector3Math import Vector3
        v = Vector3()
        result = Quaternion()
        v.x = Quaternion.DegreeToRadian(Euler.x)
        v.y = Quaternion.DegreeToRadian(Euler.y)
        v.z = Quaternion.DegreeToRadian(Euler.z)
        return result.EulerToQuaternionFloat(v)
    
    def QuaternionToEulerDegreeFloat(quat):
        from Vector3Math import Vector3
        v = Vector3()
        result = Quaternion()
        v = result.QuaternionToEulerFloat(quat)
        v.x = Quaternion.RadianToDegree(v.x)
        v.y = Quaternion.RadianToDegree(v.y)
        v.z = Quaternion.RadianToDegree(v.z)
        return v

   ##########member func################

    def EulerToQuaternionFloat(self,euler):
        cosx2 = math.cos(euler.x / 2.0)
        sinx2 = math.sin(euler.x / 2.0)
        siny2 = math.sin(euler.y / 2.0)
        cosy2 = math.cos(euler.y / 2.0)
        sinz2 = math.sin(euler.z / 2.0)
        cosz2 = math.cos(euler.z / 2.0)
        
        x = siny2 * cosx2 * sinz2 + cosy2 * sinx2 * cosz2
        y = siny2 * cosx2 * cosz2 - cosy2 * sinx2 * sinz2
        z = cosy2 * cosx2 * sinz2 - siny2 * sinx2 * cosz2
        w = cosy2 * cosx2 * cosz2 + siny2 * sinx2 * sinz2
        
        r = Quaternion(x, y, z, w)

        return r

    def QuaternionToEulerFloat(self,quat):
        from Vector3Math import Vector3
        result = Vector3()
        q0 = quat.w
        q1 = quat.y
        q2 = quat.x
        q3 = quat.z
    
        result.x = math.asin(2.0 * (q0 * q2 - q3 * q1))
        result.y = math.atan2(2.0 * (q0 * q1 + q2 * q3), 1 - 2.0 * (math.pow(q1, 2) + math.pow(q2, 2)))
        result.z = math.atan2(2.0 * (q0 * q3 + q1 * q2), 1 - 2.0 * (math.pow(q2, 2) + math.pow(q3, 2)))
    
        if result.x < 0:
            result.x = 2.0 * math.pi + result.x
        
        if result.y < 0:
            result.y = 2.0 * math.pi + result.y
        
        if result.z < 0:
            result.z = 2.0 * math.pi + result.z
        
        return result
    
    def Inverse(self):
        result = Quaternion.Identity()
        norm = self.LengthSq()
        if norm == 0.0:
            result.x = 0.0
            result.y = 0.0
            result.z = 0.0
            result.w = 0.0
            
        else:
            result.x = -x / norm
            result.y = -y / norm
            result.z = -z / norm
            result.w = w / norm
            
        self = result
        
        return
    
    def Exp(self): 
        result = Quaternion.Identity()
        norm = self.Inverse()
        norm = math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        if norm != 0.0:
            sinnorm = math.sin(norm)
            cosnorm = math.cos(norm)
            result.x = sinnorm * self.x / norm
            result.y = sinnorm * self.y / norm
            result.z = sinnorm * self.z / norm
            result.w = cosnorm

        else:
            result.x = 0.0
            result.y = 0.0
            result.z = 0.0
            result.w = 1.0
            
        return result


    def Log(self):
        result = Quaternion.Identity()
        a = math.acos(self.w)
        sina = math.sin(a)
    
        result.w = 0.0
        if (sina > 0.0):
            result.x = a*self.x / sina
            result.y = a*self.y / sina
            result.z = a*self.z / sina
        
        else: 
            result.x = 0.0
            result.y = 0.0
            result.z = 0.0

        return result
    

    
    #return type bool
    def IsIdentity(self):
        return ((self.x == 0.0) and (self.y == 0.0) and (self.z == 0.0) and (self.w == 1.0))
    
    #return type float
    def Length(self):
        return math.sqrt((self.x) * (self.x)+(self.y) * (self.y)+(self.z) * (self.z)+(self.w) * (self.w))
    
    def LengthSq(self):
        return self.x * self.x + self.y * self.y + self.z * self.z + self.w * self.w
    
    
    #return type void
    def Scale(self,Rate):
        x = Rate * x
        y = Rate * y
        z = Rate * z
        w = Rate * w
        return  

   
    def Normalize(self):
        
        norm = float()
        norm = self.Length()
        if (norm == 0.0):
            self.x = 0.0
            self.y = 0.0
            self.z = 0.0
            self.w = 0.0

        else:
            self.x = self.x / norm
            self.y = self.y / norm
            self.z = self.z / norm
            self.w = self.w / norm

        return 	

    def ToAxisAngle(self,paxis, pangle):
    
        norm = float()
    
        pangle = 0.0
        norm = self.Length()
        if norm != 0:
            paxis.x = self.x / norm
            paxis.y = self.y / norm
            paxis.z = self.z / norm
            if (math.fabs(self.w) <= 1.0) :
                pangle = 2.0 * math.acos(self.w)
        else:
            paxis.x = 1.0
            paxis.y = 0.0
            paxis.z = 0.0

        return



    ###############3#static func################33
    
    def DegreeToRadian(degree):
        return degree * (3.14159265358979323846 / 180.0)
    
    def RadianToDegree(radian):
        return (radian) * (180.0 / 3.14159265358979323846)

    def Identity():
        return Quaternion(0.0, 0.0, 0.0, 1.0)
    
    def BaryCentric(pq1, pq2, pq3, f, g):
        return Quaternion.Slerp(Quaternion.Slerp(pq1, pq2, f + g), Quaternion.Slerp(pq1, pq3, f + g), g / (f + g))
    
    def Conjugate(pq):
        result = Quaternion.Identity()
        result.x = -pq.x
        result.y = -pq.y
        result.z = -pq.z
        result.w = pq.w
        return result
    
    def EulerToQuaternion(euler):
        c1 = math.cos(euler.y / 2.0)
        s1 = math.sin(euler.y / 2.0)
        c2 = math.cos(euler.z / 2.0)
        s2 = math.sin(euler.z / 2.0)
        c3 = math.cos(euler.x / 2.0)
        s3 = math.sin(euler.x / 2.0)
        c1c2 = c1 * c2
        s1s2 = s1 * s2
        w = c1c2*c3 - s1s2*s3
        x = c1c2*s3 + s1s2*c3
        y = s1*c2*c3 + c1*s2*s3
        z = c1*s2*c3 - s1*c2*s3
        
        r = Quaternion(x, y, z, w)
        r.Normalize()
        return r
    
    def Cross(pq1, pq2, pq3):
        result = Quaternion.Identity()
        result.x = pq1.y * (pq2.z * pq3.w - pq3.z * pq2.w) - pq1.z * (pq2.y * pq3.w - pq3.y * pq2.w) + pq1.w * (pq2.y * pq3.z - pq2.z * pq3.y)
        result.y = -(pq1.x * (pq2.z * pq3.w - pq3.z * pq2.w) - pq1.z * (pq2.x * pq3.w - pq3.x * pq2.w) + pq1.w * (pq2.x * pq3.z - pq3.x * pq2.z))
        result.z = pq1.x * (pq2.y * pq3.w - pq3.y * pq2.w) - pq1.y * (pq2.x * pq3.w - pq3.x * pq2.w) + pq1.w * (pq2.x * pq3.y - pq3.x * pq2.y)
        result.w = -(pq1.x * (pq2.y * pq3.z - pq3.y * pq2.z) - pq1.y * (pq2.x * pq3.z - pq3.x * pq2.z) + pq1.z * (pq2.x * pq3.y - pq3.x * pq2.y))
        return result
    
    def Dot(pq1, pq2):
        return pq1.x * pq2.x + pq1.y * pq2.y + pq1.z * pq2.z + pq1.w * pq2.w
    
    def Max(Lhs, Rhs):
        if Lhs>=Rhs:
            return Lhs
        else:
            return Rhs

    def Min(Lhs, Rhs):
        if Lhs<=Rhs:
            return Lhs
        else:
            return Rhs   

    def Maximize(Lhs, Rhs):
        return Quaternion(\
            Quaternion.Max(Lhs.x,Rhs.x),\
            Quaternion.Max(Lhs.y,Rhs.y),\
            Quaternion.Max(Lhs.z,Rhs.z),\
            Quaternion.Max(Lhs.w,Rhs.w)
            )
    
    
    def Minimize(Lhs, Rhs):
        return Quaternion(\
            Quaternion.Min(Lhs.x, Rhs.x),\
            Quaternion.Min(Lhs.x, Rhs.x),\
            Quaternion.Min(Lhs.x, Rhs.x),\
            Quaternion.Min(Lhs.x, Rhs.x)
            )
    
    def RotationAxis(pv, angle):

        from Vector3Math import Vector3
         
        result = Quaternion.Identity()
        temp = Vector3(pv)
        temp.Normalize()
        sinangle2 = math.sin(angle / 2.0)
        cosangle2 = math.cos(angle / 2.0)
        result.x = sinangle2 * temp.x
        result.y = sinangle2 * temp.y
        result.z = sinangle2 * temp.z
        result.w = cosangle2
        return result
    
    def RotationMatrix(pm):
        result = Quaternion.Identity()
        maxi = int()
        maxdiag = float()
        S = float()
        trace = pm.m[0][0] + pm.m[1][1] + pm.m[2][2] + 1.0
        if (trace > 1.0):
            result.x = (pm.m[1][2] - pm.m[2][1]) / (2.0 * math.sqrt(trace))
            result.y = (pm.m[2][0] - pm.m[0][2]) / (2.0 * math.sqrt(trace))
            result.z = (pm.m[0][1] - pm.m[1][0]) / (2.0 * math.sqrt(trace))
            result.w = math.sqrt(trace) / 2.0
            return result
        
        maxi = 0
        maxdiag = pm.m[0][0]
        
        for i in range(1,3,1):
            if (pm.m[i][i] > maxdiag):
                maxi = i
                maxdiag = pm.m[i][i]
                
                
        if maxi==0:
            S = 2.0 * math.sqrt(1.0 + pm.m[0][0] - pm.m[1][1] - pm.m[2][2])
            result.x = 0.25 * S
            result.y = (pm.m[0][1] + pm.m[1][0]) / S
            result.z = (pm.m[0][2] + pm.m[2][0]) / S
            result.w = (pm.m[1][2] - pm.m[2][1]) / S
            return result

        elif maxi==1:
            S = 2.0 * math.sqrt(1.0 + pm.m[1][1] - pm.m[0][0] - pm.m[2][2])
            result.x = (pm.m[0][1] + pm.m[1][0]) / S
            result.y = 0.25 * S
            result.z = (pm.m[1][2] + pm.m[2][1]) / S
            result.w = (pm.m[2][0] - pm.m[0][2]) / S
            return result

        elif maxi==2:
            S = 2.0 * math.sqrt(1.0 + pm.m[2][2] - pm.m[0][0] - pm.m[1][1])
            result.x = (pm.m[0][2] + pm.m[2][0]) / S
            result.y = (pm.m[1][2] + pm.m[2][1]) / S
            result.z = 0.25 * S
            result.w = (pm.m[0][1] - pm.m[1][0]) / S
            return result
        
        return result
    
    
    def RotationYawPitchRoll(yaw, pitch, roll):
        result = Quaternion.Identity()
        cospitch2 = math.cos(pitch / 2.0)
        sinpitch2 = math.sin(pitch / 2.0)
        sinyaw2 = math.sin(yaw / 2.0)
        cosyaw2 = math.sin(yaw / 2.0)
        sinroll2 = math.sin(roll / 2.0)
        cosroll2 = math.cos(roll / 2.0)
        result.x = sinyaw2 * cospitch2 * sinroll2 + cosyaw2 * sinpitch2 * cosroll2
        result.y = sinyaw2 * cospitch2 * cosroll2 - cosyaw2 * sinpitch2 * sinroll2
        result.z = cosyaw2 * cospitch2 * sinroll2 - sinyaw2 * sinpitch2 * cosroll2
        result.w = cosyaw2 * cospitch2 * cosroll2 + sinyaw2 * sinpitch2 * sinroll2
        return result
    
    
    def Slerp(pq1, pq2, t):
        result = Quaternion.Identity()
        epsilon = 1.0
        temp = 1.0 - t
        u = t
        dot = Quaternion.Dot(pq1, pq2)
        if (dot < 0.0):
            epsilon = -1.0
            dot = -dot

        if (1.0 - dot > 0.001):
            theta = math.acos(dot)
            temp = math.sin(theta * temp) / math.sin(theta)
            u = math.sin(theta * u) / math.sin(theta)

        result.x = temp * pq1.x + epsilon * u * pq2.x
        result.y = temp * pq1.y + epsilon * u * pq2.y
        result.z = temp * pq1.z + epsilon * u * pq2.z
        result.w = temp * pq1.w + epsilon * u * pq2.w
        result.Normalize()
        return result
    
    
    def Squad(pq1, pq2, pq3, pq4, t):
        result = Quaternion.Identity()
        result = Quaternion.Slerp(Quaternion.Slerp(pq1, pq4, t), Quaternion.Slerp(pq2, pq3, t), 2.0 * t * (1.0 - t))
        return result
    
    
    def Scale(source, Rate):
        
        result = Quaternion()
        result.x = Rate * (source.x)
        result.y = Rate * (source.y)
        result.z = Rate * (source.z)
        result.w = Rate * (source.w)
        return result


    def __str__(self):
        return str(self.x) + "," + str(self.y) + "," + str(self.z) + "," + str(self.w)

    def ToString(self):
        return str(self.x) + "," + str(self.y) + "," + str(self.z) + "," + str(self.w)

    def FromString(self, s):
        if isinstance(s, bytes):
            QuaternionString = s.decode('utf-8')
        else:
            QuaternionString = s.encode().decode('utf-8')
        sp = QuaternionString.split(",")
        self.x = float(sp[0])
        self.y = float(sp[1])
        self.z = float(sp[2])
        self.w = float(sp[3])



