'''
Created by: Tsz Hey Lam 
Created on: 12.11.2022

Class for generating expanding bracket questions. 
'''

from . import numbers_fractions_operators as helper 
from . import algebra_helpers 
import random 

class AlgebraExpandingGenerator:
    def __init__(self, doc):
        self.doc = doc
        doc.add_section("Expanding Brackets")
    
    def __gen_question_single_bracket(self, num_terms, outside_letter_flag=False):
        q = algebra_helpers.gen_single_bracket_with_outer_scalar(num_terms, outside_letter_flag)
        return f"${q}$"

    def __gen_question_linear_double_bracket(self):
        bracket01 = algebra_helpers.gen_single_bracket_with_outer_scalar(2, outside_letter_flag=False)
        bracket02 = algebra_helpers.gen_single_bracket_with_outer_scalar(2, outside_letter_flag=False)
        operator = helper.gen_rnd_choice_text(['+', '-'])
        q = f"{bracket01}{operator}{bracket02}"
        return f"${q}$"
    
    def __gen_question_quadratic_expansion_easy(self):
        constant01 = helper.gen_rnd_int_text(1, 10)
        constant02 = helper.gen_rnd_int_text(1, 10)
        op01 = helper.gen_rnd_choice_text(['+', '-'])
        op02 = helper.gen_rnd_choice_text(['+', '-'])
        letter = helper.gen_rnd_choice_text(['a', 'b', 'x', 'y'])
        q = f"({letter}{op01}{constant01})({letter}{op02}{constant02})"
        return f"${q}$"


    def gen_batch_single_brackets(self):
        q1 = self.__gen_question_single_bracket(2, outside_letter_flag=False)
        q2 = self.__gen_question_single_bracket(2, outside_letter_flag=False)
        q3 = self.__gen_question_single_bracket(2, outside_letter_flag=True)
        q4 = self.__gen_question_single_bracket(3, outside_letter_flag=True)

        self.doc.add("Expand the following expressions:")
        self.doc.add(r"\begin{table}[h!]")
        self.doc.add(r"\centering")
        self.doc.add(r"\begin{tabular}{c c}")
        self.doc.add(r"\hspace{6cm} & \hspace{6cm}\\")
        self.doc.add(rf"a) {q1} & b) {q2}\\ \\")
        self.doc.add(rf"c) {q3} & d) {q4}")
        self.doc.add(r"\end{tabular}")
        self.doc.add(r"\end{table}")
        self.doc.add(r"\newline")


    def gen_batch_double_brackets(self):
        q1 = self.__gen_question_linear_double_bracket()
        q2 = self.__gen_question_linear_double_bracket()
        q3 = self.__gen_question_quadratic_expansion_easy()
        q4 = self.__gen_question_quadratic_expansion_easy()

        self.doc.add("Expand and fully simplify the following expressions:")
        self.doc.add(r"\begin{table}[h!]")
        self.doc.add(r"\centering")
        self.doc.add(r"\begin{tabular}{c c}")
        self.doc.add(r"\hspace{6cm} & \hspace{6cm}\\")
        self.doc.add(rf"a) {q1} & b) {q2} \\ \\")
        self.doc.add(rf"c) {q3} & d) {q4}")
        self.doc.add(r"\end{tabular}")
        self.doc.add(r"\end{table}")
        self.doc.add(r"\newline")