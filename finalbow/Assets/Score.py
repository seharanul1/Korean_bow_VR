class Score(Actor.Actor):
    
    curScore = 0


    def __init__(self):
        
        self.ButtonContainer0 = Container(0)
        self.ButtonContainer1 = Container(0)
        self.ButtonContainer2 = Container(0)
        self.ButtonContainer3 = Container(0)
        self.ButtonContainer4 = Container(0)
        self.ButtonContainer5 = Container(0)
        self.ButtonContainer6 = Container(0)
        self.ButtonContainer7 = Container(0)
        self.ButtonContainer8 = Container(0)
        self.ButtonContainer9 = Container(0)
        self.ButtonContainer10 = Container(0)

        return

    def OnCreate(self, uid):
        self.ButtonTrans0 = self.ButtonContainer0.FindComponentByType("TransformGroup")
        self.ButtonTrans1 = self.ButtonContainer1.FindComponentByType("TransformGroup")
        self.ButtonTrans2 = self.ButtonContainer2.FindComponentByType("TransformGroup")
        self.ButtonTrans3 = self.ButtonContainer3.FindComponentByType("TransformGroup")
        self.ButtonTrans4 = self.ButtonContainer4.FindComponentByType("TransformGroup")
        self.ButtonTrans5 = self.ButtonContainer5.FindComponentByType("TransformGroup")
        self.ButtonTrans6 = self.ButtonContainer6.FindComponentByType("TransformGroup")
        self.ButtonTrans7 = self.ButtonContainer7.FindComponentByType("TransformGroup")
        self.ButtonTrans8 = self.ButtonContainer8.FindComponentByType("TransformGroup")
        self.ButtonTrans9 = self.ButtonContainer9.FindComponentByType("TransformGroup")
        self.ButtonTrans10 = self.ButtonContainer10.FindComponentByType("TransformGroup")

        self.ButtonTrans1.PropTransform.SetShow(0)
        self.ButtonTrans2.PropTransform.SetShow(0)
        self.ButtonTrans3.PropTransform.SetShow(0)
        self.ButtonTrans4.PropTransform.SetShow(0)
        self.ButtonTrans5.PropTransform.SetShow(0)
        self.ButtonTrans6.PropTransform.SetShow(0)
        self.ButtonTrans7.PropTransform.SetShow(0)
        self.ButtonTrans8.PropTransform.SetShow(0)
        self.ButtonTrans9.PropTransform.SetShow(0)
        self.ButtonTrans10.PropTransform.SetShow(0)
        
        return 0 
    def OnDestroy(self):
        return 0 
    def OnEnable(self):
        return 0 
    def OnDisable(self):
        return 0 
    def Update(self):
        return

    def OnMessage(self, msg, number, Vector4_lparm, Vector4_wparam):
        if (msg == "LButtonDown"):
            if(self.curScore==0):
                self.ButtonTrans0.PropTransform.SetShow(0)
                self.ButtonTrans1.PropTransform.SetShow(1)
                self.curScore+=1

            elif(self.curScore==1):
                self.ButtonTrans1.PropTransform.SetShow(0)
                self.ButtonTrans2.PropTransform.SetShow(1)
                self.curScore+=1

            elif(self.curScore==2):
                self.ButtonTrans2.PropTransform.SetShow(0)
                self.ButtonTrans3.PropTransform.SetShow(1)
                self.curScore+=1

            elif(self.curScore==3):
                self.ButtonTrans3.PropTransform.SetShow(0)
                self.ButtonTrans4.PropTransform.SetShow(1)
                self.curScore+=1

            elif(self.curScore==4):
                self.ButtonTrans4.PropTransform.SetShow(0)
                self.ButtonTrans5.PropTransform.SetShow(1)
                self.curScore+=1

            elif(self.curScore==5):
                self.ButtonTrans5.PropTransform.SetShow(0)
                self.ButtonTrans6.PropTransform.SetShow(1)
                self.curScore+=1

            elif(self.curScore==6):
                self.ButtonTrans6.PropTransform.SetShow(0)
                self.ButtonTrans7.PropTransform.SetShow(1)
                self.curScore+=1

            elif(self.curScore==7):
                self.ButtonTrans7.PropTransform.SetShow(0)
                self.ButtonTrans8.PropTransform.SetShow(1)
                self.curScore+=1

            elif(self.curScore==8):
                self.ButtonTrans8.PropTransform.SetShow(0)
                self.ButtonTrans9.PropTransform.SetShow(1)
                self.curScore+=1

            elif(self.curScore==9):
                self.ButtonTrans9.PropTransform.SetShow(0)
                self.ButtonTrans10.PropTransform.SetShow(1)



            

        return;