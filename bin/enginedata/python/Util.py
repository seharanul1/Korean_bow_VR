import math
import random
import time

class Collision:
    def PlaneLineIntersectionFast(sourcePlane, lineStartPos, lineEndPos):
        from PlaneMath import Plane        
        from Vector3Math import Vector3
        u = sourcePlane.a * lineStartPos.x + sourcePlane.b * lineStartPos.y + sourcePlane.c * lineStartPos.z + sourcePlane.d
        u2 = plane.a * (lineStartPos.x - lineEndPos.x) + plane.b * (lineStartPos.y - lineEndPos.y) + sourcePlane.c * (lineStartPos.z - lineEndPos.z)
        
        resultIntersectPoint = Vector3.New()
        resultIntersect = False

        if u2 == 0:
            return resultIntersect, resultIntersectPoint
        else:
            u /= u2
            
            resultIntersectPoint = lineStartPos + (lineEndPos - lineStartPos) * u
            
            if u >= 0 and u <= 1.0:
                resultIntersect = True

        return resultIntersect, resultIntersectPoint


    #@brief X평면과 선의 교점
    def PlaneXLineIntersection(cutX, lineStartPos, lineEndPos):
        from PlaneMath import Plane        
        from Vector3Math import Vector3

        inOutIntersection = Vector3.New()

        if lineStartPos.x == lineEndPos.x:
            if cutx != lineStartPos.x:
                return 0, inOutIntersection
            else:
                inOutIntersection = lineStartPos
                return 2, inOutIntersection

        x0 = Vector3
        x1 = Vector3

        if lineStartPos.x > lineEndPos.x:
            x1 = lineStartPos
            x0 = lineEndPos
        else:
            x1 = lineEndPos
            x0 = lineStartPos
            
        if cutx > x1.x or cutx < x0.x:
            return 0, inOutIntersection

        a = (cutx - x0.x) / (x1.x - x0.x)
        inOutIntersection = (x1 - x0) * a + x0

        return 1, inOutIntersection
    

    #@brief Y평면과 선의 교점
    def PlaneYLineIntersection(cutY, lineStartPos, lineEndPos, destIntersection):
        from PlaneMath import Plane        
        from Vector3Math import Vector3

        inOutIntersection = Vector3.New()

        if lineStartPos.y == lineEndPos.y:
            if cutY != lineStartPos.y:
                return 0, inOutIntersection
            else:
                inOutIntersection = lineStartPos
                return 2, inOutIntersection

        y0 = Vector3
        y1 = Vector3

        if lineStartPos.y > lineEndPos.y:
            y1 = lineStartPos
            y0 = lineEndPos
        else:
            y1 = lineEndPos
            y0 = lineStartPos
            
        if cutY > y1.y or cutY < y0.y:
            return 0, inOutIntersection

        a = (cutY - y0.y) / (y1.y - y0.y)
        inOutIntersection = (y1 - y0) * a + y0

        return 1, inOutIntersection
    

    #@brief Z평면과 선의 교점
    def PlaneZLineIntersection(cutZ, lineStartPos, lineEndPos, destIntersection):
        from PlaneMath import Plane        
        from Vector3Math import Vector3

        inOutIntersection = Vector3.New()

        if lineStartPos.z == lineEndPos.z:
            if cutZ != lineStartPos.z:
                return 0, inOutIntersection
            else:
                inOutIntersection = lineStartPos
                return 2, inOutIntersection

        z0 = Vector3
        z1 = Vector3

        if lineStartPos.z > lineEndPos.z:
            z1 = lineStartPos
            z0 = lineEndPos
        else:
            z1 = lineEndPos
            z0 = lineStartPos
            
        if cutZ > z1.z or cutZ < z0.z:
            return 0, inOutIntersection

        a = (cutZ - z0.z) / (z1.z - z0.z)
        inOutIntersection = (z1 - z0) * a + z0

        return 1, inOutIntersection



    #@brief 평면과 선의 정확한 교점 방향
    def PlaneLineIntersectionDirectionAccurate(sourcePlane, lineStartPos, lineDirection, closedLine):
        from PlaneMath import Plane        
        from Vector3Math import Vector3
        from MatrixMath import Matrix

        destIntersection = Vector3
        destDirectionMatrix = Matrix

        destDirectionMatrix = Matrix.LookAt(direction, p1)
        
        planeNew = Plane.Transform(sourcePlanem, Matrix)
        
        if planeNew.c == 0:
            return False, destIntersection, destDirectionMatrix
        
        z = -planeNew.d / planeNew.c
        if z == 0:
            destIntersection = p1
            return True, destIntersection, destDirectionMatrix
        else:
            if closed_line:
                p2 = Vector3
                p2 = lineStartPos + lineDirection
                p2_2 = Vector3.TransformCoord(p2, matrix)
                
                if z > 0 and z <= p2_2.z:
                   destIntersection = p1 + (z / ((p2_2.z) * direction))
                   return True, destIntersection, destDirectionMatrix
                else:
                   return False, destIntersection, destDirectionMatrix
            else:
                p2 = Vector3
                p2 = lineStartPos + lineDirection
                p2_2 = Vector3.TransformCoord(p2, matrix)
                if MathUtil.IsNormalToolVerySmall(p2_2.z) == False:
                    destIntersection = p1 + z / (p2_2.z) * direction
                    return True, destIntersection, destDirectionMatrix
                else:
                    return False, destIntersection, destDirectionMatrix

        return False, destIntersection, destDirectionMatrix
    

    #@brief 평면과 선의 교점(빠르게 계산)
    def PlaneLineIntersectionDirectionFast(sourcePlane, lineStartPos, lineDirection):
        from PlaneMath import Plane        
        from Vector3Math import Vector3

        InOutIntersection = Vector3

        u = sourcePlane.a * lineStartPos.x + sourcePlane.b * lineStartPos.y + sourcePlane.c * lineStartPos.z + sourcePlane.d
        u2 = -(sourcePlane.a * (direction.x) + sourcePlane.b * (direction.y) + sourcePlane.c * (direction.z))

        if u2 == 0:
            return False, InOutIntersection
        
        u3 = u / u2
        
        if closed_line:
            if u3 >= 0:
                InOutIntersection = lineStartPos + u3 * (lineDirection)
                return True, InOutIntersection
            else:
                return False, InOutIntersection
        else:
            InOutIntersection = lineStartPos + (u3 * (lineDirection))
            return True, InOutIntersection
        

    #///@brief 폴리곤과 선의 교점
    def PolygonLineIntersection(tgriangleVertexArray, lineStartPos, lineEndPos, destIntersection):
        from PlaneMath import Plane        
        from Vector3Math import Vector3

        destIntersection = Vector3

        plane = Plane.PlaneFromPoints(tgriangleVertexArray[0], tgriangleVertexArray[1], tgriangleVertexArray[2])
        

        isIntersect, destIntersection = PlaneLineIntersectionDirectionFast(plane, lineStartPos, lineEndPos)

        if isIntersect == False:
            return False, destIntersection

        isPointBounding, destIntersection = MathUtil.IsPointBounding(tgriangleVertexArray)

        if isPointBounding :
            return True, destIntersection
        else:
            return False, destIntersection



    #///@brief 폴리곤과 선의 교점
    def PolygonLineIntersection(sourcePlane, triangleVertexArray, lineStartPos, lineEndPos):
        from PlaneMath import Plane        
        from Vector3Math import Vector3

        destIntersection = Vector3

        isIntersect, destIntersection = PlaneLineIntersectionDirectionFast(sourcePlane, lineStartPos, lineEndPos)

        if isIntersect == False:
            return False, destIntersection
        
        isPointBounding, destIntersection = MathUtil.IsPointBounding(tgriangleVertexArray)
        
        if isPointBounding :
            return True, destIntersection
        else:
            return False, destIntersection


    #///@brief 2차원에서 두 라인의 교점
    def LineLineIntersection2D(lineStartPosX0, lineStartPosY0, lineEndPosX0, lineEndPosY0,
                               lineStartPosX1, lineStartPosY1, lineEndPosX1, lineEndPosY1):
        destX = float
        destY = float

        x1 = lineStartPosX0
        x2 = lineEndPosX0
        y1 = lineEndPosY0
        y2 = lineEndPosY0
        x3 = lineStartPosX1
        x4 = lineEndPosX1
        y3 = lineEndPosY1
        y4 = lineEndPosY1

        A1 = x2 - x1
        B1 = y2 - y1
        A2 = x4 - x3
        B2 = y4 - y3

        if A1 == 0:
            if B1 == 0:
                return False, destX, destY
            
            destX = x1

            if A2 == 0:
                return False, destX, destY

            destY = ((B2 * (destX - x3) + y3 * A2) / A2)

            return True, destX, destY
        else:
            if B1 == 0:
                if A1 == 0:
                    return False, destX, destY
                
                destY = y1
                
                if B2 == 0:
                    return False, destX, destY
                
                dest = ((A2 * (destY - y3) + x3 * B2) / B2)
                return True, destX, destY
            
            if A2 == 0:
                if B2 == 0:
                    return False, destX, destY
                
                destX = x3
                if A1 == 0:
                    return False, destX, destY
                destY = ((B1 * (destX - x1) + y1 * A1) / A1)
                
                return True, destX, destY
            else:
                if B2 == 0:
                    if A2 == 0:
                        return False, destX, destY

                    destY = y3
                    
                    if B1 == 0:
                        return False, destX, destY
                    
                    destX = ((A1 * (destY - y1) + x1 * B1) / B1)
                    return True, destX, destY
                
                destX = (-(-B1 * x1 / A1 + y1 + B2 * x3 / A2 - y3) / (B1 / A1 - B2 / A2))
                destY = (-(-A1 * y1 / B1 + x1 + A2 * y3 / B2 - x3) / (A1 / B1 - A2 / B2))

                return True, destX, destY



    #@brief 3차원에서 두 라인의 교점
    def LineLineIntersection3D(p1, p2, normal, p3, p4, closedLine):
        from Vector3Math import Vector3
        from PlaneMath import Plane

        destIntersection = Vector3

        pnormal = p2 + normal

        plane = Plane.PlaneFromPoints(p1, p2, pnormal)

        dir = p4 - p3

        return Collision.PlaneLineIntersectionDirectionAccurate(plane, p3, dir, closedLine)


    #///@brief 폴리곤과 선의 교점
    def PolygonLineIntersectionDirectionAccurate(sourcePlane, triangleVertexArray, lineStartPos, lineDirection):
        from Vector3Math import Vector3
        from PlaneMath import Plane

        destIntersection = Vector3

        isIntersect, intersectPoint, intersectMat = Collision.PlaneLineIntersectionDirectionAccurate(sourcePlane, lineStartPos, lineDirection, False)

        if isIntersect == False:
            return False

        isPointBounding, destIntersection = MathUtil.IsPointBounding(tgriangleVertexArray)

        return isPointBounding



    #///@brief 폴리곤과 선의 교점
    def PolygonLineIntersectionDirectionAccurate(triangleVertexArray, lineStartPos, lineDirection):
        from Vector3Math import Vector3
        from PlaneMath import Plane
               
        plane = Plane.PlaneFromPoints(triangleVertexArray[0], triangleVertexArray[1], triangleVertexArray[2])

        isIntersect, intersectPoint, intersectMat = Collision.PlaneLineIntersectionDirectionAccurate(plane, lineStartPos, lineDirection, False)

        if isIntersect == False:
            return False
        
        isPointBounding, destIntersection = MathUtil.IsPointBounding(tgriangleVertexArray)

        return isPointBounding



    #///@brief 폴리곤과 선의 교점 (빠르게 계산)
    def PolygonLineIntersectionDirectionFast(triangleVertexArray, lineStartPos, lineDirection, destIntersection):
        from Vector3Math import Vector3
        from PlaneMath import Plane

        plane = Plane.PlaneFromPoints(triangleVertexArray[0], triangleVertexArray[1], triangleVertexArray[2])

        isIntersect, intersectPoint, intersectMat = Collision.PlaneLineIntersectionDirectionAccurate(plane, lineStartPos, lineDirection, True)

        if isIntersect == False:
            return False
        
        isPointBounding, destIntersection = MathUtil.IsPointBounding(tgriangleVertexArray)

        return isPointBounding



    #///@brief 삼각형 안에 점이 포함되었는가?  #추후 지원 
    def IsPolygonBounding2D(triangleVertexArray, pointPos):
        return 0

    #brief 삼각형을 원으로 그리고 그안에 점이 포함 되었는가? #추후 지원
    def IsPointBounding2DCircle(triangleVertexArray, pointPos, radius):
        return 0

    #///@brief 삼각형 # 추후 지원
    def IsPointBounding2DInline(triangleVertexArray, pointPos):
        return 0


    #///@brief 삼각형과 라인의 교점에 관한 법선 벱터 # 추후 지원
    def PolygonLineIntersectionYDirection(triangleVertexArray, lineStartPos, lineDirection, destIntersection):
        return 0


    #///@brief 삼각형과 라인의 교점에서 시작하는 법선 벡터 # 추후 지원
    def PolygonLineIntersectionY(triangleVertexArray, destIntersection):
        return 0

    #///@brief 삼각형과 라인의 교점에서 시작하는 법선 벡터 # 추후 지원
    def PolygonLineIntersectionY(triangleVertexArray, destIntersection, destNormal):
        return 0



