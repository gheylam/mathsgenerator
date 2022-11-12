'''
Created by: Tsz Hey Lam
Created on: 12.11.2022 
'''
from . import algebra_helpers 
from . import numbers_fractions_operators as helper 
import random 

class AlgebraFactorisingGenerator:
    def __init__(self, doc):
        self.doc = doc 
        doc.add_section("Factorising")

    def __gen_question_factorising_scalar_only(self, num_terms):
        expression_list = []
        letters = ['a', 'b', 'c', 'd', 'e']
        scalar = random.randint(-12, 12)
        for term_index in range(num_terms):
            coef = helper.convert_num_to_str(random.randint(-12, 12) * scalar)
            letter = letters[term_index]
            if term_index == num_terms-1:
                letter = ''
            expression_list.append(f"{coef}{letter}")
            if term_index != num_terms-1:
                op = helper.gen_rnd_choice_text(['+', '-'])
                expression_list.append(op)
        q = ''.join(expression_list)
        return f"${q}$"

    def __gen_question_factorising(self, num_terms, num_letters):
        expression_list = [] 
        letters = ['a', 'b', 'c', 'd', 'e', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        scalar = random.randint(1, 12)
        for term_index in range(num_terms): 
            # For each term 
            coef = random.randint(1, 12) * scalar 
            sign = helper.gen_rnd_choice_text(['+', '-'])
            
            
            if sign == '{+}' and term_index == 0:
                coef_text = f"{coef}"
            else:
                coef_text = f"{sign}{coef}"     

            expression_list.append(coef_text)
            for letter_index in range(num_letters):
                # if num_letters = 2. letter_index = 0 on the first loop, letter_index = 1 on the second loop 
                letter = letters[letter_index]
                letter_pow = random.randint(1, 5)
                if letter_pow == 1:
                    letter_with_pow = letter
                else: 
                    letter_with_pow = helper.gen_term_pow(letter, letter_pow)
                expression_list.append(letter_with_pow)
            
        q = ''.join(expression_list)
        return f"${q}$"

    def gen_batch_simple_factorising(self):
        q1 = self.__gen_question_factorising_scalar_only(2)
        q2 = self.__gen_question_factorising_scalar_only(2)
        q3 = self.__gen_question_factorising_scalar_only(3)

        self.doc.add(r"Fully factorise the following expressions:")
        self.doc.add(r"\begin{table}[h!]")
        self.doc.add(r"\centering")
        self.doc.add(r"\begin{tabular}{c c c}")
        self.doc.add(r"\hspace{4cm} & \hspace{4cm} & \hspace{4cm}\\")
        self.doc.add(rf"a) {q1} & b) {q2} & c) {q3}\\ \\")
        self.doc.add(r"\end{tabular}")
        self.doc.add(r"\end{table}")
        self.doc.add(r"\newline")

    def gen_batch_factorising(self):
        q1 = self.__gen_question_factorising(2, 2)
        q2 = self.__gen_question_factorising(2, 2)
        q3 = self.__gen_question_factorising(3, 3)

        self.doc.add(r"Fully factorise the following expressions:")
        self.doc.add(r"\begin{table}[h!]")
        self.doc.add(r"\centering")
        self.doc.add(r"\begin{tabular}{c c c}")
        self.doc.add(r"\hspace{4cm} & \hspace{4cm} & \hspace{4cm}\\")
        self.doc.add(rf"a) {q1} & b) {q2} & c) {q3}\\ \\")
        self.doc.add(r"\end{tabular}")
        self.doc.add(r"\end{table}")
        self.doc.add(r"\newline")

