import numpy as np
import pandas as pd

class Topic:
    """
    In subtopics.py we create subclasses of Topic, each with it's own custom layout and method
    to make qa pairs. 
    These subclasses are also given a dictionary of alowed operations (function
    objects that can be used in the questions) and a list of 'toggle variables' (a list of 
    attributes specific to the subclass that provide slight variations in the question depending
    on if they're true or false. Examples; is_decimal and all_pos)
    """

    def __init__(self, allowed_operator_dict, toggle_variables_list):
        self.allowed_operators = allowed_operator_dict
        self.toggle_variables = toggle_variables_list
        self.is_decimal = False
        self.range_high = 20
        self.range_low = 0

    def make_qa_pair(self):
        """
        This method should be overwritten for each instance
        """
        return True

    def make_layout(self):
        """
        This method should be overwritten for each instance
        """
        return True

"""

Removed while refactoring

class TopicStore:

    def __init__(self):
        self.operators = {'+':np.add, 'x':np.multiply, '-':np.subtract, '/':np.divide}
        self.df = pd.read_csv('topics.csv')
        self.topic_names = self.df.topic_name
        self.name_index_dict = dict(zip(self.df.topic_name, self.df.index))

    def add_topic(self):
        # TODO: add functionality to add a new topic
        return True

    def make_Topic(self, name):
        index = self.name_index_dict[name]
        return Topic(self.df.operation[index],
                     self.df.all_pos[index], 
                     self.df.is_decimal[index], 
                     self.df.range_low[index], 
                     self.df.range_high[index])
"""


# Leaving these for now in case I need to revert
"""
WholeAddition = Topic('+')
DecimalAddition = Topic('+', is_decimal=True)
NegativeNumberAddition = Topic('+', all_pos=False, range_low=-20)
WholeSubtraction = Topic('-', range_low=20, range_high=40)
DecimalSubtraction = Topic('-', is_decimal=True)
NegativeNumberSubtraction = Topic('-', all_pos=False, range_low=-20)
"""

