import math

class QuaterniontoEuler(Actor.Actor):
    
    def __init__(self):
        self.TargetContainer = Container(0)

        return

    def OnCreate(self,uid):

       
        self.TargetTrans = self.TargetContainer.FindComponentByType("TransformGroup")
        
        self.TargetAngle = self.TargetTrans.GetRotation()

        return
    def OnDestroy(self):
        return 0 
    def OnEnable(self):
        return 0 
    def OnDisable(self):
        return 0 
    def Update(self):
        
        
        

        self.CheckCollide(TargetBox.OBBIntersect(ArrowBox))
        
        
        return


    def toEulerianAngle(self,x,y,z,w):
        ysqr =y * y
	# roll (x-axis rotation)
    
	    t0 = 2.0*w*x+y*z
        t1 = 1.0 - 2.0 *(x *x + ysqr)
        roll = math.atan2(t0, t1)

	# pitch (y-axis rotation)
	    t2 = +2.0 * (q.w() * q.y() - q.z() * q.x())
        t2 = ((t2 > 1.0) ? 1.0 : t2)
        t2 = ((t2 < -1.0) ? -1.0 : t2)
        pitch = math.asin(t2);

	# yaw (z-axis rotation)
	    t3 = +2.0 * (q.w() * q.z() + q.x() * q.y())
        t4 = +1.0 - 2.0 * (ysqr + q.z() * q.z())
        yaw = math.atan2(t3, t4)

        return (roll,pitch,yaw)
