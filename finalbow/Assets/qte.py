import math

class qte(Actor.Actor):
    
    go = 0
    stop = 0

    def __init__(self):
        self.Container = Container(0)
        return

    def OnCreate(self,uid):
        self.ConTrans = self.Container.FindComponentByType("TransformGroup")
        self.ConAngle = self.ConTrans.GetRotation()

        return 0 

    def OnDestroy(self):
        return 0 
    def OnEnable(self):
        return 0 
    def OnDisable(self):
        return 0 
    def Update(self):
        print("from",self.ConAngle.w,self.ConAngle.x,self.ConAngle.y,self.ConAngle.z)

        Euler_to = self.Quaternion_toEulerianAngle(self.ConAngle.w,self.ConAngle.x,self.ConAngle.y,self.ConAngle.z)
        print(math.degrees(Euler_to[0]),math.degrees(Euler_to[1]),math.degrees(Euler_to[2]))
        
        Quaternion_to = self.Euler_toQuaternion(Euler_to[0],Euler_to[1],Euler_to[2])

        print("to",Quaternion_to[0],Quaternion_to[1],Quaternion_to[2],Quaternion_to[3])
  
        return

    def OnMessage(self, msg, number, Vector4_lparm, Vector4_wparam):

        
            return
    def Quaternion_toEulerianAngle(self,w,x, y, z):
        
        ysqr=y*y
        t0 = 2.0*(w*x+y*z)
        t1 = +1.0 - 2.0 * (x*x + ysqr)
        X = math.atan2(t0, t1)

        t2 = +2.0 * (w*y - z*x)
        t2 =  1 if t2 > 1 else t2
        t2 = -1 if t2 < -1 else t2
        Y = math.asin(t2)

        t3 = +2.0 * (w * z + x*y)
        t4 = +1.0 - 2.0 * (ysqr + z*z)
        Z = math.atan2(t3, t4)
        
        return X, Y, Z
    
    def Euler_toQuaternion(self,x,y,z):

        t0 = math.cos(z*0.5)
        t1 = math.sin(z*0.5)
        t2 = math.cos(y*0.5)
        t3 = math.sin(y*0.5)
        t4 = math.cos(x*0.5)
        t5 = math.sin(x*0.5)

        qw = t0 * t2 * t4 + t1 * t3 * t5
        qx = t0 * t3 * t4 - t1 * t2 * t5
        qy = t0 * t2 * t5 + t1 * t3 * t4
        qz = t1 * t2 * t4 - t0 * t3 * t5

        return qw,qx,qy,qz 