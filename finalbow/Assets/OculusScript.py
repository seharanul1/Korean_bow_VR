import math



class OculusScript(Actor.Actor):
    
    init_diff = 0.0
    pos_diff = 0.0
    Trigger_on = False
    shoot = False
    switch = 0

    def __init__(self):
        self.LeftHandContainer = Container(0)
        self.RightHandContainer = Container(0)
        self.CameraContainer = Container(0)
        self.BowCon = Container(0)
        self._MainCamera = Camera(0)

        self._CameraTransform = None
        self._LeftHandTransform = None
        self._RightHandTransform = None
        self.LocalArrowContainer = Container(0)
        self.ArrowwContainer = Container(0)        
        #self.ArrowControlContainer = Container(0)
        
        return

    def OnCreate(self, uid):
        self._MainCamera = self.CameraContainer.FindComponentByType("Camera")
        self._CameraTransform = self.CameraContainer.FindComponentByType("TransformGroup")
        self._LeftHandTransform = self.LeftHandContainer.FindComponentByType("TransformGroup")
        self._RightHandTransform = self.RightHandContainer.FindComponentByType("TransformGroup")    

        #self.TargetScriptComponent = self.TargetContainer.FindComponentByType("ScriptComponent")
        #self.TargetScript = self.TargetScriptComponent.GetActor()
        self.BowScriptComp = self.BowCon.FindComponentByType("ScriptComponent")
        self.BowScript = self.BowScriptComp.GetActor()
        self.ArrowTrans = self.ArrowwContainer.FindComponentByType("TransformGroup")
        #self.ArrowTrans.PropTransform.SetShow(0)
        self.ArrowwScriptComponent = self.ArrowwContainer.FindComponentByType("ScriptComponent")
        self.ArrowwScript = self.ArrowwScriptComponent.GetActor()

        self.LocalTrans = self.LocalArrowContainer.FindComponentByType("TransformGroup")
        self.locpos = self.LocalTrans.GetLocalPosition()

        self.CameraScriptComponent = self.CameraContainer.FindComponentByType("ScriptComponent")
        self.CameraScript = self.CameraScriptComponent.GetActor()

        #self.ArrowControlScriptComponent = self.ArrowControlContainer.FindComponentByType("ScriptComponent")
        #self.ArrowControlScript = self.ArrowControlScriptComponent.GetActor()
            
        return 0 

    def OnDestroy(self):
        return 0 

    def OnEnable(self):
        return 0 

    def OnDisable(self):
        return 0

    def Update(self):
        doPrint = False;
        
        camPosition = self._CameraTransform.PropTransform.GetPosition()


        hmdStatus = DeviceInput.GetHMDStatus("Oculus")
        hmdRot = DeviceInput.GetHMDOrientation("Oculus", False)
        hmdPos = DeviceInput.GetHMDPosition("Oculus", False)
        inputTime = DeviceInput.GetInputTime("Oculus")
        buttonInfo = DeviceInput.GetInputInfo("Oculus", 0)
        touchInfo = DeviceInput.GetInputInfo("Oculus", 1)
        controllerType = DeviceInput.GetControllerType("Oculus")

        if doPrint:
            print("hmd Stataus : " + str(hmdStatus))
            print("Hmd Rot : " + str(hmdRot))
            print("Hmd Pos : " + str(hmdPos))
            print("Input Time : " + str(inputTime))
            print("Button : " + str(buttonInfo))
            print("Touch : " + str(touchInfo))
            print("ControllerType : " + str(controllerType))

        for i in range(0,2):
            
            hand = i + 1

            handStatus = DeviceInput.GetHandStatus("Oculus", hand)


            if handStatus > 0:
                handRot = DeviceInput.GetHandOrientation("Oculus", hand)
                handPos1 = DeviceInput.GetHandPosition("Oculus", 1)
                handPos2 = DeviceInput.GetHandPosition("Oculus", 2)
                handTrigger = DeviceInput.GetTrigger("Oculus", 1, False, 0)
                indexTrigger = DeviceInput.GetTrigger("Oculus", 2, False, 1)
                tStick = DeviceInput.GetThumbStick("Oculus", hand, False);


                
                ###
                if handTrigger > 0.8 and indexTrigger > 0.8:
                    if(self.Trigger_on==False) :
                        DeviceInput.SetVibration("Oculus", 1, 0.1, 0.7)
                        DeviceInput.SetVibration("Oculus", 2, 0.1, 0.7)
                        self.init_diff=(handPos1-handPos2).Length()
                        print("init_diff :" + str(self.init_diff))
                        #self.init_diff =  math.sqrt((handpos1.x-handpos2.x)*(handpos1.x-handpos2.x)+(handpos1.y-handpos2.y)*(handpos1.y-handpos2.y)+(handpos1.z-handpos2.z)*(handpos1.z-handpos2.z))
                        #pos_diff = math.sqrt((handpos1.x-handpos2.x)*(handpos1.x-handpos2.x)+(handpos1.y-handpos2.y)*(handpos1.y-handpos2.y)+(handpos1.z-handpos2.z)*(handpos1.z-handpos2.z)) - self.init_diff
                        self.Trigger_on=True
                        #self.ArrowwScript.OnMessage("shoot",0, Math3d.Vector4(0,0,0,0),Math3d.Vector4(0,0,0,0))
                        #self.BowScript.OnMessage("shoot",0, Math3d.Vector4(pos_diff,0,0,0),Math3d.Vector4(0,0,0,0))
                    else:
                        self.pos_diff = (handPos1-handPos2).Length()-self.init_diff
                        self.LocalTrans.SetLocalPosition(Math3d.Vector3(0,0,-self.pos_diff/3))
                        self.BowScript.OnMessage("BowAni",self.pos_diff*10000,Math3d.Vector4(0,0,0,0),Math3d.Vector4(0,0,0,0))
                        print("pos_diff = " + str(self.pos_diff))

                elif (self.Trigger_on==True):
                        #clapscript로 박수준비
                        #arrow로 화살준비
                        self.ArrowwScript.OnMessage("shoot",self.pos_diff*10000, Math3d.Vector4(0,0,0,0),Math3d.Vector4(0,0,0,0))
                        self.ArrowTrans.PropTransform.SetShow(1)
                        #self._RightHandTransform.PropTransform.SetShow(0)
                        self.shoot = True
                        self.BowScript.OnMessage("Bowstart",0,Math3d.Vector4(0,0,0,0),Math3d.Vector4(0,0,0,0))
                        #self.BowScript.OnMessage("shoot",0, Math3d.Vector4(pos_diff,0,0,0),Math3d.Vector4(0,0,0,0))
                        #self.ArrowControlScript.OnMessage("Next_Arrow",0,Math3d.Vector4(0,0,0,0),Math3d.Vector4(0,0,0,0))
                        self.Trigger_on=False

                    #self.ArrowwScript.OnMessage("stopArrow",0, Math3d.Vector4(0,0,0,0),Math3d.Vector4(0,0,0,0))
                    

                if doPrint:
                    if i == 0:
                        print("Left Hand >>")
                    elif i == 1:
                        print("Right Hand >>")

                    print("HandStatus : " + str(handStatus))

                    
                             
                    if handStatus > 0 :
                        print("HandRot : " + str(handRot))
                        print("HandPos : " + str(handPos1))
                        print("HandTrigger : " + str(handTrigger))
                        print("IndexTrigger : " + str(indexTrigger))
                        print("ThumbStick : " + str(tStick))

                #UpdatePosition
				#handpos2 = Math3d.Vector3(-handpos.x,handpos.y,handpos.z)
                #pos_diff는 트리거가 눌렸을 때 부터 잰다.
                #트리거가 눌렸을 때의 거리를 init_diff에 저장하고, 그때 부터의 변화량이 pos_diff가 됨.
                #화살을 쏘고 나서 init_diff도 초기화해야 함
                #pos_diff = math.sqrt((handpos1.x-handpos2.x)*(handpos1.x-handpos2.x)+(handpos1.y-handpos2.y)*(handpos1.y-handpos2.y)+(handpos1.z-handpos2.z)*(handpos1.z-handpos2.z))

                
                nPos = camPosition + handPos1                
                
				#change = nPos-camPosition
				#print("change is",change.x,change.y,change.z)
                #두 컨트롤러 사이의 거리를 계산
                #length = handpos1 - handpos2
                #화살의 위치는 활에서 x축으로 length만큼 뒤로 간 모양.
                #  

                if hand == 1:
                    if self._LeftHandTransform!= None:
                        self._LeftHandTransform.PropTransform.SetPosition(nPos)
                        self._LeftHandTransform.PropTransform.SetRotation(handRot)
                        
                        #self.ArrowTrans.PropTransform.SetRotation(handRot)
                    
                    if self._RightHandTransform != None:
                        if self.shoot == True:
                            pass
                        else:
                            self.ArrowTrans.PropTransform.SetPosition(nPos+Math3d.Vector3(0.01,-0.03,0.17))
                            self._RightHandTransform.PropTransform.SetPosition(nPos)
                            self._RightHandTransform.PropTransform.SetRotation(handRot)
                            
                        #init pos
                        #self.ArrowContainerTrans.SetPosition(Math3d.Vector3(pos_diff,0.0,0.0))

                #UseButton
                btnYCheck = buttonInfo & DeviceInput.ovrButton_Y
                btnXCheck = buttonInfo & DeviceInput.ovrButton_X
                btnBCheck = buttonInfo & DeviceInput.ovrButton_B
                btnACheck = buttonInfo & DeviceInput.ovrButton_A

                if btnYCheck > 0:
                    #DeviceInput.SetVibration("Oculus", 1, 0.5, 0.5)
                    if doPrint :
                        print("btnYClick")

                if btnXCheck > 0:
                    #DeviceInput.SetVibration("Oculus", 1, 0, 0)
                    self.shoot = False
                    if doPrint :
                        print("btnXCheck")

                if btnBCheck > 0:
                    #DeviceInput.SetVibration("Oculus", 2, 0.5, 0.5)
                    if self.switch == 0 :
                        self.CameraScript.OnMessage("changeCAM",0,Math3d.Vector4(0,0,0,0),Math3d.Vector4(0,0,0,0))
                        print("cameraChange!")
                        self.switch = 1
                    if doPrint :
                        print("btnBCheck")

                if btnACheck > 0:
                    #self.TargetScript.OnMessage("MainCam",0, Math3d.Vector4(0,0,0,0),Math3d.Vector4(0,0,0,0))
                    if self.switch==1:
                        self.CameraScript.OnMessage("changeMain",0,Math3d.Vector4(0,0,0,0),Math3d.Vector4(0,0,0,0))
                        print("camera to main")
                        self.switch=0
                    if doPrint :
                        print("btnACheck")

        return

    def OnMessage(self, msg, number, Vector4_lparm, Vector4_wparam):
        return;
