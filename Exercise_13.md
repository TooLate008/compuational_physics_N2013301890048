* 摘要
   
   研究波的运动。

* 背景

   ![](http://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Partial_transmittance.gif/270px-Partial_transmittance.gif)
   ![](http://www.hanwelltech.com/uploadfile/200910/20091014155531725.gif)

   核心运动方程：
   
   ![](http://latex.codecogs.com/gif.latex?%7B%5Cfrac%7B%5Cpartial%5E2%20y%7D%7B%5Cpartial%20t%5E2%7D%7D%3Dc%5E2%5Cfrac%7B%5Cpartial%5E2%20y%7D%7B%5Cpartial%20x%5E2%7D)
   
   波动满足叠加原理。
   
   利用差分法，有：
   
   ![](http://latex.codecogs.com/gif.latex?y%28i%2Cn&plus;1%29%3D2%5B1-r%5E2%5Dy%28i%2Cn%29-y%28i%2Cn-1%29&plus;r%5E2%5By%28i&plus;1%2Cn%29&plus;y%28i-1%2Cn%29%5D)
   
   取上式r=1,公式简化为
   
   ![](http://latex.codecogs.com/gif.latex?y%28i%2Cn&plus;1%29%3D-y%28i%2Cn-1%29&plus;y%28i&plus;1%2Cn%29&plus;y%28i-1%2Cn%29)
   
   初始时刻高斯波包：
   
   ![](http://latex.codecogs.com/gif.latex?y_%7B0%7D%28x%29%3Dexp%5B-k%28x-x_%7B0%7D%29%5E2%5D)
   
* 正文

  6.6：研究两个波包的运动，证明叠加原理。
  
```python
import math
import matplotlib.pyplot as plt

dx = 1.0
dt = 0.1
c = 10.0
k = 0.1
t = 0
n = 0
r = c*dt/dx
y3 = list(range(101))
y2 = list(range(101))
y1 = list(range(101))
for i in range(101):
    #y3[i]=math.exp(-k*(30.0-i)**2)+2*math.sin(i)*math.exp(-k*(70.0-i)**2)
    y3[i]=math.exp(-k*(40.0-i)**2)+2*math.exp(-k*(60.0-i)**2)
    y1[i]=y3[i]
    y2[i]=y3[i]
plt.figure(figsize=(10,5))
while t<3.1:
    for i in range(101):
        y1[i]=y2[i]
        y2[i]=y3[i]
    for j in range(101):
        if j>0 and j<100:
            y3[j]=(y2[j+1]+y2[j-1])-y1[j]
    n=n+1
    t=n*dt
plt.plot(y3,label='t='+str(t-dt))
plt.ylabel('y')
plt.xlabel('x')
plt.legend(loc="upper right", frameon=True,prop={'size':20})
plt.ylim([-3,3])
plt.show()
``` 

* 结论
 
 考虑两个初始静止的高斯波包，他们的最大振幅比为1:2。由于波包初始静止，在开始模拟后他们分别将分裂成两个波包，向两边运动。
 
 
 
 从结果可以看出，两个波包在相遇后分离，彼此独立。
 
* 致谢

  程序借鉴臻臻。
