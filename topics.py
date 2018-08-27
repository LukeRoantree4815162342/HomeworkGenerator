import numpy as np
import pandas as pd

class Topic:
    
    operators = {'+':np.add, 'x':np.multiply, '-':np.subtract, '/':np.divide}

    def __init__(self, operation, all_pos=True, is_decimal=False, range_low=0, range_high=20):
        self.is_decimal = is_decimal
        self.all_pos = all_pos
        self.operation = self.operators[operation]
        self.operator = operation
        self.range_low = range_low
        self.range_high = range_high

    def make_qa_pair(self):
        num1 = np.random.randint(self.range_low*10**self.is_decimal, self.range_high*10**self.is_decimal)
        num2 = np.random.randint(self.range_low*10**self.is_decimal, self.range_high*10**self.is_decimal)
        if self.is_decimal:
            num1/=10
            num2/=10
            question = "{:.1f} {} {:.1f} = ".format(num1,self.operator,num2)
        else:
            question = "{} {} {} = ".format(num1,self.operator,num2)
        answer = self.operation(num1,num2)
        return (question,answer)

class TopicStore:

    def __init__(self):
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



# Leaving these for now in case I need to revert
"""
WholeAddition = Topic('+')
DecimalAddition = Topic('+', is_decimal=True)
NegativeNumberAddition = Topic('+', all_pos=False, range_low=-20)
WholeSubtraction = Topic('-', range_low=20, range_high=40)
DecimalSubtraction = Topic('-', is_decimal=True)
NegativeNumberSubtraction = Topic('-', all_pos=False, range_low=-20)
"""

