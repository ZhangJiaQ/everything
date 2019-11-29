## 一、 忘了
## 二、 忘了
## 三、 字典和集合
我们在dict中获取不存在的key的时候实际会报错

可以使用collection.defaultdict防止出现这种问题

或者在自己的dict子类中实现__missing__方法

在Python3中，一个dict.keys()可以视作一个视图集合，在其中进行In的查询操作的时间复杂度是O（1）

在Python2中，一个dict.keys()则是一个list，在其中进行查询的时间复杂度为O(n)

字典的变种

dict 标准dict

defaultdict 包含默认值的idct

orderdict

MappingProxyType 接收一个map返回一个MPT对象（只读Map）


set(**[1,2,3]**)要比{1，2，3}慢

是因为{}会使用一种BULID_SET来创建set

而前者需要先BULID_LIST然后调用转换方法

集合推导式

查询多个key in dict set list

最快为set & set

其次set 

然后dict

最后 list

前者都用了Hashtable, list需要全部扫描

在dict中增加一个key

首先会使用内置的hash()方法计算key的hash值

hash方法直接作用与内置类型，作用于用户类型的时候则是调用用户类型的__hash__方法


### Python内部解决哈希冲突
Python内部是运用一个稀疏数组对dict进行存储，数组中的每个单元我们成为bucket，每个bucket存入对key和value的引用

1. 我们在取出dict[key]的值的时候，实际上Python会调用hash(key)计算散列值，把这个值的最低几位数字当作偏移量，在散列表中查询bucket，如果查询为空，则抛出KeyError，如果非空，则判断found_key == key是否为真，为真的返回found_value
2. 如果不匹配的话，则发生了散列冲突，产生原因是散列表实际将随机的元素映射到只有几位的数字上，为了解决散列冲突，我们在散列值另外再取几位，然后用特殊方式处理下，把新抛出的数字作为偏移量进行查询，如果查到了则判断found_key == key，为真则返回found_value，如果又产生散列冲突则重复步骤2

![图片](https://uploader.shimo.im/f/zSt8NotltuACNLSg.png!thumbnail)

### ### dict的实现与其可能产生的问题
1. key必须可hash，且两个自定义对象__eq__相等时__hash__方法也得相等
2. dict内存消耗很大，因为用了稀疏数组存元素，需要空闲空间
3. 键查询很快
4. 键的顺序取决于添加顺序
5. 添加新键可能会改变已有键的顺序
### set的实现
set的实现与dict类似，只不过每个bucket上只存了一个对key的引用

## 四、 文本和字节序列
人类使用text，电脑使用bytes

大概本章讲了一下内容

1. 字符、码位和字节表述
1. bytes、bytearray 和 memoryview 等二进制序列的独特特性
1. 全部 Unicode 和陈旧字符集的编解码器
1. 避免和处理编码错误
1. 处理文本文件的最佳实践
1. 默认编码的陷阱和标准 I/O 的问题
1. 规范化 Unicode 文本，进行安全的比较
1. 规范化、大小写折叠和暴力移除音调符号的实用函数
1. 使用 locale 模块和 PyUCA 库正确地排序 Unicode 文本
1. Unicode 数据库中的字符元数据
1. 能处理字符串和字节序列的双模式 API
### 字符、码位和字节
将码位在缓缓为字节序列就是encoding   将字节序列转换为码位就是decoding

str -> utf-8 就是encoding

utf-8 -> str 就是decoding

encoding  -> 将人类可读的str 编码 成计算机可读的bytes

decoding  -> 将计算机可读的bytes 解码 成人类可读的str编码

打印ACSII码的时候出现\xe之类的，是因为其字节不在ASCII可打印的范围内

### 结构体和内存视图
地方

### 理解 Encode/Decode 问题
处理EncodeError

处理DecodeError

## 五、一等函数
### 把函数视作对象
### 高阶函数
### 匿名函数
### 可调用对象
### 用户定义得可调用类型
    可以实现__call__方法，使得对象可以像函数一样被调用

### 从定位参数到仅限关键字参数
### 获取关于参数的信息
在计算机科学中，内省是指计算机程序在运行时（Run time）检查对象（Object）类型的一种能力，通常也可以称作运行时类型检查。

不应该将内省和反射混淆。相对于内省，反射更进一步，是指计算机程序在运行时（Run time）可以访问、检测和修改它本身状态或行为的一种能力。

### 函数注解
函数注解的内容只会存在函数对象得__annotations__属性内，不做任何操作

### 支持函数式编程的包
operator下面的itemgetter可以作为sorted排序的key，而且可以支持多个参数

可以使用functools.partial冻结部分参数，然后传剩下的即可。

其实也就是基于一个函数创建一个新的可调用对象，把原函数的某些参数固定

## 六、 使用一等函数实现设计模式
我们建议在有一等函数的语言中 重新审视 策略 命令 模板方法 访问者模式

### 1  重构策略模式
abc基类，只能被继承，不能被实例化

是用函数代替只有一个方法的类，效果要比实现用户自定义的类要好，因为各个策略函数在

Python编译模块的时候只会创建一次

### 2  选择最佳策略
我们可以使用globals()查询模块中所有的函数

```
    promos = [globals()[name] for name in globals()
```
          if name.endswith("_promo") and name != "best_promo"]

