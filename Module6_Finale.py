class Figure:
    sides_count = 0
    __sides = []
    __color = []
    filled = False
    def __init__(self, rgb, *side):
        self.color = list(rgb)
        self.side = side[0]
        self.filled = True

    def get_color(self):
        self.__color = self.color
        self.filled = True
        return self.color

    def __is_valid_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        if 0 <= self.r <= 255 and 0 <= self.g <= 255 and 0 <= self.b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.color = [self.r, self.g, self.b]

    def __is_valid_sides(self, *args):
        for side in self.sides:
            if len(self.sides) == self.sides_count and side > 0 and type(side) == int:
                return True
            else:
                return False

    def get_sides(self):
        self.__sides = self.sides
        return self.__sides

    def __len__(self):
        return self.side * self.sides_count

    def set_sides(self, *args):
        new_sides = []
        self.sides = list(args)
        if self.__is_valid_sides(self, *args):
            self.get_sides()
        else:
            for i in range(self.sides_count):
                new_sides.append(self.side)
            self.sides = new_sides
            self.get_sides()

class Circle(Figure):
    sides_count = 1
    __radius = None

    def set_radius(self):
        self.__radius = self.__len__()/(2*3.141569)
        return self.__radius

    def get_square(self):
        self.set_radius()
        return (self.__radius ** 2) * 3.141569

class Triangle(Figure):
    sides_count = 3
    __height = None

    def set_height(self):
        self.__height = self.side * (3**0.5)/2
        return self.__height

    def get_square(self):
        return (self.side ** 2) * (3 ** 0.5) / 4

class Cube(Figure):
    sides_count = 12
    def new_side_list(self):
        new_side_list = []
        for element in range(self.sides_count):
            new_side_list.append(self.side)
        self.__sides = new_side_list
        return self.__sides

    def get_volume(self):
        return self.side**3

circle = Circle((10,21,230),20)
triangle = Triangle((0,0,255), 25)
cube = Cube((255,255,255), 10)

print (circle.get_square())
print (triangle.get_square())
print (cube.get_volume())

circle.set_color(0,0,1000)
print (circle.get_color())
circle.set_color(254,250,101)
print (circle.get_color())

circle.set_sides(2)
print (circle.get_sides())
cube.set_sides(101, 21, 11, 2331)
print (cube.get_sides())
