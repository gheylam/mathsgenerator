'''
Created by: Tsz Hey Lam 
Created on: 11/11/2022

Script to generate simplifying expression maths questions. 
'''


from . import numbers_fractions_operators as helper 
from . import tsz_latex_generator as doc_gen
import random 

class AlgebraSimplifyGenerator:
    def __init__(self, doc):
        self.doc = doc 
        doc.add_section("Simplifying Expressions")

    def gen_question_linear(self, num_terms):
        expression_list = []

        for term_index in range(num_terms):
            coef = helper.gen_rnd_int_text(-20, 20)
            if term_index % 2 == 0: 
                letter = 'a'
            else:
                letter = 'b'
            expression_list.append(f"{coef}{letter}")
            if term_index != num_terms-1:
                operator = helper.gen_rnd_choice_text(['+', '-'])
                expression_list.append(operator)
        q = ''.join(expression_list)
        return f"${q}$"

    def gen_question_linear_with_constants(self, num_terms):
        expression_list = []

        for term_index in range(num_terms * 3):
            coef = helper.gen_rnd_int_text(-20, 20)
            if term_index % 3 == 0: 
                letter = 'a'
            elif term_index % 3 == 1: 
                letter = 'b'
            else:
                letter = ''
            expression_list.append(f"{coef}{letter}")
            if term_index != num_terms*3-1:
                operator = helper.gen_rnd_choice_text(['+', '-'])
                expression_list.append(operator)
        q = ''.join(expression_list)
        return f"${q}$"
                

    def gen_question_non_linear(self, num_terms):
        expression_list = []

        for term_index in range(num_terms):
            coef = helper.gen_rnd_int_text(-20, 20)
            power_a = random.randint(1, 2)
            power_b = random.randint(1, 2)

            if power_a == 2:
                a_term = helper.gen_term_pow('a', 2)
            else: 
                a_term = 'a'
            if power_b == 2:
                b_term = helper.gen_term_pow('b', 2)
            else:
                b_term = 'b'
            
            expression_list.append(f"{coef}{a_term}{b_term}")
            if term_index != num_terms-1: 
                operator = helper.gen_rnd_choice_text(['+', '-'])
                expression_list.append(operator)
        q = ''.join(expression_list)
        return f"${q}$"


    def gen_batch_linear(self):
        '''
        Generate 2 linear questions without constants, generate 2 linear questions with constants 
        '''
        q1 = self.gen_question_linear(4)
        q2 = self.gen_question_linear(4)
        q3 = self.gen_question_linear_with_constants(2)
        q4 = self.gen_question_linear_with_constants(3)

        self.doc.add("Fully simplifying the following expressions:")
        self.doc.add(r"\begin{table}[h!]")
        self.doc.add(r"\centering")
        self.doc.add(r"\begin{tabular}{c c}")
        self.doc.add(r"\hspace{6cm} & \hspace{6cm}\\")
        self.doc.add(rf"a) {q1} & b) {q2}\\ \\")
        self.doc.add(rf"c) {q3} & d) {q4}")
        self.doc.add(r"\end{tabular}")
        self.doc.add(r"\end{table}")
        self.doc.add(r"\newline")

    
    def gen_batch_non_linear(self):
        '''
        Generate 3 non-linear simplifying expression questions
        '''
        q1 = self.gen_question_non_linear(4)
        q2 = self.gen_question_non_linear(5)
        q3 = self.gen_question_non_linear(6)

        self.doc.add("Fully simplifying the following expressions:")
        self.doc.add(r"\begin{table}[h!]")
        self.doc.add(r"\centering")
        self.doc.add(r"\begin{tabular}{c}")
        self.doc.add(r"\hspace{6cm}\\")
        self.doc.add(rf"a) {q1} \\ \\")
        self.doc.add(rf"b) {q2} \\ \\")
        self.doc.add(rf"c) {q3}")
        self.doc.add(r"\end{tabular}")
        self.doc.add(r"\end{table}")
        self.doc.add(r"\newline")