class Line:
    #///@brief 점과 선의 최단 거리
    def LinePointDistance(linePosX0, linePosY0, linePosX1, linePosY1, pointPosX, pointPosY):
        
        nx, ny = MathUtil.Compute2DNormal(linePosX0, linePosY0, linePosX1, linePosY1)
        polygon_distance = x1 * nx + y1 * ny
        point_distance_normal = pointPosX * nx + pointPosY * ny

        return math.fabs(point_distance_normal - polygon_distance);



    def LinePointDistance(linePosX0, linePosY0, linePosZ0,
                          linePosX1, linePosY1, linePosZ1,
                          pointPosX, pointPosY, pointPosZ):
        from Vector3Math import Vector3
        line0 = Vector3(linePosX0, linePosY0, linePosZ0)
        line1 = Vector3(linePosX1, linePosY1, linePosZ1)
        check = Vector3(pointPosX, pointPosY, pointPosZ)

        return Line.LinePointDistance(line0, line1, check)


    def LinePointDistance(line0, line1, point):
        from Vector3Math import Vector3
        l1 = line1 - line0
        l2 = line0 - check

        r1 = Vector3.Cross(l1, l2)
        
        return r1.Length() / l2.Length()

    #///@brief 점 과 선의 최단거리 제곱형태
    def LinePointDistanceSquare(lineStartPosX, lineStartPosY, lineNormalX, lineNormalY, pointPosX, pointPosY):
        polygon_distance2 = (pointPosX-lineStartPosX) * lineNormalX + (pointPosY-lineStartPosY) * lineNormalY
        return (pointPosX-lineStartPosX)*(pointPosX-lineStartPosX) + (pointPosY-lineStartPosY)*(pointPosY-lineStartPosY) - polygon_distance2 * polygon_distance2;
    

    def LinePointDistanceSquare(lineStartPosX, lineStartPosY, lineNormalX, lineNormalY, pointPosX, pointPosY):
        polygon_distance2 = (pointPosX-lineStartPosX) * lineNormalX + (pointPosY-lineStartPosY) * lineNormalY;
        destNearestX = polygon_distance2 * lineNormalX + lineStartPosX
        destNearestY = polygon_distance2 * lineNormalY + lineStartPosY

        return (pointPosX-lineStartPosX)*(pointPosX-lineStartPosX) + (pointPosY-lineStartPosY)*(pointPosY-lineStartPosY) - polygon_distance2 * polygon_distance2, destNearestX, destNearestY



    def LinePointDistanceSquare(line0, line1, point):
        from Vector3Math import Vector3
        l1 = line1 - line0
        l2 = line0 - check

        r1 = Vector3.Cross(l1, l2)
        
        return r1.LengthSq() / l2.LengthSq()



    #///@brief 2D 점 과 선의 거리와 노말벡터를 얻어옴
    def LinePointDistanceNormal(linePosX0, linePosY0, linePosX1, linePosY1, pointPosX, pointPosY):
        destNormalX = float
        destNormalY = float

        nx, ny = MathUtil.Compute2DNormal(linePosX0, linePosY0, linePosX1, linePosY1)

        polygon_distance = linePosX0 * nx + linePosY0 * ny
        point_distance_normal = pointPosX * nx + pointPosY * ny
        dist = point_distance_normal - polygon_distance
        normaldist = dist / math.fabs(dist)

        destNormalX = (nx * normaldist)
        destNormalY = (ny * normaldist)

        return dist, destNormalX, destNormalY



    #///@brief 각 라인의 끝점까지 제한하여 점과의 거리를 계산
    def LinePointDistanceLimited(linePosX0, linePosY0, linePosX1, linePosY1, pointPosX, pointPosY):
        from Vector2Math import Vector2
        dir1 = Vector2(pointPosX-linePosX0, pointPosY-linePosY0)
        dir2 = Vector2(pointPosX-linePosX1, pointPosY-linePosY1)
        line1 = Vector2(linePosX1-linePosX0, linePosY1-linePosY0)
        line2 = Vector2(linePosX0-linePosX1, linePosY0-linePosY1)
        
        dot1 = dir1.Dot(line1)
        dot2 = dir2.Dot(line2)

        if dot1 > 0 and dot2 > 0:
           return Line.LinePointDistance(x1, y1, x2, y2, checkx, checky)
        
        if dot1 <= 0:
            return dir1.Length()
        
        if dot2 <= 0:
            return dir2.Length()
        
        return 1000000.0


    def LinePointDistanceSquareLimited(linePosX0, linePosY0, linePosX1, linePosY1, pointPosX, pointPosY):
        from Vector2Math import Vector2
        dir1 = Vector2(pointPosX-linePosX0, pointPosY-linePosY0)
        dir2 = Vector2(pointPosX-linePosX1, pointPosY-linePosY1)
        line1 = Vector2(linePosX1-linePosX0, linePosY1-linePosY0)
        line2 = Vector2(linePosX0-linePosX1, linePosY0-linePosY1)
        
        dot1 = dir1.Dot(line1)
        dot2 = dir2.Dot(line2)

        if dot1 > 0 and dot2 > 0:
           return Line.LinePointDistanceSquare(x1, y1, x2, y2, checkx, checky)
        
        if dot1 <= 0:
            return dir1.LengthSq()
        
        if dot2 <= 0:
            return dir2.LengthSq()
        
        return 1000000.0



    def LinePointDistanceLimitedNormal(linePosX0, linePosY0, linePosX1, linePosY1, pointPosX, pointPosY):
        from Vector2Math import Vector2
        dir1 = Vector2(pointPosX-linePosX0, pointPosY-linePosY0)
        dir2 = Vector2(pointPosX-linePosX1, pointPosY-linePosY1)
        line1 = Vector2(linePosX1-linePosX0, linePosY1-linePosY0)
        line2 = Vector2(linePosX0-linePosX1, linePosY0-linePosY1)

        dot1 = dir1.Dot(line1)
        dot2 = dir2.Dot(line2)

        lineDist, destNormalX, destNormalY = Line.LinePointDistanceNormal(linePosX0, linePosY0, linePosX1, linePosY1, pointPosX, pointPosY)

        if dot1 > 0 and dot2 > 0:
            return lineDist, destNormalX, destNormalY

        if dot1 <= 0:
            dist = dir1.Length()
            destNormalX = dir1.x
            destNormalY = dir1.y
            if dist * lineDist < 0:
                return -dist, destNormalX, destNormalY
            else:
                return dist, destNormalX, destNormalY

        if dot2 <= 0:
            dist = dir2.Length()
            destNormalX = dir2.x
            destNormalY = dir2.y
            if dist * lineDist < 0:
                return -dist, destNormalX, destNormalY
            else:
                return dist, destNormalX, destNormalY

        destNormalX = dir2.x
        destNormalY = dir2.y

        return 1000000.0



    def LinePointDistanceSquareLimitedNormal(linePosX0, linePosY0, linePosX1, linePosY1,
                                             pointPosX, pointPosY):
         from Vector2Math import Vector2
         dir1 = Vector2(pointPosX-linePosX0, pointPosY-linePosY0)
         dir2 = Vector2(pointPosX-linePosX1, pointPosY-linePosY1)
         line1 = Vector2(linePosX1-linePosX0, linePosY1-linePosY0)
         line2 = Vector2(linePosX0-linePosX1, linePosY0-linePosY1)

         dot1 = dir1.Dot(line1)
         dot2 = dir2.Dot(line2)

         lineDist, destNormalX, destNormalY = Line.LinePointDistanceNormal(linePosX0, linePosY0, linePosX1, linePosY1, pointPosX, pointPosY)

         if dot1 > 0 and dot2 > 0:
             return lineDist * lineDist, destNormalX, destNormalY

         if dot1 <= 0:
             dist = dir1.LengthSq()
             destNormalX = dir1.x
             destNormalY = dir1.y
             return dist, destNormalX, destNormalY

         if dot2 <= 0:
             dist = dir2.LengthSq()
             destNormalX = dir2.x
             destNormalY = dir2.y
             return dist, destNormalX, destNormalY

         destNormalX = dir2.x
         destNormalY = dir2.y

         return 1000000.0



    #///@brief 선과 선과 최단거리 좌표
    def LineLineNearestPosition(linePos0, lineDir0, linePos1, lineDir1):
        from Vector3Math import Vector3
        destNearestPos = Vector3

        orgTarget = Vector3.New()
        dirTarget0 = Vector3.New()
        org1 = Vector3.New()
        dir1_0 = Vector3.New()

        orgTarget = linePos0
        dirTarget0 = lineDir0
        org1 = linePos1
        dir1_0 = lineDir1

        if dirTarget0 == dir1_0:
            return False, destNearestPos
        
        dirTarget = dirTarget0.Normalize()
        dir1 = dir1_0.Normalize()
        cross = Vector3.Cross(dirTarget, dir1)
        cross.Normalize();
        
        targetZaxis = cross
        targetYaxis = dirTarget
        targetXaxis = Vector3.Cross(targetZaxis, targetYaxis)
        targetYaxis.Normalize()
        targetXaxis.Normalize()
        targetZaxis.Normalize()
        
        dir1TargetCoord = Vector3.New()
        org1TargetCoord = Vector3.New()
        dir1TargetCoord.x = targetXaxis.Dot(dir1)
        dir1TargetCoord.y = targetYaxis.Dot(dir1)
        dir1TargetCoord.z = targetZaxis.Dot(dir1)
        
        orgT = org1 - orgTarget
        org1TargetCoord.x = targetXaxis.Dot(orgT)
        org1TargetCoord.y = targetYaxis.Dot(orgT)
        org1TargetCoord.z = targetZaxis.Dot(orgT)
        
        #// assume ax + b = y and find b   for PX, VX
        lineA = dir1TargetCoord.y / dir1TargetCoord.x
        lineB = org1TargetCoord.y - lineA * org1TargetCoord.x
        destNearestPos = orgTarget + dirTarget * lineB

        return True, destNearestPos

