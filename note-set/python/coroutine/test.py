# -*- coding: utf-8 -*-

'''
协程

使用协程之前必须预激
'''

from collections import namedtuple
from coroutil import coroutine

Result = namedtuple('Result', 'count average')


@coroutine
def averager():
    '''
    定义一个计算移动平均值的协程
    '''
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count


def averager_return():
    '''
    定义一个求平均值的协程，让它返回一个结果
    '''
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    return Result(count, average)


'''
在协程中处理异常
'''


class DemoException(Exception):
    '''
    为这次演示定义的异常类型
    '''
    pass


def demo_exc_handling():
    print('start')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled. Continuing...')
        else:
            print('coroutine received: {!r}'.format(x))
    raise RuntimeError('This line shoud never run.')
