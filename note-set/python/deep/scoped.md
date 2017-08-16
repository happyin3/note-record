## Python作用域

[PEP 227 -- Statically Nested Scopes](https://www.python.org/dev/peps/pep-0227/)

### 代码例子

1. 例子1

```
a = 1

def func():
    print a

func()

>> 1
```

全局作用域

2. 例子2

```
a = 1

def func():
    a = 2
    print a

func()

print a

>> 2
>> 1
```

局部作用域

3. 例子3

```
x = 1

for x in range(5):
    y = x

print x, y

>> 4, 4

func_list = [lambda :x for x in range(10)]

print func_list[0]()

>> 9
```

块级作用域，Python没有块级作用域

4. 例子4

```
a = 1

def func():
    b = a
    a = 2
    print b

func()

print a

>> UnboundLocalError: local variable 'a' referenced before assignment
```

声明顺序，Python变量的作用域是整个块，和变量声明位置无关。

5. 例子5

```
a = 1

def func():
    global a
    b = a
    a = 2

    def sub():
        b = 3
        print a, b

    sub()

    print a, b

func()

print a

>> 2, 3
>> 2, 1
>> 2
```

在Python中，一个嵌套的子程序无法写一个属于外层但又非全局作用域的变量。

6. 例子6

```
a = 1

def func():
    exec 'a = 2'

    def sub():
        b = a
        print a, b

    print a

func()

print a

>> SyntaxError: unqualified exec is not allowed in function 'func' because it contains a nested function with free variables

def func():
    from args import *

    def sub():
        b = a
        print a, b

    sub()

func()

>> SyntaxError: import * is not allowed in function 'func' because it contains a nested function with free variables

a = 1

def func():
    # in args, a = 2
    from args import a
    
    def sub():
        b = a
        print a, b

    sub()
    print a

func()

print a

>> 2, 2
>> 2
>> 1

a = 1

def func():
    # in args, a = 2
    import args

    def sub():
        b = a
        print a, b

    sub()
    print a

func()

print a

>> 1, 1
>> 1
>> 1

def func():
    # in args, a = 2
    import args

    def sub():
        b = args.a
        print args.a, b

    sub()

func()

>> 2, 2
```

### 基础概念

1. 作用域
2. 静态作用域、动态作用域
3. 声明次序
4. 全局作用域、局部作用域、嵌套作用域、、块作用域
5. 闭包、自由变量
