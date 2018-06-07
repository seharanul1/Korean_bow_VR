import math
class BowScript(Actor.Actor):
    
    animationLength = 0.0      
    time = 0.0

    pull = False

    def __init__(self):
        self.BowContainer = Container(0)
        
        return
    

        
    def OnCreate(self,uid):
        
        
        self.BowFbx = self.BowContainer.FindComponentByType("Fbx")
        self.animationLength = self.BowFbx.GetAnimationLength(0)
        print(self.animationLength, "animation length")
        #self.BowFbx.Pause()
        #self.BowFbx.SetAnimationCurrentTime(0)
       
        return 0
  

    def OnDestroy(self):
        return 0 
    def OnEnable(self):
        return 0 
    def OnDisable(self):
        return 0 


    def Update(self):

        
        #print(self.time)
        if self.pull == True:
            #최대로 당겼을 때 
            if self.time < 0.79:   
                self.time += 0.01
            #self.BowFbx.SetAnimationCurrentTime(self.time)
        #elif self.time != 0.0:
        #    self.time += 0.01
            
        self.BowFbx.SetAnimationCurrentTime(self.time) 
        #if self.time >= self.animationLength :
        #    self.BowFbx.Pause()
        #    self.time = 0.0

        
        #self.BowFbx.SetAnimationCurrentTime(self.time)
        #print(self.BowFbx.GetAnimationCurrentTime())
         
        return

        
     
    def OnMessage(self, msg, number, Vector4_lparm, Vector4_wparam):
        if msg == "RButtonDown" : #거리에 따라
            self.pull = True
            
        if msg == "RButtonUp" and self.pull == True : #trigger 때면
            self.pull = False
            if self.time < 0.78 :
                self.BowFbx.SetAnimationCurrentTime(0.83)
                self.time = 0.83
            self.BowFbx.Play()
        if msg=="BowAni":
            ch = 0.0
            if(number<0):
                ch = 0.0
            else:
                ch = number

            ch2 = ch/10000
            self.time=ch2/1.3*0.7
            print("now ani" + str(ch2/1.3*0.7))

        if msg=="Bowstart":
            self.BowFbx.SetAnimationCurrentTime(0)

            
        
        #print(self.time)
                   
        return
