'''
Created by: Tsz Hey Lam
Created on: 01.10.2022

Methods for generating rounding and approximation questions.
'''

from . import numbers_fractions_operators as helper 
import numpy as np
import random 

def gen_question_decimal_place_rounding():
    decimal_places = random.randint(1, 5)
    integer = helper.gen_rnd_int_text(0, 20)
    num = [integer, '.']
    for place in range(decimal_places+2):
        num.append(helper.gen_rnd_int_text(0, 9))
    num_text = ''.join(num)
    return f"${num_text}$ to {decimal_places}.d.p"

def gen_question_sig_fig_rounding():
    number_of_figures = random.randint(2, 4)
    power_ten = random.randint(0, number_of_figures+3)
    num = random.randint(np.power(10, number_of_figures-1), np.power(10, number_of_figures)-1) 
    operator_flag = random.randint(0, 1)
    if operator_flag == 0:
        num = num / np.power(10, power_ten)
    else:
        num = num * np.power(10, power_ten)
    
    sig_fig = random.randint(1, number_of_figures-1)
    q = f"${num}$ to ${sig_fig}$.s.f"
    return q

    

def gen_six_decimal_place_rounding(doc):
    q1 = gen_question_decimal_place_rounding()
    q2 = gen_question_decimal_place_rounding()
    q3 = gen_question_decimal_place_rounding()
    q4 = gen_question_decimal_place_rounding()
    q5 = gen_question_decimal_place_rounding()
    q6 = gen_question_decimal_place_rounding()

    doc.add(f"Round the following numbers to the specified number of decimal places:")
    doc.add(r"\begin{table}[h!]")
    doc.add(r"\centering")
    doc.add(r"\begin{tabular}{c c c}")
    doc.add(r"\hspace{4cm} & \hspace{4cm} & \hspace{4cm} \\")
    doc.add(rf"a) {q1} & b) {q2} & c) {q3}\\ \\")
    doc.add(rf"d) {q4} & e) {q5} & f) {q6}\\ \\")
    doc.add(r"\end{tabular}")
    doc.add(r"\end{table}")
    doc.add(r"\newline")


def gen_six_sig_fig_rounding(doc):
    q1 = gen_question_sig_fig_rounding()
    q2 = gen_question_sig_fig_rounding()
    q3 = gen_question_sig_fig_rounding()
    q4 = gen_question_sig_fig_rounding()
    q5 = gen_question_sig_fig_rounding()
    q6 = gen_question_sig_fig_rounding()

    doc.add(f"Round the following numbers to the specified number of significant figures:")
    doc.add(r"\begin{table}[h!]")
    doc.add(r"\centering")
    doc.add(r"\begin{tabular}{c c c}")
    doc.add(r"\hspace{4cm} & \hspace{4cm} & \hspace{4cm} \\")
    doc.add(rf"a) {q1} & b) {q2} & c) {q3}\\ \\")
    doc.add(rf"d) {q4} & e) {q5} & f) {q6}\\ \\")
    doc.add(r"\end{tabular}")
    doc.add(r"\end{table}")
    doc.add(r"\newline")



def gen_section_rounding(doc):
    doc.add_section("Rounding")
    gen_six_decimal_place_rounding(doc)
    gen_six_sig_fig_rounding(doc)


