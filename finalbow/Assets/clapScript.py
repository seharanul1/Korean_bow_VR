class clapScript(Actor.Actor):
    
    play = False

    def __init__(self):
        self.SoundContainer = Container(0)

        return

    def OnCreate(self,uid):

        self.SoundComponentt = self.SoundContainer.FindComponentByType("Sound")

        self.SoundComponentt.PropSound.SetSoundFilePath("$project/Assets/clap2.wav")


        return
    def OnDestroy(self):
        return 0 
    def OnEnable(self):
        return 0 
    def OnDisable(self):
        return 0 
    def Update(self):
        
        if(self.play==True):
            self.SoundComponentt.Play()
            self.play=False
        
        return 0

    def OnMessage(self, msg, number, Vector4_lparm, Vector4_wparam):
        
        if(msg=="clap"):
            if(self.play==False):
                self.play = True

        elif(msg=="clapready"):
            if(self.play==True):
                self.play=False




        return