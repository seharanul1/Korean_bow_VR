class StartButton(Actor.Actor):
    def __init__(self):
        
        self.ButtonContainer = Container(0)
        
        return

    def OnCreate(self, uid):
        
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
        if (msg == "StartButton_OnClick"):
            result = GetWorldContainer().FindComponentByType("World").LoadScene("$project/Assets/1.fsf");
            if result == True:
                print("ex1.fsf Load ok!!")
            else:
                print("ex1.fsf Load fail!!");

        return;