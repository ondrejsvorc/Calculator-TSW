from operations import *

class Calculator:
    def __init__(self):
        self._ans = 0

    @property
    def ans(self) -> int:
        return self._ans 

    def _operate(self, a, b, operator):
        self._ans = operator(a, b)
        return self._ans
        

    def plus(self, a, b):
        return self._operate(a, b, operator=add)

    def minus(self, a, b):
        return self._operate(a, b, operator=sub)