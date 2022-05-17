import copy
import random
# Consider using the modules imported above.

class Hat:

    """ Creates a Hat Class """

    def __init__(self, **balls):
        """ Initializes the required variables and lists """
        self.balls_dictionary = balls
        self.contents = []
        self.set_contents()                             # runs the set_contents method
        self.total_balls = len(self.contents)           # checks the numbers of colored balls to be drawn
        self.list_to_draw_from = []                     # a list to draw the balls from.
        self.drawn_list = []                            # a list of the drawn balls
        self.contents_copy = copy.copy(self.contents)   # used for resetting the contents list later.

    def set_contents(self):
        """ Method to appends the color of the balls to a list based on the value of the color in the dictionary """
        for key in self.balls_dictionary:
            for value in range(self.balls_dictionary[key]):
                self.contents.append(key)

    def draw(self, number_to_draw):
        """ Method to draw certain number of balls based on given value.
            - the original content list is copied to prevent affecting it.
            - each time a ball is drawn using random.choice() is it appended to drawn list and removed from the copy list. """
        self.list_to_draw_from = copy.copy(self.contents)

        if number_to_draw > self.total_balls:
            return self.contents
        else:
            for number_of_times in range(number_to_draw):
                drawn_ball = random.choice(self.contents)
                self.drawn_list.append(drawn_ball)
                self.contents.remove(drawn_ball)
            return self.drawn_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass