
# 汉诺塔问题
- 规则
    - 1.每次只能移动一个盘子
    - 2.任何一次移动，每个塔的状态必须是小盘子在上，大盘子在下
- 移动
    - A B C 三个塔 
        - n = 1 一个盘子 A-->C
        - n = 2 二个盘子 A-->B A-->C B-->C
        - n = 3 三个盘子 
            1. 把A上的两个盘子，通过C移动到B上，调用递归实现
            2. 把A上剩下的一个最大盘子移动到C上，A-->C
            3. 把B上两个盘子，借助于A，移动到C上去，调用递归
        - n = n 
            1. 把A上的n-1个盘子，通过C移动到B上，调用递归
            2. 把A上剩下的一个最大盘子移动到C上，A-->C
            3. 把B上n-1个盘子，借助于A，移动到C上去，调用递归


```python
def HanoiTower(n, a, b, c):
    '''
    n:表示几个盘子
    a:表示第一个柱子
    b:表示第二个柱子
    c:表示第三个柱子
    '''
    if n == 1:
        print(a, '-->', c)
        return None
    #把A上的n-1个盘子，通过C移动到B上，调用递归
    HanoiTower(n-1, a, c, b)
    #把A上剩下的一个最大盘子移动到C上，A-->C
    print(a, '-->', c)
    #把B上n-1个盘子，借助于A，移动到C上去，调用递归
    HanoiTower(n-1, b, a, c)
HanoiTower(1, 'A', 'B', 'C')
print('-------------------')
HanoiTower(2, 'A', 'B', 'C')
print('-------------------')
HanoiTower(3, 'A', 'B', 'C')
```

    A --> C
    -------------------
    A --> B
    A --> C
    B --> C
    -------------------
    A --> C
    A --> B
    C --> B
    A --> C
    B --> A
    B --> C
    A --> C
    

# list(列表)
- del:删除命令


```python
# del删除
a = [1, 2, 3, 4, 5]
del a[4]
print(a)
```

    [1, 2, 3, 4]
    


```python
# del删除
# 如果使用del后 a的id改变说明del删除生成了新的list
a = [1, 2, 3, 4, 5]
print(id(a))
del a[4]
print(id(a))
print(a)
```

    2612412576136
    2612412576136
    [1, 2, 3, 4]
    


```python
# del一个变量后，不能再继续使用该变量
del a
print(a)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-24-71e9f5b181af> in <module>()
          1 # del一个变量后，不能再继续使用该变量
          2 del a
    ----> 3 print(a)
    

    NameError: name 'a' is not defined



```python
# 使用加号 连接两个列表
a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
c = a + b
print(c)
```

    [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
    


```python
# 使用乘号操作列表
# 列表直接跟一个整数相乘
# 相当于把n个列表接在了一起
a = [1, 2, 3, 4, 5]
b = a * 2
print(b)
```

    [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    


```python
# 成员资格运算
# 判断一个元素是否再list中
a = [1, 2, 3, 4, 5, 6]
b = 6
c = b in a 
print(c)
# not in
print(b not in a)
```

    True
    False
    

# 链表的遍历
- for
- while


```python
# for in list
a = [1, 2, 3, 4, 5]

# 挨个打印a里边的元素
for i in a:
    print(i)
```

    1
    2
    3
    4
    5
    


```python
# range 
# in 后边的变量要求是可迭代的内容
for i in range(1,10):
    print(i)
print(type(range(1,10)))
```

    1
    2
    3
    4
    5
    6
    7
    8
    9
    <class 'range'>
    


```python
# while循环遍历list
# 一般不用while
a = [1,2,3,4,5]
length = len(a)
# indx 表示list的下标
indx = 0
while indx < length:
    print(a[indx])
    indx += 1
```

    1
    2
    3
    4
    5
    


```python
# 双层列表循环
# a为嵌套列表，或者叫双层列表
a = [['one', 1], ['two', 2], ['three', 3]]
for k,v in a:
    print(k,v)
```

    one 1
    two 2
    three 3
    


```python
# 双层列表循环变异
# a为嵌套列表，或者叫双层列表
a = [['one', 1, 2], ['two', 2, 'hello'], ['three', 3]]
for k,v in a:
    print(k,v)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-6-0ba6e5952100> in <module>()
          2 # a为嵌套列表，或者叫双层列表
          3 a = [['one', 1, 2], ['two', 2, 'hello'], ['three', 3]]
    ----> 4 for k,v in a:
          5     print(k,v)
    

    ValueError: too many values to unpack (expected 2)



