from __future__ import annotations
from typing import List, TypeVar, Callable, Generic

T = TypeVar("T")
R = TypeVar("R")


class Linq(Generic[T]):
    __list: List[T]

    def __init__(self, list: List[T]) -> None:
        self.__list = list

    def __len__(self) -> int:
        return len(self.__list)

    def any(self, exp: Callable[[T], bool] = None) -> bool:
        if exp is None:
            return len(self) > 0
        for i in self.__list:
            if exp(i):
                return True
        return False

    def where(self, exp: Callable[[T], bool]) -> Linq[T]:
        list = [i for i in self.__list if exp(i)]
        return Linq[T](list)

    def select(self, exp: Callable[[T], R]) -> Linq[R]:
        list = [exp(i) for i in self.__list]
        return Linq[R](list)

    def first(self, exp: Callable[[T], bool] = None) -> T:
        if exp is None:
            return None if len(self) == 0 else self.__list[0]
        list = self.where(exp)
        return None if len(list) == 0 else list.__list[0]

    def last(self, exp: Callable[[T], bool] = None) -> T:
        if exp is None:
            return None if len(self) == 0 else self.__list[-1]
        list = self.where(exp)
        return None if len(list) == 0 else list.__list[-1]

    def order(self, exp: Callable[[T], bool]) -> Linq[T]:
        list = sorted(self.__list, key=exp)
        return Linq[T](list)

    def orderDesc(self, exp: Callable[[T], bool]) -> Linq[T]:
        list = sorted(self.__list, key=exp, reverse=True)
        return Linq[T](list)

    def toList(self) -> List[T]:
        return list(self.__list)