class Polygon:
    def SameSide(p1, a, b, c):
        from Vector3Math import Vector3
        t1 = b - a
        t2 = c - b
        c1 = p1 - a
        c2 = p1 - b
        cp1 = Vector3.Cross(c1, t1)
        cp2 = Vector3.Cross(c2, t2)
        
        if cp1.Dot(cp2) < 0:
            return False
        
        t3 = a - c
        c3 = p1 - c
        cp3 = Vector3.Cross(c3, t3)
        if cp1.Dot(cp3) < 0:
            return False

        return True


    def SameSide2D(p1, a, b, c):
        from Vector3Math import Vector3
        t1 = b - a
        t2 = c - b
        
        c1 = p1 - a
        c2 = p1 - b
        
        cp1 = Vector3.Cross(c1, t1)
        cp2 = Vector3.Cross(c2, t2)
        
        if cp1.y < 0 and cp2.y > 0 or cp1.y > 0 and cp2.y < 0:
            return False
        t3 = a - c
        c3 = p1 - c
        cp3 = Vector3.Cross(c3, t3)
        if cp1.y < 0 and cp3.y > 0 or cp1.y > 0 and cp3.y < 0:
            return False
        
        return True


    def PolygonDistance(center, p1, p2):
        from Vector3Math import Vector3
        normal = MathUtil.ComputeNormal(center, p1, p2)
        return center.x * normal.x + center.y * normal.y + center.z * normal.z;
    
    def PolygonPointDistance(p0, p1, p2, point):
        from Vector3Math import Vector3

        normal = MathUtil.ComputeNormal(p0, p1, p2)
        
        polygon_distance = p0.x * normal.x + p0.y * normal.y + p0.z * normal.z
        point_distance_normal = normal.Dot(point)

        return point_distance_normal - polygon_distance

