class BGM(Actor.Actor):
    def __init__(self):
        self.SoundContainer = Container(0)

        return

    def OnCreate(self,uid):

        self.SoundComponent = self.SoundContainer.FindComponentByType("Sound")

        self.SoundComponent.PropSound.SetSoundFilePath("$project/Assets/wind4.wav");

        self.SoundComponent.Play()

        return
    def OnDestroy(self):
        return 0 
    def OnEnable(self):
        return 0 
    def OnDisable(self):
        return 0 
    def Update(self):
        
        return 0