也可以把所有策略放到一个模块里 使用
```
    promos = [func for name, func in
```
###     inspect.getmembers(promotions, inspect.isfunction)]

3    命令模式
## 七、函数的装饰器和闭包
闭包

Python 如何计算装饰器句法

Python 如何判断变量是不是局部的

闭包存在的原因和工作原理

nonlocal 能解决什么问题

实现行为良好的装饰器

标准库中有用的装饰器

实现一个参数化装饰器

### 1 装饰器的基础知识
### 2 Python何时执行装饰器
装饰器的关键特性是，他们在被装饰的函数定义之后立即运行，也就是通常在导入(import 

mudule)时，就运行

函数装饰器在导入模块时立即执行，而被装饰的函数只在明确调用时运行

### 3 使用装饰器改进“策略”模式
装饰器的第一个用法 ”注册“装饰器

### 4 变量作用域规则
Python编译器会将函数体中声明过的变量是为本地变量，未声明过的则会去全局变量域中

找

### 5 闭包
审查闭包返回的 averager 对象，我们发现 Python 在 __code__ 属性（表示编译后的函数定义体）中保存局部变量和自由变量的名称，

闭包是一种函数，它会保留定义函数时存在的自由变量的绑定，这样调用函数时，虽然定义作用域不可用了，但是仍能使用那些绑定。

### 6 nonlocal声明
但对于数字、字符串、元组这种不可变类型来讲，只能读取，不能更新，如果重新绑定的话，会隐式创建局部变量，对没有声明的局部变量更新会报错，当然也不会保存在闭包中。

当然可以使用nonlocal声明变量为自由变量。

### 7 实现一个简单的装饰器
实际上 被装饰的函数在Import的时候会直接持有装饰器返回的函数的引用

这是装饰器的典型行为：把被装饰的函数替换成新函数，二者接受相同的参数，而且（通常）返回被装饰的函数本该返回的值，同时还会做些额外操作。

可以使用装饰器@functools.wraps，使得被装饰函数的__name__等属性不被替换，但功能

被替换

### 8 标准库中的装饰器
lru_cache

singledispatch

实际上我们的Python不支持函数和方法的重载，所以我们如果要写一个函数，这个函数接收参数为A，当A为不同类型的参数时我们分发到不同的业务逻辑里

那么我们可能写一个函数然后if elif else 会导致函数过长

写多个函数然后进行调用也需要if leif else

这样singledispathc就可以使用了，帮助我们对不同的参数做不同的处理方式

```
from functools import singledispatch


class A:
    pass


@singledispatch
def print_type(obj):
    print(111)
    pass


@print_type.register(str)
def _(string):
    print( "This is str", string)


@print_type.register(float)
@print_type.register(int)
def _(number):
    print("This is number", number)


@print_type.register(object)
def _(obj):
    print("User object", obj)


@print_type.register(tuple)
@print_type.register(list)
def _(seq):
    for d in seq:
        print_type(d)
    print("This is a seq")


if __name__ == "__main__":
    a = A()
    print_type([1,"2", a])
```
当然 如果可能的话，register尽量使用抽象基类，
比如使用numberts.Number代替float 和 int，这样代码兼容的类型更广泛

使用abs.MutableSequest

尽量少处理具体实现

A single class with many overloaded variations of a method is better than a single function with a lengthy stretch of if/elif/elif/elif blocks.

在一个类中为同一个方法定义多个重载变体，比在一个函数中使用一长串 if/elif/elif/elif 块要更好。

### 9 叠放装饰器
离函数越近的越早被调用

### 10 参数化装饰器
参数化装饰器也就是装饰器工厂

