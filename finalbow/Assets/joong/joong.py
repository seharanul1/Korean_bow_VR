class joong(Actor.Actor):
    def __init__(self):
        
        self.joong1 = Container(0)
        self.joong2 = Container(0)
        self.joong3 = Container(0)
        self.joong4 = Container(0)
        self.joong5 = Container(0)
        self.joong6 = Container(0)
        self.joong7 = Container(0)
        self.joong8 = Container(0)
        self.joong9 = Container(0)
        self.joong10 = Container(0)
        self.joong11 = Container(0)
        self.joong12 = Container(0)
        self.joong13 = Container(0)
        self.joong14 = Container(0)
        self.joong15 = Container(0)

        
        return

    def OnCreate(self, uid):
        
        self.joong1ui = self.joong1.FindComponentByType("EGuiTexture")

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
        if(msg=="LButtonDown"):
            self.joong1ui.PropertyEGuiTexture.SetTextureFile("$project/Assets/joong/2datlas.fatlas[nojoong2.png]")
        
        return;