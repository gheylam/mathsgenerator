'''
Created by: Tsz Hey Lam
Created on: 21.09.2022

Methods for generating standard form questions
'''
from . import numbers_fractions_operators as helper 
import random
import numpy as np

def gen_std_form(first_figure, figures, power):
    std_form_num = [f"{first_figure}.{figures}", r"\times", f"10^{power}"]
    return ''.join(std_form_num)

def gen_question_large_number_to_std_form():
    figures = random.randint(1, 9999)
    multiplier = random.randint(0, 6)
    q = figures * np.power(10, multiplier)
    return f"${q}$"

def gen_question_small_number_to_std_form():
    figures = random.randint(1, 999)
    multiplier = random.randint(3, 5)
    q = figures / np.power(10, multiplier)
    return f"${q}$"

def gen_question_large_std_form_to_number():
    first_figure = random.randint(1, 9)
    figures = random.randint(1, 99999)
    multiplier = random.randint(1, 9)
    q = gen_std_form(first_figure, figures, multiplier)
    return rf"${q}$"

def gen_question_small_std_form_to_number():
    first_figure = random.randint(1, 9)
    figures = random.randint(1, 99999)
    multiplier = helper.gen_rnd_int_text(-9, -1)
    q = q = gen_std_form(first_figure, figures, multiplier)
    return rf"${q}$"

def gen_question_std_form_addition():
    first_figure01 = random.randint(1, 9)
    figures01 = random.randint(1, 99)
    pow01 = random.randint(5, 15)
    std_form_num01 = gen_std_form(first_figure01, figures01, helper.convert_num_to_str(pow01))
    first_figure02 = random.randint(1, 9)
    figures02 = random.randint(1, 99999)
    pow02 = pow01 + random.randint(-3, 3)
    std_form_num02 = gen_std_form(first_figure02, figures02, helper.convert_num_to_str(pow02))
    q = helper.gen_add_expr(std_form_num01, std_form_num02)
    return rf"${q}$"

def gen_question_std_form_subtraction():
    first_figure01 = random.randint(1, 9)
    figures01 = random.randint(1, 99)
    pow01 = random.randint(5, 15)
    std_form_num01 = gen_std_form(first_figure01, figures01, helper.convert_num_to_str(pow01))
    first_figure02 = random.randint(1, 9)
    figures02 = random.randint(1, 99999)
    pow02 = pow01 + random.randint(-3, 3)
    std_form_num02 = gen_std_form(first_figure02, figures02, helper.convert_num_to_str(pow02))
    q = helper.gen_sub_expr(std_form_num01, std_form_num02)
    return rf"${q}$"


def gen_question_std_form_multiplication():
    first_figure01 = random.randint(1, 9)
    figures01 = random.randint(1, 9)
    pow01 = random.randint(5, 15)
    std_form_num01 = gen_std_form(first_figure01, figures01, helper.convert_num_to_str(pow01))
    first_figure02 = random.randint(1, 9)
    figures02 = random.randint(1, 9)
    pow02 = pow01 + random.randint(-3, 3)
    std_form_num02 = gen_std_form(first_figure02, figures02, helper.convert_num_to_str(pow02))
    q = helper.gen_mul_expr(std_form_num01, std_form_num02)
    return rf"${q}$"


def gen_question_std_form_division():
    first_figure01 = random.randint(1, 9)
    figures01 = random.randint(1, 9)
    pow01 = random.randint(5, 15)
    std_form_num01 = gen_std_form(first_figure01, figures01, helper.convert_num_to_str(pow01))
    first_figure02 = random.randint(1, 2)
    figures02 = 0
    pow02 = pow01 + random.randint(-3, 3)
    std_form_num02 = gen_std_form(first_figure02, figures02, helper.convert_num_to_str(pow02))
    q = helper.gen_div_expr(std_form_num01, std_form_num02)
    return rf"${q}$"

def gen_four_ordinary_to_std_form(doc):
    q1 = gen_question_large_number_to_std_form()
    q2 = gen_question_large_number_to_std_form()
    q3 = gen_question_small_number_to_std_form()
    q4 = gen_question_small_number_to_std_form()
    doc.add(r"Convert the following ordinary numbers to standard form:")
    doc.add(r"\begin{table}[h!]")
    doc.add(r"\centering")
    doc.add(r"\begin{tabular}{c c c c}")
    doc.add(r"\hspace{2cm} & \hspace{5cm} & \hspace{5cm} & \hspace{4cm}\\")
    doc.add(rf"a) {q1} & b) {q2} & c) {q3} & d) {q4}\\ \\")
    doc.add(r"\end{tabular}")
    doc.add(r"\end{table}")
    doc.add(r"\newline")
    return

def gen_four_std_form_to_ordinary(doc):
    q1 = gen_question_large_std_form_to_number()
    q2 = gen_question_large_std_form_to_number()
    q3 = gen_question_small_std_form_to_number()
    q4 = gen_question_small_std_form_to_number()
    doc.add(r"Convert the following standard form numbers to ordinary numbers:")
    doc.add(r"\begin{table}[h!]")
    doc.add(r"\centering")
    doc.add(r"\begin{tabular}{c c c c}")
    doc.add(r"\hspace{2cm} & \hspace{5cm} & \hspace{5cm} & \hspace{4cm}\\")
    doc.add(rf"a) {q1} & b) {q2} & c) {q3} & d) {q4}\\ \\")
    doc.add(r"\end{tabular}")
    doc.add(r"\end{table}")
    doc.add(r"\newline")
    return

def gen_four_std_form_arithmetic(doc):
    q1 = gen_question_std_form_addition()
    q2 = gen_question_std_form_subtraction()
    q3 = gen_question_std_form_multiplication()
    q4 = gen_question_std_form_division()
    doc.add(r"Simplify the following expression into the form $A\times10^n$:")
    doc.add(r"\begin{table}[h!]")
    doc.add(r"\centering")
    doc.add(r"\begin{tabular}{c c}")
    doc.add(r"\hspace{5cm} & \hspace{5cm}\\")
    doc.add(rf"a) {q1} & b) {q2}\\ \\")
    doc.add(rf"c) {q3} & d) {q4}\\ \\")
    doc.add(r"\end{tabular}")
    doc.add(r"\end{table}")
    doc.add(r"\newline")
    return


def gen_section_standard_form(doc):
    doc.add_section("Standard Form")
    gen_four_ordinary_to_std_form(doc)
    gen_four_std_form_to_ordinary(doc)
    gen_four_std_form_arithmetic(doc)
    return
