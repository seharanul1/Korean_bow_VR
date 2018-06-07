import EngineDeviceInput





def GetHMDOrientation(deviceName, origin):
    return EngineDeviceInput.GetHMDOrientation(deviceName, origin)

def GetHMDPosition(deviceName, origin):
    return EngineDeviceInput.GetHMDPosition(deviceName, origin)

def GetHMDStatus(deviceName):
    return EngineDeviceInput.GetHMDStatus(deviceName)

def GetHandOrientation(deviceName, hand):
    return EngineDeviceInput.GetHandOrientation(deviceName, hand)

def GetHandPosition(deviceName, hand):
    return EngineDeviceInput.GetHandPosition(deviceName, hand)

def GetHandStatus(deviceName, hand):
    return EngineDeviceInput.GetHandStatus(deviceName, hand)

def GetInputTime(deviceName):
    return EngineDeviceInput.GetInputTime(deviceName)

def GetInputInfo(deviceName, Inputtype):
    return EngineDeviceInput.GetInputInfo(deviceName, Inputtype)

def GetControllerType(deviceName):
    return EngineDeviceInput.GetControllerType(deviceName)

def GetTrigger(deviceName, hand , deadzone,Triggertype):
    return EngineDeviceInput.GetTrigger(deviceName, hand , deadzone ,Triggertype)

def GetThumbStick(deviceName, hand , deadzone):
    return EngineDeviceInput.GetThumbStick(deviceName, hand, deadzone)

def SetVibration(deviceName, hand , frequency , amplitude):
    return EngineDeviceInput.SetVibration(deviceName, hand, frequency , amplitude)

ovrButton_A = 0x00000001
ovrButton_B = 0x00000002
ovrButton_RThumb = 0x00000004
ovrButton_RShoulder = 0x00000008
ovrButton_X = 0x00000100
ovrButton_Y = 0x00000200
ovrButton_LThumb = 0x00000400
ovrButton_LShoulder = 0x00000800
ovrButton_Up = 0x00010000
ovrButton_Down = 0x00020000
ovrButton_Left = 0x00040000
ovrButton_Right = 0x00080000
ovrButton_Enter = 0x00100000# // Start on XBox controller.
ovrButton_Back = 0x00200000# // Back on Xbox controller.
ovrButton_VolUp = 0x00400000#  // only supported by Remote.
ovrButton_VolDown = 0x00800000#  // only supported by Remote.
ovrButton_Home = 0x01000000


ovrTouch_A = 0x00000001
ovrTouch_B = 0x00000002
ovrTouch_RThumb = 0x00000004
ovrTouch_RThumbRest = 0x00000008
ovrTouch_RIndexTrigger = 0x00000010

ovrTouch_RButtonMask = ovrTouch_A | ovrTouch_B | ovrTouch_RThumb | ovrTouch_RThumbRest | ovrTouch_RIndexTrigger

ovrTouch_X = 0x00000100
ovrTouch_Y = 0x00000200
ovrTouch_LThumb = 0x00000400
ovrTouch_LThumbRest = 0x00000800
ovrTouch_LIndexTrigger = 0x00001000

ovrTouch_LButtonMask = ovrTouch_X | ovrTouch_Y | ovrTouch_LThumb | ovrTouch_LThumbRest | ovrTouch_LIndexTrigger;

ovrTouch_RIndexPointing = 0x00000020
ovrTouch_RThumbUp = 0x00000040

ovrTouch_RPoseMask = ovrTouch_RIndexPointing | ovrTouch_RThumbUp
ovrTouch_LIndexPointing = 0x00002000
ovrTouch_LThumbUp = 0x00004000