```python
# 双层列表循环变异
# a为嵌套列表，或者叫双层列表
a = [['one', 1, '一'], ['two', 2, '二'], ['three', 3, '三']]
# 这个例子说明 k，v，w的个数应该跟解包出来的变量个数一致
for k,v,w in a:
    print(k,v,w)
```

    one 1 一
    two 2 二
    three 3 三
    

# 列表内涵：list content
- 通过简单方法创作列表


```python
# for 创建
a = ['a', 'b', 'c']
# 用 list a 创建 list b
b = [i for i in a]
print(b)
```

    ['a', 'b', 'c']
    


```python
# 对a中所有元素乘以10，生成一个新list
a = [1, 2, 3, 4, 5]
# 用 list a 创建 list b
b = [i*10 for i in a]
print(b)
```

    [10, 20, 30, 40, 50]
    


```python
# 过滤原来的list放入新的列表
# 如原列表a 把a中所有的偶数生成新的列表b
a = [x for x in range(1,35)]# 生成从1到34的列表
b = [i for i in a if i % 2 == 0]
print(b)
```

    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34]
    


```python
# 列表生成式可以嵌套
# 有两个列表a，b
a = [i for i in range(1,4)]# 生成list a
print(a)
b = [i for i in range(100,400) if i % 100 == 0]
print(b)
# 列表生成是可以嵌套
c = [m+n for m in a for n in b]
print(c)
# 等价于下面代码
for m in a:
    for n in b:
        print(m+n, end=" ")
print()        
# 嵌套的列表生成式可以用条件表达式
c = [m+n for m in a for n in b if m+n < 250]
print(c)
```

    [1, 2, 3]
    [100, 200, 300]
    [101, 201, 301, 102, 202, 302, 103, 203, 303]
    101 201 301 102 202 302 103 203 303 
    [101, 201, 102, 202, 103, 203]
    

# 关于列表常用函数


```python
# len: 求列表的长度
a = [x for x in range(1,100)]
print(len(a))

# max: 求列表中的最大值
print(max(a))

# min: 求列表中的最小值
print(min(a))
```

    99
    99
    1
    


```python
# list: 将其他格式的数据转换成list
a = [1,2,3]
print(list(a))
b = "huojuntao"
print(list(b))
# 把range产生的内容转换成list
print(list(range(10,15)))
```

    [1, 2, 3]
    ['h', 'u', 'o', 'j', 'u', 'n', 't', 'a', 'o']
    [10, 11, 12, 13, 14]
    

## 传值与传址的区别
- 对于简单的数值，采用传值操作，即在函数内的操作不影响外面的变量
- 对于复杂变量，采用传址操作，此时函数内的参数与外部的是同一份内容，修改会同时改变


```python
# 对于简单的数值，采用传值操作，即在函数内的操作不影响外面的变量
# 对于复杂变量，采用传址操作，此时函数内的参数与外部的是同一份内容，修改会同时改变
def a(n):
    n[2] = 300
    print(n)
    return None
def b(n):
    n += 100
    print(n)
    return None

an = [1,2,3,4,5]
bn = 9

print(an)
a(an)
print(an)

print(bn)
b(bn)
print(bn)
```

    [1, 2, 3, 4, 5]
    [1, 2, 300, 4, 5]
    [1, 2, 300, 4, 5]
    9
    109
    9
    

# 关于列表的函数


```python
l = ['My', "name is HuoJuntao", 21, 3+5j]
l
```




    ['My', 'name is HuoJuntao', 21, (3+5j)]




```python
# append 插入一个内容
a = [x for x in range(1,5)]
print(a)
a.append(100)
print(a)
```

    [1, 2, 3, 4]
    [1, 2, 3, 4, 100]
    


```python
# insert 指定位置插入 insert(index,date)插入的位置是index前面
print(a)
a.insert(1,"哈哈")
print(a)
```

    [1, 2, 3, 4, 100]
    [1, '哈哈', 2, 3, 4, 100]
    


```python
# 删除
# del 删除
# pop 从队尾拿出一个元素，即把最后一个元素取出来
print(a)
last_ele = a.pop()
print(last_ele)
print(a)
del(a[0])
print(a)
```

    [1, '哈哈', 2, 3, 4, 100]
    100
    [1, '哈哈', 2, 3, 4]
    ['哈哈', 2, 3, 4]
    


