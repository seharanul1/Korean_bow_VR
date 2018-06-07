import math

class Range(object):
    
    def __init__(self, *args):
        if len(args) == 3:
            self.min = args[0]
            self.max = args[1]
            self.value = args[2]
        elif len(args) == 1:
            if isinstance(args[0], Range):
                self.min = args[0].min
                self.max = args[0].max
                self.value = args[0].value
                if self.value < args[0].min:
                    self.value = args[0].min
                elif self.value > args[0].max:
                    self.value = args[0].max
        else:
            self.min = 0.0
            self.max = 0.0
            self.value = 0.0

    # A == B
    def __eq__(self, v):
        return self.EqualRange(v)

    # A != B
    def __ne__(self, v):
        return not self.EqualRange(v)

    # for print
    def __str__(self):
        return str(self.min) + ", " + str(self.max) + ", " + str(self.value)

    def New():
        return Range()

    def ToString(self):
        return str(self.min) + ", " + str(self.max) + ", " + str(self.value)

    def FromString(self, s):
        if isinstance(s, bytes):
            rangeString = s.decode('utf-8')
        else:
            rangeString = s.encode().decode('utf-8')
        sp = rangeString.split(",")
        self.min = float(sp[0])
        self.max = float(sp[1])
        self.value = float(sp[2])

    def SetRange(self, min, max):
        self.min = min
        self.max = max
        if self.value < min:
            self.value = min
        elif self.value > max:
            self.value = max
        
    def SetValue(self, value):
        self.value = value
        if self.value < self.min:
            self.value = self.min
        elif self.value > self.max:
            self.value = self.max

    def SetValueRange(self, min, max, value):
        self.min = min
        self.max = max
        self.value = value
        if self.value < min:
            self.value = min
        elif self.value > max:
            self.value = max        

    def CopyRange(self, source):
        self.min = source.min
        self.max = source.max
        self.value = source.value

    def EqualRange(self, source):
        return self.min == source.min and self.max == source.max and self.value == source.value