所以需要多嵌套一层才可以使用

# 第三单元、面向对象惯用法
## 八、对象引用、可变性和垃圾回收
1 变量不是盒子

2 标识 相等性和别名

== 和 is 的区别

3 默认做浅复制

浅复制与深复制的区别

4 函数的参数作为引用的时候

Python唯一支持的参数传递模式是共享传参，共享传参是指函数的各个形式参数获得实参

中各个引用的副本，也就是说函数内部的形参是实参的别名。

不要使用可变类型作为函数参数的默认值

防御传递可变参数

5 del和垃圾回收

del不会删除对象，但对象可能因为执行del后变得不可获取从而被删除

6 弱引用

7 Python对不可变类型施加的把戏

不可变集合不变的是所含对象的标识

## 九、符合Python风格的对象
使用format调用对象得__format__方法

classmethod实际上可以允许类方法不被实例化调用，但能访问类属性（而不是Init的实例化

属性）

1 格式化显示

Python的私有属性和受保护的属性

Python为了防止私有属性被覆盖，会使用名称改写（name mangling）

比如 A对象有__i私有属性，我们调用这个私有属性的时候，需要输入A._A__i才能调用

2 使用__slots__节省内存空间

不应该为了避免创建实例属性而使用__slot__属性，__slot__属性只应该用于节省内存。

*多线程

只是在 IO 密集场景下才有实质用处，IO 操作时线程会主动释放 GIL。但是在 CPU 密集场景 GIL 起主导作用。记住这一句基本上就够了。

3 覆盖类属性

## 十、 序列的修改、散列和切片
2 切片

userObject[1:21:2] 实际上是传入Slice(1,21,2)到userObject的__getitem__方法中。

3 协议鸭子类型

我们在创建功能完善的序列类型无需使用继承，只要实现符合序列协议的方法。

Python的序列协议只需要__len__和__getitem__两个方法

可切片序列，需要实现__getitem__方法即可

5 动态存取属性

特殊的__getattr__方法，实现.选择符

Python只有在对象没有指定名称的属性时，Python才会调用__getattr__方法。

所以，当我们给v.x = 10赋值后，实际上Python对象内部的x属性赋值为10

而本身我们利用的简化getattr方法的值不变，好比有一个虚拟属性。

__setattr__我们自己实现的时候应对特殊情况做处理，不属于特殊情况则调用超类的__setattr__

super()函数用于动态访问超类的方法。

TIPS: 如果实现了__getattr__，同时也要实现__setattr__方法，以防对象的行为不一致。

6 散列和快速等值测试

  functools.reduce(func, iter, initializer)使用的时候尽量使用第三个属性，这样iter对象为空

序列的时候，返回initiualizer值，对于func + - 这个值应当为0， 对于* / 应当为1，因为

initializer会作为初值用于计算

## 十一、接口：从协议到对象
抽象基类是给框架所使用的

1 Python文化中的接口和协议

对Python程序员来讲，X类接口、X协议和X类对象

2 Python序列协议

