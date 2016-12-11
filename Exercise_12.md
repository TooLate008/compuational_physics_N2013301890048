* 摘要
  
  研究不同条件下的势场的数值解法。

* 背景
  
  ![](http://www.wsm.cn/uploads/allimg/160314/18-1603141G531.jpg)
  
  在空间没有电荷的情况下，电势遵守拉普拉斯方程：

  ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%5E2%20V%7D%7B%5Cpartial%20x%5E2%7D&plus;%5Cfrac%7B%5Cpartial%5E2%20V%7D%7B%5Cpartial%20y%5E2%7D&plus;%5Cfrac%7B%5Cpartial%5E2%20V%7D%7B%5Cpartial%20z%5E2%7D%3D0)
  
  尽管大多数常微分方程可以利用Euler法或Runge-Kutta法进行数值求解，但至今没有关于偏微分方程的通用方法。针对不同的偏微分方程，我们往往使用特定的方法。对于本题目中遇到的拉普拉斯方程，我们将它写成离散的形式
  
  ![](http://latex.codecogs.com/gif.latex?V%28i%2Cj%2Ck%29%3D%5Cfrac%7B1%7D%7B6%7D%5BV%28i&plus;1%2Cj%2Ck%29&plus;V%28i-1%2Cj%2Ck%29&plus;V%28i%2Cj&plus;1%2Ck%29&plus;V%28i%2Cj-1%2Ck%29&plus;V%28i%2Cj%2Ck&plus;1%29&plus;V%28i%2Cj%2Ck-1%29%5D)
      
  
* 正文

 习题5.3，利用Gauss-Seidel方法数值求解拉普拉斯方程，研究两个有限大小的平行电容板附近的电势分布。由于本题情况有比较高的对称性，可以只计算四分之一个区域的电势分布，在扩展到全区域。我画出了电势分布的三维图像以及等势面图。
 
 电势分布关于x轴对称，关于y轴反对称。因此我们只需要计算左上角的区域。为了程序编写方便，取左上角为原点。在该四分之一区域内划分50×50个像素点，其中比较特殊的点有：1、两个边界，电势保持为0；2、两个对称轴，其电势计算使用Runge-Kutta法，注意对称性；3、电容板，电势恒为1。不断重复更新各点电势值，直到前后两次所有点的电势差值之和小于0.1，认为达到足够精度。

```python
import math
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

v=[]
for i in range(50):
    v.append(range(50))
for i in range(50):
    v[0][i]=0.0
    v[i][0]=0.0
for i in range(20):
    v[49-i][30]=1.0

dv=10.0
a=0.0
while dv>1:
    dv=0.0
    for i in range(50):
        for j in range(50):
            a=v[i][j]
            if j==30 and i>29.5:
                v[i][j]=1.0
            elif i!=0 and i!=49 and j!=0 and j!=49:
                v[i][j]=(v[i+1][j]+v[i-1][j]+v[i][j+1]+v[i][j-1])/4.0
            elif i==49 and j!=49:
                v[i][j]=(v[i][j]+v[i-1][j]+v[i][j+1]+v[i][j-1])/4.0
            elif j==49 and i!=49:
                v[i][j]=(v[i+1][j]+v[i-1][j]-v[i][j]+v[i][j-1])/4.0
            elif i==49 and j==49:
                v[i][j]=(v[i][j]+v[i-1][j]-v[i][j]+v[i][j-1])/4.0
            dv=dv+abs(a-v[i][j])
x=[]
y=[]
z=[]
for i in range(100):
    z.append([])
    x.append(i)
    y.append(i)
    for j in range(100):
        if i<49.5 and j<49.5:
            z[i].append(v[i][j])
        elif i<49.5 and j>49.5:
            z[i].append(-v[i][99-j])
        elif i>49.5 and j<49.5:
            z[i].append(v[99-i][j])
        else:
            z[i].append(-v[99-i][99-j])
cs=plt.contour(x,y,z,30)
plt.clabel(cs,inline = 1, fontsize = 10)
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_trisurf(x, y, z, cmap=cm.jet, linewidth=0.01)
plt.show()
```

* 鸣谢

  臻臻
