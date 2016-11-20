* 摘要

  桌球碰撞问题。

* 背景

  运动方程：

  ![](https://www.evernote.com/shard/s140/sh/0724815b-79a9-4357-9e85-416c33cb1b69/e2b0667446e6f7d74181969ed0c7c357/res/86cd3af3-933d-4ca8-8499-b307bded2fbf/__SVG__05cf5f3318d182354b2b674079f89d7b)
  ![](https://www.evernote.com/shard/s140/sh/0724815b-79a9-4357-9e85-416c33cb1b69/e2b0667446e6f7d74181969ed0c7c357/res/d5fb88d5-f610-44d0-a4ef-b42b414a2227/__SVG__d9fad9f1f89eb879eed07b9b99b89d01)
  
  碰撞方程：

  ![](https://www.evernote.com/shard/s140/sh/0724815b-79a9-4357-9e85-416c33cb1b69/e2b0667446e6f7d74181969ed0c7c357/res/41bbcf17-c3df-4c0f-8780-b42c4229dc37/__SVG__2809492f3c39c596ab27ef6dbae43a40)

  ![](https://www.evernote.com/shard/s140/sh/0724815b-79a9-4357-9e85-416c33cb1b69/e2b0667446e6f7d74181969ed0c7c357/res/75caadd4-3f2c-4547-b66b-7cf243f29c98/__SVG__96f44ecab9d5b8fd81c234806f033b51)

* 正文

  1、方形边界：
  
  [code](https://github.com/TooLate008/compuational_physics_N2013301890048/blob/master/code_0901.py)
  
  边界点可利用前面炮弹轨迹的插值法算出，再改变速度方向。结果图示：
  
  ![](http://ww3.sinaimg.cn/large/4da31865gw1f9yuobruuzj20b407jgnr.jpg)
  
  ![](http://ww2.sinaimg.cn/large/4da31865gw1f9yuorfkqlj20b407jadu.jpg)
  
  ![](http://ww3.sinaimg.cn/large/4da31865gw1f9yup1zxobj20b407jjuy.jpg)
  
  2、圆形边界：
  
  
  (1)一般圆桌碰撞：无混沌现象
  
  [code](https://github.com/TooLate008/compuational_physics_N2013301890048/blob/master/code_0902.py)
  
  ![](http://ww3.sinaimg.cn/large/4da31865gw1f9yutmb6gaj209k09dwh6.jpg)
  
 
  (2)从x轴切开距离2ar:
  
  [code](https://github.com/TooLate008/compuational_physics_N2013301890048/blob/master/code_0903.py)
  
  ![](http://ww4.sinaimg.cn/large/4da31865gw1f9yvqcns3vj209k09dgne.jpg)
  
  a=0.01时，图像不规则。
 

* 鸣谢

  圆形边界碰撞部分的code在参考[谭善同学](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_9/%E7%90%83%E5%BD%A2%E6%A1%8C%E9%9D%A2.py)的code之后编写，十分感谢！
