class Rectangle:
    """ creates a rectangle object """

    def __init__(self, width, height):
        """ Initializes the rectangle class """
        self.width = width
        self.height = height

    def set_width(self, new_width):
        """ Method to set a new width """
        self.width = new_width

    def set_height(self, new_height):
        """ Method to set a new height """
        self.height = new_height

    def get_area(self):
        """ Method that calculates the area of the rectangle and returns it """
        area = self.width * self.height
        return area

    def get_perimeter(self):
        """ Method that calculates the perimeter of the rectangle and returns it """
        perimeter = (2 * self.width) + (2 * self.height)
        return perimeter

    def get_diagonal(self):
        """ Method that calculates the diagonal of a rectangle and returns it
            - no math library or pow for calculation; only arithmetics symbols """
        diagonal = ((self.width ** 2) + (self.height ** 2)) ** 0.5
        return diagonal

    def get_picture(self):
        """ Method that prints the shape of the rectangle using set height and width """
        picture = ''
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            for height in range(self.height):
                for width in range(self.width):
                    picture += '*'
                picture += "\n"
            return picture

    def get_amount_inside(self, inside_shape):
        """ Method to calculate how many of a certain shape can fit in current shape """
        current_shape_area = self.get_area()
        inside_shape_area = inside_shape.get_area()
        total_fit = current_shape_area // inside_shape_area # Forces to a whole number
        return total_fit

    def __repr__(self):
        """ Method to print out current width and length of Rectangle """
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    """ Creates a square object """

    def __init__(self, side):
        """ Initialize the square object. Inherits all from the Parent class plus additional attribute (side)
            - side parameter is passed as argument to Rectangle class. """
        super().__init__(side, side)  # assigns to side value to width and length of Rectangle

    def set_side(self, new_side):
        """ Method to set a new side for the square
            - additionally new side also sets the height and width """
        self.width = new_side
        self.height = new_side

    def set_width(self, new_width):
        """ Method to set a new width. New width is also set to the height. """
        self.width = new_width
        self.height = new_width

    def set_height(self, new_height):
        """ Method to set a new height. New height is also set to the width """
        self.height = new_height
        self.width = new_height

    def __repr__(self):
        """ Method to print out current sides of rectangle.
            It doesn't matter if width or height is used to represent the side length """
        return f"Square(side={self.width})"
