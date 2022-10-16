'''
Created by: Tsz Hey Lam
Created on: 04.10.2022

Methods for generating Prime Factor, HCF and LCM math questions.
'''
from . import numbers_fractions_operators as helper 
import random

def gen_question_prime_factorisation(lower_bound=4, upper_bound=100, max_steps=5):
    num = helper.gen_prime_less_than_twenty()
    curr_steps = 1
    steps = random.randint(2, max_steps)
    while(num < upper_bound and curr_steps < steps):
        num = num * helper.gen_prime_less_than_ten()
        curr_steps += 1
    return f"${num}$"

def gen_question_HCF_small():
    num_01 = gen_question_prime_factorisation(lower_bound=1, upper_bound=100, max_steps=5)
    num_02 = gen_question_prime_factorisation(lower_bound=1, upper_bound=100, max_steps=5)
    while(num_01 == num_02):
        num_02 = gen_question_prime_factorisation(lower_bound=1, upper_bound=100, max_steps=5)
    return f"{num_01} and {num_02}"


def gen_question_LCM_small():
    num_01 = gen_question_prime_factorisation(lower_bound=1, upper_bound=30, max_steps=5)
    num_02 = gen_question_prime_factorisation(lower_bound=1, upper_bound=30, max_steps=5)
    while (num_01 == num_02):
        num_02 = gen_question_prime_factorisation(lower_bound=1, upper_bound=30, max_steps=5)
    return f"{num_01} and {num_02}"


def gen_question_HCF_LCM_large():
    num_01 = gen_question_prime_factorisation(lower_bound=100, upper_bound=500, max_steps=15)
    num_02 = gen_question_prime_factorisation(lower_bound=100, upper_bound=500, max_steps=15)
    while (num_01 == num_02):
        num_02 = gen_question_prime_factorisation(lower_bound=100, upper_bound=500, max_steps=15)
    return f"{num_01} and {num_02}"

def gen_three_prime_factorisation(doc):
    q1 = gen_question_prime_factorisation()
    q2 = gen_question_prime_factorisation()
    q3 = gen_question_prime_factorisation()
    
    doc.add(f"Prime factorise the following numbers and rewrite the number as a product of prime factors:")
    doc.add(r"\begin{table}[h!]")
    doc.add(r"\centering")
    doc.add(r"\begin{tabular}{c c c}")
    doc.add(r"\hspace{4cm} & \hspace{4cm} & \hspace{4cm} \\")
    doc.add(rf"a) {q1} & b) {q2} & c) {q3}\\ \\")
    doc.add(r"\end{tabular}")
    doc.add(r"\end{table}")
    doc.add(r"\newline")

def gen_one_HCF_and_LCM_large(doc):
    q1 = gen_question_HCF_LCM_large()
    
    doc.add(f"Find the Highest Common Factor and Lowest Common Multiple of the pair of number below:")
    doc.add(r"\begin{table}[h!]")
    doc.add(r"\centering")
    doc.add(r"\begin{tabular}{c}")
    doc.add(r"\hspace{4cm}\\")
    doc.add(rf"a) {q1}\\ \\")
    doc.add(r"\end{tabular}")
    doc.add(r"\end{table}")
    doc.add(r"\newline")

def gen_section_prime_HCF_LCM(doc):
    doc.add_section("Prime Factors, HCF and LCM")
    gen_three_prime_factorisation(doc)
    gen_one_HCF_and_LCM_large(doc)

