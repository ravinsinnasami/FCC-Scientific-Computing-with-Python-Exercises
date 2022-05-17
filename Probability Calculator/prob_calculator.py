import copy
import random
# Consider using the modules imported above.

class Hat:

    """ Creates a Hat Class """

    def __init__(self, **balls):
        """ Initializes the required variables and lists """
        self.balls_dictionary = balls
        self.contents = []
        self.set_contents()

    def set_contents(self):
        """ Method to appends the color of the balls to a list based on the value of the color in the dictionary """
        for key in self.balls_dictionary:
            for value in range(self.balls_dictionary[key]):
                self.contents.append(key)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass