class CameraScript(Actor.Actor):

    #0일때 main, 1일 때 target
    whichcamera = 0
    camerachange = False

    def __init__(self):
        self.MainCamPosCon = Container(0)
        self.TargetCamPosCon = Container(0)
        
        self.CameraContainer = Container(0)
        
        return

    def OnCreate(self, uid):
        
        self.MainCamPosTrans = self.MainCamPosCon.FindComponentByType("TransformGroup")
        self.MainCamPos = self.MainCamPosTrans.GetPosition()
        self.MainCamRot = self.MainCamPosTrans.GetRotation()

        self.TargetCamPosTrans = self.TargetCamPosCon.FindComponentByType("TransformGroup")
        self.TargetCamPos = self.TargetCamPosTrans.GetPosition()
        self.TargetCamRot = self.TargetCamPosTrans.GetRotation()

        self.CameraTrans = self.CameraContainer.FindComponentByType("TransformGroup")

        return 0 
    def OnDestroy(self):
        return 0 
    def OnEnable(self):
        return 0 
    def OnDisable(self):
        return 0 
    def Update(self):
        
        if(self.camerachange==True):
            if(self.whichcamera==0):
                self.CameraTrans.SetPosition(self.MainCamPos)
                self.CameraTrans.SetRotation(self.MainCamRot)
                self.camerachange=False

            elif(self.whichcamera==1):
                self.CameraTrans.SetPosition(self.TargetCamPos)
                self.CameraTrans.SetRotation(self.TargetCamRot)
                self.camerachange=False



        return


    def OnMessage(self, msg, number, Vector4_lparm, Vector4_wparam):
        if (msg == "changeCAM"):
            if(self.whichcamera==0):
                self.whichcamera=1
                self.camerachange=True
        elif(msg=="changeMain"):
            if(self.whichcamera==1):
                self.whichcamera=0
                self.camerachange=True       
            
        return