import matplotlib.pyplot as plt
import numpy as np

v = 2
a = 0.01
x = [0.2]
y = [0]
vx = 2
vy = 1.6
dt = 0.01
for i in range(5000):
    x.append(x[-1]+vx*dt)
    y.append(y[-1]+vy*dt)  
    t = i*dt
    if (x[-1]*x[-1]+y[-1]*y[-1])>1 and y[-1]>0.01:
        while (x[-1]*x[-1]+y[-1]*y[-1])<1:
            x[-1] = x[-2] + vx/100*dt
            y[-1] = y[-2] + vy/100*dt
        m = np.sqrt(x[-1]**2+y[-1]**2)  
        x[-1] = x[-1]/m
        y[-1] = (y[-1]-0.01)/m+0.01
        v = np.sqrt(vx**2+vy**2)
        cos1 = (vx*x[-1]+vy*(y[-1]-0.01))/v
        cos2 = (vx*(y[-1]-0.01)-vy*x[-1])/v
        vt = -v*cos1
        vc = v*cos2 
        vx = vt*x[-1]+vc*(y[-1]-0.01)
        vy = vt*(y[-1]-0.01)-vc*x[-1]
    elif (x[-1]*x[-1]+y[-1]*y[-1])>1 and y[-1]<-0.01:
        while (x[-1]*x[-1]+y[-1]*y[-1])<1:
            x[-1] = x[-2] + vx/100*dt
            y[-1] = y[-2] + vy/100*dt
        m = np.sqrt(x[-1]**2+y[-1]**2)  
        x[-1] = x[-1]/m
        y[-1] = (y[-1]+0.01)/m-0.01
        v = np.sqrt(vx**2+vy**2)
        cos1 = (vx*x[-1]+vy*(y[-1]+0.01))/v
        cos2 = (vx*(y[-1]+0.01)-vy*x[-1])/v
        vt = -v*cos1
        vc = v*cos2 
        vx = vt*x[-1]+vc*(y[-1]+0.01)
        vy = vt*(y[-1]+0.01)-vc*x[-1]
    elif x[-1]<-1 and y[-1]>-0.01 and y[-1]<0.01:
        x[-1] = x[-2] + vx/100*dt
        y[-1] = y[-2] + vy/100*dt
        vx=-vx
    elif x[-1]>1 and y[-1]>-0.01 and y[-1]<0.01:
        x[-1] = x[-2] + vx/100*dt
        y[-1] = y[-2] + vy/100*dt
        vx=-vx
plt.figure(figsize = (5,5))
plt.xlim(-1,1)
plt.ylim(-1,1)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Stadium billiard  a=0.01')