```python
# remove 在列表中删除指定的值的元素
# 如果被删除的值没在list中 会报错
# 即 删除list指定值的操作应该使用try...excepty语句，或者先行判断
# if x in list:
#     list.remove(x)
print(a)
print(id(a))
a.remove('哈哈')
print(a)
print(id(a))
#两个id一样 说明remove操作是在原list直接操作
```

    ['哈哈', 2, 3, 4]
    2338791969352
    [2, 3, 4]
    2338791969352
    


```python
# clear 清空
print(a)
print(id(a))
a.clear()
print(a)
print(id(a))
# 如果不需要列表地址保持不变，则清空列表可以使用以下方式
# a = list()
# a = []
```

    [2, 3, 4]
    2338791969352
    []
    2338791969352
    


```python
# reverse 翻转 原地翻转
a = [1,2,3,4,5,6]
print(id(a))
print(a)
a.reverse()
print(a)
print(id(a))
```

    2338791849864
    [1, 2, 3, 4, 5, 6]
    [6, 5, 4, 3, 2, 1]
    2338791849864
    


```python
# extend 扩展列表，两个列表，把一个直接拼接到后一个上
print(a)
b = [1,2,3]
a.extend(b)
print(a)
```

    [6, 5, 4, 3, 2, 1]
    [6, 5, 4, 3, 2, 1, 1, 2, 3]
    


```python
# count 查找列表中指定值或元素的个数
print(a)
a_len = a.count(3)
print(a_len)
```

    [6, 5, 4, 3, 2, 1, 1, 2, 3]
    2
    


```python
# copy 拷贝 钱拷贝

# 列表类型变量复制示例
a = [1,2,3,4,5,666]
print(a)
print(id(a))
# list类型，简单的赋值操作是传地址
b = a
b[3] = 777
print(a)
print(b)
print(id(b))
print("*" * 30)
# 为了解决以上问题，list赋值需要采用copy函数
c = a.copy()
print(c)
# id变化，不是同一个地址
print(id(c))
```

    [1, 2, 3, 4, 5, 666]
    2338792523784
    [1, 2, 3, 777, 5, 666]
    [1, 2, 3, 777, 5, 666]
    2338792523784
    ******************************
    [1, 2, 3, 777, 5, 666]
    2338791939464
    


```python
# 深拷贝与浅拷贝的区别
# 出现该问题的原因是 copy是浅拷贝，即只拷贝一层内容
# 深拷贝需要使用特定工具
a = [1,2,3,[10,20,30]]
b = a.copy()
print(id(a))
print(id(b))
print("*" * 30)
print(id(a[3]))
print(id(b[3]))
a[3][2] = 6666
print(a)
print(b)
print(id(a))
print(id(b))

```

    1946088732040
    1946089521736
    ******************************
    1946089391816
    1946089391816
    [1, 2, 3, [10, 20, 6666]]
    [1, 2, 3, [10, 20, 6666]]
    1946088732040
    1946089521736
    

# 元祖- tuple
- 元祖可以看成是一个不可更改的list
## 元祖创建


```python
# 创建空元祖
t = ()
print(type(t))
print("*" * 30)

# 创建只有一个值的元祖
t =(1)
print(type(t))
t =(1,)
print(type(t))

t = 1,
print(type(t))
print("*" * 30)

# 创建多个值的元祖
t = (1,2,3,4,5)
print(type(t))
t = 1,2,3,4,5,6
print(type(t))

# 使用其他结构创建
l = [1,2,3,4,5,6,7]
t = tuple(l)
print(t)
print(type(t))
```

    <class 'tuple'>
    ******************************
    <class 'int'>
    <class 'tuple'>
    <class 'tuple'>
    ******************************
    <class 'tuple'>
    <class 'tuple'>
    (1, 2, 3, 4, 5, 6, 7)
    <class 'tuple'>
    

## 元祖的特性
- 是序列表，有序
- 元祖数据值可以访问，不能修改
- 元祖数据可以是任意类型
- list的所有特性，除了可修改外tuple都具有


```python
# 索引操作
t = (1,2,3,4,5,6)
print(t[3])
```

    4
    


