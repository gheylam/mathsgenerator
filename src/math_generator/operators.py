'''
Created by: Tsz Hey Lam
Created on: 08/10/2022
'''

from . import numbers_fractions_operators as helper 
import numpy as np

def gen_question_long_divison(num_figures_01=3, num_figures_02=1):
    num_01 = random.randint(np.power(10, num_figures_01-1), np.power(10, num_figures_02)-1)
    num_02 = random.randint(np.power(10, num_figures_01-1), np.power(10, num_figures_02)-1)
    q = helper.gen_div_expr(num_01, num_02)
    return f"${q}$"

def gen_three_long_division(doc, decimal_places):
    q1 = gen_question_long_divison()
    q2 = gen_question_long_divison(3, 1)
    q3 = gen_question_long_divison(3, 2)
    doc.add(f"Work out the value of the following expression and leave your answers to {decimal_places} decimal place:")
    doc.add(r"\begin{table}[h!]")
    doc.add(r"\centering")
    doc.add(r"\begin{tabular}{c c c}")
    doc.add(r"\hspace{4cm} & \hspace{4cm} & \hspace{4cm} \\")
    doc.add(rf"a) {q1} & b) {q2} & c) {q3}\\ \\")
    doc.add(r"\end{tabular}")
    doc.add(r"\end{table}")
    doc.add(r"\newline")

def gen_section_operators(doc):
    doc.add_section("Operators")
    gen_three_long_division(doc, 1)
