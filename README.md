# UJS python course labs

## Lab1

### 题目1-1：找素数

输出101到200之间的素数，要求每行输出10个，多余换行。



### 题目1-2：计算n阶调和数

先一个定义计算并返回第n阶调和数（1 + 1/2 + 1/3 + … + 1/n）的函数，然后在命令行中输入参数n，调用函数计算前n个调和数之和，并将每次函数调用的结果放入一个列表，最后输出该列表，以及列表中所有元素之和（精确到小数点后面一位）。



### 题目1-3：列表的操作

由用户输入n个整数，将这些整数构成一个列表。要求显示出该列表的元素个数、最大值、最小值、所有元素之和、平均值。请思考用多种方法来实现。



### 题目1-4：利用循环语句求和

分别利用for循环和while循环求1~100中所有数之和，以及所有奇数的和、所有偶数的和。



### 题目1-5：判断闰年

至少使用2种方法编写一个函数来判断某一年是否为闰年。

年份数据由用户输入，调用该函数，函数调用完毕后，输出判断结果。



### 题目1-6：判断回文

编写程序，判断用户输入的一个字符串是否为回文。如果是则输出True，否则输出Flase



### 题目1-7：计算三角形面积

由用户输入三角形的三条边的边长a、b和c，计算并输出三角形的面积。提示:利用三角形周长的一半h来计算面积。

在写出基本程序之后建议尝试增加如下一些功能：

(1) 使用2种输出格式控制方式。

(2) 若由用户输入三角形的三条边的边长（即a、b、c），则必须对三角形的边长小于或等于0和两边之和小于或等于第三边的情况识别出来，并提示用户。请思考下面两种解决方案：

1.   用while循环语句进行判断，出现上述错误会提示并要求用户重新输入三条边长，直到用户输入合法边长之后计算并输出三角形的面积。

2.   用异常处理机制（raise语句和ValueError对象）来终止程序并提醒用户错误的原因。（注意：可以在学完异常处理之后再来完善该题）

## Lab2

### 题目2-1：求阶乘

编写程序，定义一个求阶乘的函数fact(n)，并编写测试代码，要求输入整数n（n>=0）。请分别使用递归和非递归方式实现

### 题目2-2：折半查找

用折半查找法查33和58在列表[1,13,26,33,45,55,68,72,83,99]中的位置，

要求：分别用递归和非递归的方法来实现。

输出结果是：

关键字33在列表中的索引是：3

关键字58不在该列表中

### 题目2-3：文本文件的读写

(1) 打开该文件file2.txt，并将元组t = "spring", "summer", "autumn"写入到文件中，要求元组中每个元素单独放在一行中，建议使用for循环语句。

(2) 打开该文件并字符串" winter"追加到文件最后一行下面的一行，使得文件中的内容包括如下4行文字：

spring

summer

autumn

winter

(3) 打开该文件并将其中的最后两行文字显示到屏幕上。

(4) 思考：若一开始文件file2.txt不存在，一定要先创建该文件？若要在读取文件的过程中增加异常处理的代码，以便在文件不存在或打开失败的异常情况下，向用户提示“文件file2.txt打开失败！”，应该怎么修改代码

### 题目2-4：二进制（随机）文件的读写

**二进制（随机）文件的读写**

1、打开一个空的随机文件my.dat，往里面写入下面2行字节数据：

Xiaoming

student

2、然后读入该文件的后7个字节并输出到屏幕上。

### 题目2-5：类的继承

通过继承，派生类继承基类中除构造方法之外的所有成员。如果在子类类中重新定义从基类继承的方法，则派生类中定义的方法覆盖从基类中继承的方法，即子类同名方法优先。反之，若子类没有重新定义，则使用从父类继承过来的方法。

先定义父类Dimension，在类中定义计算面积的函数area，该函数就输出一行话“形状没定，无法计算面积！”。然后定义Dimension的一个子类Triangle（表示三角形），在其中定义构造函数、计算面积的函数area。

之后再按照类似的方式分别创建圆形、矩形的类。

最后分别创建上述3种对象，然后输出它们的面积。

说明：相关参数可以自己定义。

### 题目2-6：运算符重载

编写运算符重载的程序，定义一个MyList1类，在其中重新定义运算符"+"、运算符"-"、运算符"*"、运算符"/"，以实现对某个整数构成的列表中的每个元素都进行加减乘除运算。

### 题目2-7：使用MyMath类对象计算圆和球的面积等

