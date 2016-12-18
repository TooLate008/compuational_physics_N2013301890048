# 计算物理期末作业：有限元程序
土木建筑工程学院  工程力学系  周璟怡  2013301890048

## 摘要
  有限单元法是力学系的核心知识。作为力学系的学生，本人利用fortran编写了平面三角形三节点有限元程序。
    
  该程序仅仅是本人学习有限单元法等系列课程后写出的极其粗糙版本，只能计算简单（理想）问题，不能应用于实际工程。因为实际工程涉及大型矩阵计算，需要更多的内存与算法优化的知识，已远远超出本人掌握范围。
  
## 背景

![](http://www.cadjapan.com/products/cae_kouzou/ansys/img/index_04.jpg)

　　有限单元法是当今工程分析中获得最广泛应用的数值方法。由于它的通用性和有效性，受到工程技术界的高度重视。伴随着计算机科学和技术的快速发展，现已经成为计算机辅助设计和计算机辅助制造的重要组成部分。
  
  　在工程和科技领域内，对于许多力学问题和物理问题，人们可以给出它们的数学模型，即应遵循的基本方程（常微分方程或偏微分方程）和相应的定解条件。但能用解析方法求出精确解的只是少数方程性质比较简单，且几何形状相当规则的情况。对于大多数问题，由于方程的非线性性质，或由于求解域的几何形状比较复杂，则只能采用数值方法求解。
   
  　有限单元法的基础是变分原理和加权余量法，其基本求解思想是把计算域划分为有限个互不重叠的单元，在每个单元内，选择一些合适的节点作为求解函数的插值点，将微分方程中的变量改写成由各变量或其导数的节点值与所选用的插值函数组成的线性表达式 ，借助于变分原理或加权余量法，将微分方程离散求解。采用不同的权函数和插值函数形式，便构成不同的有限元方法。
   
## 正文
一、弹性力学问题有限元分析的执行步骤

1、对结构进行离散；

2、形成单元的刚度矩阵和等效结点载荷列阵；

3、集成结构的刚度矩阵和等效结点载荷列阵；

4、引入强制（给定位移）边界条件；

5、求解有限元求解方程（线性代数方程组），得到结点位移a.

![](http://latex.codecogs.com/gif.latex?Ka%3DP)

6、计算单元应变和应力(就是单位受力和变形=。=)；

![](http://latex.codecogs.com/gif.latex?%5Cvarepsilon%20%3DBa%5Ee)

![](http://latex.codecogs.com/gif.latex?%5Csigma%20%3DD%28%5Cvarepsilon%20-%5Cvarepsilon%20_%7B0%7D%29&plus;%5Csigma%20_%7B0%7D)

7、进行必要的后处理。

二、程序说明

　　该程序能计算弹性力学的平面应力问题和平面应变问题；能考虑自重和结点集中力两种荷载的作用，在计算自重时y轴取垂直向上为正；能处理非零已知位移，如支座沉降的作用。主要输出的内容包括：结点位移、单元应力、单元应变。
  
  
  ```fortran
   !=====变量说明======
!JDS节点数
!DYS单元数
!E弹性模量
!v泊松比
!t板厚
!rou质量密度
!FL平面问题分类
!YSJDS约束节点个数
!JZHZS节点集中荷载数
!JBHZS均布侧压荷载数
!DYJDH单元节点号数组
!JDZB节点坐标数组
!ZHZ总荷载数组
!YS约束条件数组
!AREA面积
!DYGD单元刚度矩阵
!ZGD总刚度矩阵
!JDHZ节点荷载数组
!JBHZ均布荷载数组
!u位移列阵
!DYYL单元应力
!DYYB单元应变
!====================
PROGRAM main
IMPLICIT NONE
!定义
INTEGER::JDS,DYS,YSJDS,JZHZS,FL,JBHZS,error
REAL::E,v,t,rou
INTEGER, ALLOCATABLE::DYJDH(:,:)
REAL, ALLOCATABLE::JDZB(:,:)
REAL,allocatable::AREA(:)
REAL,allocatable::ZHZ(:)
REAL,allocatable::YS(:,:)
REAL,allocatable::ZGD(:,:)
REAL,allocatable::JDHZ(:,:)
REAL,allocatable::JBHZ(:,:)
REAL,allocatable::u(:)
REAL,allocatable::YB(:,:)
REAL,allocatable::YL(:,:)
CHARACTER(100)::title
!打开文件
INTEGER::ierror
OPEN(UNIT=7,FILE='input.txt',STATUS='OLD',ACTION='READ',IOSTAT=ierror)
OPEN(UNIT=8,FILE='output.txt',STATUS='REPLACE',ACTION='WRITE')
!读取控制信息文字部分
READ (7,'(a)') title
write(8,*) title
READ (7,'(a)') title
write(8,*) title
!读取控制信息
READ (7,*) JDS,DYS,E,v,t,rou,FL
WRITE(8,110)JDS,DYS,E,v,t,rou,FL
110 FORMAT (2I7,es14.4,3F10.2,I14)
!读取控制信息文字部分
READ (7,'(a)') title
write(8,*) title
!读取控制信息
READ (7,*) YSJDS,JZHZS,JBHZS
WRITE(8,113)YSJDS,JZHZS,JBHZS
113 FORMAT (3I14)
!确定可调数组大小
ALLOCATE(DYJDH(DYS,4))
ALLOCATE(JDZB(JDS,3))
ALLOCATE(AREA(DYS))
ALLOCATE(YS(YSJDS,5))
ALLOCATE(ZGD(2*JDS,2*JDS))
ALLOCATE(ZHZ(2*JDS))
ALLOCATE(JDHZ(JZHZS,3))
ALLOCATE(JBHZ(JBHZS,3))
ALLOCATE(u(2*JDS))
ALLOCATE(YB(DYS,4))
ALLOCATE(YL(DYS,4))
!判断平面问题类型
IF (FL==1) THEN
   E=E;v=v
   ELSE IF (FL==2) THEN
   E=E/(1-v**2);v=v/(1-v)
END IF 
!调用子程序INPUT，输入原始数据
CALL INPUT(JDS,DYS,YSJDS,JZHZS,JBHZS,DYJDH,JDZB,YS,JDHZ,JBHZ)
!调用子程序A，计算单元面积 
CALL A(JDS,DYS,DYJDH,JDZB,AREA)
!调用子程序ZG，计算总刚度矩阵
CALL ZG(ZGD,E,v,t,AREA,DYS,JDS,DYJDH,JDZB)
!调用子程序HZLZ，计算荷载列阵
CALL HZLZ(ZHZ,JDS,DYS,DYJDH,JDZB,t,rou,AREA,JZHZS,JDHZ,JBHZS,JBHZ)
!调用子程序BOUNDARY，引入强制边界条件
CALL BOUNDARY(JDS,YSJDS,YS,ZGD,ZHZ,u)
!调用子程序SOLVE，利用高斯消元法解出位移
CALL SOLVE(JDS,ZGD,ZHZ,u,error)
!调用子程序YLYB，计算应力应变
CALL YLYB(E,v,u,AREA,DYS,JDS,DYJDH,JDZB,YB,YL)
END PROGRAM main
  ```
  
## 结论

## 致谢
