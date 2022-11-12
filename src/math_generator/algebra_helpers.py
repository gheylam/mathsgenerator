'''
Created by: Tsz Hey Lam 
Created on: 12.11.2022

Set of functions used for algebra type questions 
'''
from . import numbers_fractions_operators as helper 
import random 

def gen_simplified_linear_expression(num_terms, constants_flag=True):
    expression_list = []
    letters=['a', 'b', 'c', 'd', 'e']
    if constants_flag == True:
        non_constant_terms = num_terms - 1 
    else:
        non_constant_terms = num_terms
    for term_index in range(non_constant_terms): 
        coef = helper.gen_rnd_int_text(1, 10)
        letter = letters[term_index]
        if term_index == 0:
            first_term_sign = helper.gen_rnd_choice_text(['', '-'])
            expression_list.append(first_term_sign)
        operator = helper.gen_rnd_choice_text(['+', '-'])
        expression_list.append(f"{coef}{letter}")
        if constants_flag==False and term_index!=non_constant_terms-1:
            expression_list.append(operator)
        elif constants_flag==True:
            expression_list.append(operator)
    if constants_flag == True: 
        constant = helper.gen_rnd_int_text(1, 10)
        expression_list.append(constant)
    expr = ''.join(expression_list)
    return expr


def gen_single_bracket(num_terms):
    # generate inner bracket expression
    inner_expr = gen_simplified_linear_expression(num_terms)
    q = f"({inner_expr})"
    return q

def gen_single_bracket_with_outer_scalar(num_terms, outside_letter_flag=False):
    # generate the coefficient infront of the scalar outside the bracket
    outside_coef = helper.gen_rnd_int_text(-5, 10)
    if outside_coef == "{0}":
        outside_coef = ""
    outside_letter = ''
    if outside_letter_flag == True: 
        outside_letter = 'a'
    
    # generate inner bracket expression
    inner_expr = gen_simplified_linear_expression(num_terms)
    q = f"{outside_coef}{outside_letter}({inner_expr})"
    return q