![图片](https://uploader.shimo.im/f/m3v4uuNnamozuqNv.png!thumbnail)

如果序列协议中没有实现__iter__和__contains__方法时，Python会调用__getitem__方法

3 运行时的补丁

Python可变序列需要实现__getitem__方法

实现运行时的补丁，我们可以实现一个函数，然后动态赋值给 UserObject.__getitem__方

法

猴子补丁： 在运行时期修改一个class或者module，但不修改他们的源代码。

鸭子类型： 对象的类型无关紧要，只要实现了特定协议即可。

4 水禽（标题名）

5 定义抽象基类的子类

![图片](https://uploader.shimo.im/f/BckSgp1pZ34Ww7v2.png!thumbnail)

6 标准库的抽象基类

![图片](https://uploader.shimo.im/f/IMK6wvepM3kJveg4.png!thumbnail)

7 定义并使用一个抽象基类

抽象方法指一些只有方法声明，而没有具体方法体的方法

声明一个抽象基类最简单的方法就是继承abc.ABC类

与其他装饰符一起使用时，@abstractmethod应放在最内层

虚拟子类

类的继承关系放置在对象的__mro__属性中

## 十二、继承的优缺点
1 子类化内置类型的缺点

内置类型（C编写）不会调用用户定义的类覆盖的特殊方法

直接子类化内置类型(如dict\list\str)容易出错，因为内置类型的方法通常会忽略用户覆盖的

方法。不要子类化内置类型，用户自定义的类应该继承collections模块中的类，例如

UserDict\UserList\UserString,这些类做了特殊的设计，因此易于扩展。

2 多重继承和方法解析顺序

3 多重继承的真实应用

4 处理多重继承

5 Django通用视图中的混入


## 十三、正确重载运算符
1 运算符重载基础

2 一元运算符

3 重载向量加法运算符 +  

Python在执行 + 操作的时候，例如 执行 a + b时

如果 a 有 __add__ 方法， 而且返回值不是 NotImplemented， 调用a.__add__(b)， 然后返回结果。

如果 a 没有 __add__ 方法， 或者调用 __add__ 方法返回NotImplemented， 检查 b 有没有 __radd__ 方法， 如果有， 而且没有返回 NotImplemented， 调用 b.__radd__(a)， 然后返回结果。

如果 b 没有 __radd__ 方法， 或者调用 __radd__ 方法返回NotImplemented， 抛出 TypeError， 并在错误消息中指明操作数类型不支持。

![图片](https://uploader.shimo.im/f/G26hpYPkFuEgsfDt.png!thumbnail)

4 重载乘法运算符 *

6 增量赋值运算符 += *= 

如果未实现__iadd__时， a += b  ----->    a = a + b 

也就是新建实例后重新绑定

如果实现__iadd__则会调用这个方法，原地修改左操作数。

# 第四单元 控制流程
## 十四、可迭代的对象、迭代器和是生成器
### 1 可迭代序列第一版
序列可迭代的原因： iter()函数

1- 函数iter会检查对象是否实现了__iter__()方法，实现了就调用它， 并生成一个迭代器。

2- 如果对象没有实现__iter__()方法，但是实现了__getitem__方法，Python会创建一个迭

代器，尝试按顺序获取元素。

3- 如果都没实现会抛出TypeError

### 2 可迭代对象与迭代器的对比
标准的迭代器接口需要两个方法__next__和__iter__

__next__返回下一个可用的元素，如果没有元素则抛出StopIteration

__iter__返回self，以便在可用迭代器的地方使用迭代器，例如在for循环中

![图片](https://uploader.shimo.im/f/FZkoHshK3sk7rtlJ.png!thumbnail)

      Iterator不是一种type而是一种protocol

检查X是否为迭代器最好的办法是isinstance(x, abc.Iterator)

迭代器是这样的对象：实现了无参数的__next__方法，返回序列中的下一个元素；如果没有元素了，则抛出StopIteration异常，Python中的迭代器还实现了__iter__方法，因此迭代器可以迭代。

### 3  典型的迭代器
可迭代对象需要有个__iter__方法，每次实例化一个新的迭代器。

迭代器需要有一个__next__方法，返回单个元素，并且也要有__iter__方法，返回selvf。

迭代器模式可以用来

1- 访问一个聚合对象的内容而无需暴露它的内部表示。

2- 支持对聚合内容的多种遍历

3- 为遍历不同的聚合结构提供一个统一的接口

### 4 生成器函数
符合Python习惯的方式是，用生成器函数代替迭代器。

只要Python函数的定义体中有yield关键字，该函数就是生成器函数，调用生成器函数时，会返回一个生成器对象。

生成器函数会创建一个生成器对象，包装生成器函数的定义体。把生成next(...)器传给函数时，生成器函数会向前，执行函数定义体中的yield下一个语句，返回产出的值，并在函数定义体的当前位置暂停。最终，函数的定义体返回时，外层的生成器对象会抛出StopIteration异常这一点与迭代器协议一致。

### 5 惰性实现
re.finditer是re.findall的惰性求值版本，可以节省内存。

### 6 生成器表达式
生成器表达式“()”可以理解为列表表达式的惰性求值版本，不会迫切的生成列表，而是需要时生成

### 7 何时使用生成器表达式
生成器表达式是创建生成器的间接语法，无需先定义函数后使用。

如果生成器表达式需要分多行写，那么应重构为生成器函数。

### 8 生成器实例
--

### 9 标准库中的生成器
--

### 10 yield from
--

### 11 可迭代的归约函数
--

### 12 深入分析iter函数
--

### 13 案例分析：在数据库转换工具中使用生成器
--

### 14 把生成器当作协程
--


## 十五、上下文管理器和else块
### 1 if语句
### 2 上下文管理器和with块
上下文管理器的存在是为了管理with语句，上下文管理协议中包含__enter__和__exit__方法。

with语句开始运行时候，会在上下文管理器中调用__enter__方法

with语句结束的时候，会调用上下文管理器对象中的__exit__方法

## 十六、协程
### 1 生成器如何进化成协程
PEP 342—Coroutines via Enhanced Generators 中对生成器API增加了.send()方法，生成器的调用方可以使用.send()方法发送数据，发送的数据会被生成器当做yield的值，所以生成器可以当做协程使用。

### 2 用作协程的生成器的基本行为
协程有四个状态，我们可以使用inspect.getgeneratorstate()来查询协程目前处于的状态

"GEN_CREATED" 等待开始执行

"GEN_RUNNING" 解释器正在执行

"GEN_SUSPENDED" 在yield表达式中暂停

"GEN_CLOSED" 执行结束

我们通常需要首先使用next(generator)来“预激”协程，也就是让协程向前执行到第一个yield表达式上，从而作为活跃的协程使用

### 3 示例： 使用协程计算移动平均值
-

### 4 预激协程的装饰器
每次激活协程都需要使用next(generator)，我们需要简化协程的用法

使用一个装饰器，传入一个协程，调用next，然后返回。

### 5 终止协程和异常处理
协程运行完了或者出现错误后，如果尝试重新激活携程会抛出StopIteration异常。

### 6 让协程返回值
协程return的时候，会将return的值与StopIteration一起抛出。

我们可以使用yield from结构，在内部自动捕获StopIteration异常。

yield from会自动捕获StopIteration异常，还会将return的值作为yield from的值。

### 7 使用yield from
在生成器gen中使用yield from subgen()时，subgen会获得控制权，把产出的值传给gen的调用方，即调用方可以直接控制subgen()

PEP380 Syntax for Delegating to a Subgenerator

yield from的主要功能是打开双向通道，把最外层的调用方与最内层的子生成器连接起来，这样二者可以直接发送和产出值，还可以直接传入异常，而不用在位于中间的协程中添加大量处理异常的代码。

### 8 使用yield from的意义
把迭代器当作生成器使用，相当于把子生成器的定义内联在yield from表达式中。此外，子生成器可以执行return语句，返回一个值，而返回的值会成为yield from表达式的值。

### 9 使用协程做离散事件仿真
--


## 十七、使用期物处理并发
### 1 网络下载的三种风格
**按顺序下载**

--

**线程池下载**

concurrent.futures模块的主要特色是ThreadPoolExecutor和ProcessPoolExecutor类，这两个类实现的接口能分别在不同的线程或进程中执行可调用的对象。

我们可以使用ThreadPoolExecutor.map

当然我们也可以使用futures.as_completed

**期物**

期物封装待完成的操作，可以放入队列，完成的状态可以查询，得到结果（或抛出异常）后可以获取结果，通常情况下不要自己创建Futures,而是交由框架实例化。

### 2 阻塞型IO和GIL
Python标准库中的每一个阻塞性I/O函数都会释放GIL，比较适合IO密集型任务。

首先，要从你常用的IO操作谈起，比如read和write，通常IO操作都是阻塞I/O的，也就是说当你调用read时，如果没有数据收到，那么线程或者进程就会被挂起，直到收到数据。阻塞的意思，就是一直等着。阻塞I/O就是等着数据过来，进行读写操作。应用的函数进行调用，但是内核一直没有返回，就一直等着。应用的函数长时间处于等待结果的状态，我们就称为阻塞I/O。

### 3 使用concurrent.futures模块启动启程
我们在做计算密集型任务的时候，可以使用多进程来加速任务完成速度。

ThreadPoolExcutor在使用的时候需要传入max_worker

ProcessPoolExecutor在使用的时候不需要，默认为os.cpu_count().

### 4 实验Executor.map方法
实验很容易就可以完成

总结： 我们在使用executor.map方法时候，只能传入一个函数和一组数据。

而使用Executor.submit和futures.as_completed方法可以传入多个函数和多个数据（当然是一个一个传入）

### 5 显示下载进度并处理错误
线程与多进程的替代方案

如果futures模块无法满足我们的需要，我们可能就需要使用更高级的threading模块以及mutiprocessing模块，mutiprocess模块更优势在于可以在进程中传递数据。

## 十八、使用asyncio包并发处理
使用aiohttp的时候

1. 调用aiohttp.request中，实例化一个ClientSession对象，

    然后将ClientSession对象的_request方法传给SessionRequestContextManager

2. SessionRequestContextManager实现了 __aenter__与__aexit__方法，用与建立和关闭连接