编写程序，创建类MyMath，计算圆的周长和面积以及球的表面积和体积，并编写测试代码，结果均保留两位小数。

### 题目2-8：学校信息管理系统

 建立学校信息管理系统：

- 建立Person类，包括：姓名name、性别sex、年龄age这3个数据成员，一个构造函数、一个输出信息的printInfo函数。

- 建立Student类，该类继承自Person类，并且新增数据成员：班级classes（用string类型）、学号studentID（用int类型）、成绩score（用字典类型，可以自己定义三门课程，比如语数外）、总人数count（用int类型，这是静态属性，即类属性），和一个构造函数、一个输出信息的printInfo函数。

- 建立Teacher类，该类也继承自Person类，并且新增：部门department（用string类型）、工号teacherID（用int类型）、讲授课程course（用列表类型）、薪水salary（用int类型，这是私有数据）这4个数据成员，和一个构造函数、一个输出信息的printInfo函数（这里不输出私有数据，但可以考虑一下如何提供私有数据的输出方法）。

然后创建2个学生对象和1个教师对象，然后分别调用这3个对象的printInfo函数输出各自的（非私有）数据信息。在学生的构造函数中让count自增，在析构函数中让count自减。

## lab3

### 题目3-1：用2个列表来生成字典

编写程序，输入2个列表，以第一个列表中的元素为“键”，以第二个列表中的元素为“值”创建字典。若两个列表长度不等，则以短的为准而丢弃较长列表中后面的元素。最后输出字典。

### 题目3-2：猜数字

随机产生一个0到100之间（包括0和100）的偶数，请用户猜测具体是哪个数，即：不断从标准输入读取用户的猜测值（用户每次输入一个偶数），并根据猜测值给出提示信息：“太大”、“太小”或“正确!”

### 题目3-3：用迭代器和生成器函数来输出斐波那契数列（本题为选做题）

分别用迭代器和生成器函数来输出斐波那契数列的第**10**项~第**20**项

### 题目3-4：获取系统当前的时间等信息

编写一个程序，获取系统当前的时间等信息，输出格式如下面方框里所示。然后将这些信息写入一个文本文件，最后将文件中的内容读出来后显示在屏幕上。

说明：第一行是时间和日期，第二行是星期几，第三行是本月有几天。
```
2021-11-09 21:19:43
Tuesday
There are 30 days in this month
```
### 题目3-5：集合及其关系程序

随机生成10个从0~10区间内（包含0和10）的整数，分别组成集合A、集合B，输出A和B的内容、长度、最大值、最小值，以及A和B的并集、交集和差集

### 题目3-6：整数排序和计算平均值

随机产生10个两位的正整数，存入列表ls中，然后对该列表中的数进行排序（由小到大），最后分别输出：排序后的列表、这10个数的平均数，以及大于平均值的数的个数。

### 题目3-7：根据奖金计算利润

企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

### 题目3-8：求s=a+aa+aaa+aaaa+aa...a的值

求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

```
2 = 0 + 2*10^0
22 = 2 + 2*10^1 
222 = 22 + 2*10^2
```

### 题目3-9：对文本文件进行统计

参考例15.14编写一个文本统计程序，利用正则表达式对文本文件“abstract.txt”中读取字符串序列，统计文本文件“abstract.txt”中包含的段落数、行数、句数、单词数，以及统计各单词出现的频率。abstract.txt文件的内容如下面框中所示，要事先创建该文件。
```
Cloud services are exploding, and organizations are converging their data centers in order to take advantage of the predictability, continuity, and quality of service delivered by virtualization technologies. 
In parallel, energy-efficient and high-security networking is of increasing importance. Network operators, and service and product providers require a new network solution to efficiently tackle the increasing demands of this changing network landscape. Software-defined networking has emerged as an efficient network technology capable of supporting the dynamic nature of future network functions and intelligent applications while lowering operating costs through simplified hardware, software, and management. 
In this article, the question of how to achieve a successful carrier grade network with software-defined networking is raised. Specific focus is placed on the challenges of network performance, scalability, security, and interoperability with the proposal of potential solution directions.
```

### 题目3-10：单词的去重和排序

编写一个程序，接收一系列单个空格分隔的单词作为输入，在删除所有重复的单词并按各单词的首字母的升序排序后，打印这些单词。

假设向程序提供以下输入:

`hello world and practice makes perfect and hello world again `

则输出为:

`again and hello makes perfect practice world`