* 摘要

  利用欧勒法计算炮弹的轨迹。
* 背景介绍
  
  忽略空气阻力时，炮弹的运动方程由牛顿第二定律给出：
  
  ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E2x%7D%7Bdt%5E2%7D%3D0)　　　　
  ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E2y%7D%7Bdt%5E2%7D%3D-g)
  
  若考虑空气阻力，炮弹受到阻力：
  
  ![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%7D%3D-B_2v%5E2)
  
  使用欧勒法，有
  
  ![](http://latex.codecogs.com/gif.latex?x_%7Bi&plus;1%7D%3Dx_%7Bi%7D&plus;v_%7Bx%2Ci%7D%5CDelta%7Bt%7D)　　　　　　　　
  ![](http://latex.codecogs.com/gif.latex?y_%7Bi&plus;1%7D%3Dy_%7Bi%7D&plus;v_%7By%2Ci%7D%5CDelta%7Bt%7D)
  
  ![](http://latex.codecogs.com/gif.latex?v_%7Bx%2Ci&plus;1%7D%3Dv_%7Bx%2Ci%7D&plus;F_%7Bdrag%2Cx%7D%5CDelta%20t)　　　　
  ![](http://latex.codecogs.com/gif.latex?v_%7By%2Ci&plus;1%7D%3Dv_%7By%2Ci%7D&plus;%28-g&plus;F_%7Bdrag%2Cy%7D%29%5CDelta%7Bt%7D)
  
  其中，
  
  ![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%2Cx%7D%3D-%5Cfrac%7BB_2%7D%7Bm%7Dvv_%7Bx%2Ci%7D)　  　　　
  ![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%2Cy%7D%3D-%5Cfrac%7BB_2%7D%7Bm%7Dvv_%7By%2Ci%7D)
  
  由于炮弹通常在高空中运行，从地面到高空空气密度的变化较大，需考虑此项影响。此时，空气阻力变为：
  
  ![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%7D%5E%7B*%7D%3D%5Cfrac%7B%5Crho%7D%7B%5Crho%20_%7B0%7D%7DF_%7Bdrag%7D%28y%3D0%29)
  
  空气密度随高度的变化公式：
    
  ![](http://latex.codecogs.com/gif.latex?%5Crho%3D%5Crho_%7B0%7D%281-%5Cfrac%7Bay%7D%7BT_%7B0%7D%7D%29%5E%7B%5Calpha%7D)　　　　
  ![](http://latex.codecogs.com/gif.latex?a%20%5Capprox%206.5%5Ctimes%2010%5E%7B-3%7D%20m%5E%7B-1%7D)　　
  ![](http://latex.codecogs.com/gif.latex?%5Calpha%20%5Capprox%202.5)（绝热近似）
  
* 正文

  【题目】：2.9同时考虑空气阻力和密度的影响，计算不同角度下的炮弹运动轨迹，并找到能使炮弹飞得最远的初始角度。
  
  【解决思路】：
  
  （1）核心公式均出自前文。其中要注意触地点的计算：
  
  ![](http://latex.codecogs.com/gif.latex?x%3D%5Cfrac%7Bx_%7Bn%7D&plus;rx_%7Bn&plus;1%7D%7D%7Br&plus;1%7D)　　　　
  ![](http://latex.codecogs.com/gif.latex?r%3D-%5Cfrac%7By_%7Bn%7D%7D%7By_%7Bn&plus;1%7D%7D)
  
  （2）利用循环计算不同角度下的炮弹运动轨迹；
  
  （3）使用如下语句，得出能使炮弹飞得最远的初始角度：
  ```python
   if max(x)>=mx:
        mx = max(x)
        ma = angle
  ```
  
  [完整程序](https://github.com/TooLate008/compuational_physics_N2013301890048/blob/master/Exercise_05_code.py)
    
* 结论
  
  设置初始速度为1000m/s，温度为300K
  
  (1)当初始角度为45°时，轨迹如下：
  
  ![](http://ww3.sinaimg.cn/large/6ccfb470jw1f8u6gmztblj20b807tdgm.jpg)
  
  (2)利用循环，每改变5°绘图一次，叠合图像如下：
  
  ![](http://ww4.sinaimg.cn/large/6ccfb470jw1f8u6ig1fplj20b807twgg.jpg)
  
  (3)继续加密步长，每改变0.5°绘图一次：
  
  ![](http://ww4.sinaimg.cn/large/6ccfb470gw1f8u6jrug4qj20b807tn0b.jpg)
  
  很鬼畜。
  
  (4)更变态地加密步长，不绘图，可得出最远距离及其对应的角度：
  maxangle=46.6°
  maxx=37998.396m
  
* 致谢

  感谢臻臻同学提供意见，感谢徐同学debug！
