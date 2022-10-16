'''
Created by: Tsz Hey Lam
Created on: 17.09.2022

For generating power rule related maths questions.
'''
from . import numbers_fractions_operators as helper 
import random 

def gen_question_multiplication_rule(base_num, pow1, pow2):
    question_arr = ["$", f"{base_num}^{pow1}", r"\times", f"{base_num}^{pow2}", "$"]
    question = ''.join(question_arr)
    return question


def gen_question_division_rule(base_num, pow1, pow2):
    question_arr = ["$", f"{base_num}^{pow1}", r"\div", f"{base_num}^{pow2}", "$"]
    question = ''.join(question_arr)
    return question

def gen_question_pow_pow_rule(base_num, pow1, pow2):
    question = f"$({base_num}^{pow1})^{pow2}$"
    return question

def gen_question_zero_rule(base_num):
    question = f"$({base_num})^0$"
    return question

def gen_question_one_rule(base_num):
    question = f"$({base_num})^1$"
    return question

def gen_question_neg_pow_rule(base_num, neg_num):
    question = f"${base_num}^{neg_num}$"
    return question

def gen_question_fraction_pow_rule(base_num, numerator, denominator):
    fraction = helper.gen_fraction(numerator, denominator)
    question_arr = [f"${base_num}^", f"{fraction}", "$"]
    question = ''.join(question_arr)
    return question

def gen_question_neg_pow_frac_simplify():
    coin_toss = random.randint(1, 4)
    coin_toss2 = random.randint(0, 1)
    coin_toss3 = random.randint(0, 1)
    base = helper.gen_rnd_int_text(2, 4)
    term1 = helper.gen_term_pow(base, helper.gen_rnd_int_text(-3, -1))

    if coin_toss2 == 0:
        term2 = helper.gen_term_pow(base, helper.gen_rnd_int_text(-3, -1))
    else:
        term2 = helper.gen_rnd_int_text(1, 4)

    if coin_toss3 == 0:
        temp = term1
        term1 = term2
        term2 = temp

    if coin_toss == 1:
        q = f"${helper.gen_add_expr(term1, term2)}$"
    elif coin_toss == 2:
        q = f"${helper.gen_sub_expr(term1, term2)}$"
    elif coin_toss == 3:
        q = f"${helper.gen_mul_expr(term1, term2)}$"
    elif coin_toss == 4:
        q = f"${helper.gen_div_expr(term1, term2)}$"

    return q

def gen_nine_simplify_questions(doc):
    # 3 multiplication questions
    q1 = gen_question_multiplication_rule(helper.gen_rnd_int_text(2, 10), helper.gen_rnd_int_text(1, 10), helper.gen_rnd_int_text(1, 10))
    q2 = gen_question_multiplication_rule(helper.gen_rnd_int_text(2, 10), helper.gen_rnd_int_text(-5, 5), helper.gen_rnd_int_text(-10, -1))
    q3 = gen_question_multiplication_rule(helper.gen_rnd_int_text(2, 10), helper.gen_rnd_int_text(-10, -1), helper.gen_rnd_int_text(-10, -1))

    # 3 division question
    q4 = gen_question_division_rule(helper.gen_rnd_int_text(2, 10), helper.gen_rnd_int_text(1, 10), helper.gen_rnd_int_text(1, 10))
    q5 = gen_question_division_rule(helper.gen_rnd_int_text(2, 10), helper.gen_rnd_int_text(-5, 5), helper.gen_rnd_int_text(-10, -1))
    q6 = gen_question_division_rule(helper.gen_rnd_int_text(2, 10), helper.gen_rnd_int_text(-10, -1), helper.gen_rnd_int_text(-10, -1))

    # 2 power rules
    q7 = gen_question_pow_pow_rule(helper.gen_rnd_int_text(2, 10), helper.gen_rnd_int_text(1, 10), helper.gen_rnd_int_text(1, 10))
    q8 = gen_question_pow_pow_rule(helper.gen_rnd_int_text(2, 10), helper.gen_rnd_int_text(-5, 5), helper.gen_rnd_int_text(-10, -1))

    # 1 power zero rule or power 1 rule
    if random.randint(1, 10) <= 5:
        q9 = gen_question_zero_rule(helper.gen_rnd_int_text(-1000, 1000))
    else:
        q9 = gen_question_one_rule(helper.gen_rnd_int_text(-1000, 1000))

    doc.add(r"Keeping the answer in power form, simplify the following expression:")
    doc.add(r"\begin{table}[h!]")
    doc.add(r"\centering")
    doc.add(r"\begin{tabular}{c c c}")
    doc.add(r"\hspace{5cm} & \hspace{5cm} & \hspace{5cm} \\")
    doc.add(rf"a) {q1} & b) {q2} & c) {q3} \\ \\")
    doc.add(rf"d) {q4} & e) {q5} & f) {q6} \\ \\")
    doc.add(rf"g) {q7} & h) {q8} & i) {q9} \\ \\")
    doc.add(r"\end{tabular}")
    doc.add(r"\end{table}")
    doc.add(r"\newline")
    return


def gen_three_neg_rules(doc):
    q1 = gen_question_neg_pow_rule(helper.gen_rnd_int_text(2, 5), helper.gen_rnd_int_text(-3, -1))
    q2 = gen_question_neg_pow_frac_simplify()
    q3 = gen_question_neg_pow_frac_simplify()

    doc.add(r"Simplify the following expression into fractions. Fully simplify your answer where possible:")
    doc.add(r"\begin{table}[h!]")
    doc.add(r"\centering")
    doc.add(r"\begin{tabular}{c c c}")
    doc.add(r"\hspace{5cm} & \hspace{5cm} & \hspace{5cm} \\")
    doc.add(rf"a) {q1} & b) {q2} & c) {q3} \\ \\")
    doc.add(r"\end{tabular}")
    doc.add(r"\end{table}")
    doc.add(r"\newline")


def gen_three_fraction_rules(doc):
    choices = [2, 4, 9, 16, 25, 36, 49, 64, 81, 100, 8, 27, 64, 125]
    q1 = gen_question_fraction_pow_rule(helper.gen_rnd_choice_text(choices), 1, helper.gen_rnd_int_text(2, 3))
    q2 = gen_question_fraction_pow_rule(helper.gen_rnd_choice_text(choices), 1, helper.gen_rnd_int_text(2, 3))
    q3 = gen_question_fraction_pow_rule(helper.gen_rnd_choice_text(choices), 1, helper.gen_rnd_int_text(2, 3))


    doc.add(r"Rewrite the following expressions into surds:")
    doc.add(r"\begin{table}[h!]")
    doc.add(r"\centering")
    doc.add(r"\begin{tabular}{c c c}")
    doc.add(r"\hspace{5cm} & \hspace{5cm} & \hspace{5cm} \\")
    doc.add(rf"a) {q1} & b) {q2} & c) {q3} \\ \\")
    doc.add(r"\end{tabular}")
    doc.add(r"\end{table}")
    doc.add(r"\newline")


def gen_section_power_rules(doc):
    doc.add_section("Power rules")
    gen_nine_simplify_questions(doc)
    gen_three_neg_rules(doc)
    gen_three_fraction_rules(doc)
