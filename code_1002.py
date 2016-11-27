import math
import matplotlib.pyplot as plt
import numpy as np

x = [1]
y = [0]
vx = [0]
vy =[2*np.pi]
dt = 0.01
b = 2
t = 0
n = 0
a = 0
for i in range (1000):
    r = math.sqrt(x[-1]**2+y[-1]**2)
    vx.append(vx[-1]-4*np.pi*np.pi*x[-1]/(r**(b+1))*dt)
    x.append(x[-1]+vx[-1]*dt)
    vy.append(vy[-1]-4*np.pi*np.pi*y[-1]/(r**(b+1))*dt)
    y.append(y[-1]+vy[-1]*dt) 
plt.figure(figsize = (5,5))
plt.xlim(-1,1)
plt.ylim(-1,1)
plt.plot(x,y,'-g')
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.title('Simulation of elliptical orbit (b=2)')
