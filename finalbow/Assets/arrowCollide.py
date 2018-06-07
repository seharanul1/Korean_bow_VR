
import math
class arrowCollide(Actor.Actor):

    go = 0
    stop = 0
    speed = 0.2

    def __init__(self):
        self.ArrowContainer = Container(0)
        return

    def OnCreate(self,uid):

        self.ArrowTrans = self.ArrowContainer.FindComponentByType("TransformGroup");
        self.CurPos = self.ArrowTrans.GetPosition()
        self.CurRot = self.ArrowTrans.GetRotation()
        #self.CurArrowPos = [self.CurPos.x,self.CurPos.y,self.CurPos.z]

        return 0

    def OnDestroy(self):
        return 0 
    def OnEnable(self):
        return 0 
    def OnDisable(self):
        return 0 
    def Update(self):
        
        
        if(self.stop==0):
            self.go+=self.speed
            self.speed-=0.0022
            self.ArrowTrans.SetPosition(Math3d.Vector3(self.CurPos.x,self.CurPos.y-self.go/8,self.CurPos.z+self.go))
        return

    def OnMessage(self, msg, number, Vector4_lparm, Vector4_wparam):

        if msg == "stopArrow":
            self.stop=1
            
            return