import math

class BoundingBox2D(object):
    
    def __init__(self, *args):
        from Vector2Math import Vector2
        if len(args) == 4:
            self.Vertex = [Vector2(args[0], args[1]), Vector2(args[2], args[3])]
        elif len(args) == 1:
            if isinstance(args[0], BoundingBox2D):
                self.Vertex = [Vector2(args[0].Vertex[0]), Vector2(args[0].Vertex[1])]
        elif len(args) == 2:
            if isinstance(args[0], Vector2) and isinstance(args[1], Vector2):
                self.Vertex = [args[0], args[1]]
        else:
            self.Vertex = [Vector2.New(1.7976931348623157e+308, 1.7976931348623157e+308), Vector2.New(-1.7976931348623157e+308, -1.7976931348623157e+308)]
        
    # A * 2, A * B, A *= 2, A *= B
    def __mul__(self, mat):
        b = BoundingBox2D(self)
        if b.IsNotEmpty() == True:
            b.Transform(mat)
        return b

    # 2 * A, B * A
    def __rmul__(self, mat): # 
        b = BoundingBox2D(self)
        if b.IsNotEmpty() == True:
            b.Transform(mat)
        return b

    # A == B
    def __eq__(self, v):
        return self.Vertex[0] == v.Vertex[0] and self.Vertex[1] == v.Vertex[1];

    # A != B
    def __ne__(self, v):
        return self.Vertex[0] != v.Vertex[0] or self.Vertex[1] != v.Vertex[1];

    # for print
    def __str__(self):
        return str(self.Vertex[0].x) + ", " + str(self.Vertex[0].y) + ", " + str(sself.Vertex[1].x) + ", " + str(sself.Vertex[1].y)

    def New():
        return BoundingBox2D(1.7976931348623157e+308, 1.7976931348623157e+308, -1.7976931348623157e+308, -1.7976931348623157e+308)

    def Zero(self):
        self.Vertex = [Vector2.New(), Vector2.New()]

    def __str__(self):
        return str(self.Vertex[0].x) + "," + str(self.Vertex[0].y) + "," + str(self.Vertex[1].x) + "," + str(self.Vertex[1].y)

    def FromString(self, s):
        if isinstance(s, bytes):
            vectorString = s.decode('utf-8')
        else:
            vectorString = s.encode().decode('utf-8')
        sp = vectorString.split(",")
        self.Vertex = [Vector2(float(sp[0]), float(sp[1])), Vector2(float(sp[2]), float(sp[3]))]

    def HasVolume(self):
        return self.Vertex[1].x > self.Vertex[0].x and self.Vertex[1].y > self.Vertex[0].y

    def IsNotEmpty(self):
        return self.Vertex[0].x != 1.7976931348623157e+308 or\
            self.Vertex[0].y != 1.7976931348623157e+308 or\
            self.Vertex[1].x != -1.7976931348623157e+308 or\
            self.Vertex[1].y != -1.7976931348623157e+308

    def Cover(self, *args):
        from Vector2Math import Vector2

        if len(args) == 1:
            if isinstance(args[0], BoundingBox2D):
                sbox = args[0]

                if self.Vertex[0].x > sbox.Vertex[0].x:
                    self.Vertex[0].x = sbox.Vertex[0].x
                
                if self.Vertex[0].y > sbox.Vertex[0].y:
                    self.Vertex[0].y = sbox.Vertex[0].y
                
                if self.Vertex[1].x < sbox.Vertex[1].x:
                    
                    self.Vertex[1].x = sbox.Vertex[1].x
                
                if self.Vertex[1].y > sbox.Vertex[1].y:
                    self.Vertex[1].y = sbox.Vertex[1].y
            elif isinstance(args[0], Vector2):
                vec = args[0]

                if(self.Vertex[0] > vec.x):
                    self.Vertex[0].x = vec.x
                
                if(self.Vertex[1] < vec.x):
                    self.Vertex[1].x = vec.x

                if(self.Vertex[0] > vec.y):
                    self.Vertex[0].y = vec.y

                if(self.Vertex[1] < vec.y):
                    self.Vertex[1].y = vec.y

        elif len(args) == 2:
            if(self.Vertex[0] > x):
                self.Vertex[0].x = x

            if(self.Vertex[1] < x):
                self.Vertex[1].x = x

            if(self.Vertex[0] > y):
                self.Vertex[0].y = y

            if(self.Vertex[1] < y):
                self.Vertex[1].y = y


    def Intersect(self, box):
        if(self.Vertex[0] > box.x):
            self.Vertex[0].x = box.x
                
        if(self.Vertex[1] < box.x):
            self.Vertex[1].x = box.x

        if(self.Vertex[0] > box.y):
            self.Vertex[0].y = box.y

        if(self.Vertex[1] < box.y):
            self.Vertex[1].y = box.y

    def GetDiagonal(self):
        return self.Vertex[1] - self.Vertex[0]

    def GetDiagonalLength(self):
        return GetDiagonal().Length()

    def GetCenter(self):
        return self.Vertex[0] - self.Vertex[1] * 0.5

    def GetVolumeSize(self):
        return (self.Vertex[1].x - self.Vertex[0].x) * (self.Vertex[1].y - self.Vertex[0].y)

    def Transform(self, mat):
        from Vector2Math import Vector2
        v0 = [Vector2(self.Vertex[0].x, self.Vertex[0].y),
              Vector2(self.Vertex[1].x, self.Vertex[0].y),
              Vector2(self.Vertex[0].x, self.Vertex[1].y),
              Vector2(self.Vertex[1].x, self.Vertex[1].y)]

        for i in range(0,4):
            v0[i].TransformCoord(mat)
        
        box = BoundingBox2D.Zero()
        
        for i in range(0,4):
            box.Cover(v0[i])

        return box, v0[0], v0[1], v0[2], v0[3]

    def TransformNoRotate(self, mat):
        from Vector2Math import Vector2
        
        v0 = Vector2(self.Vertex[0])
        v1 = Vector2(self.Vertex[1])
        vc = GetCenter()

        v0 -= vc
        v1 -= vc

        v = Vector2(vc)
        v2 = Vector2(self.Vertex[0])

        v.TransformCoord(mat)
        v2.TransformCoord(mat)
        v2 -= v

        len = v0.Length()

        box = BoundingBox2D.New()

        box.Vertex[0] = v0 + vc
        box.Vertex[1] = v1 + vc

        if len > 0:
            scale = v2.Length / len
            box.Vertex[0] *= scale
            box.Vertex[1] *= scale

        return box

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
                self.Vertex[1].x += args[0]
                self.Vertex[1].y += args[0]
            else:
                if v != 0:
                    self.Vertex[0].x -= args[0]
                    self.Vertex[0].y -= args[0]
                    self.Vertex[1].x += args[0]
                    self.Vertex[1].y += args[0]

                    if self.Vertex[0].x > self.Vertex[1].x:
                        self.Vertex[0].x = (self.Vertex[0].x + self.Vertex[1].x) / 2
                        self.Vertex[1].x = self.Vertex[0].x

                    if self.Vertex[0].y > self.Vertex[1].y:
                        self.Vertex[0].y = (self.Vertex[0].y + self.Vertex[1].y) / 2
                        self.Vertex[1].y = self.Vertex[0].y

        elif len(args) == 2:
            self.Vertex[0].x -= args[0]
            self.Vertex[0].y -= args[1]
            self.Vertex[1].x += args[0]
            self.Vertex[1].y += args[1]

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

    def GetVertices(self):
        return Vector2(self.Vertex[0].x, self.Vertex[0].y),\
            Vector2(self.Vertex[1].x, self.Vertex[0].y),\
            Vector2(self.Vertex[0].x, self.Vertex[1].y),\
            Vector2(self.Vertex[1].x, self.Vertex[1].y)

    def CheckCollide(self, target):
        self.Intersect(target)
        return self.HasVolume()

    def CheckContact(self, target):
        self.Intersect(target)
        return self.IsNotEmpty()

    def ChekcInclude(self, source):
        from Vector2Math import Vector2
        if isinstance(source, BoundingBox2D):
            return self.Vertex[0].x <= source.Vertex[0].x and\
                self.Vertex[0].y <= source.Vertex[0].y and\
                self.Vertex[1].x >= source.Vertex[1].x and\
                self.Vertex[1].y >= source.Vertex[1].y
        elif isinstance(source, Vector2):
            return self.Vertex[0].x <= source.x and\
                self.Vertex[0].y <= source.y and\
                self.Vertex[1].x >= source.x and\
                self.Vertex[1].y >= source.y

    def GetIntersection(fDst1, fDst2, P1, P2):
        from Vector2Math import Vector2

        if (fDst1 * fDst2) >= 0:
            return False, Vector2.New()
        if (fDst1 == fDst2):
            return False, Vector2.New()

        v2 = Vector2(P1+(P2-P1)*(-fDst1 / (fDst2 - fDst1)))
        return True, v2

    def Intersect(arg, arg1):
        b = BoundingBox2D(arg1)
        if b.Vertex[0].x < arg.Vertex[0].x:
            b.Vertex[0].x = arg.Vertex[0].x
        if b.Vertex[1].x > arg.Vertex[1].x:
            b.Vertex[1].x = arg.Vertex[1].x
        if b.Vertex[0].y < arg.Vertex[0].y:
            b.Vertex[0].y = arg.Vertex[0].y
        if b.Vertex[1].y > arg.Vertex[1].y:
            b.Vertex[1].y = arg.Vertex[1].y
        return b


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





