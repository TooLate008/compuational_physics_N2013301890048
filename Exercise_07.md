* 摘要
  
  比较用不同方法处理振动问题的结果，讨论在实际情况下振动产生的混沌现象。

* 背景介绍

  对简谐运动，我们可以精确解出其运动方程，但若使用数值方法，则有如下一阶微分方程：
  
  ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20%5Comega%20%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D-%5Cfrac%7Bg%7D%7Bl%7D%5Ctheta)
  
  ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20%5Ctheta%20%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D%5Comega)
  
  【计算方法】
  
  使用Euler法计算：
  
  ![](http://latex.codecogs.com/gif.latex?%5Comega_%7Bi&plus;1%7D%3D%5Comega_%7Bi%7D-%28g/l%29%5Ctheta_%7Bi%7D%5CDelta%20t)
  
  ![](http://latex.codecogs.com/gif.latex?%5Ctheta_%7Bi&plus;1%7D%3D%5Ctheta_%7Bi%7D&plus;%5Comega_%7Bi%7D%5CDelta%20t)
  
  ![](http://latex.codecogs.com/gif.latex?t_%7Bi&plus;1%7D%3Dt_%7Bi%7D&plus;%5CDelta%20t)
  
  但是这一方法并不满足能量守恒条件，不管每一步的时间间隔取多小，能量总增加。故在经过足够长的时间后，结果一定会发散。改进可用如下Euler Cromer法：
  
  ![](http://latex.codecogs.com/gif.latex?%5Comega_%7Bi&plus;1%7D%3D%5Comega_%7Bi%7D-%28g/l%29%5Ctheta_%7Bi%7D%5CDelta%20t)
  
  ![](http://latex.codecogs.com/gif.latex?%5Ctheta_%7Bi&plus;1%7D%3D%5Ctheta_%7Bi%7D&plus;%5Comega_%7Bi&plus;1%7D%5CDelta%20t)
  
  ![](http://latex.codecogs.com/gif.latex?t_%7Bi&plus;1%7D%3Dt_%7Bi%7D&plus;%5CDelta%20t)
  
  【复杂情况】
  
  引入耗散，非线性特征和驱动力后，有如下运动方程：
  
  ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%5E2%20%5Ctheta%7D%7B%5Cmathrm%7Bd%7D%5E2%20t%7D%3D-%5Cfrac%7Bg%7D%7Bl%7Dsin%7B%5Ctheta%7D-q%5Cfrac%7B%5Cmathrm%7Bd%7D%20%5Ctheta%7D%7B%5Cmathrm%7Bd%7D%20t%7D&plus;F_%7BD%7Dsin%7B%5COmega_%7BD%7Dt%7D)
  
  化成两个一阶微分方程：
  
  ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20%5Comega%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D-%5Cfrac%7Bg%7D%7Bl%7Dsin%7B%5Ctheta%7D-q%5Cfrac%7B%5Cmathrm%7Bd%7D%20%5Ctheta%7D%7B%5Cmathrm%7Bd%7D%20t%7D&plus;F_%7BD%7Dsin%7B%5COmega_%7BD%7Dt%7D)
  
  ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20%5Ctheta%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D%5Comega)
  
  使用Euler Cromer法有：
  
  ![](http://latex.codecogs.com/gif.latex?%5Comega_%7Bi&plus;1%7D%3D%5Comega_%7Bi%7D&plus;%5B-%5Cfrac%7Bg%7D%7Bl%7Dsin%7B%5Ctheta_%7Bi%7D%7D-q%5Comega_%7Bi%7D&plus;F_%7BD%7Dsin%7B%5COmega_%7BD%7Dt_%7Bi%7D%7D%5D%5CDelta%20t)
  
  ![](http://latex.codecogs.com/gif.latex?%5Ctheta_%7Bi&plus;1%7D%3D%5Ctheta_%7Bi%7D&plus;%5Comega_%7Bi&plus;1%7D%5CDelta%20t)
  
  ![](http://latex.codecogs.com/gif.latex?t_%7Bi&plus;1%7D%3Dt_%7Bi%7D&plus;%5CDelta%20t)
  
  【混沌现象】
  
  混沌现象是确定但不可预测的。当系统满足如下条件：非线性，有耗散，有能量输入时，将会产生混沌现象。
  
  
    
* 正文
  
  【3.11】使用与课本figure3.6相同的数据，计算系统的总能量随时间的变化。
  
  能量计算公式（计算中取m为单位质量1）：
  
  ![](http://latex.codecogs.com/gif.latex?E%3D%5Cfrac%7B1%7D%7B2%7Dmgl%5E2%5Comega%5E2&plus;mgl%281-cos%7B%5Ctheta%7D%29)
  
  1、当驱动力Fd=0时，结果如图：
  
  ![](http://ww2.sinaimg.cn/large/6ccfb470gw1f95yulydxuj20ax07w74e.jpg)
  
  由于外力输入，能量逐渐耗散，趋于0。
  
  2、当驱动力Fd=0.5时，结果如图：
  
  ![](http://ww4.sinaimg.cn/large/6ccfb470gw1f95yvqneeqj20au07wdgj.jpg)
  
  外力周期性地和阻尼的耗散抵消，能量呈周期性变化。
  
  3、当驱动力Fd=1.2时，结果如图：
  
  ![](http://ww4.sinaimg.cn/large/6ccfb470gw1f95ywd18enj20b007w3z4.jpg)
  
  能量变化毫无规律。
  
  
  
  
  
* 结论

  上面三个结果说明系统的能量变化形式与角度的变化形式相近，同时也证明Euler Cromer法的稳定性，

* 致谢
