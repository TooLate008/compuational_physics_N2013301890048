import math
xx = 10000#x position of the target,unit:m
yy = 0 #altitude of the target,unit:m
g = 9.8 #gravity
a = (6.5)*(math.pow(10,-3)) 
Bm = 4*math.pow(10,-5) #B2/m,unit:m^(-1)
T = 300 #temperature,unit:K
vw = -10 #velocity of wind, unit:m/s
sv = [0]
sa = [0]
n = 0
s = xx
v0 = 0
vm = 1000 #initial_velocity,unit:m/s
for i in range(10):
    while s>=500:
        x = [0] #initial_x,unit:m
        y = [0] # initial_y,unit:m
        dt = 0.1 #time_step,unit:s
        v = vm
        angle = 30 + i*5 #initial_angle=30°,add 5° each time
        vx = [v*math.cos(math.pi*angle/180)]
        vy = [v*math.sin(math.pi*angle/180)]
        while (y[-1]>=yy): 
            v = math.sqrt(math.pow(vx[-1],2)+math.pow(vy[-1],2))
            if y[-1] > 46153.84615:
                c = 0
            else:
                c = math.pow((1-(a*y[-1]/T)),2.5)
            Fx = -Bm*math.sqrt(v*v-vw*vw)*(vx[-1]-vw)*c
            Fy = -Bm*math.sqrt(v*v-vw*vw)*vy[-1]*c
            vx.append(vx[-1]+Fx*dt)
            vy.append(vy[-1]+(-g+Fy)*dt)  
            x.append(x[-1]+vx[-2]*dt)
            y.append(y[-1]+vy[-2]*dt)
        r = (yy-y[-2])/(y[-1]-yy)
        x[-1] = (x[-2]+r*x[-1])/(r+1)
        y[-1] = yy
        s = abs(x[-1]-xx) #deviation of distance 
        if x[-1] > xx:
            vt = v
            v = (v0+vt)/2
            v0 = v          
        if x[-1]<xx:
            v0 = v
            v = (v0+vt)/2
            vt = v
    sv.append(v)
    sa.append(a)
print (sv,sa)
