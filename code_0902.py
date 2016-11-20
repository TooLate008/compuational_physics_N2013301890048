import matplotlib.pyplot as plt
import numpy as np

v = 2
a = 0.01
x = [0.2]
y = [0]
vx = 2
vy = 1.6
dt = 0.01
for i in range(10000):
    x.append(x[-1]+vx*dt)
    y.append(y[-1]+vy*dt)  
    t = i*dt
    if (x[-1]*x[-1]+y[-1]*y[-1])>1:
        x[-1] = x[-2] + vx/100*dt
        y[-1] = y[-2] + vy/100*dt
        m = np.sqrt(x[-1]**2+y[-1]**2)  
        x[-1] = x[-1]/m
        y[-1] = y[-1]/m
        v = np.sqrt(vx**2+vy**2)
        cos1 = (vx*x[-1]+vy*y[-1])/v
        cos2 = (vx*y[-1]-vy*x[-1])/v
        vt = -v*cos1
        vc = v*cos2 
        vx = vt*x[-1]+vc*y[-1]
        vy = vt*y[-1]-vc*x[-1]
plt.figure(figsize = (5,5))
plt.xlim(-1,1)
plt.ylim(-1,1)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Circular stadium - trajectory')
