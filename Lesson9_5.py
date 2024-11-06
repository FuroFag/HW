class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step = 1):
        if step == 0:
            raise StepValueError('Шаг не может равняться нулю')
        self.start = start
        self.stop = stop
        self.pointer = start
        self.step = step

    def __iter__(self):
        self.pointer == self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration
        current = self.pointer
        self.pointer += self.step
        return current

iter = Iterator(-5, 10, 3)
for i in iter:
    print(i, end=' ')
