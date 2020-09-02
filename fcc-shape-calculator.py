class Rectangle:
    # Rectangle object should be initialized with width and height attributes. 
    # Rectangle class should also contain the following methods:
    # set_side, set_width, set_height, get_area, get_perimter, 
    # get diagonal, get_picture, get_amount_inside
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return 'Rectangle(width=' + str(self.width) + ', height=' + str(self.height)+')'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return self.width *2 + self.height * 2

    def get_diagonal(self):
        return (self.width **2 + self.height ** 2) ** 0.5

    def get_picture(self):
        
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            pict = ''
            i = 0
            while i < self.height:
                pict += '*' * self.width + '\n'
                i += 1
            return pict
    
    # return number of times shape 2 can fit inside Shape 1 with no rotation
    def get_amount_inside(self, shape):
        no_horizontal_fits = self.width // shape.width
        no_vertical_fits = self.height // shape.height
        return  no_horizontal_fits * no_vertical_fits

# Construct Square so subclass of Rectangle
class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return 'Square(side=' + str(self.width) + ')'

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.width = side

    def set_height(self, side):
        self.height = side

