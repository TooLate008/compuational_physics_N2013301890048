* Abstract
  
  Exploring the routes to chaos when period doubling.
  

* Background
  
  
  【Period doubling】
  
  ![](https://www.evernote.com/shard/s140/sh/0724815b-79a9-4357-9e85-416c33cb1b69/e2b0667446e6f7d74181969ed0c7c357/res/7caddf85-f460-492e-9f06-eeaddfc5a649/8a7ec7661cbfa51e.png)
  
  【Bifurcation diagram】
  
  * bifurcation diagram 
  
  ![](https://www.evernote.com/shard/s140/sh/0724815b-79a9-4357-9e85-416c33cb1b69/e2b0667446e6f7d74181969ed0c7c357/res/03180ea4-8323-45df-8a92-a93f345a9c68/3afdad5f2daf22ac.png)
  
  * transition points 
  
  ![](https://www.evernote.com/shard/s140/sh/0724815b-79a9-4357-9e85-416c33cb1b69/e2b0667446e6f7d74181969ed0c7c357/res/469eea57-f2fa-4f6d-94d4-766204e50803/__SVG__ec8f24b2a9e020cc7042b8ce128bfe57)
  
  * period doubling is one specific route to chaos
  
  * Feigenbaum ![](https://www.evernote.com/shard/s140/sh/0724815b-79a9-4357-9e85-416c33cb1b69/e2b0667446e6f7d74181969ed0c7c357/res/21a4e1f4-9e72-47ec-a79f-f98c8cbb37bf/__SVG__38f1e2a089e53d5c990a82f284948953)
  
  ![](https://www.evernote.com/shard/s140/sh/0724815b-79a9-4357-9e85-416c33cb1b69/e2b0667446e6f7d74181969ed0c7c357/res/7d81b532-6bab-4b5a-9590-f58da415a169/__SVG__bda36544657ca3761478c23cb183f581)
  
* Body

  Exersice3.18:Calculate Poincare sections for the pendulum as it undergoes the period-doubling route to chaos.

  CODE: 
  ```python
import math
import matplotlib.pyplot as plt
import numpy as np

l = 9.8 #the length of the string
q = 1/2#the strength of the damping
Fd = 1.35#the amplitude of the driving force 
Od = (2/3)/4#angular frequency of the driving force
dt = 0.01
#2*math.pi/(Od*1000)#step of time
g = 9.8#gravity
a = 0
b = 0
Omega = []#initial angular velocity
angle = []#initial angle1
t = 0#time
while t<5000:
    for i in range (1000):
        b=b+(-(g/l)*math.sin(a)-q*b+Fd*math.sin(Od*t))*dt
        a=a+b*dt
        while a > np.pi:
            a=a-2*np.pi
        while a<-np.pi:
            a=a+2*np.pi
        t = t + dt
    angle.append(a)
    Omega.append(b)
plt.scatter(angle,Omega,2)
plt.title('omega versus angle     Fd=1.465')
plt.xlabel('angle($radians$)')
plt.ylabel('omega($radians/s$)')
  ```
  (1)When Fd=1.35, used a time step of 0.01, the other parameters were the same as in Fig3.6. Plot omega versus theta.
  
  ![](http://ww1.sinaimg.cn/large/4da31865gw1f9qmy45pwsj20b507xmxg.jpg)
  
  (2)When Fd=1.44 and the period is twice the drive period.
  
  ![](http://ww1.sinaimg.cn/large/4da31865gw1f9qmzoi07fj20aw07x74p.jpg)
  
  (3)When Fd=1.465 and the period is four times the drive period.
  
  ![](http://ww2.sinaimg.cn/large/4da31865gw1f9qn0usxytj20aw07xaao.jpg)

* Conclusion

  From the above we can see that as the period doubling, the maxima alternate of theta double.

* Thx

  ma