```python
# 超标错误
print(t[10])
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-19-a7f4fce0da2c> in <module>()
          1 # 超标错误
    ----> 2 print(t[10])
    

    IndexError: tuple index out of range



```python
t = (1,2,3,4,5,6,7)
t1 = t[1::2]#从下标1开始，到结束，步长为2
print(id(t))
print(id(t1))
print(t1)
# 切片可以超标
t2 = t[2:100]
print(t2)
```

    1946089252760
    1946089496440
    (2, 4, 6)
    (3, 4, 5, 6, 7)
    


```python
# 序列相加
t1 = (1,2,3)
t2 = (4,5,6)
# 传址操作
print(t1)
print(id(t1))
t1 += t2
# 类似于 t1 = (1, 2, 3, 4, 5, 6)
print(t1)
print(id(t1))
t3 = t1 + t2
print(t3)
# tuple的不可修改指的是内容的不可修改
t1[1] = 100
```

    (1, 2, 3)
    1946090123696
    (1, 2, 3, 4, 5, 6)
    1946089236904
    (1, 2, 3, 4, 5, 6, 4, 5, 6)
    


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-27-72b78c063e28> in <module>()
         12 print(t3)
         13 # tuple的不可修改指的是内容的不可修改
    ---> 14 t1[1] = 100
    

    TypeError: 'tuple' object does not support item assignment



```python
# 元祖相乘
t = (1,2,3)
t = t * 3
print(t)
```

    (1, 2, 3, 1, 2, 3, 1, 2, 3)
    


```python
# 成员检测
t = (1,2,3,4)
if 2 in t:
    print("YES")
else:
    print("NO")
```

    YES
    


```python
# 元祖遍历，一般采用for
# 1.单层元祖遍历
t = (1,2,3,"huojutuntao","哈哈")
for i in t:
    print(i , end=" ")
```

    1 2 3 huojutuntao 哈哈 


```python
# 2.双层元祖的遍历
t = ((1,2,3),(2,3,4),("my","name","huojuntao"))

for i in t:
    print(i)
    
for k,m,n in t:
    print(k, "---", m, "---", n)
```

    (1, 2, 3)
    (2, 3, 4)
    ('my', 'name', 'huojuntao')
    1 --- 2 --- 3
    2 --- 3 --- 4
    my --- name --- huojuntao
    

# 关于元祖的函数


```python
# len:获取元祖长度
t = (1,2,3,4,5,6)
len(t)
```




    6




```python
# max,min:最大值最小值
print(max(t))
print(min(t))
```

    6
    1
    


```python
# tuple:转化或创建元祖
l = [1,2,3,4,5]
t = tuple(l)
print(t)

t = tuple()
print(t)
```

    (1, 2, 3, 4, 5)
    ()
    

# 元祖的函数
- 基本跟list通用


```python
# count: 计算指定数据出现的次数
t = (2,21,21,2,2,2,1,3,64,8)
print(t.count(2))
# index: 求指定元素在元祖中的索引位置,如果多个返回第一个
print(t.index(1))
```

    4
    6
    

# 元祖变量交换法
- 两个变量交换值


```python
# 两个变量交换值
a = 1
b = 3
print(a)
print(b)
print("*" * 30)
# java程序员
c = a
a = b
b = c
print(a)
print(b)
print("*" * 30)
# python写法
a, b = b, a
print(a)
print(b)
```

    1
    3
    ******************************
    3
    1
    ******************************
    1
    3
    

# 集合-Set
- 集合是高中数学的一个概念
- 一堆确定的无序的唯一的数据，集合中每一个数据成为一个元素


```python
# 集合的定义
s = set()
print(s)
print(type(s))

# 大括号定义必须要有值，否则定义出的是一个dict
s = {1,2,3,4,5}
print(s)
print(type(s))
```

    set()
    <class 'set'>
    {1, 2, 3, 4, 5}
    <class 'set'>
    


```python
# 如果只用大括号定义，则定义的是一个dict类型
d = {}
print(d)
print(type(d))
```

    {}
    <class 'dict'>
    

# 集合的特征
- 集合内数据无序，即无法使用索引和分片
- 集合内数据元素具有唯一性，可以用来排除重复数据
- 集合内数据，str，int，float，tuple，冰冻集合等，即内部只能放置可哈希数据

# 集合序列操作


```python
# 成员检测
# in，not in
s = {1,2,3,"hjt",4,5,6,"name"}
print(s)
if "hjt" in s:
    print("YES")
else:
    print("NO")
```

    {1, 2, 3, 'hjt', 4, 5, 6, 'name'}
    YES
    

# 集合遍历操作


```python
# for循环
s = {1,2,3,"hjt",4,5,6,"name"}
for i in s:
    print(i, end=" ")
