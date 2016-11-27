import math
import numpy as np
import matplotlib.pyplot as plt

a = [0.39,0.72,1.00,1.52,5.20,9.54,19.19,30.06,39.53]
e = [0.206,0.007,0.017,0.093,0.048,0.056,0.046,0.010,0.248]
m = []
plt.figure(figsize = (12,12))
for j in range(9):
    theta = 0
    x = []
    y = []
    r = []
    c = a[j]*e[j]
    k = a[j]*(1-e[j]**2)
    theta = 0
    dt = 0.005*np.pi
    n = np.int(2*np.pi/dt)+2
    for i in range(n):
        r.append(k/(1-e[j]*math.cos(theta)))
        x.append(r[-1]*math.cos(theta)-c)
        y.append(r[-1]*math.sin(theta))
        theta=theta+dt
    m.append(max(y))
    plt.plot(x,y)
    plt.xlim(-40,40)
    plt.ylim(-40,40)
    plt.xlabel('x(AU)')
    plt.ylabel('y(AU)')
    plt.title('Planetary Motion of Solar System')
    plt.hold(True)
