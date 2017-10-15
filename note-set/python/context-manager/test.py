# -*- coding: utf-8 -*-


class ContextManager(object):
    def __init__(self):
        self.entered = False

    def __enter__(self):
        self.entered = True
        return self

    def __exit__(self, exc_type, exc_instance, traceback):
        self.entered = False


'''
import psycopg2
class DBConnection(object):
    def __init__(self, dbname=None, user=None, password=None, host='localhost'):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password

    def __enter__(self):
        self.connection = psycopg2.connect(
            dbname=self.dbname,
            host=self.host,
            user=self.user,
            password=self.password
        )
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_instance, traceback):
        self.connection.close()
'''


class BubbleExceptions(object):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_instance, traceback):
        if exc_instance:
            print 'Bubbling up exception: %s.' % exc_instance
        return False


class HandleValueError(object):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_instance, traceback):
        # Return True if there is no exception.
        if not exc_type:
            return True

        # If this is a ValueError, note that it is being handled and
        # return True
        if issubclass(exc_type, ValueError):
            print 'Handling ValueError: %s' % exc_instance
            return True

        # Propagate anything else.
        return False
