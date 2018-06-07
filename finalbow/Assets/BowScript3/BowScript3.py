import math
class BowScript3(Actor.Actor):
    
    animationLength = 0.0      
    time = 0.0

    pull = False
    ispulled = False
    fullypulled = False

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

        
        
        if (self.pull == True):
            #최대로 당겼을 때
            self.ispulled=True 
            if self.time < 0.72:   
                self.time += 0.003
            else :
                self.fullypulled=True

            

        elif (self.pull == False):
            if(self.ispulled==True):
                if(self.fullypulled==True):
                    if(0.72<self.time<self.animationLength):
                        self.time+=0.003
                    else:
                        self.ispulled=False
                        self.fullypulled=False
                        self.time=0

                else:
                    if(self.time>0):
                        self.time-=0.003
                    else:
                        self.ispulled=False
                        self.fullypulled=False
                        self.time=0
                        
                
        print(self.time)
        self.BowFbx.SetAnimationCurrentTime(self.time)

        return

     
    def OnMessage(self, msg, number, Vector4_lparm, Vector4_wparam):
        if msg == "RButtonDown" :
            self.pull = True
            
            
        if msg == "RButtonUp" :
            self.pull = False
            
            
        
                         
        return
