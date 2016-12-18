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
  
三、程序结构流程

![](http://ww4.sinaimg.cn/large/6ccfb470jw1favdx7ukr6j20ab0bcq34.jpg)

main：主程序，计算节点位移，单元应力应变

input：输入结点坐标、单元信息和材料参数

A:计算单元面积

ZG:计算总体刚度矩阵

HZLZ:计算荷载列阵

BOUNDARY:引入边界条件

SOLVE：利用高斯消元法求解刚度方程

YLYB:利用所得结点位移计算应力应变

四、算例

计算如图所示三角形平板结构。

![](http://ww3.sinaimg.cn/large/6ccfb470gw1fave0asexvj20c30aut8w.jpg)

1、打开”input.txt”文件，按中文提醒替换控制信息、单元信息、节点坐标、约束条件、荷载信息

![](http://ww1.sinaimg.cn/large/6ccfb470jw1fave1pepddj20ad07ggm4.jpg)

2、打开三角形单元project![](http://ww2.sinaimg.cn/large/6ccfb470jw1fave2ea4wkj203e00rmwy.jpg),在project outline中打开main.f90，执行。

![](http://ww1.sinaimg.cn/large/6ccfb470jw1fave2vonwmj202p03s3yg.jpg)

3、打开”output.txt”文件，查看位移、应力、应变解

![](http://ww1.sinaimg.cn/large/6ccfb470jw1fave3f7nskj207i09cjs4.jpg)

## 结论

  由于fortran较为强大的是数值计算，图形绘制比较麻烦，故本程序没有编写图形输出部分，计算结果不太直观。
  
  可改进程序使用CAD接口，把结构受力后变形情况画出。

  用成熟的有限元软件计算一个平面桁架结构，有如下效果：
  
  原结构：
  
  ![](http://ww2.sinaimg.cn/large/6ccfb470gw1favedghwyxj20hq08wwgu.jpg)
  
  变形后：
  
  ![](http://ww4.sinaimg.cn/large/6ccfb470gw1favedtdjomj20tx0mitae.jpg)
  
  受力：
  
  ![](http://ww4.sinaimg.cn/large/6ccfb470gw1faveedc83gj21kw16pgpk.jpg)
  
## 致谢

《有限单元法》 王勖成 清华大学出版社

## 源程序

1、主程序triangle.f90
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

2、子程序INPUT
```fortran
!=====================================
!子程序用途：从输入文件里读入信息
!=====================================
SUBROUTINE INPUT(JDS,DYS,YSJDS,JZHZS,JBHZS,DYJDH,JDZB,YS,JDHZ,JBHZ)
IMPLICIT NONE
!输入输出变量声明
INTEGER::JDS,DYS,YSJDS,JZHZS,JBHZS
INTEGER,DIMENSION(DYS,4)::DYJDH
REAL,DIMENSION(JDS,3)::JDZB
REAL,DIMENSION(YSJDS,5)::YS
REAL,DIMENSION(JZHZS,3)::JDHZ
REAL,DIMENSION(JBHZS,3)::JBHZ
CHARACTER(80)::title
!临时变量声明
INTEGER::i,j,k,m,n
!读入单元信息文字部分
    READ (7,'(a)') title
    write(8,*) title
    READ (7,'(a)') title
    write(8,*) title
!读入单元节点号数组
DO i=1,DYS
   READ(7,*)DYJDH(i,:)
   WRITE(8,111)DYJDH(i,:)    
   111 FORMAT(4I8)
END DO
!读入节点信息文字部分
    READ (7,'(a)') title
    write(8,*) title
    READ (7,'(a)') title
    write(8,*) title
!读入节点坐标数组
DO j=1,JDS 
   READ(7,*)JDZB(j,:)
   WRITE(8,112)JDZB(j,:)    
   112 FORMAT(3F8.4)
END DO
!读入约束矩阵
    READ (7,'(a)') title
    write(8,*) title
    READ (7,'(a)') title
    write(8,*) title
    DO k=1,YSJDS
       READ(7,*)YS(k,:)
       WRITE(8,*)YS(k,:)
    END DO
!读入节点荷载矩阵
    READ (7,'(a)') title
    write(8,*) title
    READ (7,'(a)') title
    write(8,*) title
    DO m=1,JZHZS
       READ(7,*)JDHZ(m,:)
       WRITE(8,*)JDHZ(m,:)
    END DO
!读入均布荷载矩阵
    READ (7,'(a)') title
    write(8,*) title
    READ (7,'(a)') title
    write(8,*) title
    DO n=1,JBHZS
       READ(7,*)JBHZ(n,:)
       WRITE(8,*)JBHZ(n,:)
    END DO 
END SUBROUTINE INPUT
```

3、子程序A
```fortran
!=====================================
!子程序用途：求单元面积
!=====================================
SUBROUTINE A(JDS,DYS,DYJDH,JDZB,AREA)
!输入输出变量声明
INTEGER::JDS,DYS
INTEGER,DIMENSION(DYS,4)::DYJDH
REAL,DIMENSION(JDS,3)::JDZB
REAL,DIMENSION(DYS)::AREA
!临时变量声明
INTEGER::i,k
REAL,DIMENSION(3)::b,c
INTEGER,DIMENSION(3)::x
REAL,DIMENSION(3,2)::JBZB
!按单元循环
DO i=1,DYS
   x(1)=DYJDH(i,2)
   x(2)=DYJDH(i,3)   
   x(3)=DYJDH(i,4)  
   !集成单元局部坐标数组JBZB
   DO k=1,3
         JBZB(k,1)=JDZB(x(k),2)
         JBZB(k,2)=JDZB(x(k),3)
   END DO
   !计算每个单元的面积
   b(1)=JBZB(2,2)-JBZB(3,2)
   b(2)=JBZB(3,2)-JBZB(1,2)   
   c(1)=-JBZB(2,1)+JBZB(3,1)
   c(2)=-JBZB(3,1)+JBZB(1,1)
   AREA(i)=(b(1)*c(2)-b(2)*c(1))/2.0    
END DO
!write(8,*)AREA
RETURN
END SUBROUTINE A
```

4、子程序DG
```fortran
!=====================================
!子程序用途：运用公式求解单元刚度矩阵
!=====================================
SUBROUTINE DG(x,i,DYGD,E,v,t,AREA,DYS,JDS,JDZB)
!输入输出变量声明
REAL::E,v,t
INTEGER::JDS,DYS,i
REAL,DIMENSION(JDS,3)::JDZB
REAL,DIMENSION(DYS)::AREA
REAL,DIMENSION(6,6)::DYGD
INTEGER,DIMENSION(3)::x!用于存储每单元节点号的临时数组
!临时变量声明
INTEGER::j,r,s,L
REAL::M
REAL,DIMENSION(2,2)::KK!分块矩阵
REAL,DIMENSION(3,2)::JBZB!单元局部坐标数组
REAL,DIMENSION(3)::b,c
REAL,DIMENSION(4)::K 
M=E*t/(4*(1-v**2)*AREA(I))
!集成单元局部坐标数组JBZB   
   DO j=1,3
      JBZB(j,1)=JDZB(x(j),2)
      JBZB(j,2)=JDZB(x(j),3)
   END DO
!计算每个单元的b,c
   b(1)=JBZB(2,2)-JBZB(3,2)
   b(2)=JBZB(3,2)-JBZB(1,2)   
   b(3)=JBZB(1,2)-JBZB(2,2)
   c(1)=-JBZB(2,1)+JBZB(3,1)
   c(2)=-JBZB(3,1)+JBZB(1,1)
   c(3)=-JBZB(1,1)+JBZB(2,1)
!计算分块矩阵并集成到单元刚度矩阵
   DO r=1,3
      DO s=1,3
        K(1)=b(r)*b(s)+(1-v)/2*c(r)*c(s)
        K(2)=v*c(r)*b(s)+(1-v)/2*b(r)*c(s)
        K(3)=v*b(r)*c(s)+(1-v)/2*c(r)*b(s)
        K(4)=c(r)*c(s)+(1-v)/2*b(r)*b(s)
        KK(:,:)=RESHAPE(K,(/2,2/))
        DYGD(2*r-1:2*r,2*s-1:2*s)=M*KK(1:2,1:2)
        !DO L=1,6
        !   WRITE(8,*) DYGD(L,:)
        !END DO
      END DO
   END DO
RETURN
END SUBROUTINE DG
```

5、子程序ZG
```fortran
!=====================================
!子程序用途：运用公式求解总刚度矩阵
!=====================================
SUBROUTINE ZG(ZGD,E,v,t,AREA,DYS,JDS,DYJDH,JDZB)
!输入输出变量声明
REAL::E,v,t
INTEGER::JDS,DYS
INTEGER,DIMENSION(DYS,4)::DYJDH
REAL,DIMENSION(JDS,3)::JDZB
REAL,DIMENSION(DYS)::AREA
REAL,DIMENSION(2*JDS,2*JDS)::ZGD
!临时变量声明
REAL,DIMENSION(6,6)::DYGD
INTEGER,DIMENSION(3)::x!用于存储每单元节点号的临时数组
INTEGER::i,j,k,l
!按单元循环
DO i=1,DYS
     x(1)=DYJDH(i,2)
     x(2)=DYJDH(i,3)   
     x(3)=DYJDH(i,4) 
     !调用子程序DG，逐个把单元刚度矩阵添加进总刚度矩阵中
     CALL DG(x,i,DYGD,E,v,t,AREA,DYS,JDS,JDZB)
     DO j=1,3
        DO k=1,3
        ZGD(2*x(j)-1:2*x(j),2*x(k)-1:2*x(k))= ZGD(2*x(j)-1:2*x(j),2*x(k)-1:2*x(k))+DYGD(2*j-1:2*j,2*k-1:2*k)
        END DO
     END DO 
END DO
!WRITE(8,*)'总刚度矩阵为：'  
!DO l=1,JDS*2
!   WRITE(8,*)ZGD(l,:)
!END DO
RETURN
END SUBROUTINE ZG
```

6、子程序HZLZ
```fortran
!=====================================================================================
!子程序用途：计算并集成荷载列阵（可计算自重，节点集中荷载，垂直于三角形边的均布荷载）
!=====================================================================================
SUBROUTINE HZLZ(ZHZ,JDS,DYS,DYJDH,JDZB,t,rou,AREA,JZHZS,JDHZ,JBHZS,JBHZ)
IMPLICIT NONE
!输入输出变量声明
INTEGER::JDS,DYS,JZHZS,JBHZS
REAL::t,rou
INTEGER,DIMENSION(DYS,4)::DYJDH
REAL,DIMENSION(JDS,3)::JDZB
REAL,DIMENSION(DYS)::AREA
REAL,DIMENSION(JDS*2)::ZHZ
REAL,DIMENSION(JZHZS,3)::JDHZ
REAL,DIMENSION(JBHZS,3)::JBHZ
!临时变量声明
REAL,PARAMETER::g=9.8
INTEGER::i,j,m,k,l,a,b
REAL::c,d,e,f,q
REAL,DIMENSION(6)::U,P!单元荷载
INTEGER,DIMENSION(3)::x!用于存储每单元节点号的临时数组
REAL,DIMENSION(3,2)::JBZB!单元局部坐标数组
!集成单元局部坐标数组
DO i=1,DYS
   x(1)=DYJDH(i,2)  
   x(2)=DYJDH(i,3)  
   x(3)=DYJDH(i,4)  
   DO k=1,3
      JBZB(k,1)=JDZB(x(k),2)
      JBZB(k,2)=JDZB(x(k),3)
   END DO
   !计算自重
   U=(/0.0,1.0,0.0,1.0,0.0,1.0/)
   P(:)=-1/3*rou*g*t*AREA(i)*U(:)
   !集成到总荷载矩阵ZHZ
   DO j=1,3
   ZHZ(2*x(j)-1)=ZHZ(2*x(j)-1)+P(2*j-1)
   ZHZ(2*x(j))=ZHZ(2*x(j))+P(2*j)
   END DO
END DO   
!计算节点集中荷载
   DO m=1,JZHZS 
     a=JDHZ(m,1)
     ZHZ(2*a-1)=ZHZ(2*a-1)+JDHZ(m,2)
     ZHZ(2*a)=ZHZ(2*a)+JDHZ(m,3)
   END DO
!计算均布荷载
   DO l=1,JBHZS
     a=JBHZ(l,1)
     b=JBHZ(l,2)
     c=JDZB(a,2)
     d=JDZB(a,3)
     e=JDZB(b,2)
     f=JDZB(b,3)
     q=JBHZ(l,3)
     U=(/d-f,e-c,d-f,e-c,0.0,0.0/)
     P(:)=1/2*q*t*U
     ZHZ(2*a-1)=ZHZ(2*a-1)+P(1)
     ZHZ(2*a)=ZHZ(2*a)+P(2)
     ZHZ(2*b-1)=ZHZ(2*b-1)+P(3)
     ZHZ(2*b)=ZHZ(2*b)+P(4)
   END DO
!WRITE(8,*)'总荷载列阵为：'  
!WRITE(8,*)ZHZ
RETURN    
END SUBROUTINE HZLZ
```

7、子程序BOUNDARY
```fortran
!=======================================
!子程序用途：运用乘大数法消除总刚奇异性
!=======================================
SUBROUTINE BOUNDARY(JDS,YSJDS,YS,ZGD,ZHZ,u)
!输入输出变量声明
INTEGER::JDS,YSJDS
REAL,DIMENSION(YSJDS,5)::YS
REAL,DIMENSION(2*JDS,2*JDS)::ZGD
REAL,DIMENSION(JDS*2)::ZHZ
REAL,DIMENSION(JDS*2)::u
!临时变量声明
INTEGER::i,j,n
REAL::H
H=2.0*10**9
DO i=1,YSJDS
   n=YS(i,1)
   IF (YS(i,2)==1) THEN
      u(2*n-1)=YS(i,4)
   END IF
   IF (YS(i,3)==1) THEN
      u(2*n)=YS(i,5)
   END IF
   DO j=-1,0
   ZHZ(2*n+j)=H*u(2*n+j)*ZGD(2*n+j,2*n+j)
   ZGD(2*n+j,2*n+j)=H*ZGD(2*n+j,2*n+j)
   END DO
END DO
RETURN
END SUBROUTINE BOUNDARY
```

8、子程序SOLVE
```fortran
!=====================================
!子程序用途：利用高斯消元法求解方程
!=====================================
SUBROUTINE SOLVE(JDS,ZGD,ZHZ,u,error)
!输入输出变量声明
INTEGER::JDS,error
REAL,DIMENSION(2*JDS,2*JDS)::ZGD
REAL,DIMENSION(JDS*2)::ZHZ
REAL,DIMENSION(JDS*2)::u
!临时变量声明
INTEGER::n
REAL,PARAMETER::EPSILON=1.0E-6
REAL::factor,temp
INTEGER::irow,ipeak,jrow,kcol
n=2*JDS
!循环n次求解
mainloop: DO irow=1,n
!找出每一列的最大值并将其放到所在矩阵的首行首列
ipeak=irow
DO jrow=irow+1,n
  IF (ABS(ZGD(jrow,irow))>ABS(ZGD(ipeak,irow))) THEN
     ipeak=jrow
  END IF
END DO
!判断是否为奇异矩阵
IF (ABS(ZGD(ipeak,irow))<EPSILON) THEN
   error=1
   RETURN
END IF 
!将最大值与第一行互换
IF (ipeak/=irow) THEN
   DO kcol=1,n
      temp=ZGD(ipeak,kcol)
      ZGD(ipeak,kcol)=ZGD(irow,kcol)
      ZGD(irow,kcol)=temp
   END DO
   temp=ZHZ(ipeak)
   ZHZ(ipeak)=ZHZ(irow)
   ZHZ(irow)=temp
END IF
!消去第一列除第一行外其余值
DO jrow=1,n
   IF (jrow/=irow) THEN
      factor=-ZGD(jrow,irow)/ZGD(irow,irow)
      DO kcol=1,n 
		 ZGD(jrow,kcol)=ZGD(irow,kcol)*factor+ZGD(jrow,kcol)
      END DO
	  ZHZ(jrow)=ZHZ(irow)*factor+ZHZ(jrow)
   END IF
END DO
END DO mainloop
!对每个等式除以系数得解
DO irow=1,n
  ZHZ(irow)=ZHZ(irow)/ZGD(irow,irow)
  ZGD(irow,irow)=1
END DO
u(:)=ZHZ(:)
error=0
WRITE(8,"(/,1X,'位移解为：')")
WRITE(8,"(/,'节点号',3X,'x方向位移',5X'y方向位移')")
DO i=1,JDS
   WRITE(8,130) i,u(2*i-1),u(2*i)
   130 FORMAT (I5,2es14.4)
END DO
RETURN
END SUBROUTINE SOLVE
```

9、子程序YLYB
```fortran
!================================================================
!子程序用途：利用应变矩阵求解单元应变，利用弹性矩阵求解单元应力
!================================================================
SUBROUTINE YLYB(E,v,u,AREA,DYS,JDS,DYJDH,JDZB,YB,YL)
!输入输出变量声明
INTEGER::JDS,DYS
REAL::E,v
INTEGER,DIMENSION(DYS,4)::DYJDH
REAL,DIMENSION(JDS,3)::JDZB
REAL,DIMENSION(DYS)::AREA
REAL,DIMENSION(DYS,4)::YB
REAL,DIMENSION(DYS,4)::YL
REAL,DIMENSION(JDS*2)::u
!临时变量声明
INTEGER::i,j,k,l
INTEGER,DIMENSION(3)::xindex!用于存储每单元节点号的临时数组
REAL,DIMENSION(3,6)::JBZB!单元局部坐标数组
REAL,DIMENSION(3)::b,c
REAL,DIMENSION(3,6)::BJZ!单元应变矩阵
REAL,DIMENSION(3)::DYYB!单元应变
REAL,DIMENSION(3)::DYYL!单元应力
REAL,DIMENSION(6)::a!单元位移
REAL,DIMENSION(3,3)::D!弹性矩阵
!按单元循环
DO i=1,DYS
   xindex(1)=DYJDH(i,2)
   xindex(2)=DYJDH(i,3)   
   xindex(3)=DYJDH(i,4)  
   !提取单元位移
   DO j=1,3
      a(j)=u(xindex(j))
   END DO
   !集成单元局部坐标数组JBZB
   DO k=1,3
         JBZB(k,1)=JDZB(xindex(k),2)
         JBZB(k,2)=JDZB(xindex(k),3)
   END DO
   !计算每个单元的b,c
   b(1)=JBZB(2,2)-JBZB(3,2)
   b(2)=JBZB(3,2)-JBZB(1,2)   
   b(3)=JBZB(1,2)-JBZB(2,2)
   c(1)=-JBZB(2,1)+JBZB(3,1)
   c(2)=-JBZB(3,1)+JBZB(1,1)
   c(3)=-JBZB(1,1)+JBZB(2,1)
   !计算应变矩阵
   BJZ(1,:)=(/b(1),0.0,b(2),0.0,b(3),0.0/)/(2*AREA(i))
   BJZ(2,:)=(/0.0,c(1),0.0,c(2),0.0,c(3)/)/(2*AREA(i))
   BJZ(3,:)=(/c(1),b(1),c(2),b(2),c(3),b(3)/)/(2*AREA(i))
   !计算每单元应变，存入YB矩阵中
   do j=1,3
     do l=1,6
        DYYB(j)=DYYB(j)+BJZ(j,l)*a(l)
	 end do
   end do
   YB(i,1)=i
   DO l=1,3
   YB(i,l+1)=DYYB(l)
   END DO
   !计算弹性矩阵
   D(:,:)=0.0
   D(1,1)=E/(1-V**2)
   D(2,2)=D(1,1)
   D(1,2)=V*D(1,1)
   D(2,1)=D(1,2)
   D(3,3)=(1-V)/2*D(1,1)
   !计算每单元应力，存入YL矩阵中
   do j=1,3
     do l=1,3
	    DYYL(J)=DYYL(J)+D(J,L)*DYYB(L)
	 end do
   end do
   YL(i,1)=i
   DO l=1,3
   YL(i,l+1)=DYYL(l)
   END DO
END DO
!输入各单元应变
WRITE(8,"(/,1X,'各单元应变为：')")
WRITE(8,"(/,4X,'单元号',8X,'εx ',9X,'εy',11X'γxy')")
DO i=1,DYS
   WRITE(8,119)YB(i,:)
   119 FORMAT(f10.0,3es14.4)
END DO
!输入各单元应变
WRITE(8,"(/,1X,'各单元应力为：')")
WRITE(8,"(/,4X,'单元号',5X,'σx(Pa)',6X,'σy(Pa)',7X'τxy(Pa)')")
DO i=1,DYS
   WRITE(8,120)YL(i,:)
   120 FORMAT(f10.0,3es14.4)
END DO   
END SUBROUTINE YLYB
```
