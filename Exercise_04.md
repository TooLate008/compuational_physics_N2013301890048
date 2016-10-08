* 摘要

  利用Euler method近似求解原子衰变问题。
* 背景介绍

  对原子数量函数进行泰勒展开并略去高阶小量后，得到：
  
  ![](http://latex.codecogs.com/gif.latex?Nu%28t&plus;%5CDelta%20t%29%5Capprox%20Nu%28t%29&plus;%5Cfrac%7BdNu%7D%7Bdt%7D%5CDelta%20t)

  此公式即可以用作编程的近似计算。
* 正文

  有两个原子A和B可相互转化，其数量随时间的变化关系如下：
  
  ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7BdNa%7D%7Bdt%7D%3D%5Cfrac%7BNb%7D%7B%5Ctau%7D-%5Cfrac%7BNa%7D%7B%5Ctau%7D)
  
  ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7BdNb%7D%7Bdt%7D%3D%5Cfrac%7BNa%7D%7B%5Ctau%7D-%5Cfrac%7BNb%7D%7B%5Ctau%7D)
  
  利用如下代码可计算若干时间内A和B数量的变化：
  ```python
import pylab as pl
Na = 100
Nb = 0
tc = 1 
delta = 0.01    
pl.xlabel('time/s')
pl.ylabel('number')
pl.title('numbers of nuclei depending on time')
for i in range(500):
    t = delta*i
    Nc = Na
    Na = Na + (Nb-Na)/tc*delta
    Nb = Nb + (Nc-Nb)/tc*delta
    plotNa=pl.plot(t,Na,'r*')
    plotNb=pl.plot(t,Nb,'b*')
pl.annotate('Na=100,Nb=0,T=1s',xy=(3,10),xytext=(3,20))
pl.annotate('number of Na',xy=(1,80),xytext=(0.5,80))
pl.annotate('number of Nb',xy=(1,20),xytext=(0.5,20))
  ```
  当Na=100,Nb=0,衰变时间t=1s时，图象如下：
  
  ![](http://ww3.sinaimg.cn/large/6ccfb470jw1f8lbxxifimj20au07tdg6.jpg)
  
  Na与Nb初始数量交换后，图象如下：
  
  ![](http://ww2.sinaimg.cn/large/6ccfb470jw1f8lbzew8rqj20au07tdg6.jpg)
  
  继续改变初始数据：
  
  ![](http://ww4.sinaimg.cn/large/6ccfb470jw1f8lbzxiy1vj20au07t0t4.jpg)


* 结论
  
  从上面的结果中可以看出，不管初始数据如何，在一定时间后，A与B的数量趋于一致，为总数量的一半。
