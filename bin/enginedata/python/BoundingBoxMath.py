import math

class BoundingBox(object):
    
    def __init__(self, *args):
        from Vector3Math import Vector3
        from MatrixMath import Matrix

        self.UseTransform = False
        self.TransformMatrix = Matrix.New()
        self.TransformMatrixInverse = Matrix.New()

        if len(args) == 6:
            self.Vertex = [Vector3(args[0], args[1], args[2]), Vector3(args[3], args[4], args[5])]
        elif len(args) == 1:
            if isinstance(args[0], BoundingBox):
                self.Vertex = [Vector3(args[0].Vertex[0]), Vector3(args[0].Vertex[1])]
                self.UseTransform = args[0].UseTransform
                self.TransformMatrix = args[0].TransformMatrix
                self.TransformMatrixInverse = args[0].TransformMatrixInverse
        elif len(args) == 2:
            if isinstance(args[0], Vector3) and isinstance(args[1], Vector3):
                self.Vertex = [args[0], args[1]]
        else:
            self.Vertex = [Vector3(1.7976931348623157e+308, 1.7976931348623157e+308, 1.7976931348623157e+308), Vector3(-1.7976931348623157e+308, -1.7976931348623157e+308, -1.7976931348623157e+308)]
       
    # A * 2, A * B, A *= 2, A *= B
    def __mul__(self, mat):
        b = BoundingBox(self)
        if b.IsNotEmpty() == True:
            b.Transform(mat)
        return b

    # 2 * A, B * A
    def __rmul__(self, mat): # 
        b = BoundingBox(self)
        if b.IsNotEmpty() == True:
            b.Transform(mat)
        return b

    # A == B
    def __eq__(self, v):
        return self.Vertex[0] == v.Vertex[0] and self.Vertex[1] == v.Vertex[1] and ((UseTransform == False and v.UseTransform == False) or (TransformMatrix and v.TransformMatrix))

    # A != B
    def __ne__(self, v):
        return self.Vertex[0] == v.Vertex[0] or self.Vertex[1] == v.Vertex[1] or ((UseTransform != False and v.UseTransform != False) or (TransformMatrix or v.TransformMatrix))

    # for print
    def __str__(self):
        return str(self.Vertex[0].x) + ", " + str(self.Vertex[0].y) + ", " + str(self.Vertex[0].z) + ", " + str(self.Vertex[1].x) + ", " + str(self.Vertex[1].y) + ", " + str(self.Vertex[1].z)

    def New():
        return BoundingBox(1.7976931348623157e+308, 1.7976931348623157e+308, 1.7976931348623157e+308, -1.7976931348623157e+308, -1.7976931348623157e+308, -1.7976931348623157e+308)

    def Zero(self):
        self.Vertex = [Vector3.New(), Vector3.New()]
        self.UseTransform = False
        self.TransformMatrix = Matrix.New()
        self.TransformMatrixInverse = Matrix.New()

    def __str__(self):
        return str(self.Vertex[0].x) + "," + str(self.Vertex[0].y) + "," + str(self.Vertex[1].x) + "," + str(self.Vertex[1].y)

    def FromString(self, s):
        from Vector3Math import Vector3
        from MatrixMath import Matrix

        if isinstance(s, bytes):
            vectorString = s.decode('utf-8')
        else:
            vectorString = s.encode().decode('utf-8')
        sp = vectorString.split(",")
        self.Vertex = [Vector3(float(sp[0]), float(sp[1]), float(sp[2])), Vector3(float(sp[3]), float(sp[4]), float(sp[5]))]

    def HasVolume(self):
        return self.Vertex[1].x > self.Vertex[0].x and self.Vertex[1].y > self.Vertex[0].y and self.Vertex[1].z > self.Vertex[1].z

    def IsNotEmpty(self):
        return self.Vertex[1].x >= self.Vertex[0].x and self.Vertex[1].y >= self.Vertex[0].y and self.Vertex[1].z >= self.Vertex[1].z

    def ToLocalNormal(self, normal):
        from Vector3Math import Vector3
        n = Vector3(normal)
        if self.UseTransform:
            n.TransformNormal(self.TransformMatrixInverse)
        return n

    def ToLocal(self, source):
        from Vector3Math import Vector3
        from MatrixMath import Matrix

        if isinstance(source, Vector3):
            p = Vector3(pos)
            if UseTransform:
                p.TransformCoord(self.TransformMatrixInverse)
            return p
        elif isinstance(source, BoundingBox):
            usemat = True
            if source.UseTransform and self.UseTransform:
                mat = self.TransformMatrixInverse * source.TransformMatrix
            else:
                if source.UseTransform:
                    mat = source.TransformMatrix
                else:
                    if self.UseTransform:
                        mat = TransformMatrixInverse
                    else:
                        usemat = False
        if usemat:
            source.Transform(mat)
        else:
            res = BoundingBox(source)
            
        return res
    
    def ToWorld(self, pos):
        from Vector3Math import Vector3
        p = Vector3(pos)
        if self.UseTransform:
            p.TransformCoord(self.TransformMatrix)
        return p




    def Cover(self, *args):
        from Vector3Math import Vector3

        if len(args) == 1:
            if isinstance(args[0], BoundingBox):
                sbox = ToLocal(args[0])

                if self.Vertex[0].x > sbox.Vertex[0].x:
                    self.Vertex[0].x = sbox.Vertex[0].x
                
                if self.Vertex[0].y > sbox.Vertex[0].y:
                    self.Vertex[0].y = sbox.Vertex[0].y

                if self.Vertex[0].z > sbox.Vertex[0].z:
                    self.Vertex[0].z = sbox.Vertex[0].z
                
                if self.Vertex[1].x < sbox.Vertex[1].x:
                    
                    self.Vertex[1].x = sbox.Vertex[1].x
                
                if self.Vertex[1].y > sbox.Vertex[1].y:
                    self.Vertex[1].y = sbox.Vertex[1].y

                if self.Vertex[1].z < sbox.Vertex[1].z:
                    self.Vertex[1].z = sbox.Vertex[1].z

            elif isinstance(args[0], Vector3):
                
                if self.Vertex[0].x > self.Vertex[1].x:
                    self.Vertex[0] = Vector3(args[0])
                    self.Vertex[1] = Vector3(args[0])
                else:
                    self.Cover(args[0].x, args[0].y, args[0].z)

        elif len(args) == 3:
            if(self.Vertex[0] > x):
                self.Vertex[0].x = x

            if(self.Vertex[1] < x):
                self.Vertex[1].x = x

            if(self.Vertex[0] > y):
                self.Vertex[0].y = y

            if(self.Vertex[1] < y):
                self.Vertex[1].y = y

            if(self.Vertex[0] > z):
                self.Vertex[0].z = z

            if(self.Vertex[1] < z):
                self.Vertex[1].z = z


    def Intersect(self, box):

        sbox = ToLocal(box)

        if self.Vertex[0].x < sbox.Vertex[0].x:
            self.Vertex[0].x = sbox.Vertex[0].x
        if self.Vertex[1].x > sbox.Vertex[1].x:
            self.Vertex[1].x = sbox.Vertex[1].x
        
        if self.Vertex[0].y < sbox.Vertex[0].y:
            self.Vertex[0].y = sbox.Vertex[0].y

        if self.Vertex[1].y > sbox.Vertex[1].y:
            self.Vertex[1].y = sbox.Vertex[1].y
        
        if self.Vertex[0].z < sbox.Vertex[0].z:
            self.Vertex[0].z = sbox.Vertex[0].z
            
        if (self.Vertex[1].z > sbox.Vertex[1].z):
            self.Vertex[1].z = sbox.Vertex[1].z

    def GetDiagonal(self):
        if self.UseTransform == False:
            return self.Vertex[1] - self.Vertex[0]
        else:
            return ToWorld(self.Vertex[1]) - ToWorld(self.Vertex[0])

    def GetDiagonalLength(self):
        return GetDiagonal().Length()

    def GetCenter(self):
        return ToWorld(self.Vertex[0] - self.Vertex[1] * 0.5)

    def GetVolumeSize(self):
        from Vector3Math import Vector3
        if self.UseTransform:
            return (self.Vertex[1].x - self.Vertex[0].x) * (self.Vertex[1].y - self.Vertex[0].y) * (self.Vertex[1].z - self.Vertex[0].z)
        else:
            v0 = ToWorld(self.Vertex[0])
            v1 = ToWorld(self.Vertex[1])
            return (v1.x - v0.x) * (v1.y - v0.y) * (v1.z - v0.z)

    def GetPlaneSize(self, plane):
        #//int Plane; // 0 xz  1 zy  2 xy
        if plane == 0:#  // xz
            return (self.Vertex[1].x - self.Vertex[0].x) * (self.Vertex[1].z - self.Vertex[0].z)
        else:
            if plane == 1: # // zy
                return (self.Vertex[1].y - self.Vertex[0].y) * (self.Vertex[1].z - self.Vertex[0].z)
            else: #// xy
                return (self.Vertex[1].x - self.Vertex[0].x) * (self.Vertex[1].y - self.Vertex[0].y)

    def GetVertices(self):
        from Vector3Math import Vector3
        v = [Vector3(self.Vertex[0].x, self.Vertex[0].y, self.Vertex[0].z),\
            Vector3(self.Vertex[1].x, self.Vertex[0].y, self.Vertex[0].z),\
            Vector3(self.Vertex[0].x, self.Vertex[1].y, self.Vertex[0].z),\
            Vector3(self.Vertex[1].x, self.Vertex[1].y, self.Vertex[0].z),\
            Vector3(self.Vertex[0].x, self.Vertex[0].y, self.Vertex[1].z),\
            Vector3(self.Vertex[1].x, self.Vertex[0].y, self.Vertex[1].z),\
            Vector3(self.Vertex[0].x, self.Vertex[1].y, self.Vertex[1].z),\
            Vector3(self.Vertex[1].x, self.Vertex[1].y, self.Vertex[1].z)]
        
        if self.UseTransform:
            for i in range(0, 8):
                v[i] = ToWorld(v[i])

        return v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7]

    def Transform(self, mat):
        from Vector3Math import Vector3
        v0, v1, v2, v3, v4, v5, v6, v7 = self.GetVertices()

        v = [v0, v1, v2, v3, v4, v5, v6, v7]

        box = BoundingBox.New()

        for i in range(0,8):
            nv = Vector3(v[i].TransformCoord(mat))
            v[i] = Vector3(nv)
            box.Cover(nv)

        self.Vertex[0] = box.Vertex[0]
        self.Vertex[1] = box.Vertex[1]

        return box, v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7]



    def MultiplySize(self, rate):
        line = self.Vertex[1] - self.Vertex[0]
        line2 = line * ((rate - 1) * 0.5)

        self.Vertex[0] -= line2
        self.Vertex[1] += line2

    def Inflate(self, *args):
        
        if len(args) == 1:
            if(args[0] > 0):
                self.Vertex[0].x -= args[0]
                self.Vertex[0].y -= args[0]
                self.Vertex[0].z -= args[0]
                self.Vertex[1].x += args[0]
                self.Vertex[1].y += args[0]
                self.Vertex[1].z += args[0]
            else:
                if v != 0:
                    self.Vertex[0].x -= args[0]
                    self.Vertex[0].y -= args[0]
                    self.Vertex[0].z -= args[0]
                    self.Vertex[1].x += args[0]
                    self.Vertex[1].y += args[0]
                    self.Vertex[1].z += args[0]

                    if self.Vertex[0].x > self.Vertex[1].x:
                        self.Vertex[0].x = (self.Vertex[0].x + self.Vertex[1].x) / 2
                        self.Vertex[1].x = self.Vertex[0].x

                    if self.Vertex[0].y > self.Vertex[1].y:
                        self.Vertex[0].y = (self.Vertex[0].y + self.Vertex[1].y) / 2
                        self.Vertex[1].y = self.Vertex[0].y

                    if self.Vertex[0].z > self.Vertex[1].z:
                        self.Vertex[0].z = (self.Vertex[0].z + self.Vertex[1].z) / 2
                        self.Vertex[1].z = self.Vertex[0].z

        elif len(args) == 3:
            self.Vertex[0].x -= args[0]
            self.Vertex[0].y -= args[1]
            self.Vertex[0].z -= args[2]
            self.Vertex[1].x += args[0]
            self.Vertex[1].y += args[1]
            self.Vertex[1].z += args[2]


    def CheckPlaneX(self, x):
        if self.Vertex[0].x > x:
            return 1
        if self.Vertex[1].x < x:
            return -1
        return 0

    def CheckPlaneY(self, y):
        if self.Vertex[0].y > y:
            return 1
        if self.Vertex[1].y < y:
            return -1
        return 0

    def CheckPlaneZ(self, z):
        if self.Vertex[0].z > z:
            return 1
        if self.Vertex[1].z < z:
            return -1
        return 0



    def CheckCollide(self, target):
        self.Intersect(target)
        return self.HasVolume()

    def CheckContact(self, target):
        self.Intersect(target)
        return self.IsNotEmpty()

    def ChekcInclude(self, source):
        from Vector3Math import Vector3
        if isinstance(source, BoundingBox):
            if self.UseTransform == False and source.UseTransform == False:
                return self.Vertex[0].x <= source.Vertex[0].x and\
                self.Vertex[0].y <= source.Vertex[0].y and\
                self.Vertex[0].z <= source.Vertex[0].z and\
                self.Vertex[1].x >= source.Vertex[1].x and\
                self.Vertex[1].y >= source.Vertex[1].y and\
                self.Vertex[1].z >= source.Vertex[1].z
            else:
                nBox = ToLocal(source)
                return self.Vertex[0].x <= nBox.Vertex[0].x and\
                self.Vertex[0].y <= nBox.Vertex[0].y and\
                self.Vertex[0].z <= nBox.Vertex[0].z and\
                self.Vertex[1].x >= nBox.Vertex[1].x and\
                self.Vertex[1].y >= nBox.Vertex[1].y and\
                self.Vertex[1].z >= nBox.Vertex[1].z
        elif isinstance(source, Vector3):
            nv = ToLocal(source)
            
            return self.Vertex[0].x <= nv.x and\
                self.Vertex[0].y <= nv.y and\
                self.Vertex[0].z <= nv.z and\
                self.Vertex[1].x >= nv.x and\
                self.Vertex[1].y >= nv.y and\
                self.Vertex[1].z >= nv.z

    def FindNearCollision(self, posfrom0, posto0):
        from Vector3Math import Vector3
        from Util import Collision
        from PlaneMath import Plane

        posfrom = ToLocal(posfrom0)
        posto = ToLocal(posto0)
        
        planex0 = Plane(1, 0, 0, -self.Vertex[0].x)
        planex1 = Plane(1, 0, 0, -self.Vertex[1].x)
        planey0 = Plane(0, 1, 0, -self.Vertex[0].y)
        planey1 = Plane(0, 1, 0, -self.Vertex[1].y)
        planez0 = Plane(0, 0, 1, -self.Vertex[0].z)
        planez1 = Plane(0, 0, 1, -self.Vertex[1].z)
        
        intersection = Vector3.New()
        minDist = 1.7976931348623157e+308
        minIntersect = Vector3.New()
        collide = False

        colCheck, intersection = Collision.PlaneLineIntersectionFast(planex0, posfrom, posto)

        if colCheck:
            if (intersection.y >= self.Vertex[0].y and intersection.y <= self.Vertex[1].y) and (intersection.z >= self.Vertex[0].z and intersection.z <= self.Vertex[1].z):
                intersectionWorld = ToWorld(intersection)
                distv = intersectionWorld - posfrom0
                dist = distv.LengthSq()
                minIntersect = intersectionWorld
                collide = True
                minDist = dist


        colCheck, intersection = Collision.PlaneLineIntersectionFast(planex1, posfrom, posto)
        
        if colCheck:
            if ((intersection.y >= self.Vertex[0].y and intersection.y <= self.Vertex[1].y) and (intersection.z >= self.Vertex[0].z and intersection.z <= self.Vertex[1].z)):
                intersectionWorld = ToWorld(intersection)
                distv = intersectionWorld - posfrom0
                dist = distv.LengthSq()
                if collide == False or dist < minDist:
                    collide = True
                    minIntersect = intersectionWorld
                    minDist = dist

        colCheck, intersection = Collision.PlaneLineIntersectionFast(planey0, posfrom, posto)

        if colCheck:
            if ((intersection.x >= self.Vertex[0].x and intersection.x <= self.Vertex[1].x) and (intersection.z >= self.Vertex[0].z and intersection.z <= self.Vertex[1].z)):
                intersectionWorld = ToWorld(intersection)
                distv = intersectionWorld - posfrom0
                dist = distv.LengthSq()
                if collide == False or dist < minDist:
                    collide = True
                    minIntersect = intersectionWorld
                    minDist = dist

        colCheck, intersection = Collision.PlaneLineIntersectionFast(planey1, posfrom, posto)
        
        if colCheck:
            if ((intersection.x >= self.Vertex[0].x and intersection.x <= self.Vertex[1].x) and (intersection.z >= self.Vertex[0].z and intersection.z <= self.Vertex[1].z)):
                intersectionWorld = ToWorld(intersection)
                distv = intersectionWorld - posfrom0
                dist = distv.LengthSq()
                if collide == False or dist < minDist:
                    collide = True
                    minIntersect = intersectionWorld
                    minDist = dist

        colCheck, intersection = Collision.PlaneLineIntersectionFast(planez0, posfrom, posto)

        if colCheck:
            if ((intersection.x >= self.Vertex[0].x and intersection.x <= self.Vertex[1].x) and (intersection.y >= self.Vertex[0].y and intersection.y <= self.Vertex[1].y)):
                intersectionWorld = ToWorld(intersection)
                distv = intersectionWorld - posfrom0
                dist = distv.LengthSq()
                
                if collide == False or dist < minDist:
                    collide = True
                    minIntersect = intersectionWorld
                    minDist = dist

        colCheck, intersection = Collision.PlaneLineIntersectionFast(planez1, posfrom, posto)

        if colCheck:
            if ((intersection.x >= self.Vertex[0].x and intersection.x <= self.Vertex[1].x) and (intersection.y >= self.Vertex[0].y and intersection.y <= self.Vertex[1].y)):
                intersectionWorld = ToWorld(intersection)
                distv = intersectionWorld - posfrom0
                dist = distv.LengthSq()

                if collide == False or dist < minDist:
                    collide = True
                    minIntersect = intersectionWorld
                    minDist = dist
                    
        if collide:
            return True, minIntersect, minDist
        
        return False, Vector3.New(), 0


    def GetPlane(self):
        from PlaneMath import Plane
        boxplane = [Plane(1, 0, 0, self.Vertex[1].x), Plane(1, 0, 0, self.Vertex[0].x), Plane(0, 1, 0, self.Vertex[1].y),\
            Plane(0, 1, 0, self.Vertex[0].y), Plane(0, 0, 1, self.Vertex[1].z), Plane(0, 0, 1, self.Vertex[0].z)]

        if self.UseTransform:
            for i in range(0, 6):
                boxplane[i].TransformPlane(self.TransformMatrix)

        return boxplane[0], boxplane[1], boxplane[2], boxplane[3], boxplane[4], boxplane[5]

    def InBox(self, Hit, B1, B2,Axis):
        if Axis == 1 and Hit.z > B1.z and Hit.z < B2.z and Hit.y > B1.y and Hit.y < B2.y:
            return True
        if Axis == 2 and Hit.z > B1.z and Hit.z < B2.z and Hit.x > B1.x and Hit.x < B2.x:
            return True
        if Axis == 3 and Hit.x > B1.x and Hit.x < B2.x and Hit.y > B1.y and Hit.y < B2.y:
            return True
        return False
    
    def GetLineIntersection(fDst1, fDst2, P1, P2):
        if (fDst1 * fDst2) >= 0:
            return False, Vector3.New()
        if fDst1 == fDst2:
            return False, Vector3.New()
        intersect = P1 + (P2 - P1) * (-fDst1 / (fDst2 - fDst1))
        return True, intersect

    def GetLineIntersect(sefl, pos0, pos1):
        intersect = Vector3.New()
        if pos1.x < self.Vertex[0].x and pos0.x < self.Vertex[0].x:
            return False
        if (pos1.x > self.Vertex[1].x and pos0.x > self.Vertex[1].x):
            return False
        if (pos1.y < self.Vertex[0].y and pos0.y < self.Vertex[0].y):
            return False
        if (pos1.y > self.Vertex[1].y and pos0.y > self.Vertex[1].y):
            return False
        if (pos1.z < self.Vertex[0].z and pos0.z < self.Vertex[0].z):
            return False
        if (pos1.z > self.Vertex[1].z and pos0.z > self.Vertex[1].z):
            return False
        
        if pos0.x > self.Vertex[0].x and pos0.x < self.Vertex[1].x and pos0.y > self.Vertex[0].y and pos0.y < self.Vertex[1].y and pos0.z > self.Vertex[0].z and pos0.z < self.Vertex[1].z:
            intersect = pos0
            return True, intersect
        
        if (GetLineIntersection(pos0.x - self.Vertex[0].x, pos1.x - self.Vertex[0].x, pos0, pos1, intersect) and InBox(intersect, self.Vertex[0], self.Vertex[1], 1)) or\
            (GetLineIntersection(pos0.y - self.Vertex[0].y, pos1.y - self.Vertex[0].y, pos0, pos1, intersect) and InBox(intersect, self.Vertex[0], self.Vertex[1], 2)) or\
            (GetLineIntersection(pos0.z - self.Vertex[0].z, pos1.z - self.Vertex[0].z, pos0, pos1, intersect) and InBox(intersect, self.Vertex[0], self.Vertex[1], 3)) or\
            (GetLineIntersection(pos0.x - self.Vertex[1].x, pos1.x - self.Vertex[1].x, pos0, pos1, intersect) and InBox(intersect, self.Vertex[0], self.Vertex[1], 1)) or\
            (GetLineIntersection(pos0.y - self.Vertex[1].y, pos1.y - self.Vertex[1].y, pos0, pos1, intersect) and InBox(intersect, self.Vertex[0], self.Vertex[1], 2)) or\
            (GetLineIntersection(pos0.z - self.Vertex[1].z, pos1.z - self.Vertex[1].z, pos0, pos1, intersect) and InBox(intersect, self.Vertex[0], self.Vertex[1], 3)):
            return True, intersect
        
        return False, intersect
    
    # OBB
    # 충돌시 True, 비충돌시 False 반환
    def OBBIntersect(self, arg):
        from Vector3Math import Vector3



        PointsA = [Vector3.New(), Vector3.New(), Vector3.New(), Vector3.New(), Vector3.New(), Vector3.New(), Vector3.New(), Vector3.New()]
        PointsB = [Vector3.New(), Vector3.New(), Vector3.New(), Vector3.New(), Vector3.New(), Vector3.New(), Vector3.New(), Vector3.New()]
        CenterA = Vector3(0, 0, 0)
        CenterB = Vector3(0, 0, 0)
        
        PointsA[0], PointsA[1], PointsA[2], PointsA[3], PointsA[4], PointsA[5], PointsA[6], PointsA[7] = self.GetVertices()
        PointsB[0], PointsB[1], PointsB[2], PointsB[3], PointsB[4], PointsB[5], PointsB[6], PointsB[7] = arg.GetVertices()
        
        for i in range(0,8):
            CenterA += PointsA[i]
            CenterB += PointsB[i]
        
        #// 중점
        CenterA /= 8
        CenterB /= 8
            
        #// A박스 3개 축
        Ax = PointsA[1] - PointsA[0]
        Ax.Normalize();
            
        Ay = PointsA[2] - PointsA[0]
        Ay.Normalize()
            
        Az = PointsA[4] - PointsA[0]
        Az.Normalize()
            
        #// B박스 3개 축
        Bx = PointsB[1] - PointsB[0]
        Bx.Normalize()
            
        By = PointsB[2] - PointsB[0]
        By.Normalize()
            
        Bz = PointsB[4] - PointsB[0]
        Bz.Normalize()
            
        Wa = (PointsA[1] - PointsA[0]).Length() * 0.5
        Ha = (PointsA[2] - PointsA[0]).Length() * 0.5
        Da = (PointsA[4] - PointsA[0]).Length() * 0.5
            
        Wb = (PointsB[1] - PointsB[0]).Length() * 0.5
        Hb = (PointsB[2] - PointsB[0]).Length() * 0.5
        Db = (PointsB[4] - PointsB[0]).Length() * 0.5
            
        isParallel = False
            
        #// 중점사이의 거리
        T = CenterB - CenterA
            
        cutoff = 0.999999
            
        absC = [[0,0,0], [0,0,0], [0,0,0]]
        c = [[0,0,0], [0,0,0], [0,0,0]]
        d = [0,0,0]
            
        r0 = 0
        r1 = 0
        r = 0
            
        #// 1
        c[0][0] = Ax.Dot(Bx)
        c[0][1] = Ax.Dot(By)
        c[0][2] = Ax.Dot(Bz)

        for i in range(0,3):
            absC[0][i] = math.fabs(c[0][i])
                
            if absC[0][i] > cutoff:
                isParallel = True
                    
        d[0] = T.Dot(Ax)
            
        r = math.fabs(d[0])
        r0 = Wa
        r1 = Wb * absC[0][0] + Hb * absC[0][1] + Db * absC[0][2]
        if r > r0 + r1:
            return False
            
        #// 2
        c[1][0] = Ay.Dot(Bx)
        c[1][1] = Ay.Dot(By)
        c[1][2] = Ay.Dot(Bz)
            
        for i in range(0,3):
            absC[1][i] = math.fabs(c[1][i])
            if (absC[1][i] > cutoff):
                isParallel = True
                
        d[1] = T.Dot(Ay)

        r = math.fabs(d[1])
        r0 = Ha
        r1 = Wb * absC[1][0] + Hb * absC[1][1] + Db * absC[1][2]
            
        if r > r0 + r1:
            return False
        
        #// 3
        c[2][0] = Az.Dot(Bx)
        c[2][1] = Az.Dot(By)
        c[2][2] = Az.Dot(Bz)
        
        for i in range(0,3):
            absC[2][i] = math.fabs(c[2][i])
            
            if absC[2][i] > cutoff:
                isParallel = True
                
        d[2] = T.Dot(Az)
        
        r = math.fabs(d[2])
        r0 = Da
        r1 = Wb * absC[2][0] + Hb * absC[2][1] + Db * absC[2][2]
        
        if r > r0 + r1:
            return False
        
        #// 4
        r = math.fabs(T.Dot(Bx))
        r0 = Wa * absC[0][0] + Ha * absC[1][0] + Da * absC[2][0]
        r1 = Wb
        if r > r0 + r1:
            return False
        
        #// 5
        r = math.fabs(T.Dot(By))
        r0 = Wa * absC[0][1] + Ha * absC[1][1] + Da * absC[2][1]
        r1 = Hb
        if r > r0 + r1:
            return False
        
        #// 6
        r = math.fabs(T.Dot(Bz))
        r0 = Wa * absC[0][2] + Ha * absC[1][2] + Da * absC[2][2]
        r1 = Db
        
        if r > r0 + r1:
            return False
        
        if isParallel == True:
            return True
        
        #// 7
        r = math.fabs(d[2] * c[1][0] - d[1] * c[2][0])
        r0 = Ha * absC[2][0] + Da * absC[1][0]
        r1 = Hb * absC[0][2] + Db * absC[0][1]
        
        if r > r0 + r1:
            return False
        
        #// 8
        r = math.fabs(d[2] * c[1][1] - d[1] * c[2][1])
        r0 = Ha * absC[2][1] + Da * absC[1][1]
        r1 = Wb * absC[0][2] + Db * absC[0][0]
        
        if r > r0 + r1:
            return False
        
        #// 9
        r = math.fabs(d[2] * c[1][2] - d[1] * c[2][2])
        r0 = Ha * absC[2][2] + Da * absC[1][2]
        r1 = Wb * absC[0][1] + Hb * absC[0][0]
        
        if r > r0 + r1:
            return False
        
        #// 10
        r = math.fabs(d[0] * c[2][0] - d[2] * c[0][0])
        r0 = Wa * absC[2][0] + Da * absC[0][0]
        r1 = Hb * absC[1][2] + Db * absC[1][1]
        if r > r0 + r1:
            return False
        
        #// 11
        r = math.fabs(d[0] * c[2][1] - d[2] * c[0][1])
        r0 = Wa * absC[2][1] + Da * absC[0][1]
        r1 = Wb * absC[1][2] + Db * absC[1][0]
        
        if r > r0 + r1:
            return False
        
        #// 12
        r = math.fabs(d[0] * c[2][2] - d[2] * c[0][2])
        r0 = Wa * absC[2][2] + Da * absC[0][2]
        r1 = Wb * absC[1][1] + Hb * absC[1][0]
        
        if r > r0 + r1:
            return False
        
        #// 13
        r = math.fabs(d[1] * c[0][0] - d[0] * c[1][0])
        r0 = Wa * absC[1][0] + Ha * absC[0][0]
        r1 = Hb * absC[2][2] + Db * absC[2][1]
        
        if r > r0 + r1:
            return False
        
        #// 14
        r = math.fabs(d[1] * c[0][1] - d[0] * c[1][1])
        r0 = Wa * absC[1][1] + Ha * absC[0][1]
        r1 = Wb * absC[2][2] + Db * absC[2][0]
        
        if r > r0 + r1:
            return False
        
        #// 15
        r = math.fabs(d[1] * c[0][2] - d[0] * c[1][2])
        r0 = Wa * absC[1][2] + Ha * absC[0][2]
        r1 = Wb * absC[2][1] + Hb * absC[2][0]
        
        if r > r0 + r1:
            return False
        
        return True


#main




