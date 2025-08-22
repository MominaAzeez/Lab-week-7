class Range:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
        self._current = start

    def __iter__(self):
        self._current = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self._current >= self.end) or (self.step < 0 and self._current <= self.end):
            raise StopIteration
        val = self._current
        self._current += self.step
        return val

    def __contains__(self, value):
        if self.step > 0:
            return self.start <= value < self.end and (value - self.start) % self.step == 0
        else:
            return self.end < value <= self.start and (self.start - value) % abs(self.step) == 0

    def __str__(self):
        return f"Range({self.start}, {self.end}, {self.step})"
