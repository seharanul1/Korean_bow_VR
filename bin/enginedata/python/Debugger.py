

import EngineDebugger

def Log(msgstr):
    return EngineDebugger.Log(msgstr)

MB_OK = 0x0
MB_OKCANCEL = 0x1
MB_ABORTRETRYIGNORE = 0x2
MB_YESNOCANCEL = 0x3
MB_YESNO = 0x4
MB_RETRYCANCEL = 0x5
MB_ICONHAND = 0x10
MB_ICONQUESTION = 0x20
MB_ICONEXCLAMATION = 0x30
MB_ICONASTERISK = 0x40

IDOK = 1
IDCANCEL = 2
IDABORT = 3
IDRETRY = 4
IDIGNORE = 5
IDYES = 6
IDNO = 7
    
def MsgBox(msgstr, msgboxType):
    return EngineDebugger.MsgBox(msgstr, msgboxType)

#test debugger
Log('Debugger is OK inside debugger\n')


def EvaluateReturn_float(value):
    EngineDebugger.EvaluateReturn_float(value)
def EvaluateReturn_int(value):
    EngineDebugger.EvaluateReturn_int(value)
def EvaluateReturn_String(value):
    EngineDebugger.EvaluateReturn_String(value)
def EvaluateReturn_Color(value):
    EngineDebugger.EvaluateReturn_Color(value)
def EvaluateReturn_Vector2(value):
    EngineDebugger.EvaluateReturn_Vector2(value)
def EvaluateReturn_Vector3(value):
    EngineDebugger.EvaluateReturn_Vector3(value)
def EvaluateReturn_Vector4(value):
    EngineDebugger.EvaluateReturn_Vector4(value)
def EvaluateReturn_Quaternion(value):
    EngineDebugger.EvaluateReturn_Quaternion(value)
def EvaluateReturn_bool(value):
    EngineDebugger.EvaluateReturn_bool(value)
def EvaluateReturn_UID(value):
    EngineDebugger.EvaluateReturn_UID(value)


