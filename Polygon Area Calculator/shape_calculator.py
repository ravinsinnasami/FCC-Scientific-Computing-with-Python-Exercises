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


class Square:
    pass
