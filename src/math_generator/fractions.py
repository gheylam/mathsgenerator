'''
Created by: Tsz Hey Lam
Created on: 17.09.2022

Generate fraction related maths questions.
'''

from . import numbers_fractions_operators as helper 
import random 

class Fraction_Generator:
    def __init__(self, doc):
        self.doc = doc 
        doc.add_section("Fractions")

    def gen_question_adding(self, frac1, frac2):
        q = helper.gen_add_expr(frac1, frac2)
        return f"${q}$"

    def gen_question_subtracting(self, frac1, frac2):
        q = helper.gen_sub_expr(frac1, frac2)
        return f"${q}$"

    def gen_question_multiplying(self, frac1, frac2):
        q = helper.gen_mul_expr(frac1, frac2)
        return f"${q}$"

    def gen_question_dividing(self, frac1, frac2):
        q = helper.gen_div_expr(frac1, frac2)
        return f"${q}$"

    def gen_question_simplify(self, frac):
        return f"${frac}$"

    def gen_question_order_fractions(self, num_fractions=3):
        q = ['$']
        denominator = random.randint(1, 12)
        for index in range(num_fractions):
            numerator = random.randint(1, 12)
            multiplier = random.randint(1, 12)
            frac = helper.gen_fraction(numerator*multiplier, denominator*multiplier)
            q.append(frac)
            if index != num_fractions-1:
                q.append(', ')
            else:
                q.append('$')
        return ''.join(q)


    def gen_question_reoccurring_decimal(self, type=1):
        if type==1: 
            fig1 = random.randint(1, 9)
            q_list = ['$0.', r'\dot{', str(fig1), r'}$']
            q = ''.join(q_list)
        elif type==2:
            fig1 = random.randint(1, 9)
            fig2 = random.randint(1, 9)
            q_list = ['$0.', r'\dot{', str(fig1), '}', r'\dot{', str(fig2), '}']
            q = ''.join(q_list)
        elif type==3:
            fig = random.randint(1, 9)
            fig1 = random.randint(1, 9)
            fig2 = random.randint(1, 9)
            q_list = [f'$0.{fig}', r'\dot{', str(fig1), '}', r'\dot{', str(fig2), '}']
            q = ''.join(q_list)
        return q

    def gen_six_simplifying_fractions(self):
        list_of_frac = []
        for index in range(6):
            numerator = random.randint(1, 12)
            denominator = random.randint(2, 12)
            multiplier = random.randint(2, 12)
            frac = helper.gen_fraction(numerator*multiplier, denominator*multiplier)
            list_of_frac.append(self.gen_question_simplify(frac))

        self.doc.add("Simplifying the following fractions leaving your answer in their simplest form:")
        self.doc.add(r"\begin{table}[h!]")
        self.doc.add(r"\centering")
        self.doc.add(r"\begin{tabular}{c c c}")
        self.doc.add(r"\hspace{2cm} & \hspace{6cm} & \hspace{4cm}\\")
        self.doc.add(rf"a) {list_of_frac[0]} & b) {list_of_frac[1]} & c) {list_of_frac[2]}\\ \\")
        self.doc.add(rf"d) {list_of_frac[3]} & e) {list_of_frac[4]} & f) {list_of_frac[5]}\\ \\")
        self.doc.add(r"\end{tabular}")
        self.doc.add(r"\end{table}")
        self.doc.add(r"\newline")


    def gen_three_ordering_fractions(self, n1=3, n2=3, n3=3):
        q1 = self.gen_question_order_fractions(n1)
        q2 = self.gen_question_order_fractions(n2)
        q3 = self.gen_question_order_fractions(n3)
        self.doc.add("Order the following lists of fractions from smallest to largest:")
        self.doc.add(r"\begin{table}[h!]")
        self.doc.add(r"\centering")
        self.doc.add(r"\begin{tabular}{c}")
        self.doc.add(r"\hspace{4cm}\\")
        self.doc.add(rf"a) {q1}\\ \\")
        self.doc.add(rf"b) {q2}\\ \\")
        self.doc.add(rf"c) {q3}\\ \\")
        self.doc.add(r"\end{tabular}")
        self.doc.add(r"\end{table}")
        self.doc.add(r"\newline")



    def gen_eight_questions(self):
        # two adding questions
        q1 = self.gen_question_adding(helper.gen_fraction(helper.gen_rnd_int_text(1, 10), helper.gen_rnd_int_text(1, 10)),
                                helper.gen_fraction(helper.gen_rnd_int_text(1, 10), helper.gen_rnd_int_text(1, 10)))
        q2 = self.gen_question_adding(helper.gen_fraction(helper.gen_rnd_int_text(-10, 10), helper.gen_rnd_int_text(-10, 10)),
                                helper.gen_fraction(helper.gen_rnd_int_text(-10, 10), helper.gen_rnd_int_text(1, 10)))

        # two substracting questions
        q3 = self.gen_question_subtracting(helper.gen_fraction(helper.gen_rnd_int_text(1, 10), helper.gen_rnd_int_text(1, 10)),
                                helper.gen_fraction(helper.gen_rnd_int_text(1, 10), helper.gen_rnd_int_text(1, 10)))
        q4 = self.gen_question_subtracting(helper.gen_fraction(helper.gen_rnd_int_text(-10, 10), helper.gen_rnd_int_text(-10, 10)),
                                helper.gen_fraction(helper.gen_rnd_int_text(-10, 10), helper.gen_rnd_int_text(1, 10)))

        # two multiplying questions
        q5 = self.gen_question_multiplying(helper.gen_fraction(helper.gen_rnd_int_text(1, 10), helper.gen_rnd_int_text(1, 10)),
                                helper.gen_fraction(helper.gen_rnd_int_text(1, 10), helper.gen_rnd_int_text(1, 10)))
        q6 = self.gen_question_multiplying(helper.gen_fraction(helper.gen_rnd_int_text(-10, 10), helper.gen_rnd_int_text(-10, 10)),
                                helper.gen_fraction(helper.gen_rnd_int_text(-10, 10), helper.gen_rnd_int_text(1, 10)))

        # two dividing questions
        q7 = self.gen_question_dividing(helper.gen_fraction(helper.gen_rnd_int_text(1, 10), helper.gen_rnd_int_text(1, 10)),
                                    helper.gen_fraction(helper.gen_rnd_int_text(1, 10), helper.gen_rnd_int_text(1, 10)))
        q8 = self.gen_question_dividing(helper.gen_fraction(helper.gen_rnd_int_text(-10, 10), helper.gen_rnd_int_text(-10, 10)),
                                    helper.gen_fraction(helper.gen_rnd_int_text(-10, 10), helper.gen_rnd_int_text(1, 10)))

        self.doc.add("Simplifying the following expression leaving your answer in their simplest form:")
        self.doc.add(r"\begin{table}[h!]")
        self.doc.add(r"\centering")
        self.doc.add(r"\begin{tabular}{c c c c}")
        self.doc.add(r"\hspace{4cm} & \hspace{4cm} & \hspace{4cm} & \hspace{4cm}\\")
        self.doc.add(rf"a) {q1} & b) {q2} & c) {q3} & d) {q4} \\ \\")
        self.doc.add(rf"e) {q5} & f) {q6} & g) {q7} & h) {q8} \\ \\")
        self.doc.add(r"\end{tabular}")
        self.doc.add(r"\end{table}")
        self.doc.add(r"\newline")

    def gen_batch_reoccurring_decimals(self):
        q1 = self.gen_question_reoccurring_decimal(type=1)
        q2 = self.gen_question_reoccurring_decimal(type=2)
        q3 = self.gen_question_reoccurring_decimal(type=3)
        self.doc.add("Convert the following reoccurring decimals to fractions:")
        self.doc.add(r"\begin{table}[h!]")
        self.doc.add(r"\centering")
        self.doc.add(r"\begin{tabular}{c c c}")
        self.doc.add(r"\hspace{2cm} & \hspace{6cm} & \hspace{4cm}\\")
        self.doc.add(rf"a) {q1} & b) {q2} & c) {q3}\\ \\")
        self.doc.add(r"\end{tabular}")
        self.doc.add(r"\end{table}")
        self.doc.add(r"\newline")
