class ArrowControlScript(Actor.Actor):

    Arrow_Num = 0

    def __init__(self):
        self.ArrowContainer1 = Container(0)
        self.ArrowContainer2 = Container(0)
        self.ArrowContainer3 = Container(0)
        self.ArrowContainer4 = Container(0)
        self.ArrowContainer5 = Container(0)

        self.ArrowContainer6 = Container(0)
        self.ArrowContainer7 = Container(0)
        self.ArrowContainer8 = Container(0)
        self.ArrowContainer9 = Container(0)
        self.ArrowContainer10 = Container(0)

        self.ArrowContainer11 = Container(0)
        self.ArrowContainer12 = Container(0)
        self.ArrowContainer13 = Container(0)
        self.ArrowContainer14 = Container(0)
        self.ArrowContainer15 = Container(0)

    def OnCreate(self.uid):
        
        self.ArrowTrans1 = self.ArrowContainer1.FindCompoentByType("TransformGroup")
        self.ArrowScriptComponent1 = self.ArrowContainer1.FindCompoentByType("ScriptComponent")
        self.ArrowScript1 = self.ArrowScriptComponent1.GetActor()

        self.ArrowTrans2 = self.ArrowContainer2.FindCompoentByType("TransformGroup")
        self.ArrowScriptComponent2 = self.ArrowContainer2.FindCompoentByType("ScriptComponent")
        self.ArrowScript2 = self.ArrowScriptComponent2.GetActor()

        self.ArrowTrans3 = self.ArrowContainer3.FindCompoentByType("TransformGroup")
        self.ArrowScriptComponent3 = self.ArrowContainer3.FindCompoentByType("ScriptComponent")
        self.ArrowScript3 = self.ArrowScriptComponent3.GetActor()

        self.ArrowTrans4 = self.ArrowContainer4.FindCompoentByType("TransformGroup")
        self.ArrowScriptComponent4 = self.ArrowContainer4.FindCompoentByType("ScriptComponent")
        self.ArrowScript4 = self.ArrowScriptComponent4.GetActor()

        self.ArrowTrans5 = self.ArrowContainer5.FindCompoentByType("TransformGroup")
        self.ArrowScriptComponent5 = self.ArrowContainer5.FindCompoentByType("ScriptComponent")
        self.ArrowScript5 = self.ArrowScriptComponent5.GetActor()

        self.ArrowTrans6 = self.ArrowContainer6.FindCompoentByType("TransformGroup")
        self.ArrowScriptComponent6 = self.ArrowContainer6.FindCompoentByType("ScriptComponent")
        self.ArrowScript6 = self.ArrowScriptComponent6.GetActor()

        self.ArrowTrans7 = self.ArrowContainer7.FindCompoentByType("TransformGroup")
        self.ArrowScriptComponent7 = self.ArrowContainer7.FindCompoentByType("ScriptComponent")
        self.ArrowScript7 = self.ArrowScriptComponent7.GetActor()

        self.ArrowTrans8 = self.ArrowContainer8.FindCompoentByType("TransformGroup")
        self.ArrowScriptComponent8 = self.ArrowContainer8.FindCompoentByType("ScriptComponent")
        self.ArrowScript8 = self.ArrowScriptComponent8.GetActor()

        self.ArrowTrans9 = self.ArrowContainer9.FindCompoentByType("TransformGroup")
        self.ArrowScriptComponent9 = self.ArrowContainer9.FindCompoentByType("ScriptComponent")
        self.ArrowScript9 = self.ArrowScriptComponent9.GetActor()

        self.ArrowTrans10 = self.ArrowContainer10.FindCompoentByType("TransformGroup")
        self.ArrowScriptComponent10 = self.ArrowContainer10.FindCompoentByType("ScriptComponent")
        self.ArrowScript10 = self.ArrowScriptComponent10.GetActor()

        self.ArrowTrans11 = self.ArrowContainer11.FindCompoentByType("TransformGroup")
        self.ArrowScriptComponent11 = self.ArrowContainer11.FindCompoentByType("ScriptComponent")
        self.ArrowScript11 = self.ArrowScriptComponent11.GetActor()

        self.ArrowTrans12 = self.ArrowContainer12.FindCompoentByType("TransformGroup")
        self.ArrowScriptComponent12 = self.ArrowContainer12.FindCompoentByType("ScriptComponent")
        self.ArrowScript12 = self.ArrowScriptComponent12.GetActor()

        self.ArrowTrans13 = self.ArrowContainer13.FindCompoentByType("TransformGroup")
        self.ArrowScriptComponent13 = self.ArrowContainer13.FindCompoentByType("ScriptComponent")
        self.ArrowScript13 = self.ArrowScriptComponent13.GetActor()

        self.ArrowTrans14 = self.ArrowContainer14.FindCompoentByType("TransformGroup")
        self.ArrowScriptComponent14 = self.ArrowContainer14.FindCompoentByType("ScriptComponent")
        self.ArrowScript14 = self.ArrowScriptComponent14.GetActor()

        self.ArrowTrans15 = self.ArrowContainer15.FindCompoentByType("TransformGroup")
        self.ArrowScriptComponent15 = self.ArrowContainer15.FindCompoentByType("ScriptComponent")
        self.ArrowScript15 = self.ArrowScriptComponent15.GetActor()

        self.ArrowScriptList = [self.ArrowScript1,self.ArrowScript2,self.ArrowScript3,self.ArrowScript4,self.ArrowScript5,self.ArrowScript6,self.ArrowScript7,self.ArrowScript8,self.ArrowScript9,self.ArrowScript10,self.ArrowScript11,self.ArrowScript12,self.ArrowScript13,self.ArrowScript14,self.ArrowScript15]

        self.ArrowTransList = [self.ArrowTrans1,self.ArrowTrans2,self.ArrowTrans3,self.ArrowTrans4,self.ArrowTrans5,self.ArrowTrans6,self.ArrowTrans7,self.ArrowTrans8,self.ArrowTrans9,self.ArrowTrans10,self.ArrowTrans11,self.ArrowTrans12,self.ArrowTrans13,self.ArrowTrans14,self.ArrowTrans15]

    return

    def OnDestroy(self):
        return 0 

    def OnEnable(self):
        return 0 

    def OnDisable(self):
        return 0

    def Update(self):

        return 0
    def OnMessage(self, msg, number, Vector4_lparm, Vector4_wparam):
        
        if(msg=="Next_Arrow"):
            self.Arrow_Num+=1
            self.ArrowTransList[self.Arrow_Num].PropTransform.SetShow(1)

        elif(msg=="shoot"):
            self.ArrowScriptList[self.Arrow_Num].OnMessage("shoot",0,Vector4_lparm,Vector4_wparam)

        return 0