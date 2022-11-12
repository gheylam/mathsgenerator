'''
Created by: Tsz Hey Lam
Created on: 12.11.2022 
'''
import algebra_helpers 
import numbers_fractions_operators as helper 
import tsz_latex_generator as doc_gen 
import random 

class AlgebraFactorising:
    def __init__(self, doc):
        self.doc = doc 
        doc.add_section("Factorising")

    def gen_question_factorising_scalar_only(self, num_terms):
        expression_list = []
        letters = [a, b, c, d, e]
        scalar = random.randint(-12, 12)
        for term_index in range(num_terms):
            coef = helper.convert_num_to_str(random.randint(-12, 12) * scalar)
            letter = letters[term_index]
            if term_index == num_terms-1:
                letter = ''
            expression_list.append("{coef}{letter}")
            if term_index != num_terms-1:
                op = helper.gen_rnd_choice_text(['+', '-'])
                expression_list.append(op)
        q = ''.join(expression_list)
        return f"${q}$"

    def gen_question_factorising(self, num_terms, num_letters):
        
