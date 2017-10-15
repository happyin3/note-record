# -*- coding: utf-8 -*-

import functools
import time


def sortable_by_creation_time(cls):
    '''Given a class, argument the class to have its instances be sortable
    by the timestamp at which they were instanticated.
    '''
    # Argument the class' original `__init__` method to also store a
    # `_created` attribute on the instance, which corresponds to when it
    # was instantiated.
    original_init = cls.__init

    @functools.wraps(original_init)
    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        self._created = time.time()
    cls.__init = new_init

    # Add `__lt__` and `__gt__` methods that return True or False based on
    # the created values in question
    cls.__lt__ = lambda self, other: self._created < other._created
    cls.__gt__ = lambda self, other: self._created > other._created

    # Done; return the class object.
    return cls