class MathUtil:
    def Max(lhs, rhs):
        if lhs>=rhs:
            return lhs
        else:
            return rhs

    def Min(lhs, rhs):
        if lhs<=rhs:
            return lhs
        else:
            return rhs
        
    def FresnelTerm(cosTheta, refractionIndex):
        g = math.sqrt(refractionIndex * refractionIndex + cosTheta * cosTheta - 1.0)
        a = g + cosTheta
        d = g - cosTheta
        result = (cosTheta * a - 1.0) * (cosTheta * a - 1.0) / ((cosTheta * d + 1.0) * (cosTheta * d + 1.0)) + 1.0
        result = result * 0.5 * d * d / (a * a)
        return result

    def RadianToDegree(radian):
        return ((radian) * (180.0 / math.pi))

    def DegreeToRadian(degree):
        return ((degree) * (math.pi / 180.0))


    def Clamp(sourceX, minRange, maxRange):

        result = float()
        if (sourceX < minRange):
            result = minRange 
        if (sourceX > maxRange):
            result = maxRange
        return result     

    def ClampValue(value, minRange, maxRange):
        if value >= minRange and value <= maxRange:
            return value
        elif value < minRange:
            return minRange
        else:
            return maxRange


	#@brief 난수 생성 0.0f~ 1.0f
    def RandomFloatPlus():
        RandomInitialized = False

        if RandomInitialized == False:
            random.seed(int(time.time()))
            RandomInitialized = True
            
        r = random.randint(0,0x7fff)
        
        return ((r) / float((0x7fff-1)))
 
    #///@brief 난수 색상 생성
    def RandomColor():
        from ColorMath import Color
        
        return Color(RandomFloatPlus(), RandomFloatPlus(), RandomFloatPlus(), RandomFloatPlus())

    #///@brief 스펙트럼 색상 생성  0..1 사이로 선택
    def SpectrumColor(r):
        from ColorMath import Color
        pos = r * 3.0;
        c = Color(0,0,0,1);
        if pos >= 0.0 and pos <= 1.0:	
            c.r = (1.0-pos)
            c.g = pos

        elif pos >= 1.0 and pos <= 2.0:
            c.g = (1.0-(pos-1.0))
            c.b = (pos-1.0)

        else:
            c.g = (2.0-(pos-2.0))
            c.r = (pos-2.0)

        return c
      
    #///@brief 난수 스펙트럼 색상 생성
    def GetRandomSpectrumColor():

        return MathUtil.SpectrumColor(MathUtil.RandomFloatPlus())

    #///@brief 난수 생성 -1.0f~ 1.0f;
    def RandomFloatPlusMinus():
        ran = MathUtil.RandomFloatPlus()
        return (ran - 0.5)*2.0

    #///@brief x의 절대값이 0.01f 보다 작은가?
    def IsNormalToolSmall(x):
        Istrue = False
        if math.fabs(x) < 0.01:
            Istrue = True
        else:
            Istrue = False

        return Istrue

    #///@brief x의 절대값이 0.00001f 보다 작은가?
    def IsNormalToolVerySmall(x):
        Istrue = False
        if math.fabs(x) < 0.00001:
            Istrue = True
        else:
            Istrue = False
           
        return Istrue

    #///@brief  Normal Vector 구하기
    
    def ComputeNormal(center, v1, v2):
        from Vector3Math import Vector3
        u = v1 - center
        v = v2 - center
        normal = Vector3()
        normal = Vector3.Cross(u, v)
        normal.Normalize()
        return normal

    def Compute2DNormal(x1, y1, x2, y2):
        from Vector3Math import Vector3
        p0 = Vector3(x1,y1,0)
        p1 = Vector3(x2,y2,0)
        p2 = Vector3(x1,y1,10)

        vout = MathUtil.ComputeNormal(p0,p1,p2)
        resultX = vout.x
        resultY = vout.y
        
        return resultX, resultY

    #///@brief p점 과 q점 같은 것 만큼 리턴값
    def CountSamePoint(p0, p1, p2, q0, q1, q2):
        cnt = 0
        if p0 == q0 or p0 == q1 or p0 == q2:
            cnt += 1
        if p1 == q0 or p1 == q1 or p1 == q2:
            cnt += 1
        if p2 == q0 or p1 == q1 or p1 == q2:
            cnt += 1
            
        return cnt

	#///@brief 점과 점 거리
    def PointPointDistance(lhs, rhs):
        return math.sqrt(MathUtil.PointPointDistanceSquare(lhs, rhs))
    #///@brief 두점간의 거리 제곱
    def PointPointDistanceSquare(lhs, rhs):
        return (lhs.x - rhs.x) * (lhs.x - rhs.x) + \
            (lhs.y - rhs.y) * (lhs.y - rhs.y)+ \
            (lhs.z - rhs.z) * (lhs.z - rhs.z)

    #///@brief 점과 평면의 거리면의 거리
    def PlanePointDistance(sourcePlane, *args):
        from Vector3Math import Vector3
        if len(args) ==3:
            testPoint = Vector3(x,y,z)

        elif len(args) ==1:
            if isinstance(args[0],Vector3):
                testPoint = args[0]

        normal = Vector3()
        normal.x = sourcePlane.a
        normal.y = sourcePlane.b
        normal.z = sourcePlane.c
        point_distance_normal = float(normal.Dot(testPoint))
        
        return point_distance_normal + sourcePlane.d

       

    #///@brief 폴리곤으로 평면 얻기
    def GetPlaneFromPolygon(p0,	p1, p2):
        from PlaneMath import Plane
        from Vector3Math import Vector3
        normal = Vector3()
        normal = MathUtil.ComputeNormal(p0, p1, p2)
        
        distance =  p0.x *normal.x +p0.y * normal.y + p0.z * normal.z
        resultPlane = Plane()
        resultPlane.a = normal.x
        resultPlane.b = normal.y
        resultPlane.c = normal.z
        resultPlane.d = float((-distance))
        return resultPlane
   
    #///@brief 평면 변환
    def PlaneTransform(sourcePlane, sourceMatrix):
        from Vector3Math import Vector3
        
        point = Vector3()
        
        if MathUtil.IsNormalToolSmall(sourcePlane.c) == False:
            point = (Vector3(0,0, -sourcePlane.d / sourcePlane.c))
        else:
            if MathUtil.IsNormalToolSmall(sourcePlane.b):
                point =( Vector3(0,-sourcePlane.d / sourcePlane.b,0))
            else:
                point =( Vector3(-sourcePlane.d / sourcePlane.a,0,0))


        normal = Vector3(sourcePlane.a ,sourcePlane.b, sourcePlane.c)
        point.TransformCoord(sourceMatrix)
        normal.TransformNormal(sourceMatrix)
        from PlaneMath import Plane
        result = Plane(Plane.PlaneFromPointNormal(point,normal))
        return result

    def GetCosine(lhsNormalVector, rhsNormalVector):
        cosine = rhsNormalVector.Dot(lhsNormalVector)

        return cosine
        

    def GetAngle(lhsNormalVector, rhsNormalVector):
        cosine = rhsNormalVector.Dot(lhsNormalVector)

        if cosine >= 1.0:
            return 0
        else:
            return math.acos(cosine)

    #///@brief 시계방향으로 얼마나 회전했는지 알아옴
    def GetDegreeAngleClockwise(lhs, rhs):
        from Vector2Math import Vector2
        from Vector3Math import Vector3
        v1 = Vector2((lhs))
        v2 = Vector2((rhs))
        v1.Normalize()
        v2.Normalize()
        
        f = v1.Dot(v2)
        
        if f >= 1.0:
            return 0.0
        angle = math.acos(f)
        
        v1_1 = Vector3(v1.x, v1.y, 0.0)
        v2_1 = Vector3(v2.x, v2.y, 0.0)
        vx = Vector3(Vector3.Cross(v1_1, v2_1))

        if vx.z > 0.0:
            angle = -angle
            
        return float((180.0 * angle / math.pi))
    # ///@brief 라인 검사
    def SameSide2DLine(p1, p2, center, centerToPoint):
        from Vector3Math import Vector3
        cp1 = Vector3()
        cp2 = Vector3()
        t1 = Vector3()
        t2 = Vector3()
        t3 = Vector3()
        
        t1 = centerToPoint-center
        t2 = p1-center
        t3 = p2-center
        
        cp1 = Vector3.Cross(t1, t2)
        cp2 = Vector3.Cross(t1, t3)
        
        if cp1.y * cp2.y >= 0:
            return True
        else:
            return False
    #///@brief 라인 검사
    def SameSideLine(p1, p2, center, centerToPoint):
        from Vector3Math import Vector3
        cp1 = Vector3()
        cp2 = Vector3()
        t1 = Vector3()
        t2 = Vector3()
        t3 = Vector3()
        
        t1 = centerToPoint-center
        t2 = p1-center
        t3 = p2-center
        
        cp1 = Vector3.Cross(t1, t2)
        cp2 = Vector3.Cross(t1, t3)
        
        check = float(cp1.Dot(cp2))
        if check >= 0:
            return True
        else:
            return False

    def LocalNormal(world, source):
        from Vector3Math import Vector3
        from MatrixMath import Matrix
        local = Vector3()
        resultWorldInverse = Matrix()
        resultWorldInverse = world
        resultWorldInverse.Inverse()
        local = Vector3.TransformNormal(source, resultWorldInverse)
        return local, resultWorldInverse;
        
    def LocalNormal(worldInverse, source):
        from Vector3Math import Vector3
        local= Vector3() 
        local = Vector3.TransformNormal(source, worldInverse)
        return local

    #///@brief 두 벡터의 시계방향 기준으로 사잇각
    def GetClockWiseAngle(lhsNormal, rhsNormal):
        from Vector3Math import Vector3
        dot = float(lhsNormal.Dot(rhsNormal))
        angle = float(math.acos(dot))

        result = Vector3()
        resultAxis = Vector3.Cross(lhsNormal, rhsNormal)
        resultAxis.Normalize()
        return angle

    #//두 벡터의 시계방향 기준으로 사잇각, 실패 조건시 return false
    def GetClockWiseAngleSafe(normal1, normal2):
        dot = float(normal1.Dot( normal2 ))
        from Vector3Math import Vector3
        if math.fabs(dot) >= 0.9999 :
            return False
        
        angle = float(math.acos(dot))
        if math.fabs(angle) <= 0.001 :
            return False
        
        resultAxis = Vector3()
        resultAngle = float()
        resultAxis = normal1.Cross( normal2 )
        resultAxis.Normalize()
        resultAngle = angle
        return True, resultAxis, resultAngle 
        
    def SphericalToCartesian(angleLatitude, angleLongitude):
        from Vector3Math import Vector3
        slong = float(math.sin(angleLongitude))
        slati = float(math.sin(angleLatitude))
        clati = float(math.cos(angleLatitude))
        clong = float(math.cos(angleLongitude))
        x = float(slong * clati)
        z = float(slong * slati)
        y = float(clong)
        return Vector3(x,y,z)

    def CartesianToSpherical(v):
        from Vector3Math import Vector3

        resultRadius = float()
        resultRadius = v.Length()
        resultAngleLatitude = float()
        resultAngleLongitude = float()
        
        resultAngleLatitude = math.atan(v.z / v.x)

        if v.x < 0:
            resultAngleLatitude += math.pi

        if resultAngleLatitude < 0:
            resultAngleLatitude += math.pi * 2
            
        resultAngleLatitude = math.fmod(resultAngleLatitude, math.pi * 2.0 )
        
        resultAngleLongitude = math.acos( v.y / resultRadius )

        return resultRadius, resultAngleLatitude, resultAngleLongitude
    
    def IsPointBounding(polygonArray, p1):
        bbox = boundingBox()
        bbox.Empty()
        bbox.Cover(polygonArray[0])
        bbox.Cover(polygonArray[1])
        bbox.Cover(polygonArray[2])
        bbox.Inflate(0.1, 0.1, 0.1)
        bbox.MultiplySize(1.1)
        if bbox.CheckInclude(p1)==False:
            return false

        if Polygon.SameSide(p1,polygonArray[0], polygonArray[1], polygonArray[2])==True:
            return True
        else: 
            return False		



