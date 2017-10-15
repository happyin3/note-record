# -*- coding: utf-8 -*-

'''
从数组找数字（网易2017校园招聘）

http://mp.weixin.qq.com/s/Hz7jdfbAYf1enMepNEI3og

## 参考
1. 寻找数组中只出现一次的数，http://www.cnblogs.com/luxiaoxun/archive/2012/09/08/2676610.html
2. 一个整型数组里除了一个或者两个或者三个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)，http://www.cnblogs.com/joyclub/p/4470357.html
3. 【算法】给定一个数组，除了一个数出现1次之外，其余数都出现3次，输出出现一次的那个数，http://blog.csdn.net/bug_moving/article/details/52634362
4. 除了一个数出现一次外所有数均出现n次的问题，http://www.zhimengzhe.com/bianchengjiaocheng/cbiancheng/169317.html

## 要点

1. 异或运算
两数异或，数值相同的位为0，数值不同的位为1
0同任何一个数x异或的结果都是x

## 方案
'''


