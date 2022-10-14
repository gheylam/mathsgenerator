'''
Created by: Tsz Hey Lam
Created on: 17.09.2022

For negative number related maths questions.
'''
from . import numbers_fractions_operators 


def gen_question_adding(term1, term2):
    q = gen_add_expr(term1, term2)
    return f"${q}$"


def gen_question_subtracting(term1, term2):
    q = gen_sub_expr(term1, term2)
    return f"${q}$"


def gen_question_multilplying(term1, term2):
    q = gen_mul_expr(term1, term2)
    return f"${q}$"


def gen_question_dividing(term1, term2):
    q = gen_div_expr(term1, term2)
    return f"${q}$"


def gen_twelve_negative_number_questions(doc):
    # gen 3 adding
    q1 = gen_question_adding(gen_rnd_int_text(-20, -1), gen_rnd_int_text(-20, 20))
    q2 = gen_question_adding(gen_rnd_int_text(-20, -1), gen_rnd_int_text(-30, -1))
    q3 = gen_question_adding(gen_rnd_int_text(-200, -1), gen_rnd_int_text(-200, -1))

    # gen 3 subtracting
    q4 = gen_question_subtracting(gen_rnd_int_text(-20, -1), gen_rnd_int_text(-20, 20))
    q5 = gen_question_subtracting(gen_rnd_int_text(-20, -1), gen_rnd_int_text(-30, -1))
    q6 = gen_question_subtracting(gen_rnd_int_text(-200, -1), gen_rnd_int_text(-200, -1))

    # gen 3 multiplying
    q7 = gen_question_multilplying(gen_rnd_int_text(-12, -1), gen_rnd_int_text(-12, 12))
    q8 = gen_question_multilplying(gen_rnd_int_text(-12, -1), gen_rnd_int_text(-12, -1))
    q9 = gen_question_multilplying(gen_rnd_int_text(-100, -1), gen_rnd_int_text(-20, 20))

    # gen 3 dividing
    q10 = gen_question_dividing(gen_rnd_int_text(-12, -1), gen_rnd_int_text(-12, 12))
    q11 = gen_question_dividing(gen_rnd_int_text(-12, -1), gen_rnd_int_text(-12, -1))
    q12 = gen_question_dividing(gen_rnd_int_text(-300, -1), gen_rnd_int_text(-10, 10))

    doc.add("Find the value of the following expressions. When dividing, leave your answer to 1 decimal place.")
    doc.add(r"\begin{table}[h!]")
    doc.add(r"\centering")
    doc.add(r"\begin{tabular}{c c c}")
    doc.add(r"\hspace{5cm} & \hspace{5cm} & \hspace{5cm} \\")
    doc.add(rf"a) {q1} & b) {q2} & c) {q3} \\ \\")
    doc.add(rf"d) {q4} & e) {q5} & f) {q6} \\ \\")
    doc.add(rf"g) {q7} & h) {q8} & i) {q9} \\ \\")
    doc.add(rf"j) {q10} & k) {q11} & l) {q12} \\ \\")
    doc.add(r"\end{tabular}")
    doc.add(r"\end{table}")
    doc.add(r"\newline")
    return


def gen_section_negative_numbers(doc):
    doc.add_section("Negative numbers")
    gen_twelve_negative_number_questions(doc)