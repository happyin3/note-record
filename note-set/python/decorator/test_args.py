# -*- coding: utf-8 -*-

import functools
import json


class JSONOutputError(Exception):
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message


def json_output(indent=None, sort_keys=False):
    '''Run the decorated function, serialize the result of that function
    to JSON, and return the JSON string.
    '''
    def actual_decorator(decorated):
        @functools.wraps(decorated)
        def inner(*args, **kwargs):
            try:
                result = decorated(*args, **kwargs)
            except JSONOutputError as ex:
                result = {
                    'status': 'error',
                    'message': str(ex),
                }
            return json.dumps(result, indent=indent, sort_keys=sort_keys)
        return inner
    return actual_decorator


@json_output(indent=4)
def do_nothing():
    return {'status': 'done'}


def json_output_strong(decorated_=None, indent=None, sort_keys=False):
    '''Run the decorated function, serialize the result of that function
    to JSON, and return the JSON string.
    '''
    # Did we get both a decorated method and keyword arguments?
    # That should not happen
    if decorated_ and (indent or sort_keys):
        raise RuntimeError('Unexpected arguments.')

    # Define the actual decorator function.
    def actual_decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except JSONOutputError as ex:
                result = {
                    'status': 'error',
                    'message': str(ex)
                }
            return json.dumps(result, indent=indent, sort_keys=sort_keys)
        return inner

    # Return either the actual decorator, or the result of applying
    # the actual decorator, depending on what arguments we got.
    if decorated_:
        return actual_decorator(decorated_)
    else:
        return actual_decorator
