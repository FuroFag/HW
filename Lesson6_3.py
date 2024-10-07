class Horse:
    def __init__(self, *args):
        self.x_distance = 0
        self.sound = 'frrr'
        super().__init__(*args)

    def run(self, dx:int):
        self.dx = dx
        if self.dx > 0:
            self.x_distance += self.dx
            print (self.x_distance)

class Eagle:
    def __init__(self, *args):
        self.y_distance = 0
        self.sound = 'i train, eat, sleep, repeat'
        super().__init__(*args)

    def fly(self, dy):
        self.dy = dy
        if self.dy > 0:
            self.y_distance += self.dy
            print(self.y_distance)

class Pegasus(Horse, Eagle):
    def __init__(self, *args):
        super().__init__(*args)

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return self.y_distance, self.x_distance

    def voice(self):
        print (self.sound)


pegasus = Pegasus()
pegasus.move(11,63)
pegasus.move(2, 9)
pegasus.voice()