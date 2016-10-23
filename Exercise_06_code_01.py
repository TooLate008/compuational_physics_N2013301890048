import math
xx = 1000#x position of the target,unit:m
yy = 100 #altitude of the target,unit:m
g = 9.8 #gravity
a = (6.5)*(math.pow(10,-3)) 
Bm = 4*math.pow(10,-5) #B2/m,unit:m^(-1)
T = 300 #temperature,unit:K
vw = -10 #velocity of wind, unit:m/s
va = 200 #initial_velocity,unit:m/s
sv = [va]
sa = [0]
s = xx
 
for i in range(21):
    v = va 
    v0 = 0
    angle = 25 + i*2 #initial_angle=25°,add 2° each time
    for j in range(20):
        x = [0] #initial_x,unit:m
        y = [0] # initial_y,unit:m
        dt = 0.1 #time_step,unit:s
        vx = [v*math.cos(math.pi*angle/180)]
        vy = [v*math.sin(math.pi*angle/180)]
        while (x[-1]<=xx): 
            if y[-1] > 46153.84615:
                c = 0
            else:
                c = math.pow((1-(a*y[-1]/T)),2.5)
            Fx = -Bm*math.sqrt((v-vw)*(v-vw))*(vx[-1]-vw)*c
            Fy = -Bm*math.sqrt((v-vw)*(v-vw))*vy[-1]*c
            vx.append(vx[-1]+Fx*dt)
            vy.append(vy[-1]+(-g+Fy)*dt)  
            x.append(x[-1]+vx[-2]*dt)
            y.append(y[-1]+vy[-2]*dt)
        r = (xx-x[-2])/(x[-1]-xx)
        y[-1] = (y[-2]+r*y[-1])/(r+1)
        x[-1] = xx
        if y[-1]>yy:
            vt = v
            v = v0+(vt-v0)/2
        if y[-1]<yy:
            v0 = v
            v = v0+(vt-v0)/2
    sv.append(v)
    sa.append(angle)
print (sv,sa)
vmin = min(sv)
l = sv.index(vmin)
amin = sa[l]
print ('The minimum initial velocity:'+str(vmin)+'m/s')
print('angle:'+str(amin)+'°')