class PrimitiveMesh:
    def GetCubeMesh(width, height, depth, flip):
        from Vector2Math import Vector2
        from Vector3Math import Vector3
        from BoundingBoxMath import BoundingBox

        w = width / 2
        h = height / 2
        d = depth / 2

        pos = [Vector3(-w, -h, -d), Vector3(w, -h, -d), Vector3(w, -h, d), Vector3(-w, -h, d),\
            Vector3(-w, h, -d), Vector3(w, h, -d), Vector3(w, h, d), Vector3(-w, h, d)]

        box = BoundingBox(Vector3(-w, -h, -d), Vector3(w, h, d))

        normal = [Vector3(0, -1, 0), Vector3(0, 0, -1), Vector3(1, 0, 0),\
            Vector3(0, 0, 1), Vector3(-1, 0, 0), Vector3(0, 1, 0)]

        uv = [Vector2(0, 1), Vector2(0, 0), Vector2(1, 0), Vector2(1, 1)]

        positions = [pos[0], pos[1], pos[2], pos[3],\
            pos[0], pos[4], pos[5], pos[1],\
            pos[1], pos[5], pos[6], pos[2],\
            pos[2], pos[6], pos[7], pos[3],\
            pos[3], pos[7], pos[4], pos[0],\
            pos[4], pos[7], pos[6], pos[5]]

        normals = list()
        n = 0
        for k in range(0, 6):
            normals.append(normal[n])
            normals.append(normal[n])
            normals.append(normal[n])
            normals.append(normal[n])
            n += 1

        uvs = list()
        for k in range(0, 6):
            uvs.append(uv[0])
            uvs.append(uv[1])
            uvs.append(uv[2])
            uvs.append(uv[3])

        index1 = [0, 3, 1, 1, 3, 2,\
                  0+4, 3+4, 1+4, 1+4, 3+4, 2+4,\
                  0+8, 3+8, 1+8, 1+8, 3+8, 2+8,\
                  0+12, 3+12, 1+12, 1+12, 3+12, 2+12,\
                  0+16, 3+16, 1+16, 1+16, 3+16, 2+16,\
                  0+20, 3+20, 1+20, 1+20, 3+20, 2+20]
        
        index2 = [0, 1, 3, 1, 2, 3,\
            0+4, 1+4, 3+4, 1+4, 2+4, 3+4,\
            0+8, 1+8, 3+8, 1+8, 2+8, 3+8,\
            0+12, 1+12, 3+12, 1+12, 2+12, 3+12,\
            0+16, 1+16, 3+16, 1+16, 2+16, 3+16,\
            0+20, 1+20, 3+20, 1+20, 2+20, 3+20]

        resultIndex = index1
        
        if flip:
            resultIndex = index2

        return 12, positions, resultIndex, normals, uvs, box

    def GetCylinderMesh(radius, height, flip):
        from Vector2Math import Vector2
        from Vector3Math import Vector3
        from BoundingBoxMath import BoundingBox

        h = height / 2
        size = (3*1*32) + (3*1*32) + (3*2*32)
        basePos = list()
        baseIndex1 = [None] * size
        baseIndex2 = [None] * size
        
        basePos.append(Vector3(0,-1,0))

        #position
        j = 0
        for i in range(1,66):
            theta = (2 * math.pi) * (i / 32)
            basePos.append(Vector3(radius * math.cos(theta), -1, radius * math.sin(theta)))

            if i >= 33:
                basePos[i] = Vector3(basePos[i - 33])
                basePos[i].y = h

        basePos[33] = Vector3(0, h, 0)

        box = BoundingBox(Vector3(-radius, -h, -radius), Vector3(radius, h, radius))

        positions = [Vector3.New()] * (128 + 66)

        for idx in range(0,66):
            positions[idx] = Vector3(basePos[idx])

        posIdx = 0
        for i in range(0,31):
            positions[posIdx + 66] = Vector3(basePos[i + 1])
            positions[posIdx + 67] = Vector3(basePos[i + 34])
            positions[posIdx + 68] = Vector3(basePos[i + 35])
            positions[posIdx + 69] = Vector3(basePos[i + 2])
            posIdx += 4

        positions[190] = Vector3(basePos[32])
        positions[191] = Vector3(basePos[65])
        positions[192] = Vector3(basePos[34])
        positions[193] = Vector3(basePos[1])

        #uvs
        uv = [Vector3.New()] * (128 + 66)

        for i in range(0, 66):
            uv[i] = Vector2((basePos[i].x + radius) / 2 * radius, (1 - (basePos[i].z + radius) / 2 * radius))

        uvx = 1
        for i in range(66, 194, 4):
            uv[i] = Vector2(uvx / 16, 1)
            uv[i+1] = Vector2(uvx / 16, 0)
            uv[i+2] = Vector2(uvx + 1 / 16, 0)
            uv[i+3] = Vector2(uvx + 1 / 16, 1)

            if uvx + 1 / 16 == 1:
                uvx = 0
            else:
                uvx += 1

        uvs = [Vector2.New()] * 194

        for i in range(0,194):
            uvs[i] = Vector2(uv[i])

        #normal
        normal = [Vector3(0, -1, 0), Vector3(0, 1, 0)]

        normals = [Vector3.New()] * 194

        nidx = 0
        n = 0
        g = 0

        for j in range(0,32):
            normals[j] = Vector3(normal[0])
            normals[j+33] = Vector3(normal[1])

        normals[32] = Vector3(normal[0])
        normals[65] = Vector3(normal[1])

        for i in range(0,31):
            normals[nidx + 66] = Vector3(basePos[i+1].x, 0, basePos[i+1].z)
            normals[nidx + 67] = Vector3(basePos[i+34].x, 0, basePos[i+34].z)
            normals[nidx + 68] = Vector3(basePos[i+35].x, 0, basePos[i+35].z)
            normals[nidx + 69] = Vector3(basePos[i+2].x, 0, basePos[i+2].z)
            nidx += 4

        normals[190] = Vector3(basePos[32].x, 0, basePos[32].z)
        normals[191] = Vector3(basePos[65].x, 0, basePos[65].z)
        normals[192] = Vector3(basePos[34].x, 0, basePos[65].z)
        normals[193] = Vector3(basePos[1].x, 0, basePos[1].z)

        #indices
        #//1.밑면 - 반시계 윗면 시계 - 옆면 - 반시계로 그림

        idx = 0
        k = 0
        sideIndex = 0
        for i in range(0,32):
            baseIndex1[idx] = 0
            baseIndex1[idx + 96] = 33
            baseIndex1[sideIndex + 192] = k + 66
            baseIndex1[sideIndex + 195] = k + 69
            
            if i == 31:
                baseIndex1[idx + 1] = 32
                baseIndex1[idx + 2] = 1
                baseIndex1[idx + 97] = 34
                baseIndex1[idx + 98] = 65
            else:
                baseIndex1[idx + 1] = i + 1
                baseIndex1[idx + 2] = i + 2
                baseIndex1[idx + 97] = i + 35
                baseIndex1[idx + 98] = i + 34
                
            baseIndex1[sideIndex + 193] = k + 67
            baseIndex1[sideIndex + 194] = k + 69
            baseIndex1[sideIndex + 196] = k + 67
            baseIndex1[sideIndex + 197] = k + 68
            
            idx = idx + 3
            sideIndex = sideIndex + 6
            k = k + 4
        #//2.밑면 - 시계 윗면 - 반시계 - 옆면 - 시계로 그림
        k = 0
        idx = 0
        sideIndex = 0
        for i in range(0,6):
            baseIndex2[idx] = 0
            baseIndex2[idx + 18] = 7
            baseIndex2[sideIndex + 36] = k + 14
            baseIndex2[sideIndex + 39] = k + 17
            
            if i == 5:
                baseIndex2[idx + 1] = 6
                baseIndex2[idx + 2] = 1
                baseIndex2[idx + 19] = 13
                baseIndex2[idx + 20] = 8
            else:
                baseIndex2[idx + 1] = i + 2
                baseIndex2[idx + 2] = i + 1
                baseIndex2[idx + 19] = i + 8
                baseIndex2[idx + 20] = i + 9

            baseIndex2[sideIndex + 37] = k + 17
            baseIndex2[sideIndex + 38] = k + 15
            baseIndex2[sideIndex + 40] = k + 16
            baseIndex2[sideIndex + 41] = k + 15
            
            idx = idx + 3
            sideIndex = sideIndex + 6
            k = k + 4
        indices = baseIndex2
        if flip:
            indices = baseIndex1
        
        return size / 3, positions, indices, normals, uvs, box


    def GetGeometricSphereMesh(radius, latitutionalCut, longitutionalCut, useRect, oneEndVertex):
        from Vector2Math import Vector2
        from Vector3Math import Vector3
        from BoundingBoxMath import BoundingBox
        
        indexArray = list()
        posArray = list()
        uvArray = list()

        xcut = latitutionalCut
        ycut = longitutionalCut

        linePosArray = [Vector3.New()] * (xcut + 1)
        lineUVArray = [Vector2.New()] * (xcut + 1)

        angleUnitX = 2 * math.pi / xcut
        angleUnitY = math.pi / ycut
        
        switchIndex = False
        angleY = 0
        uvx = 0
        uvy = 0
        rangeFrom = 0
        rangeTo = 0
        endIndex = 0

        for y in range(0, ycut):
            if y == 0:
                if oneEndVertex:
                    posArray.append(Vector3(0, 1, 0))
                    uvArray.append(Vector2(0,0))
                    continue
                else:
                    uvy = angleY / math.pi
                    rangeFrom = len(posArray)
                    
                    shiftAngleX = (angleUnitX * switchIndex) / 2
                    angleX = shiftAngleX

                    for x in range(0, xcut):
                        linePosArray[x] = Vector3(0, 1, 0)
                        uvx = angleX / (2 * math.pi)
                        lineUVArray[x] = Vector2(uvx, uvy)
                        angleX += angleUnitX
                        posArray.append(Vector3(linePosArray[x]))
                        uvArray.append(Vector2(lineUVArray[x]))

                    rangeTo =len(posArray)
            
            if y == ycut:
                if oneEndVertex:
                    posArray.append(Vector3(0, -1, 0))
                    endIndex = len(posArray)
                    uvArray.append(Vector2(0,1))
                else:
                    uvy = angleY / math.pi
                    rangeFrom = len(posArray)
                    shiftAngleX = ((angleUnitX * switchIndex) / 2)
                    angleX = shiftAngleX
                    
                    for  x in range(0, xcut):
                        linePosArray[x] = Vector3(0, -1, 0)
                        uvx = angleX / (2 * math.pi)
                        lineUVArray[x] = Vector2( uvx, uvy )
                        angleX += angleUnitX
                        posArray.append(Vector3(linePosArray[x]))
                        uvArray.append(Vector2(lineUVArray[x]))
                    rangeTo = len(posArray)
            else:
                uvy = angleY / math.pi
                rangeFrom = len(posArray)
                
                if useRect:
                    shiftAngleX = 0
                else:
                    shiftAngleX = angleUnitX * switchIndex / 2
                
                angleX = shiftAngleX
                
                for x in range(0, xcut):
                    v = MathUtil.SphericalToCartesian(angleX, angleY)
                    linePosArray[x] = v
                    uvx = angleX / (2 * math.pi)
                    lineUVArray[x] = Vector2(uvx, uvy)
                    posArray.append(linePosArray[x])
                    uvArray.append(lineUVArray[x])
                    angleX += angleUnitX
                rangeTo = len(posArray)

            if y == 1:
                if oneEndVertex:
                    startIndex = 0
                    for i in range(rangeFrom, rangeTo):
                        indexArray.append(startIndex)
                        indexArray.append(i + 1)
                        indexArray.append(i)
                else:
                    for i in range(rangeFrom, rangeTo):
                        p00 = i - (xcut+1)
                        p01 = i
                        p10 = i - (xcut+1) + 1
                        p11 = i + 1
                        
                        indexArray.append(p10)
                        indexArray.append(p11)
                        indexArray.append(p01)
            else:
                if oneEndVertex and y == ycut:
                    if oneEndVertex:
                        for i in range(rangeFrom, rangeTo):
                            indexArray.append(i)
                            indexArray.append(i+1)
                            indexArray.append(endIndex)
                    else:
                        for i in range(rangeFrom, rangeTo):
                            p00 = i - (xcut+1)
                            p01 = i
                            p10 = i - (xcut+1) + 1
                            indexArray.append(p00)
                            indexArray.append(p10)
                            indexArray.append(p01)
                else:
                    for i in range(rangeFrom, rangeTo):
                        p00 = i - (xcut+1)
                        p01 = i
                        p10 = i - (xcut+1) + 1
                        p11 = i + 1
                        
                        indexArray.append(p00)
                        indexArray.append(p10)
                        indexArray.append(p01)
                        indexArray.append(p10)
                        indexArray.append(p11)
                        indexArray.append(p01)

            angleY += angleUnitY
            switchIndex ^= True
            
            normals = list()
            import copy
            normals = copy.deepcopy(posArray)

            for i in posArray:
                i *= radius

            primitiveCount = len(indexArray) / 3

            box = BoundingBox(Vector3(-radius, -radius, -radius), Vector3(radius, radius, radius))
            
            
        return primitiveCount, posArray, indexArray, normals, uvArray, box


    def GetUIMesh(size, flip):
        from Vector2Math import Vector2
        from Vector3Math import Vector3
        from BoundingBoxMath import BoundingBox
        pos = [Vector3(-size, -size, 0), Vector3(size, size, 0), Vector3(size, size, 0), Vector3(-size, size, 0)]

        box = BoundingBox(Vector3(-size, -size, 0), Vector3(size, size, 0))

        uv = [Vector2(1,1), Vector2(0,1), Vector2(0,0), Vector2(1,0)]

        uvs = [Vector2(uv[1]), Vector2(uv[0]), Vector2(uv[3]), Vector2(uv[2])]

        index1 = [0, 3, 1, 1, 3, 2]
        index2 = [0, 1, 3, 1, 2, 3]

        indexArray = index1

        if flip:
            indexArray = index2

        return 2, pos, indexArray, uvs, box
               				
