from topics import Topic
import numpy as np
from sympy import var, solve, simplify, expand, pretty

"""
This file is a prototype for a more generic way of making Topics.
If we go for it, the contents should be moved to a subfolder with a file for each Topic
"""

####################################
# Basic Operations
####################################

basic_operators_ops = {'+':np.add, 'x':np.multiply, '-':np.subtract, '/':np.divide}
basic_operators_toggles = ['is_decimal', 'all_pos', 'range_low', 'range_high']

def basic_operators_make_qa_pair(self):
    num1,num2 = np.random.randint(self.range_low*10**self.is_decimal, self.range_high*10**self.is_decimal, 2)
    operator = np.random.choice(list(self.allowed_operators.keys()))
    question = basic_operators_make_layout([num1,num2], operator, self.toggle_variables)
    op = self.allowed_operators[operator]
    answer = op(num1,num2)
    return (question,answer)

def basic_operators_make_layout(number_list, operator_key, toggle_vars_list):
    """
    number_list and operator_list here refer to numbers and operators that have already been generated/chosen,
    and are now just being plugged into the correct format
    """
    if 'is_decimal' in toggle_vars_list:
        number_list[0]/=10
        number_list[1]/=10
        return "{:.1f} {} {:.1f} = ".format(number_list[0],operator_key,number_list[1])
    else:
        return "{} {} {} = ".format(number_list[0],operator_key,number_list[1])

BasicOperators = Topic(basic_operators_ops, basic_operators_toggles)
BasicOperators.make_layout = basic_operators_make_layout
BasicOperators.make_qa_pair = basic_operators_make_qa_pair


####################################
# Quadratics
####################################

quadratics_ops = {}
quadratics_toggles = ['range_low', 'range_high']

def make_coeffs():
    psi1, psi2, phi1, phi2 = np.random.randint(-5,5,4)
    if (psi1==0 or phi1==0):
        psi1, psi2, phi1, phi2 = make_coeffs()
    return psi1, psi2, phi1, phi2

def quadratics_make_qa_pair(self):
    """
    range high/low not used in this prototype
    """
    x = var('x')
    psi1, psi2, phi1, phi2 = make_coeffs()
    lhs = expand((psi1*x + psi2)*(phi1*x + phi2))
    question = quadratics_make_layout(self, lhs)
    answer = solve(lhs, x)
    return (question,answer)

def quadratics_make_layout(self, lhs_expr):
    """
    number_list and operator_list here refer to numbers and operators that have already been generated/chosen,
    and are now just being plugged into the correct format
    """
    coeffs = lhs_expr.as_poly().all_coeffs()
    return "{x_sq_coeff}x^2 {sgn_x_coeff} {x_coeff}x {sgn_offset_coeff} {offset_coeff} = 0".format(
        x_sq_coeff = coeffs[0],
        sgn_x_coeff = '+' if coeffs[1] >= 0 else '-',
        x_coeff = np.abs(coeffs[1]),
        sgn_offset_coeff = '+' if coeffs[1] >= 0 else '-',
        offset_coeff = np.abs(coeffs[2])
    )
    
Quadratics = Topic(quadratics_ops, quadratics_toggles)
Quadratics.make_layout = quadratics_make_layout
Quadratics.make_qa_pair = quadratics_make_qa_pair


######################################################
# Topic instances dict (for use in homework_generator)
######################################################
available_topics = {'Basic Operations': BasicOperators, 'Quadratics': Quadratics}
