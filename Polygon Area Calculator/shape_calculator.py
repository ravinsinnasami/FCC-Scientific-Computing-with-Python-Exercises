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



class Square:
    pass
