import matplotlib.pyplot as plt

vx = 3
vy = 3.5
x = [0.2]
y = [0]
dt = 0.01
for i in range(10000):
    x.append(x[-1]+vx*dt)
    y.append(y[-1]+vy*dt)
    t = i*dt
    if x[-1]>1:
        r=(x[-2]-1)/(1-x[-1])
        y[-1]=(y[-2]+r*y[-1])/(r+1)
        x[-1]=1
        vx=-vx
    if x[-1]<-1:
        r=-(1+x[-2])/(x[-1]+1)
        y[-1]=(y[-2]+r*y[-1])/(r+1)
        x[-1]=-1
        vx=-vx
    if y[-1]>1:
        r=(y[-2]-1)/(1-y[-1])
        x[-1]=(x[-2]+r*x[-1])/(r+1)
        y[-1]=1
        vy=-vy
    if y[-1]<-1:
        r=-(1+y[-2])/(y[-1]+1)
        x[-1]=(x[-2]+r*x[-1])/(r+1)
        y[-1]=-1
        vy=-vy
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