```

    1 2 3 hjt 4 5 6 name 


```python
# 带有元祖的集合遍历
s = {(1,2,3),("huo","jun","tao"),(4,5,6)}
for k,m,n in s:
    print(k, "--", m, "--", n)
for k in s:
    print(k)
```

    huo -- jun -- tao
    4 -- 5 -- 6
    1 -- 2 -- 3
    ('huo', 'jun', 'tao')
    (4, 5, 6)
    (1, 2, 3)
    

# 集合的内涵


```python
# 普通集合内涵
# 以下集合在初始化后，自动过滤掉重复元素
s = {123,3214,1,1,1,1,1,23232,434,123,124,5,1}
print(s)

# 带条件的集合内涵
ss = {i for i in s if i % 2 == 0}
print(ss)
```

    {23232, 1, 5, 3214, 434, 123, 124}
    {23232, 434, 124, 3214}
    


```python
# 多循环的集合内涵
s1 = {1,2,3,4}
s2 = {"my","name","is","hjt"}

s = {m*n for m in s1 for n in s2}
print(s)

s = {m*n for m in s1 for n in s2 if m == 2}
print(s)
```

    {'namename', 'hjt', 'mymymy', 'isisisis', 'isis', 'namenamenamename', 'is', 'mymymymy', 'mymy', 'my', 'name', 'hjthjt', 'isisis', 'hjthjthjthjt', 'hjthjthjt', 'namenamename'}
    {'namename', 'mymy', 'isis', 'hjthjt'}
    

# 集合函数/关于集合的函数


```python
# len,max,min:跟其他基本函数一致
s = {321,123,123,4,3,24,1232,23,1,23,123}
print(s)
print(len(s))
print(max(s))
print(min(s))
```

    {321, 1, 3, 4, 1232, 23, 24, 123}
    8
    1232
    1
    


```python
# set: 生成一个集合
l = [1,2,32,4,4,5]
s = set(l)
print(s)
```

    {32, 1, 2, 4, 5}
    


```python
# add: 向集合内添加元素
s = {1}
s.add(123)
print(s)
```

    {1, 123}
    


```python
# clear: 原地清空数据
s = {1,1,2,31,23,5}
print(s)
print(id(s))
s.clear()
print(s)
print(id(s))
```

    {1, 2, 5, 23, 31}
    1946090332680
    set()
    1946090332680
    


```python
# copy: 拷贝
# remove: 移除指定的值，如果要删除的值不存在 会报错
# discard: 移除集合中指定的值，如果值不存在不会报错
s = {1,2,3,4,5,6,7,"haha"}
s1 = s.copy()
print(s)
print(s1)
print(id(s))
print(id(s1))
print("*" * 30)

s.remove("haha")
print(s)
print(id(s))

s.discard("13212312312")
print(s)
print(id(s))
```

    {'haha', 1, 2, 3, 4, 5, 6, 7}
    {'haha', 1, 2, 3, 4, 5, 6, 7}
    3082314433928
    3082300333640
    ******************************
    {1, 2, 3, 4, 5, 6, 7}
    3082314433928
    {1, 2, 3, 4, 5, 6, 7}
    3082314433928
    


```python
# pop 随机移除一个元素
s = {1,1,23,214,124,123,412,5}
d = s.pop()
print(d)
print(s)
```

    1
    {5, 214, 23, 412, 123, 124}
    


```python
# 集合函数
# intersection： 交集
# difference： 差集
# union： 并集
# issubset： 检查一个集合是否为另一个的子集
# issuperset： 检查一个集合是否为另一个的超集
s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}

print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.union(s2))
print(s1.issubset(s2))
print(s1.issuperset(s2))
```

    {4, 5, 6}
    {1, 2, 3}
    {1, 2, 3, 4, 5, 6, 7, 8, 9}
    False
    False
    


```python
# 集合的数学操作
s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7}

s_1 = s1 - s2
print(s_1)
s_2 = s1 + s2
print(s_2)
```

    {1, 2, 3}
    


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-22-30e395f4f067> in <module>()
          5 s_1 = s1 - s2
          6 print(s_1)
    ----> 7 s_2 = s1 + s2
          8 print(s_2)
    

    TypeError: unsupported operand type(s) for +: 'set' and 'set'


# frozen set: 冰冻集合
- 就是不可以进行任何修改的集合
- frozenset是一种特殊的集合


```python
# 创建
s = frozenset()
print(type(s))
print(s)
```

    <class 'frozenset'>
    frozenset()
    

# dict字典
- 字典是一种组合数据，没有顺序的组合数据，数据以键值对形式出现


```python
# 字典的创建
# 创建空字典
d = {}
print(type(d))

