class Example:
    def __init__(self, number: int):
        self._num = number

    @property
    def number(self):
        return self._num


class Something:
    def __init__(self, factor=2):
        self._factor = factor

    def double(self, number: int): # Commented out code
        # return number*self._factor
        return number*self._factor


