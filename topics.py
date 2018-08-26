import numpy as np

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

# Some example topics
WholeAddition = Topic('+')
DecimalAddition = Topic('+', is_decimal=True)
NegativeNumberAddition = Topic('+', all_pos=False, range_low=-20)
WholeSubtraction = Topic('-', range_low=20, range_high=40)
DecimalSubtraction = Topic('-', is_decimal=True)
NegativeNumberSubtraction = Topic('-', all_pos=False, range_low=-20)

