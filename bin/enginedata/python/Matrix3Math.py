
import math
#용진

class Matrix3(object):

    def __init__(self, *args):
        if len(args) == 9:
            self.m = [[args[0], args[1], args[2]],[args[3], args[4], args[5]],[args[6], args[7], args[8]]]
        elif len(args) == 1:
            if isinstance(args[0], Matrix3):
                self.m = args[0].m
        else:
            self.m = [[1.0, 0.0, 0.0],[0.0, 1.0, 0.0],[0.0, 0.0, 1.0]]
        
    
    # A + B, A += B
    def __add__(self, v):
        return Matrix3(\
            self.m[0][0] + v.m[0][0], self.m[0][1] + v.m[0][1], self.m[0][2] + v.m[0][2], \
            self.m[1][0] + v.m[1][0], self.m[1][1] + v.m[1][1], self.m[1][2] + v.m[1][2], \
            self.m[2][0] + v.m[2][0], self.m[2][1] + v.m[2][1], self.m[2][2] + v.m[2][2])

    
    # A - B, A -= B
    def __sub__(self, v):
        return Matrix3(\
            self.m[0][0] - v.m[0][0], self.m[0][1] - v.m[0][1], self.m[0][2] - v.m[0][2], \
            self.m[1][0] - v.m[1][0], self.m[1][1] - v.m[1][1], self.m[1][2] - v.m[1][2], \
            self.m[2][0] - v.m[2][0], self.m[2][1] - v.m[2][1], self.m[2][2] - v.m[2][2])

    
    # A * 2, A * B, A *= 2, A *= B
    def __mul__(self, v):
        result = Matrix3.Identity() 
        if isinstance(v, Matrix3):
            for i in range(0,3):
                for j in range(0,3):
                    result.m[i][j] = self.m[i][0]* v.m[0][j] + self.m[i][1] * v.m[1][j] + self.m[i][2] * v.m[2][j]
            return result

        else:
            return Matrix3(\
            self.m[0][0] * v, self.m[0][1] * v, self.m[0][2] * v, \
            self.m[1][0] * v, self.m[1][1] * v, self.m[1][2] * v, \
            self.m[2][0] * v, self.m[2][1] * v, self.m[2][2] * v)
    
    # 2 * A, B * A
    def __rmul__(self, v): #
        result = Matrix3.Identity()
        if isinstance(v, Matrix3):
           for i in range(0,3):
               for j in range(0,3):
                   result.m[i][j] = v.m[i][0] * self.m[0][j] + v.m[i][1] * self.m[1][j] + v.m[i][2] * self.m[2][j]
           return result
        else:
            return Matrix3(\
            self.m[0][0] * v, self.m[0][1] * v, self.m[0][2] * v, \
            self.m[1][0] * v, self.m[1][1] * v, self.m[1][2] * v, \
            self.m[2][0] * v, self.m[2][1] * v, self.m[2][2] * v)
    
    # A / 2, A / B, A /= 2, A /= B
    def __truediv__(self, v):
        if isinstance(v, Matrix3):
            return Matrix3(\
            self.m[0][0] / v.m[0][0], self.m[0][1] / v.m[0][1], self.m[0][2] / v.m[0][2], \
            self.m[1][0] / v.m[1][0], self.m[1][1] / v.m[1][1], self.m[1][2] / v.m[1][2], \
            self.m[2][0] / v.m[2][0], self.m[2][1] / v.m[2][1], self.m[2][2] / v.m[2][2])
        else:
            return Matrix3(\
            self.m[0][0] / v, self.m[0][1] / v, self.m[0][2] / v, \
            self.m[1][0] / v, self.m[1][1] / v, self.m[1][2] / v, \
            self.m[2][0] / v, self.m[2][1] / v, self.m[2][2] / v)
    
    # A == B
    def __eq__(self, v):
        return \
            self.m[0][0] == v.m[0][0] and self.m[0][1] == v.m[0][1] and self.m[0][2] == v.m[0][2] and \
            self.m[1][0] == v.m[1][0] and self.m[1][1] == v.m[1][1] and self.m[1][2] == v.m[1][2] and \
            self.m[2][0] == v.m[2][0] and self.m[2][1] == v.m[2][1] and self.m[2][2] == v.m[2][2]

    # A != B
    def __ne__(self, v):
        return \
            self.m[0][0] != v.m[0][0] and self.m[0][1] != v.m[0][1] and self.m[0][2] != v.m[0][2] and \
            self.m[1][0] != v.m[1][0] and self.m[1][1] != v.m[1][1] and self.m[1][2] != v.m[1][2] and \
            self.m[2][0] != v.m[2][0] and self.m[2][1] != v.m[2][1] and self.m[2][2] != v.m[2][2]
    
    # for print
    def __str__(self):
        return \
            str(self.m[0][0]) + ", " + str(self.m[0][1]) + ", " + str(self.m[0][2]) + \
            str(self.m[1][0]) + ", " + str(self.m[1][1]) + ", " + str(self.m[1][2]) + \
            str(self.m[2][0]) + ", " + str(self.m[2][1]) + ", " + str(self.m[2][2]) 

    #working Function

    #determinent
    def Determinent(self):
       return \
           self.m[0][0] * (self.m[2][2] * self.m[1][1] - self.m[2][1] * self.m[1][2]) \
		- self.m[1][0] * (self.m[2][2] * self.m[0][1] - self.m[2][1] * self.m[0][2]) \
		+ self.m[2][0] * (self.m[1][2] * self.m[0][1] - self.m[1][1] * self.m[0][2])

    #Inverse
    def Inverse(self):
        result = Matrix3()
        det = Matrix3.Determinent(self);
        result.m[0][0] = self.m[2][2] * self.m[1][1] - self.m[2][1] * self.m[1][2]
        result.m[0][1] = -(self.m[2][2] * self.m[0][1] - self.m[2][1] * self.m[0][2])
        result.m[0][2] = self.m[1][2] * self.m[0][1] - self.m[1][1] * self.m[0][2]
        result.m[1][0] = -(self.m[2][2] * self.m[1][0] - self.m[2][0] * self.m[1][2])
        result.m[1][1] = self.m[2][2] * self.m[0][0] - self.m[2][0] * self.m[0][2]
        result.m[1][2] = -(self.m[1][2] * self.m[0][0] - self.m[1][0] * self.m[0][2])
        result.m[2][0] = self.m[2][1] * self.m[1][0] - self.m[2][0] * self.m[1][1]
        result.m[2][1] = -(self.m[2][1] * self.m[0][0] - self.m[2][0] * self.m[0][1])
        result.m[2][2] = self.m[1][1] * self.m[0][0] - self.m[1][0] * self.m[0][1] 
        
        result /= det 
        Matrix3.Copy(self,result)

        return


    #Transpose
    def Transpose(self):

        result = Matrix3.Identity()
        
        
        for i in range(0,3,1):
            for j in range(0,3,1):
                result.m[i][j] = self.m[j][i];
        Matrix3.Copy(self, result);

        return
        
    
    #IsIdentity       
    def IsIdentity(self):
        
        id = Matrix3.Identity()
        if self == id:
            return True
        else:
            return False


#//Static Function


    #Identity
    def Identity():
        
        return Matrix3(\
		 1.0,0.0,0.0,\
		 0.0,1.0,0.0,\
		 0.0,0.0,1.0)


    #Copy
    def Copy(dst, src):
        dst.m = src.m

        return
    
    #Rotation
    def Rotation(angle):
        result = Matrix3.Identity()
        result.m[0][0] = math.cos(angle);
        result.m[1][1] = result.m[0][0];
        result.m[0][1] = math.sin(angle);
        result.m[1][0] = -result.m[0][1]; 
        return result
    
    
    #Scaling
    def Scaling(sx, sy):
        result = Matrix3.Identity()
        result.m[0][0] = sx
        result.m[1][1] = sy
        return result

    #translation
    def Translation(x, y):
        result = Matrix3.Identity()
        result.m[2][0] = x
        result.m[2][1] = y
        return result



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
