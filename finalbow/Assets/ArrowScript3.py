import math
class ArrowScript3(Actor.Actor):

    def __init__(self):
        self.ArrowContainer = Container(0)
        self.ArrowPosCon = Container(0)
        self.ScoreCon = Container(0)
        self.SoundCon = Container(0)
        self.TargetCon = Container(0)
        
        return
    
    ### 상수
    G = 9.8
    KM = 0.006               # 활 상수 * 활 무게
    K = 0.86                 # 화살 탄성 계수
    E = 4.0                  # 효율
        
    ### 입력값
    targetDist = 145.0       # 과녁 까지의 거리
    
    arrow_len = 2.5 * 0.303  # 화살 길이
    pulled_len = 0.95 * arrow_len # 화살 당기는 정도
    bow_str = 40 * 0.45  * 1.5    # 활 세기
    arrow_wt = 5.5 * 3.75 * 0.01  #화살 무게

    w_angle = 0.0    # 화살 발시 좌우 각도
    h_angle = 0.0
    rot_cov = (0, w_angle, h_angle)

    strtP = 3.0  # 화살의 시작 위치
    cov = arrow_len *2.0 / 3.0  #무게 중심
        

    ### 계산
    # 화살의 속력   
    velo = math.sqrt(E * bow_str * (pulled_len) / (arrow_wt + KM))  

    """   # 화살을 targetDist만큼 보내기 위한 상하 발시 각도 (플레이어에게 보여주는 용도)
    temp = (targetDist + 3.0) * G / (velo * velo * math.cos(w_angle * math.pi / 180))
    h_angle = 0.5 * math.asin(temp) * 180 / math.pi  """
         
    initV = 0.0
    curV = 0.0
    init_coord_cov = Math3d.Vector3(0, 0, 0)
    init_rot = Math3d.Vector4(0,0,0,0)
    coord_cov = Math3d.Vector3(0, 0, 0)
    
    shoot = False
    got = False
    time = 0.0


    tick = 0
        
    def OnCreate(self,uid):
        self.ArrowTrans = self.ArrowContainer.FindComponentByType("TransformGroup")
        self.ArrowPosTrans = self.ArrowPosCon.FindComponentByType("TransformGroup")
        self.ArrowPos = self.ArrowPosTrans.GetPosition()
        #self.ArrowTrans.SetPosition(Math3d.Vector3(-1.13858,1.265878,-4.518424))
        self.ScoreTrans = self.ScoreCon.FindComponentByType("TransformGroup")
        

        self.SoundScriptComponent = self.SoundCon.FindComponentByType("ScriptComponent")
        self.SoundScript = self.SoundScriptComponent.GetActor()

        self.TargetScriptComponent = self.TargetCon.FindComponentByType("ScriptComponent")
        self.TargetScript = self.TargetScriptComponent.GetActor()
        self.tempRot = self.ArrowTrans.GetRotation()
        self.init_rot = self.tempRot
        self.rot_cov = self.Quaternion_toEulerianAngle(self.tempRot.w,self.tempRot.x,self.tempRot.y,self.tempRot.z)
        
        if self.time == 0.0 :
            self.coord_cov = self.init_coord_cov            
            self.w_angle = math.degrees(self.rot_cov[1])
            self.h_angle = math.degrees(self.rot_cov[0]) * -1.0
            print("angle", self.w_angle, self.h_angle)
            
            
            # 화살의 속도
            self.initV = [math.cos(math.pi / 180 * self.h_angle) * math.sin(math.pi / 180 * self.w_angle), math.sin(math.pi / 180 * self.h_angle), math.cos(math.pi / 180 * self.h_angle) * math.cos(math.pi / 180 * self.w_angle)]
            self.initV = [self.initV[0]*self.velo,self.initV[1]*self.velo, self.initV[2]*self.velo]
            self.curV= [self.initV[0],self.initV[1],self.initV[2]]

            """# 화살 무게중심 좌표
            initV_mag = math.sqrt((initV[0]*initV[0])+(initV[1]*initV[1])+(initV[2]*initV[2]))
            del_v = [initV[0]*(1 / initV_mag),initV[1]*(1 / initV_mag),initV[2]*(1 / initV_mag)]
            init_coord_cov = [ cov * del_v[0], strtP + cov * del_v[1], cov * del_v[2] ]
            coord_cov = [ init_coord_cov[0], init_coord_cov[1], init_coord_cov[2] ]
             
            strPoint = (coord_cov[0] - cov * del_v[0], coord_cov[1] - cov * del_v[1], coord_cov[2] - cov * del_v[2])
            endPoint = (strPoint[0] + arrow_len * del_v[0], strPoint[1] + arrow_len * del_v[1], strPoint[2] + arrow_len * del_v[2])"""
                
        return 0

    def OnDestroy(self):
        return 0 
    def OnEnable(self):
        return 0 
    def OnDisable(self):
        return 0 


    def Update(self):
         
        """if (self.time == 7.0):
            
            self.temp = self.Euler_toQuaternion(self.rot_cov[0], self.rot_cov[1], self.rot_cov[2])
            self.ArrowTrans.SetRotation(self.temp)
            self.ArrowTrans.SetPosition(self.coord_cov)
        """

        """ 화살을 움직이는 중일 때
        self.coord_cov = self.ArrowTrans.GetPosition()
        

        self.tempRot = self.ArrowTrans.GetRotation()
        self.rot_cov = self.Quaternion_toEulerianAngle(self.tempRot.w,self.tempRot.x,self.tempRot.y,self.tempRot.z)
        """
        #print("Y : ", self.w_angle, "도", "Z: " , self.h_angle, "도")

         
        if(self.shoot):
            self.init_coord_cov = self.ArrowTrans.GetPosition()
            self.SoundScript.OnMessage("clapready",0,Math3d.Vector4(0,0,0,0),Math3d.Vector4(0,0,0,0))
            
                
            self.coord_cov = Math3d.Vector3(self.initV[0] * self.time, self.initV[1] * self.time - 0.5 * self.G * math.pow(self.time, 2), self.initV[2] * self.time)
            self.coord_cov += self.init_coord_cov

            self.curV[1] = self.initV[1] - self.G * self.time

            

            self.curV_mag = math.sqrt((self.curV[0]*self.curV[0])+(self.curV[1]*self.curV[1])+(self.curV[2]*self.curV[2]))
            self.tempXZ = math.sqrt(self.curV[0]*self.curV[0] + self.curV[2]*self.curV[2])
            
            #self.tempXY = math.sqrt(self.curV[0]*self.curV[0] + self.curV[1]*self.curV[1])
            #self.del_v = (self.curV[0]*(1/self.curV_mag),self.curV[1]*(1/self.curV_mag),self.curV[2]*(1/self.curV_mag))       
            #self.rot_cov = (math.cos(math.pi / 180 * self.del_v[2]) * math.cos(math.pi / 180 * self.del_v[1]), math.sin(math.pi / 180 * self.del_v[2]), math.cos(math.pi / 180 * self.del_v[2]) * math.sin(math.pi / 180 * self.del_v[1]))
            #self.rot_cov = (0, math.acos(self.del_v[0] / math.sqrt(self.del_v[0]*self.del_v[0] + self.del_v[2]*self.del_v[2])), math.acos(self.del_v[0]*self.del_v[0] + self.del_v[2]*self.del_v[2]))


            if (self.curV[1] != 0) :
                self.h = self.curV[1] / math.sqrt(self.curV[1] * self.curV[1])
            else :
                self.h = 1.0
                
            if (self.curV[2] != 0) :
                self.w = self.curV[2] / math.sqrt(self.curV[2] * self.curV[2])
            else :
                self.w = 1.0

                
            #print( self.curV[1] * self.curV[1], math.sqrt(self.curV[1] * self.curV[1]))
            
            self.rot_cov = (math.acos(self.tempXZ /self.curV_mag) * self.h * -1.0 , math.acos(self.curV[0] / self.tempXZ) * self.w , 0)
            

            #print(self.time, ": ", self.curV[1], math.degrees(self.rot_cov[2]), self.h)
            
            #self.temp = self.Euler_toQuaternion(math.radians(self.rot_cov[0]), math.radians(self.rot_cov[1]), math.radians(self.rot_cov[2]))
            self.temp = self.Euler_toQuaternion(self.rot_cov[0], self.rot_cov[1], self.rot_cov[2])

            self.ArrowTrans.SetRotation(self.temp)
            self.ArrowTrans.SetPosition(self.coord_cov)
            #print(str(self.init_coord_cov))
            #print(str(self.coord_cov))

            self.time += 0.005

            #print("!!!!!!!!!!!!!")
            #print(self.time)
        if self.got == True :
            if self.tick < 7 :
                print("ticking")
                self.tick += 1
            else :
                self.tick = 0
                self.got = False
                self.ArrowTrans.SetPosition(self.init_coord_cov)
                self.ArrowTrans.SetRotation(self.init_rot)
                self.coord_cov = self.init_coord_cov
                self.ScoreTrans.PropTransform.SetShow(0)
                self.TargetScript.OnMessage("targetready",0,Math3d.Vector4(0,0,0,0),Math3d.Vector4(0,0,0,0))
                self.time = 0.0

        if self.shoot == True and self.coord_cov.y < -5 :
            self.shoot = False
            self.coord_cov = Math3d.Vector3(self.init_coord_cov.x, self.init_coord_cov.y, self.init_coord_cov.z)
            print("arrow stop")
            self.ArrowTrans.SetPosition(self.init_coord_cov)
            self.ArrowTrans.SetRotation(self.init_rot)
            self.coord_cov = self.init_coord_cov
            self.ScoreTrans.PropTransform.SetShow(0)
            self.TargetScript.OnMessage("targetready",0,Math3d.Vector4(0,0,0,0),Math3d.Vector4(0,0,0,0))
            self.time = 0.0

            
        return

        
     
    def OnMessage(self, msg, number, Vector4_lparm, Vector4_wparam):

        if msg == "stopArrow" :
            self.shoot = False
            self.got = True
            self.pulled_len = 0.95 * self.arrow_len
        elif msg == "shoot":
            self.shoot = True
            ch = 0.0
            ch = number/10000
            self.pulled_len = self.pulled_len*ch
            print("vector4 is"+str(ch))
            print("!!!!!!!!shoot!!!!!!!!!!")
        elif msg == "RButtonDown" :
            self.shoot = True           
            
        return

    def Quaternion_toEulerianAngle(self,w,x, y, z):
        
        ysqr=y*y
        t0 = 2.0*(w*x+y*z)
        t1 = +1.0 - 2.0 * (x*x + ysqr)
        X = math.atan2(t0, t1)

        t2 = +2.0 * (w*y - z*x)
        t2 =  1 if t2 > 1 else t2
        t2 = -1 if t2 < -1 else t2
        Y = math.asin(t2)

        t3 = +2.0 * (w * z + x*y)
        t4 = +1.0 - 2.0 * (ysqr + z*z)
        Z = math.atan2(t3, t4)
        
        return (X, Y, Z)
    
    def Euler_toQuaternion(self,x,y,z):

        t0 = math.cos(z*0.5)
        t1 = math.sin(z*0.5)
        t2 = math.cos(y*0.5)
        t3 = math.sin(y*0.5)
        t4 = math.cos(x*0.5)
        t5 = math.sin(x*0.5)

        qw = t0 * t2 * t4 + t1 * t3 * t5
        qx = t0 * t3 * t4 - t1 * t2 * t5
        qy = t0 * t2 * t5 + t1 * t3 * t4
        qz = t1 * t2 * t4 - t0 * t3 * t5

        return (qx,qy,qz, qw)

