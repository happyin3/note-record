# -*- coding: utf-8 -*-


import functools
import json
import logging
import time


def decorated_by(func):
    func.__doc__ += '\nDecorated by decorated_by.'
    return func


def add(x, y):
    '''Return the sum of x and y.'''
    return x + y

add = decorated_by(add)


registry = []


def register(decorated):
    registry.append(decorated)
    return decorated


@register
def foo():
    return 3


@register
def bar():
    return 5

answers = []
for func in registry:
    answers.append(func())
print answers


class Registry(object):
    def __init__(self):
        self._functions = []

    def register(self, decorated):
        self._functions.append(decorated)
        return decorated

    def run_all(self, *args, **kwargs):
        return_values = []
        for func in self._functions:
            return_values.append(func(*args, **kwargs))
        return return_values

a = Registry()
b = Registry()


@a.register
def foo1(x=3):
    return x


@b.register
def bar1(x=5):
    return x


@a.register
@b.register
def baz(x=7):
    return x

print a.run_all()
print b.run_all()
print a.run_all(x=4)


def requires_ints(decorated):
    @functools.wraps(decorated)
    def inner(*args, **kwargs):
        # get any values that may have been sent as keyword arguments
        kwarg_values = [i for i in kwargs.values()]

        # iterate over every value sent to the decorated method, and
        # ensure that each one is an integer; raise TypeError if not.
        for arg in list(args) + kwarg_values:
            if not isinstance(arg, int):
                raise TypeError('%s only accepts integers as arguments.' % decorated.__name__)

        # run the decorated method, and return the result
        return decorated(*args, **kwargs)
    return inner


@requires_ints
def foo2(x, y):
    '''return the sum of x and y.'''
    return x + y


class JSONOutputError(Exception):
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message


def json_output(decorated):
    '''run the decorated function, serialize the result of that function
       to JSON, and return the JSON string
    '''
    @functools.wraps(decorated)
    def inner(*args, **kwargs):
        try:
            result = decorated(*args, **kwargs)
        except JSONOutputError as ex:
            result = {
                'status': 'error',
                'message': str(ex),
            }
        return json.dumps(result)
    return inner


@json_output
def error():
    raise JSONOutputError('This function is erratic.')


def logged(method):
    '''Cause the decorated method to be run and its results logged, along
    with some other diagnostic information.
    '''
    @functools.wraps(method)
    def inner(*args, **kwargs):
        # Record our start time
        start = time.time()

        # Run the decorated method.
        return_value = method(*args, **kwargs)

        # Record our completion time, and calculate the delta
        end = time.time()
        delta = end - start

        # Log the method call and the result
        logger = logging.getLogger('decorated.logged')
        logger.warn('Called method %s %s %s' % (method.__name__, delta, return_value))

        return return_value
    return inner
