import numpy as np
import pandas as pd
from quadroots import genQuadraticSimple

class Topic:
    
    #operators = {'+':np.add, 'x':np.multiply, '-':np.subtract, '/':np.divide}

    def __init__(self, operation, all_pos=True, is_decimal=False, range_low=0, range_high=20):
        self.is_decimal = is_decimal
        self.all_pos = all_pos
        self.operation = TopicStore().operators[operation]
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

class QuadEqns(Topic):
        # At the moment, does not read any extra args. However, good ones
        # would be: enforce a = 1 (easier qs), allow irrational roots (harder qs), prevent a=0
    def __init__(self):
        
        # CHRISHAX: Inherits current Topic class for no good reason
        # But it should probably inherit the new improved one, when it exists.
        self.is_decimal = False        
    def make_qa_pair(self):
        answer = genQuadraticSimple()
        question = answer[0]
        answer = "\n".join(answer)
        return (question,answer)

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
        
        # CHRISHACK
        print(name)
        if name=="Quadratic Equations":
            return QuadEqns()
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

