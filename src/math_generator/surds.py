'''
Created by: Tsz Hey Lam
Created on: 24.09.2022

Methods to generate surd questions.
'''

from . import numbers_fractions_operators as helper 
import numpy as np
import random

def gen_question_simplify_into_a_sqrt_b():
    simple_flag = random.randint(0, 1)
    if simple_flag == 0:
        prime_num = helper.gen_prime_less_than_ten()
        rootable_num = helper.gen_rootable_number(small=True)
        surd_num = np.power(prime_num, 3) * rootable_num
    else:
        prime_num = helper.gen_prime_less_than_ten()
        rootable_num = helper.gen_rootable_number()
        surd_num = prime_num * rootable_num
    return helper.gen_term_sqrt(surd_num)


def gen_question_simplify_expression():
    return

def gen_question_simplify_multiply():
    return

def gen_question_rationalise():
    scalar = random.randint(1, 12)
    prime_num = helper.gen_prime_less_than_ten()
    surd = helper.gen_term_sqrt(prime_num, scalar)
    numerator = random.randint(1, 12)
    return helper.gen_fraction(numerator, surd)

def gen_question_simplify_into_k_plus_a_sqrt_b():
    # The answers to these questions should be in the form k + a\sqrt{b}
    return


def gen_three_simplify_surds(doc):
    q1 = gen_question_simplify_into_a_sqrt_b()
    q2 = gen_question_simplify_into_a_sqrt_b()
    q3 = gen_question_simplify_into_a_sqrt_b()
    doc.add(r"Simplifying the following surd expressions leaving your answer in the form $a\sqrt{b}$:")
    doc.add(r"\begin{table}[h!]")
    doc.add(r"\centering")
    doc.add(r"\begin{tabular}{c c c}")
    doc.add(r"\hspace{4cm} & \hspace{4cm} & \hspace{4cm}\\")
    doc.add(rf"a) {q1} & b) {q2} & c) {q3}\\ \\")
    doc.add(r"\end{tabular}")
    doc.add(r"\end{table}")
    doc.add(r"\newline")

def gen_three_rationalize_surds(doc):
    q1 = gen_question_rationalise()
    q2 = gen_question_rationalise()
    q3 = gen_question_rationalise()
    doc.add(r"Rationalise the following fractions to remove the surd in the denominator:")
    doc.add(r"\begin{table}[h!]")
    doc.add(r"\centering")
    doc.add(r"\begin{tabular}{c c c}")
    doc.add(r"\hspace{4cm} & \hspace{4cm} & \hspace{4cm}\\")
    doc.add(rf"a) {q1} & b) {q2} & c) {q3}\\ \\")
    doc.add(r"\end{tabular}")
    doc.add(r"\end{table}")
    doc.add(r"\newline")

def gen_section_surds(doc):
    doc.add_section("Surds")
    gen_three_simplify_surds(doc)
    gen_three_rationalize_surds(doc)


