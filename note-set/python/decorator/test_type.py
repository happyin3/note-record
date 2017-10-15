# -*- coding: utf-8 -*-

'''
类型转换
'''


class Task(object):
    '''A trivial task class. Task classes have a `run` method, which runs
    the task.
    '''
    def __call__(self, *args, **kwargs):
        return self.run(*args, **kwargs)

    def run(self, *args, **kwargs):
        raise NotImplementedError('Subclasses must implement `run`.')

    def identify(self):
        return 'I am a task.'


def task(decorated):
    '''Return a class that runs the given function if its run method is
    called.
    '''
    class TaskSubclass(Task):
        def run(self, *args, **kwargs):
            return decorated(*args, **kwargs)
    return TaskSubclass()
