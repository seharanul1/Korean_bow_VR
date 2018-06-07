class TargetScript(Actor.Actor):
    

    arrow_hit1 = 0




    def __init__(self):
        self.TargetContainer1 = Container(0)
        self.TargetContainer2 = Container(0)
        self.TargetContainer3 = Container(0)
        self.TargetContainer4 = Container(0)
        self.TargetContainer5 = Container(0)
        self.TargetContainer6 = Container(0)
        self.TargetContainer7 = Container(0)
        self.TargetContainer8 = Container(0)
        self.TargetContainer9 = Container(0)
        self.TargetContainer0 = Container(0)

        self.ArrowContainer1 = Container(0)
        

        self.ScoreContainer = Container(0) 

        self.SoundContainer = Container(0)
       
        return

    def OnCreate(self,uid):

        self.world = GetWorldContainer().FindComponentByType("World")

        if(self.world == None):
            print("World None")
            return

        self.TargetTrans1 = self.TargetContainer1.FindComponentByType("TransformGroup")
        self.TargetTrans2 = self.TargetContainer2.FindComponentByType("TransformGroup")
        self.TargetTrans3 = self.TargetContainer3.FindComponentByType("TransformGroup")
        self.TargetTrans4 = self.TargetContainer4.FindComponentByType("TransformGroup")
        self.TargetTrans5 = self.TargetContainer5.FindComponentByType("TransformGroup")
        self.TargetTrans6 = self.TargetContainer6.FindComponentByType("TransformGroup")
        self.TargetTrans7 = self.TargetContainer7.FindComponentByType("TransformGroup")
        self.TargetTrans8 = self.TargetContainer8.FindComponentByType("TransformGroup")
        self.TargetTrans9 = self.TargetContainer9.FindComponentByType("TransformGroup")
        self.TargetTrans0 = self.TargetContainer0.FindComponentByType("TransformGroup")

        self.ArrowTrans1 = self.ArrowContainer1.FindComponentByType("TransformGroup")
        self.ArrowScriptComponent1 = self.ArrowContainer1.FindComponentByType("ScriptComponent")
        self.ArrowScript1 = self.ArrowScriptComponent1.GetActor()

        
      
        self.SoundScriptComponent = self.SoundContainer.FindComponentByType("ScriptComponent")
        self.SoundScript = self.SoundScriptComponent.GetActor()

        self.ScoreTrans = self.ScoreContainer.FindComponentByType("TransformGroup")
        
        

        return 0

    def OnDestroy(self):
        return 0 
    def OnEnable(self):
        return 0 
    def OnDisable(self):
        return 0 
    def Update(self):
        
        TargetBox1 = self.TargetTrans1.GetSumBox()
        TargetBox2 = self.TargetTrans2.GetSumBox()
        TargetBox3 = self.TargetTrans3.GetSumBox()
        TargetBox4 = self.TargetTrans4.GetSumBox()
        TargetBox5 = self.TargetTrans5.GetSumBox()
        TargetBox6 = self.TargetTrans6.GetSumBox()
        TargetBox7 = self.TargetTrans7.GetSumBox()
        TargetBox8 = self.TargetTrans8.GetSumBox()
        TargetBox9 = self.TargetTrans9.GetSumBox()
        TargetBox0 = self.TargetTrans0.GetSumBox()

        ArrowBox1 = self.ArrowTrans1.GetSumBox()
        
        

        self.CheckCollide1(TargetBox1.OBBIntersect(ArrowBox1))
        self.CheckCollide1(TargetBox2.OBBIntersect(ArrowBox1))
        self.CheckCollide1(TargetBox3.OBBIntersect(ArrowBox1))
        self.CheckCollide1(TargetBox4.OBBIntersect(ArrowBox1))
        self.CheckCollide1(TargetBox5.OBBIntersect(ArrowBox1))
        self.CheckCollide1(TargetBox6.OBBIntersect(ArrowBox1))
        self.CheckCollide1(TargetBox7.OBBIntersect(ArrowBox1))
        self.CheckCollide1(TargetBox8.OBBIntersect(ArrowBox1))
        self.CheckCollide1(TargetBox9.OBBIntersect(ArrowBox1))
        self.CheckCollide1(TargetBox0.OBBIntersect(ArrowBox1))

        
        
        return 

    
    def CheckCollide1(self , colVal):
      
        if colVal == True :
            #print("!!Collide!!")
            if self.arrow_hit1 == 0 :
                self.ArrowScript1.OnMessage("stopArrow",0,Math3d.Vector4(0,0,0,0),Math3d.Vector4(0,0,0,0))
                self.SoundScript.OnMessage("clap",0,Math3d.Vector4(0,0,0,0),Math3d.Vector4(0,0,0,0))
                self.ScoreTrans.PropTransform.SetShow(1)
                self.arrow_hit1 = 1
               
        return
    

    def OnMessage(self, msg, number, Vector4_lparm, Vector4_wparam):
        
        if(msg=="targetready"):
            self.arrow_hit1=0
        

        return;
