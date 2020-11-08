class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return ((2 * self.width) + (2 * self.height))

    def get_diagonal(self):
        return (((self.width ** 2) + (self.height ** 2)) ** .5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        else:
            pic = ""
            for i in range(self.height):
                pic += (("*" * self.width) + "\n")

            return pic

    def get_amount_inside(self, obj):
        area_self = self.get_area()
        area_other = obj.get_area()

        return int(area_self / area_other)


class Square(Rectangle):

    def __init__(self, side):
        self.side = side
        self.width = side
        self.height = side

    def __str__(self):
        return "Square(side={})".format(self.side)

    def set_side(self, side):
        self.width = side
        self.height = side
        self.side = side

    def set_width(self, width):
        self.width = width
        self.height = width
        self.side = width

    def set_height(self, height):
        self.width = height
        self.height = height
        self.side = height


x = Rectangle(4, 8)
y = Square(2)

print(y.get_picture())
