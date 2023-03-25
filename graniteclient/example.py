class Example:
    def __init__(self, number: int):
        self._num = number

    @property
    def number(self):
        return self._num


class Something:
    def __init__(self, factor=2):
        self._factor = factor
        
    def double(self, number: int):
        return number*self._factor


