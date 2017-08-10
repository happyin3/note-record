## Python作用域

> Python 2.7.6

通过例子来熟悉下Python变量在使用中的几种情况。

1. **全局作用域**

```
a = 1

def func():
    b = a
    print b

func()

>> 1
```

**全局作用域**：这里在`func`中使用全局变量a给局部变量b进行了赋值，输出结果1。

2. **局部作用域**

```
def func():
    a = 1
    print a

func()
pirnt a

>> 1
>> NameError: name 'name' is not defined
```

**局部作用域**：`func()`能正确输出1；而在外部直接打印`a`是报错的，因为`a`是定义在函数`func`中的局部变量，在全局中无法调用，即使执行了`func()`，变量`a`的作用域也只是在函数内部，外部依然无法调用。

3. **块级作用域**

```
if 1:
    a = 1

print a

for i in range(2):
    b = i

print i
print b

>> 1
>> 1
>> 1
```

**块级作用域**：Python没有块级作用域，代码块里的变量，外部可以调用。

4. **嵌套作用域**

```
a = 1

def func():
    a = 2
    def sub():
        print a
    return sub

test = func()
test()

>> 2
```

**嵌套作用域**：`sub()`输出了定义在`sub`父函数`func`中的`a`，查找顺序由内而外。这里有个问题，函数`func`执行完成后，已经退出，函数中定义的变量理应退出，为什么还是正确输出了2，这就涉及**闭包**的概念了。

5. **声明顺序**

```
a = 1

def func1():
    global a
    b = a
    a = 2
    print a, b

def func2():
    b = a
    a = 2
    print a, b

func1()
func2()

>> 2, 1
>> UnboundLocalError: local variable 'a' referenced before assignment
```

**声明顺序**：Python变量声明的作用域是“整个块”，即和声明顺序无关。

6. **混合**

```
i, j = 1, 3

def outer():
    def middle(k):
        def inner():
            global i
            i = 4
        inner()
        return i, j, k
    i = 2
    return middle(j)

print outer()
print i, j

>> 2, 3, 3
>> 4, 3
```

看过以上的例子后，下面来进行一些概念的梳理。

### 概念

#### 作用域