class EaseTypeCurve():
    PI = 3.14159274
    PI2 = 1.57079637
    
    def enum(*sequential, **named):
        enums = dict(zip(sequential, range(len(sequential))), **named)
        reverse = dict((value, key) for key, value in enums.items())
        enums['reverse_mapping'] = reverse
        return type('Enum', (), enums)

    EaseType = enum("Linear",\
        "EaseInSine", "EaseOutSine","EaseInOutSine",\
        "EaseInQuad", "EaseOutQuad","EaseInOutQuad",\
        "EaseInCubic","EaseOutCubic","EaseInOutCubic",\
        "EaseInQuart","EaseOutQuart","EaseInOutQuart",\
        "EaseInQuint","EaseOutQuint","EaseInOutQuint",\
        "EaseInExpo", "EaseOutExpo", "EaseInOutExpo",\
        "EaseInCric", "EaseOutCric", "EaseInOutCric",\
        "EaseInBack", "EaseOutBack", "EaseInOutBack",\
        "EaseInElastric", "EaseOutElastric", "EaseInOutElastric",\
        "EaseInBounce", "EeaseOutBounce", "EaseInOutBounce")
    
    def GetEaseValue(begin, end, t, easyType):

        if easyType == EaseTypeCurve.EaseType.Linear:
            return (end - begin) * t + begin;
        
        myCode = "(" + str(end) + "-" + str(begin) + ") * EaseTypeCurve." + EaseTypeCurve.EaseType.reverse_mapping[easyType] + "(" + str(t) + ") + " + str(begin)
        return eval(myCode)
    
    #print(EaseTypeCurve.EaseType.reverse_mapping[0])

    def Linear(begin, end, t):
        return (end-begin) * t + begin

    def EaseInSine(t):
        return -math.cosf(t * EaseTypeCurve.PI2) + 1.0;

    def EaseOutSine(t):
        return math.sin(t * EaseTypeCurve.PI2)

    def EaseInOutSine(t):
        return -0.5 * (math.sinf(EaseTypeCurve.PI * t) - 1.0)

    def EaseInQuad(t):
        return t * t

    def EaseOutQuad(t):
        return -t * (t - 2.0)

    def EaseInOutQuad(t):
        t *= 2.0
        if t < 1.0:
            return 0.5 * t * t
        return -0.5 * ( (t-1.0) * (t - 2.0) - 1.0)
    
    def EaseInCubic(t):
        return t * t * t
    
    def EaseOutCubic(t):
        
        return (t-1.0) * t * t + 1.0
    
    def EaseInOutCubic(t):
        t *= 2.0
        if t < 1.0:
            return 0.5 * t * t * t
        t -= 2.0
        return 0.5 * (t * t * t + 2.0)

    def EaseInQuart(t):
        return t * t * t * t
    
    def EaseOutQuart(t):
        return -((t-1.0) * t * t * t - 1.0)
    
    def EaseInOutQuart(t):
        t *= 2.0
        if t < 1.0:
            return 0.5 * t * t * t * t
        t -= 2
        return -0.5 * (t * t * t * t - 2.0)
    
    def EaseInQuint(t):
        return t * t * t * t * t
    
    def EaseOutQuint(t):
        return -((t-1.0) * t * t * t * t - 1.0)
    
    def EaseInOutQuint(t):
        t *= 2.0
        if t < 1.0:
            return 0.5 * t * t * t * t * t
        t -= 2.0
        return -0.5 * (t * t * t * t * t - 2.0)
    
    def EaseInExpo(t):
        if t == 0.0:
            return 0.0
        return pow(2.0, 10.0 * (t - 1.0))

    def EaseOutExpo(t):
        if t == 1.0:
            return 1.0
        return pow(2.0, -10.0 * t) + 1.0

    def EaseInOutExpo(t):
        if t == 0.0:
            return 0.0
        if t == 1.0:
            return 1.0
        t *= 2.0
        if t < 1.0:
            return 0.5 * pow(2.0, 10.0 * (t - 1.0))
        return 0.5 * (-pow(2.0, -10.0 * (t-1.0)) + 2.0)

    def EaseInCric(t):
        return -(math.sqrt(1.0 - t * t) - 1.0)

    def EaseOutCric(t):
        return math.sqrt(1.0 - (t-1.0) * t)

    def EaseInOutCric(t):
        t *= 2.0
        if t < 1.0:
            return -0.5 * (math.sqrt(1.0 - t * t) - 1.0)
        t -= 2.0
        return 0.5 * (math.sqrt(1.0 - t * t) + 1.0)

    def EaseInBack(t):
        s = 1.70158
        return t * t * ((s + 1.0) * t - s)

    def EaseOutBack(t):
        s = 1.70158
        return ((t-1.0) * t * ((s + 1.0) * t + s) + 1.0);

    def EaseInOutBack(t):
        s = 1.70158 * 1.525
        t *= 2.0
        if t < 1.0:
            return 0.5 * (t * t * ((s + 1.0) * t - s))
        t -= 2.0
        return 0.5 * (t * t * ((s + 1.0) * t + s) + 2.0)

    def EaseInElastric(t):
        if t == 0.0:
            return 0.0
        if t == 1.0:
            return 1.0
        return -(pow(2.0, 10.0 * (t-1.0)) * math.sin((t / 0.3 - 0.25) * (2.0 * PI)))

    def EaseOutElastric(t):
        if t == 0.0:
            return 0.0
        if t == 1.0:
            return 1.0
        return (pow(2.0, -10.0 * t) * math.sinf((t / 0.3 - 0.25) * (2.0 * PI)) + 1.0)

    def EaseInOutElastric(t):
        if (t == 0.0):
            return 0.0
        if t == 1.0:
            return 1.0
        t = t * 2.0 - 1.0
        if t < 1.0:
            return -0.5 * pow(2.0, 10.0 * t) * math.sin((t / 0.3 * 1.5 - 0.25) * 2.0 * PI)
        return pow(2.0, -10.0 * t) * math.sin((t / 0.3 * 1.5 - 0.25) * 2.0 * PI) * 0.5 + 1.0

    def EaseInBounce(t):
        return 1.0 - EaseOutBounce(1.0 - t)

    def EaseOutBounce(t):
        if t < (1 / 2.75):
            return 7.5625 * t * t
        elif t < (2.0 / 2.75):
            t -= 1.5 / 2.75
            return (7.5625 * t * t + 0.75)
        elif t < (2.5 / 2.75):
            t -= 2.25 / 2.75
            return (7.5625 * t * t + 0.9375)
        else:
            t -= 2.625 / 2.75
            return (7.5625 * t * t + 0.984375)

    def EaseInOutBounce(t):
        if t < 0.5:
            return EaseInBounce(t * 2.0) * 0.5
        return EaseOutBounce(t * 2.0 - 1.0) * 0.5 + 0.5

    def LinearInterpolate(v1, v2, r1):
        return (T)(v1 * (1.0 - r1) + v2 * r1)

    def LinearInterpolate(v2, r1):
        return LinearInterpolate(v2[0], v2[1], r1)

    def BilinearInterpolate(v11, v21, v12, v22, rx, ry):
        v1 = LinearInterpolate(v11, v21, rx)
        v2 = LinearInterpolate(v12, v22, rx)
        return LinearInterpolate( v1, v2, ry)

    def BilinearInterpolate(v4, rx, ry):
        return BilinearInterpolate(v4[0],v4[1],v4[2],v4[3],rx,ry)

    def TrilinearInterpolate(v111, v211, v121, v221, v112, v212, v122, v222, rx, ry, rz):
        v1 = BilinearInterpolate(v111, v211, v121, v221, rx, ry)
        v2 = BilinearInterpolate(v112, v212, v122, v222, rx, ry)
        return LinearInterpolate(v1, v2, rz)

    def TrilinearInterpolate(v8, rx, ry, rz):
        return TrilinearInterpolate(v8[0], v8[1], v8[2], v8[3], v8[4], v8[5], v8[6], v8[7], rx, ry, rz)

    def QuadricBezierSpline(v1, v2, v3, r1):
        b1 = (v2 - v1) * r1 + v1
        b2 = (v3 - v2) * r1 + v2
        return (b2 - b1) * r1 + b1
    
    def CubicBezierSpline(v1, v2, v3, v4, r1):
        b1 = QuadricBezierSpline(v1, v2, v3, r1)
        b2 = QuadricBezierSpline(v2, v3, v4, r1)
        return (b2 - b1) * r1 + b1

    def BSpline(v1, m1, v2, m2, r1, length):
        rv = v1 + m1 / 3 * length
        lv = v2 - m2 / 3 * length
        return CubicBezierSpline(v1, rv, lv, v2, r1)

    def CatmullRomSpline(v1, v2, v3, v4, r1):
        return 0.5 * (2.0 * v2 + (v3 - v1) * r1 + (2.0 * v1 - 5.0 * v2 + 4.0 * v3 - v4) * r1 * r1 + (v4 - 3.0 * v3 + 3.0 * v2 - v1) * r1 * r1 * r1)

