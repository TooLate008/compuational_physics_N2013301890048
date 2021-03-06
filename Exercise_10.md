* 摘要

  研究太阳系行星运动。

* 背景
  
  【开普勒定律】

  ![](http://latex.codecogs.com/gif.latex?F_%7BG%7D%3D%5Cfrac%7BGM_%7Bs%7DM_%7BE%7D%7D%7Br%5E2%7D)

  ![](http://img2.duitang.com/uploads/item/201212/14/20121214005713_zfWF3.thumb.600_0.gif)
  
  数值解法：

  ![](http://latex.codecogs.com/gif.latex?v_%7Bx%2Ci&plus;1%7D%3Dv_%7Bx%2Ci%7D-%5Cfrac%7B4%20%5Cpi%5E2%20x_%7Bi%7D%7D%7Br_%7Bi%7D%5E3%7D%5CDelta%20t)
  
  ![](http://latex.codecogs.com/gif.latex?x_%7Bi&plus;1%7D%3Dx_%7Bi%7D&plus;v_%7Bx%2Ci&plus;1%7D%5CDelta%20t)
      
  ![](http://latex.codecogs.com/gif.latex?v_%7By%2Ci&plus;1%7D%3Dv_%7By%2Ci%7D-%5Cfrac%7B4%20%5Cpi%5E2%20y_%7Bi%7D%7D%7Br_%7Bi%7D%5E3%7D%5CDelta%20t)
      
  ![](http://latex.codecogs.com/gif.latex?y_%7Bi&plus;1%7D%3Dy_%7Bi%7D&plus;v_%7By%2Ci&plus;1%7D%5CDelta%20t)


  【平方反比定律与行星轨道的稳定性】
  
  对于地日系统，太阳质量远远大于地球质量，轨迹方程如下：
  
  ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E2%7D%7Bd%5Ctheta%5E2%7D%28%5Cfrac%7B1%7D%7Br%7D%29&plus;%5Cfrac%7B1%7D%7Br%7D%3D-%5Cfrac%7B%5Cmu%20r%5E2%7D%7BL%5E2%7DF%28r%29)
  
  取初始转角为零，方程解为：
  
  ![](http://latex.codecogs.com/gif.latex?r%3D%28%5Cfrac%7B%5Cmu%20G%20M_%7BS%7DM_%7BP%7D%7D%7BL%5E2%7D%29%5Cfrac%7B1%7D%7B1-ecos%5Ctheta%7D)
  
  也可计算出如下数据：
  
  ![](http://latex.codecogs.com/gif.latex?r_%7Bmin%7D%3Da%281-e%29)
  
  ![](http://latex.codecogs.com/gif.latex?r_%7Bmax%7D%3Da%281&plus;e%29)
  
  ![](http://latex.codecogs.com/gif.latex?v_%7Bmax%7D%3D%5Csqrt%7BGM_%7BS%7D%7D%5Csqrt%7B%5Cfrac%7B%281&plus;e%29%7D%7Ba%281-e%29%7D%281&plus;%5Cfrac%7BM_%7BP%7D%7D%7BM_%7BS%7D%7D%29%7D)
  
  ![](http://latex.codecogs.com/gif.latex?v_%7Bmin%7D%3D%5Csqrt%7BGM_%7BS%7D%7D%5Csqrt%7B%5Cfrac%7B%281-e%29%7D%7Ba%281&plus;e%29%7D%281&plus;%5Cfrac%7BM_%7BP%7D%7D%7BM_%7BS%7D%7D%29%7D)
  
  
  求运动周期可利用开普勒第二定理。  
      
      
  【水星进动】
      
  ![](http://imgsrc.baidu.com/forum/w%3D580/sign=8c71377d41166d223877159c76220945/9f4702003af33a8730dab0acc45c10385243b554.jpg)
  
  满足：
  
  ![](http://latex.codecogs.com/gif.latex?F_%7BG%7D%5Capprox%20%5Cfrac%7BGM_%7BS%7DM_%7BM%7D%7D%7Br%5E2%7D%281&plus;%5Cfrac%7B%5Calpha%7D%7Br%5E2%7D%29)
  
* 正文

  1、太阳系行星轨道
  
  [code](https://github.com/TooLate008/compuational_physics_N2013301890048/blob/master/code_1001.py)
  
  根据书上表4.1，可绘出太阳星各行星运动轨迹：
  
  ![](http://ww3.sinaimg.cn/large/4da31865gw1fa6rw4gychj20ka0k876d.jpg)
  
  可以看出，虽然轨迹是椭圆，但是由于偏心率较小），看起来还是很像圆轨道（水星和冥王星偏心率稍大但在图纸尺度上不明显）。

  2、平方反比定律
  
  若行星受力公式中的平方项有极小的偏离，设:
  
  ![](http://latex.codecogs.com/gif.latex?F_%7BG%7D%3D%5Cfrac%7BGM_%7Bs%7DM_%7BE%7D%7D%7Br%5E%5Cbeta%7D)
  
  此时对开普勒定律略作修改，有；
  
  [code](https://github.com/TooLate008/compuational_physics_N2013301890048/blob/master/code_1002.py)
  
  这程序明显有问题。

* 致谢
