class Horse:
    def __init__(self, sound = 'frrr', x_distance = 0):
        self.x_distance = x_distance

    def run(self, dx:int):
        self.dx = dx
        if self.dx > 0:
            self.x_distance += self.dx
            print (self.x_distance)

class Eagle:
    def __init__(self, y_distance = 0, sound = 'i train, eat, sleep, repeat'):
        self.y_distance = y_distance

    def fly(self, dy):
        self.dy = dy
        if self.dy > 0:
            self.y_distance += self.dy
            print(self.y_distance)

class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self, sound = 'frrr', x_distance = 0)
        Eagle.__init__(self, y_distance = 0, sound = 'i train, eat, sleep, repeat')

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return y_distance, x_distance

    def voice(self):
        return self.sound

horse = Horse()
horse.run(10)
horse.run(2)
pegasus = Pegasus()
pegasus.move(11,63)
pegasus.move(2, 9)