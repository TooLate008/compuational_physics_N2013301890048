* 摘要
  
  ![](http://m.shulife.com/uploads/20111025/20111025105439135.jpg)
  
  研究土星卫星heprion的混沌现象。

* 背景
  
  ![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Hyperion_true.jpg/270px-Hyperion_true.jpg)

  土卫七密度较低，表面犹如海绵，是太阳系已知天体中自转混沌的最大天体，每21.3天绕土星旋转一周，土卫七可能是一颗更大卫星遭到撞击后剩余的残骸。
土卫七绕土星轨道的偏心率较大，且与土星最大卫星土卫六轨道接近，容易受到土星与土卫六引力的共同影响。这些因素集合在一起限制了它自转稳定的条件。

  ![](http://himg2.huanqiu.com/attachment2010/2015/0729/20150729075650610.jpg)
  
  为探究hyperion的混沌运动，我们简化问题为如下模型：
  
  ![](http://ww4.sinaimg.cn/large/4da31865gw1facpjgtg1mj209d07kjrc.jpg)
  
  这样我们就可以对原来的行星运动程序略做修改得到模拟轨迹。
  
  
  计算可得如下关系：

  ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5Comega%7D%7Bdt%7D%3D-%5Cfrac%7B3GM_%7BSat%7D%7D%7Br_%7Bc%7D%5E5%7D%28x_%7Bc%7Dsin%5Ctheta-y_%7Bc%7Dcos%5Ctheta%29%28x_%7Bc%7Dcos%5Ctheta&plus;y_%7Bc%7Dsin%5Ctheta%29)


  利用Euler-Cromer法可计算。    
  
* 正文

```python
import math
import matplotlib.pyplot as plt
import numpy as np

GM = 4*(np.pi**2)
x = [1]
y = [0]
vx = [0]
vy =[2*np.pi]
theta = [0]
w = [0]
dt = 0.0001
t = [0]
n = 0
for i in range (100000):
    r = math.sqrt(x[-1]*x[-1]+y[-1]*y[-1])
    vx.append(vx[-1]-4*np.pi*np.pi*x[-1]/(r**3)*dt)
    x.append(x[-1]+vx[-1]*dt)
    vy.append(vy[-1]-4*np.pi*np.pi*y[-1]/(r**3)*dt)
    y.append(y[-1]+vy[-1]*dt)
    w.append(w[-1]-3*GM/(r**5)*(x[-1]*math.sin(theta[-1])-y[-1]*math.cos(theta[-1]))*(x[-1]*math.cos(theta[-1])+y[-1]*math.sin(theta[-1]))*dt)
    theta.append(theta[-1]+w[-1]*dt)
    t.append(t[-1]+dt)
    if theta[-1]>np.pi:
        theta[-1]=theta[-1]-2*np.pi
    if theta[-1]<-np.pi:
        theta[-1]=theta[-1]+2*np.pi
plt.figure(figsize = (5,5))
plt.plot(t,w,'-g')
plt.xlabel('time(yr)')
plt.ylabel('w(radians/yr)')
plt.title('Hyperion w versus time')
```
  
  （1）当轨道为圆轨道时，令轨道半径为1HU,且![](http://latex.codecogs.com/gif.latex?GM_%7BSat%7D%3D4%5Cpi%5E2),时间步长为0.0001hyperion year.可画出如下结果：
  
  ![](http://ww3.sinaimg.cn/large/4da31865jw1faf5vmbv52j209909d3z7.jpg)
  ![](http://ww4.sinaimg.cn/large/4da31865jw1faf5w4gu41j209909d0to.jpg)
  
  (2)当轨道为椭圆轨道时，令轨道半径为1HU,初始速度为5HU/Hyperion year,且![](http://latex.codecogs.com/gif.latex?GM_%7BSat%7D%3D4%5Cpi%5E2),时间步长为0.0001hyperion year.可画出如下结果：
  
  ![](http://ww2.sinaimg.cn/large/4da31865jw1faf5xgikb8j209909dt9l.jpg)
  ![](http://ww4.sinaimg.cn/large/4da31865jw1faf5xw9z0nj209f09d3z3.jpg)
  
  此时有混沌现象产生。
  
  (3)探究初始角度微小变化对结果的影响：
  
  分别计算初始角度为0和0.01并求差值，有如下结果：
  
  ![](http://ww4.sinaimg.cn/large/4da31865gw1faf61evqyrj20dw0e00u9.jpg)
  ![](http://ww1.sinaimg.cn/large/4da31865gw1faf6246rvij20dw0e00ud.jpg)
 
