import math

class Frustum(object):
    
    Left = 0
    Right = 1
    Top = 2
    Bottom = 3
    Near = 4
    HexahedronPlaneMax = 5

    EdgeCheckIndex = [[0,1], [1,2], [2,3], [3,0], [0,4], [1,5], [2,6], [3,7], [4,5], [5,6], [6,7], [7,4]]
    

    def __init__(self, *args):
        from Vector3Math import Vector3
        from MatrixMath import Matrix
        from PlaneMath import Plane

        self.ViewProjMatrixCacheEnabled = False
        self.FarNearDisabled = False

        self.ViewProjMatrixCache = Matrix()

        self.HexahedronPlane = [Plane.New(), Plane.New(), Plane.New(), Plane.New(), Plane.New(), Plane.New()] 
        self.FrustumVertex = [Vector3.New(), Vector3.New(), Vector3.New(), Vector3.New(),\
            Vector3.New(), Vector3.New(), Vector3.New(), Vector3.New()]
        self.FrustumVertexsource = [Vector3(1,1,0), Vector3(-1,1,0), Vector3(-1,-1,0), Vector3(1,-1,0),\
        Vector3(1,1,1), Vector3(-1,1,1), Vector3(-1,-1,1), Vector3(1,-1,1)]
        self.FrustumID = 0
        
    def ExtractFromProjectMatrix(self, viewProj, viewProjInverse):
        from MatrixMath import Matrix
        if ViewProjMatrixCacheEnabled:
            if ViewProjMatrixCache == viewProj:
                return
            
        self.FrustumID += 1
        self.ViewProjMatrixCacheEnabled = True
        selfViewProjMatrixCache = Matrix(viewProj)
        
        for i in range(0,8):
            self.FrustumVertex[i] = Vector3.TransformCoord(self.FrustumVertexsource[i] , viewProjInverse)
            
        self.HexahedronPlane[0] = Plane(viewProj.m[0][3] + viewProj.m[0][0],\
		viewProj.m[1][3] + viewProj.m[1][0],\
		viewProj.m[2][3] + viewProj.m[2][0],\
		viewProj.m[3][3] + viewProj.m[3][0])
        
        self.HexahedronPlane[0].Normalize()
        
        self.HexahedronPlane[1] = Plane(viewProj.m[0][3] - viewProj.m[0][0],\
		viewProj.m[1][3] - viewProj.m[1][0],\
		viewProj.m[2][3] - viewProj.m[2][0],\
		viewProj.m[3][3] - viewProj.m[3][0])
        self.HexahedronPlane[1].Normalize()
        
        #// index bug (code mistake) fix  2015.09.03
        self.HexahedronPlane[2] = Plane( viewProj.m[0][3] - viewProj.m[0][1],\
            viewProj.m[1][3] - viewProj.m[1][1],\
            viewProj.m[2][3] - viewProj.m[2][1],\
            viewProj.m[3][3] - viewProj.m[3][1])
        self.HexahedronPlane[2].Normalize()
        
        self.HexahedronPlane[3] = Plane(viewProj.m[0][3] + viewProj.m[0][1],\
            viewProj.m[1][3] + viewProj.m[1][1],\
            viewProj.m[2][3] + viewProj.m[2][1],\
            viewProj.m[3][3] + viewProj.m[3][1])
        self.HexahedronPlane[3].Normalize()
        
        self.HexahedronPlane[4] = Plane(viewProj.m[0][2], viewProj.m[1][2], viewProj.m[2][2], viewProj.m[3][2])
        self.HexahedronPlane[4].Normalize()
        
        self.HexahedronPlane[5] = Plane( viewProj.m[0][3] - viewProj.m[0][2],\
            viewProj.m[1][3] - viewProj.m[1][2],\
            viewProj.m[2][3] - viewProj.m[2][2],\
            viewProj.m[3][3] - viewProj.m[3][2])
        self.HexahedronPlane[5].Normalize()



        def IsPointInbound(self, x, y, z):
            from Vector3Math import Vector3
            from Util import MathUtil
            p = Vector3(x, y, z)
            
            if self.FarNearDisabled:
                if MathUtil.PlanePointDistance(self.HexahedronPlane[0], p) < 0 and\
                    MathUtil.PlanePointDistance(self.HexahedronPlane[1], p) < 0 and\
                    MathUtil.PlanePointDistance(self.HexahedronPlane[2], p) < 0 and\
                    MathUtil.PlanePointDistance(self.HexahedronPlane[3], p) < 0:
                    return True

                return False
            else:
                if (MathUtil.PlanePointDistance(self.HexahedronPlane[0], p) < 0 and\
                    MathUtil.PlanePointDistance(self.HexahedronPlane[1], p) < 0 and\
                    MathUtil.PlanePointDistance(self.HexahedronPlane[2], p) < 0 and\
                    MathUtil.PlanePointDistance(self.HexahedronPlane[3], p) < 0 and\
                    MathUtil.PlanePointDistance(self.HexahedronPlane[4], p)< 0 and\
                    MathUtil.PlanePointDistance(self.HexahedronPlane[5], p) < 0):
                    return True
                return False
            

    #// Point가 Frustum 외부에 존재하는지 검사
    def IsPointOutbound(self, x, y, z):
        from Vector3Math import Vector3
        p = Vector3(x, y, z)

        if self.FarNearDisabled:
            if MathUtil.PlanePointDistance(HexahedronPlane[0], p) > 0 or\
                MathUtil.PlanePointDistance(HexahedronPlane[1], p) > 0 or\
                MathUtil.PlanePointDistance(HexahedronPlane[2], p) > 0 or\
                MathUtil.PlanePointDistance(HexahedronPlane[3], p) > 0:
                return True
            return False
        else:
            if MathUtil.PlanePointDistance(HexahedronPlane[0], p) > 0 or\
                MathUtil.PlanePointDistance(HexahedronPlane[1], p) > 0 or\
                MathUtil.PlanePointDistance(HexahedronPlane[2], p) > 0 or\
                MathUtil.PlanePointDistance(HexahedronPlane[3], p) > 0 or\
                MathUtil.PlanePointDistance(HexahedronPlane[4], p) > 0 or\
                MathUtil.PlanePointDistance(HexahedronPlane[5], p) > 0:
                return True
            return False
        

    def IsLineIntersectPlane(self, sourcePlane, LineStartPos, LineEndPos):
        from Util import MathUtil
        if MathUtil.PlanePointDistance(sourcePlane, LineStartPos) * MathUtil.PlanePointDistance(sourcePlane, LineEndPos) <= 0:
            return True
        else:
            return False
    
    #// BoundingBox 가 완전히 frustum 밖에 있을 때만 True
    def IsBoundingBoxOutbound(self, sourceBox):
        from Vector3Math import Vector3
        from BoundingBoxMath import BoundingBox
        from Util import MathUtil

        v0 = Vector3(sourceBox.Vertex[0])
        v1 = Vector3(sourceBox.Vertex[1])

        countPlane = 0

        if self.FarNearDisabled:
            countPlane = 4
        else:
            countPlane = 6

        for i in countPlane:
            p = Plane(self.HexahedronPlane[i])
            if MathUtil.PlanePointDistance(p, v0.x, v0.y, v0.z) > 0:
                continue
            if MathUtil.PlanePointDistance(p, v1.x, v0.y, v0.z) > 0:
                continue
            if MathUtil.PlanePointDistance(p, v0.x, v1.y, v0.z) > 0:
                continue
            if MathUtil.PlanePointDistance(p, v1.x, v1.y, v0.z) > 0:
                continue
            if MathUtil.PlanePointDistance(p, v0.x, v0.y, v1.z) > 0:
                continue
            if MathUtil.PlanePointDistance(p, v1.x, v0.y, v1.z) > 0:
                continue
            if MathUtil.PlanePointDistance(p, v0.x, v1.y, v1.z) > 0:
                continue
            if MathUtil.PlanePointDistance(p, v1.x, v1.y, v1.z) > 0:
                continue

            return True

        return False
    
    #// BoundingBox 가 완전히 frustum 안에 있을 때만 True
    def IsBoundingBoxInbound(self, sourceBox):
        from Vector3Math import Vector3
        from BoundingBoxMath import BoundingBox
        from Util import MathUtil
        
        v0 = Vector3(sourceBox.Vertex[0])
        v1 = Vector3(sourceBox.Vertex[1])
        
        countPlane = 0

        if self.FarNearDisabled:
            countPlane = 4
        else:
            countPlane = 6

        for i in countPlane:
            p = Plane(self.HexahedronPlane[i])
            if MathUtil.PlanePointDistance(p, v0.x, v0.y, v0.z) < 0:
                continue
            if MathUtil.PlanePointDistance(p, v1.x, v0.y, v0.z) < 0:
                continue
            if MathUtil.PlanePointDistance(p, v0.x, v1.y, v0.z) < 0:
                continue
            if MathUtil.PlanePointDistance(p, v1.x, v1.y, v0.z) < 0:
                continue
            if MathUtil.PlanePointDistance(p, v0.x, v0.y, v1.z) < 0:
                continue
            if MathUtil.PlanePointDistance(p, v1.x, v0.y, v1.z) < 0:
                continue
            if MathUtil.PlanePointDistance(p, v0.x, v1.y, v1.z) < 0:
                continue
            if MathUtil.PlanePointDistance(p, v1.x, v1.y, v1.z) < 0:
                continue
            return True
    
        return False
    
    #// BoundingBox 모서리 일부가 frustum 안에 있을 때 True
    def IsBoundingBoxVertexInbound(self, sourceBox):
        from Vector3Math import Vector3
        from BoundingBoxMath import BoundingBox
        from Util import MathUtil
        
        v0 = Vector3(sourceBox.Vertex[0])
        v1 = Vector3(sourceBox.Vertex[1])
        
        countPlane = 0

        if self.FarNearDisabled:
            countPlane = 4
        else:
            countPlane = 6

        for i in countPlane:
            p = Plane(self.HexahedronPlane[i])
            if MathUtil.PlanePointDistance(p, v0.x, v0.y, v0.z) < 0:
                continue
            if MathUtil.PlanePointDistance(p, v1.x, v0.y, v0.z) < 0:
                continue
            if MathUtil.PlanePointDistance(p, v0.x, v1.y, v0.z) < 0:
                continue
            if MathUtil.PlanePointDistance(p, v1.x, v1.y, v0.z) < 0:
                continue
            if MathUtil.PlanePointDistance(p, v0.x, v0.y, v1.z) < 0:
                continue
            if MathUtil.PlanePointDistance(p, v1.x, v0.y, v1.z) < 0:
                continue
            if MathUtil.PlanePointDistance(p, v0.x, v1.y, v1.z) < 0:
                continue
            if MathUtil.PlanePointDistance(p, v1.x, v1.y, v1.z) < 0:
                continue
            return True
        return False


    def MakeObjectFrustum(self, viewPos, objectBox):
        from Vector3Math import Vector3
        from BoundingBoxMath import BoundingBox
        from Util import MathUtil
        from MatrixMath import Matrix
        
        pos = objectBox.GetCenter()
        dist = pos - viewPos
        distance = dist.Length()
        ydir = Vector3(0,1,0)
        
        posTop = pos + distance * Vector3(0,1,0)
        #//Vector3 posBottom = pos + distance * Vector3(0,-1,0);
        leftdir = Vector3.New()
        leftdir.Cross(dist)
        
        #//NXVec3Cross(&leftdir, &dist, &ydir);  // right handed
        posLeft = pos + leftdir
        #//Vector3 posRight = pos - leftdir;
        
        viewMatrix = Matrix.New()
        #//NXMatrixLookAtLH(&viewMatrix, &viewPos, &pos, &ydir);
        viewMatrix = Matrix.LookAtLH(viewPos , pos, ydir)
        
        sumBox = BoundingBox.New()
        #//objectbox.Transform(buffer8, viewMatrix, NULL);
        sumBox, tv0, tv1, tv2, tv3, tv4, tv5, tv6, tv7 = objectBox.Transform(viewMatrix)
        buffer8 = [tv0, tv1, tv2, tv3, tv4, tv5, tv6, tv7]
        
        bv0 = Vector3(objectBox.Vertex[0])
        bv1 = Vector3(objectBox.Vertex[1])
        
        #// original reffere 
        v0 = [Vector3( bv0.x, bv0.y, bv0.z ),\
            Vector3( bv1.x, bv0.y, bv0.z ),\
            Vector3( bv0.x, bv1.y, bv0.z ),\
            Vector3( bv1.x, bv1.y, bv0.z ),\
            Vector3( bv0.x, bv0.y, bv1.z ),\
            Vector3 (bv1.x, bv0.y, bv1.z ),\
            Vector3( bv0.x, bv1.y, bv1.z ),\
            Vector3 (bv1.x, bv1.y, bv1.z )]
        
        topIndex = 0
        max = -1.7976931348623157e+308
        for i in range(0,8):
            if buffer8[i].y > max:
                max = buffer8[i].y
                topIndex = i

        bottomIndex = 0
        max = 1.7976931348623157e+308
        
        for i in range(0,8):
            if buffer8[i].y < max:
                max = buffer8[i].y
                bottomIndex = i
                
        leftIndex = 0			#//## 확인 사항
        max = 1.7976931348623157e+308
        
        for i in range(0,8):
            if buffer8[i].x < max:
                max = buffer8[i].x
                leftIndex = i
                
        rightIndex = 0#//## 확인 사항
        max = -1.7976931348623157e+308

        for i in range(0,8):
            if buffer8[i].x > max:
                max = buffer8[i].x
                rightIndex = i
                
        self.HexahedronPlane[2] = MathUtil.GetPlaneFromPolygon(viewPos, posLeft, v0[topIndex])
        self.HexahedronPlane[3] = MathUtil.GetPlaneFromPolygon(viewPos, posLeft, v0[bottomIndex])
        self.HexahedronPlane[0] = MathUtil.GetPlaneFromPolygon(viewPos, posTop, v0[leftIndex])
        self.HexahedronPlane[1] = MathUtil.GetPlaneFromPolygon(viewPos, posTop, v0[rightIndex])
        
        self.FarNearDisabled = False
        
        return True
    
    def Clear():
        from Vector3Math import Vector3
        from MatrixMath import Matrix
        from PlaneMath import Plane

        self.ViewProjMatrixCacheEnabled = False
        self.FarNearDisabled = False

        self.ViewProjMatrixCache = Matrix()

        self.HexahedronPlane = [Plane.New(), Plane.New(), Plane.New(), Plane.New(), Plane.New(), Plane.New()] 
        self.FrustumVertex = [Vector3.New(), Vector3.New(), Vector3.New(), Vector3.New(),\
            Vector3.New(), Vector3.New(), Vector3.New(), Vector3.New()]
        self.FrustumVertexsource = [Vector3(1,1,0), Vector3(-1,1,0), Vector3(-1,-1,0), Vector3(1,-1,0),\
        Vector3(1,1,1), Vector3(-1,1,1), Vector3(-1,-1,1), Vector3(1,-1,1)]
        self.FrustumID = 0
        
    #// 여러가지 충돌 검사 복함 처리 
    def IsBoundingBoxCollide(self, sourceBox):
        from Vector3Math import Vector3
        from MatrixMath import Matrix
        from PlaneMath import Plane
        from BoundingBoxMath import BoundingBox

        # 1) frustum 어떤 하나의 면 밖으로 obb의 모든 점들이 모여 있다면 시야에 없음.(끝)
        if self.IsBoundingBoxOutbound(sourceBox):
            return False
            
        #   2) frustum 6면의 면 안쪽으로 obb의 점들이 모두 있다면 시야 안에 물체가 완전히 들어옴.(끝)
        #   3) obb점들의 일부는 frustum 6면의 안쪽에 있고 일부는 6면의 밖에 있다면 시야 안에 물체의 일부만 들어옴.(끝)
            
        if self.IsBoundingBoxVertexInbound(sourceBox):
            return True
            
        #  3) box의 어떤 하나의 면 밖으로 frustum의 모든 점들이 모여 있다면 시야에 없음.(끝)
            
        if self.FrustumVertex[0].x <= sourceBox.Vertex[0].x and\
            self.FrustumVertex[1].x <= sourceBox.Vertex[0].x and\
            self.FrustumVertex[2].x <= sourceBox.Vertex[0].x and\
            self.FrustumVertex[3].x <= sourceBox.Vertex[0].x and\
            self.FrustumVertex[4].x <= sourceBox.Vertex[0].x and\
            self.FrustumVertex[5].x <= sourceBox.Vertex[0].x and\
            self.FrustumVertex[6].x <= sourceBox.Vertex[0].x and\
            self.FrustumVertex[7].x <= sourceBox.Vertex[0].x:
                return False
                
        if self.FrustumVertex[0].x >= sourceBox.Vertex[1].x and\
            self.FrustumVertex[1].x >= sourceBox.Vertex[1].x and\
            self.FrustumVertex[2].x >= sourceBox.Vertex[1].x and\
            self.FrustumVertex[3].x >= sourceBox.Vertex[1].x and\
            self.FrustumVertex[4].x >= sourceBox.Vertex[1].x and\
            self.FrustumVertex[5].x >= sourceBox.Vertex[1].x and\
            self.FrustumVertex[6].x >= sourceBox.Vertex[1].x and\
            self.FrustumVertex[7].x >= sourceBox.Vertex[1].x:
            return False
        
        if self.FrustumVertex[0].y <= sourceBox.Vertex[0].y and\
            self.FrustumVertex[1].y <= sourceBox.Vertex[0].y and\
            self.FrustumVertex[2].y <= sourceBox.Vertex[0].y and\
            self.FrustumVertex[3].y <= sourceBox.Vertex[0].y and\
            self.FrustumVertex[4].y <= sourceBox.Vertex[0].y and\
            self.FrustumVertex[5].y <= sourceBox.Vertex[0].y and\
            self.FrustumVertex[6].y <= sourceBox.Vertex[0].y and\
            self.FrustumVertex[7].y <= sourceBox.Vertex[0].y:
            return False
        
        if self.FrustumVertex[0].y >= sourceBox.Vertex[1].y and\
            self.FrustumVertex[1].y >= sourceBox.Vertex[1].y and\
            self.FrustumVertex[2].y >= sourceBox.Vertex[1].y and\
            self.FrustumVertex[3].y >= sourceBox.Vertex[1].y and\
            self.FrustumVertex[4].y >= sourceBox.Vertex[1].y and\
            self.FrustumVertex[5].y >= sourceBox.Vertex[1].y and\
            self.FrustumVertex[6].y >= sourceBox.Vertex[1].y and\
            self.FrustumVertex[7].y >= sourceBox.Vertex[1].y:
            return False
        
        if self.FrustumVertex[0].z <= sourceBox.Vertex[0].z and\
            self.FrustumVertex[1].z <= sourceBox.Vertex[0].z and\
            self.FrustumVertex[2].z <= sourceBox.Vertex[0].z and\
            self.FrustumVertex[3].z <= sourceBox.Vertex[0].z and\
            self.FrustumVertex[4].z <= sourceBox.Vertex[0].z and\
            self.FrustumVertex[5].z <= sourceBox.Vertex[0].z and\
            self.FrustumVertex[6].z <= sourceBox.Vertex[0].z and\
            self.FrustumVertex[7].z <= sourceBox.Vertex[0].z:
            return False
        
        if self.FrustumVertex[0].z >= sourceBox.Vertex[1].z and\
            self.FrustumVertex[1].z >= sourceBox.Vertex[1].z and\
            self.FrustumVertex[2].z >= sourceBox.Vertex[1].z and\
            self.FrustumVertex[3].z >= sourceBox.Vertex[1].z and\
            self.FrustumVertex[4].z >= sourceBox.Vertex[1].z and\
            self.FrustumVertex[5].z >= sourceBox.Vertex[1].z and\
            self.FrustumVertex[6].z >= sourceBox.Vertex[1].z and\
            self.FrustumVertex[7].z >= sourceBox.Vertex[1].z:
            return False
        #  1) frustum 의 edge들이 obb의 면들과 충돌 한다면 시야 안의 물체가 일부만 들어옴.(끝)
        intersect = Vector3.New()
        for i in range(0, 12):
            check, intersect = sourceBox.GetLineIntersect(self.FrustumVertex[edgeCheckIndex[i][0]], self.FrustumVertex[edgeCheckIndex[i][1]])
            if check:
                return True
        
        countPlane = 0
        
        if self.FarNearDisabled:
            countPlane = 4
        else:
            countPlnae = 6
        
        # 2) box의 edge들이 frustum의 면들과 충돌 한다면 시야 안의 물체가 일부만 들어옴.(끝)
        boxVertex = [Vector3(sourceBox.Vertex[0].x, sourceBox.Vertex[0].y, sourceBox.Vertex[0].z),\
            Vector3(sourceBox.Vertex[0].x, sourceBox.Vertex[1].y, sourceBox.Vertex[0].z),\
            Vector3(sourceBox.Vertex[1].x, sourceBox.Vertex[1].y, sourceBox.Vertex[0].z),\
            Vector3(sourceBox.Vertex[1].x, sourceBox.Vertex[0].y, sourceBox.Vertex[0].z),\
            Vector3(sourceBox.Vertex[0].x, sourceBox.Vertex[0].y, sourceBox.Vertex[1].z),\
            Vector3(sourceBox.Vertex[0].x, sourceBox.Vertex[1].y, sourceBox.Vertex[1].z),\
            Vector3(sourceBox.Vertex[1].x, sourceBox.Vertex[1].y, sourceBox.Vertex[1].z),\
            Vector3(sourceBox.Vertex[1].x, sourceBox.Vertex[0].y, sourceBox.Vertex[1].z)]
        
        for i in range(0, 12):
            for k in countPlane:
                p = Plane(self.HexahedronPlane[k])
                # if plus point in bound
                # if minus point out of bound
                d0 = MathUtil.PlanePointDistance(p, boxVertex[edgeCheckIndex[i][0]].x, boxVertex[edgeCheckIndex[i][0]].y, boxVertex[edgeCheckIndex[i][0]].z)
                d1 = MathUtil.PlanePointDistance(p, boxVertex[edgeCheckIndex[i][1]].x, boxVertex[edgeCheckIndex[i][1]].y, boxVertex[edgeCheckIndex[i][1]].z)
                if d0 * d1 <= 0:
                    return True
                
        return False