d = dict()
print(type(d))

# 创建有值的字典
# 每一组数据用冒号隔开，每一对数据用逗号隔开
d = {"one":1, "two":2, "three":3}
print(d)

d = dict({"one":1, "two":2, "three":3})
print(d)

d = dict(one=1, two=2, three=3)
print(d)

d = dict([("one",1), ("two",2), ("three",3)])
print(d)
```

    <class 'dict'>
    <class 'dict'>
    {'one': 1, 'two': 2, 'three': 3}
    {'one': 1, 'two': 2, 'three': 3}
    {'one': 1, 'two': 2, 'three': 3}
    {'one': 1, 'two': 2, 'three': 3}
    

# 字典的特征
- 字典是序列类型，但是是无序序列，所以没有分片与索引
- 字典中的数据每个都由键值对组成，即k，v对
    - key: 必须是可哈希的值，比如int,string,float,tuple 但是list,set,dict不行
    - value: 任何值

# 字典常见操作


```python
# 访问数据
d = {1:"one", 2:"two", 3:"three"}
# 注意访问格式，中括号内是键值
print(d[1])

d[1] = "一"
print(d)

# 删除 使用del操作
del d[1]
print(d)
```

    one
    {1: '一', 2: 'two', 3: 'three'}
    {2: 'two', 3: 'three'}
    


```python
# 成员检测 in, not in
# 成员检测，检测的是key的内容
d = {1:"one", 2:"two", 3:"three", 4:"four"}
if 1 in d:
    print("key")
if "one" in d:
    print("value")
if (2,"two") in d:
    print("key+value")
```

    key
    


```python
# 遍历 在python2与3中 区别比较大，代码不通用
d = {1:"one", 2:"two", 3:"three", 4:"four"}
# 按key来使用for循环
for k in d:
    print(k, "--", d[k])
print("*" * 30)  

# 上面代码可改写为
for k in d.keys():
    print(k, "--", d[k])   
print("*" * 30)

# 只访问字典的值
for v in d.values():
    print(v)
print("*" * 30)

# 注意以下特殊用法
for k,v in d.items():
    print(k, v)
```

    1 -- one
    2 -- two
    3 -- three
    4 -- four
    ******************************
    1 -- one
    2 -- two
    3 -- three
    4 -- four
    ******************************
    one
    two
    three
    four
    ******************************
    1 one
    2 two
    3 three
    4 four
    

# 字典生成式


```python
d = {1:"one", 2:"two", 3:"three", 4:"four"}

# 加限制条件的字典生成式
dd = {k:v for k,v in d.items() if k % 2 == 0}
print(dd)
```

    {2: 'two', 4: 'four'}
    

# 字典的相关函数


```python
# 通用函数: len, max, min, dict
# str(函数): 返回字典的字符串格式
d = {1:"one", 2:"two", 3:"three", 4:"four"}
print(str(d))
```

    {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
    


```python
# clear: 清空字典
# items: 返回字典的键值对组成的元祖格式

d = {1:"one", 2:"two", 3:"three", 4:"four"}
i = d.items()
print(i)
print(type(i))
```

    dict_items([(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')])
    <class 'dict_items'>
    


```python
# keys: 返回键组成的一个结构
k = d.keys()
print(k)
print(type(k))
```

    dict_keys([1, 2, 3, 4])
    <class 'dict_keys'>
    


```python
# values: 同理
v = d.values()
print(v)
print(type(v))
```

    dict_values(['one', 'two', 'three', 'four'])
    <class 'dict_values'>
    


```python
# get: 根据指定键，返回相应值 可以设置默认值
d = {1:"one", 2:"two", 3:"three", 4:"four"}

# get的默认值是None 可以设置
print(d.get(1, "默认值"))
print(d.get(11, "默认值"))

#
print(d.get(111))
print(d[111])
```

    one
    默认值
    None
    


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-64-3fda524f4807> in <module>()
          8 
          9 print(d.get(111))
    ---> 10 print(d[111])
    

    KeyError: 111



```python
# fromkeys: 使用指定的序列作为键，使用一个值作为字典的所有键的值
l = ["壹", "贰", "叁"]
# 注意fromkeys两个参数的类型
# 注意fromkeys的调用主题
d = dict.fromkeys(l, "hahah")
print(d)
```

    {'壹': 'hahah', '贰': 'hahah', '叁': 'hahah'}
    
