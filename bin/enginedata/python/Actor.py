class Actor:
    def __init__(self):
        return

    def FieldCheck(self):
        if len(vars(self)) == 0:
            return vars(self)

        print(vars(self))
        return vars(self)

    def OnUpdate(self):
        return 0 
    def OnMessage(self, msg, arg0, arg1, arg2):
        return 0 
    def OnCreate(self, uid):
        return 0 
    def OnDestroy(self):
        return 0 
    def OnEnable(self):
        return 0 
    def OnDisable(self):
        return 0 


