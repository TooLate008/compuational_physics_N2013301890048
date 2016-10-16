import pylab as pl
import math
mx = 0
my = 0
for i in range(19):
    T = 300 #temperature,unit:K
    Bm = 4*math.pow(10,-5) #B2/m,unit:m^(-1)
    dt = 0.1 #time_step,unit:s
    x = [0] #initial_x,unit:m
    y = [0] # initial_y,unit:m
    v = 1000 #initial_velocity,unit:m/s
    angle = 0 + i*5 #initial_angle=0°,add 5° each time
    vx = [v*math.cos(math.pi*angle/180)]
    vy = [v*math.sin(math.pi*angle/180)]
    g = 9.8 #gravity
    a = (6.5)*(math.pow(10,-3)) 
    while (y[-1]>=0):
        v = math.sqrt(math.pow(vx[-1],2)+math.pow(vy[-1],2))
        c = math.pow((1-a*y[-1]/T),2.5)
        Fx = -Bm*v*vx[-1]*c
        Fy = -Bm*v*vy[-1]*c
        vx.append(vx[-1]+Fx*dt)
        vy.append(vy[-1]+(-g+Fy)*dt)  
        x.append(x[-1]+vx[-2]*dt)
        y.append(y[-1]+vy[-2]*dt)
    r = -y[-2]/y[-1]
    x[-1] = (x[-2]+r*x[-1])/(r+1)
    y[-1] = 0
    font = {'family': 'serif',
                    'color':  'darkred',
                    'weight': 'normal',
                    'size': 10,
           }
    if max(x)>=mx:
        mx = max(x)
        ma = angle
    if max(y)>=my:
        my=max(y)
    pl.grid()
    pl.plot(x,y,label = angle)
    pl.text(0.5*max(x), 0.95*max(y),angle, fontdict = font)
    pl.hold('on')
pl.xlim(0,mx)
pl.ylim(0,my)
pl.text(0.6*mx, 0.9*my,'temperature = 300K',fontdict = font)
pl.text(0.6*mx, 0.8*my,'initial velocity = 1000m/s', fontdict = font)
#pl.legend(loc='upper right')
pl.xlabel('x ($m$)')
pl.ylabel('y ($m$)')
pl.title('Trajectory of cannon shell with air drag & density correction', fontdict = font)
pl.show()
