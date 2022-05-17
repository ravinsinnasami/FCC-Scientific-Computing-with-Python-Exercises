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
    """ Function to repeat drawing process a certain number of times to get best approximate probability. """

    # declaring variables needed for final calculations.
    desired_result = 0
    yes_counter = 0

    # loops through the number of times an experiment should be conducted and gets the number of times desired output turns up
    for number in range(num_experiments):
        recovery_content = copy.copy(hat.contents_copy)  # copy the contents value so that it can be used for resetting the contents.
        current_result = hat.draw(num_balls_drawn)       # puts the number of balls to be drawn into draw method and returns list into current_result
        # print(current_result)
        for key, value in expected_balls.items():        # for every item in the dictionary, get the key and value.
            if current_result.count(key) >= value:       # check if the number of the key word in the result is same or higher than the value.
                yes_counter += 1                         # if yes, add 1 to counter, else set to 0
            else:
                yes_counter = 0
        if yes_counter // len(expected_balls.keys()) == 1:  # check if the number of yes divided by total keys is 1. if yes, increase desired result
            desired_result += 1
            yes_counter = 0

        hat.contents = recovery_content                  # resets the contents list so that the draw can begin with a full set
        hat.drawn_list.clear()                           # clears the drawn_list so new result can be appended.

    probability = desired_result/num_experiments         # calculates the probability

    return probability