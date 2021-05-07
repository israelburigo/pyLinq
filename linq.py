import datetime as dt
from pprint import*

import math

class Linq(object):

    def __init__(self, obj):
        self.__list = obj

    def __len__(self):
        return len(self.__list)

    def select(self, exp):
        l = [exp(item) for item in self.__list]
        return Linq(l)

    def where(self, exp):
        l = [item for item in self.__list if exp(item)]
        return Linq(l)

    def any(self, exp = None):
        if exp is None:
            return len(self.__list) > 0
        l = self.where(exp)
        return len(l) > 0  

    def all(self, exp):
        l = self.where(exp)
        return len(self.__list) == len(l)

    def first(self, exp = None):
        if exp is None:
            return None if len(self.__list) == 0 else self.__list[0]
        l = self.where(exp)
        return None if len(l) == 0 else l[0]

    def last(self, exp = None):
        if exp is None:
            return None if len(self.__list) == 0 else self.__list[-1]
        l = self.where(exp)
        return None if len(l) == 0 else l[-1]

    def group(self, exp):        
        l = set(self.select(exp).toList())
        l = [[item for item in self.__list if exp(item) == key] for key in l]
        return Linq(l)

    def order(self, exp):
        l = sorted(self.__list, key = exp)
        return Linq(l)

    def orderDesc(self, exp):
        l = sorted(self.__list, key = exp, reverse=True)
        return Linq(l)

    def toList(self):
        return list(self.__list)

