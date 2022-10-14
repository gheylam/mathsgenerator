'''
Created by: Tsz Hey Lam
Created on: 17.09.2022

Generate fraction related maths questions.
'''

from . import numbers_fractions_operators as helper 

class Fraction_Generator:
    def __init__(self, doc):
        self.doc = doc 
        doc.add_section("Fractions")

    def gen_question_adding(frac1, frac2):
        q = helper.gen_add_expr(frac1, frac2)
        return f"${q}$"

    def gen_question_subtracting(frac1, frac2):
        q = helper.gen_sub_expr(frac1, frac2)
        return f"${q}$"

    def gen_question_multiplying(frac1, frac2):
        q = helper.gen_mul_expr(frac1, frac2)
        return f"${q}$"

    def gen_question_dividing(frac1, frac2):
        q = helper.gen_div_expr(frac1, frac2)
        return f"${q}$"

    def gen_question_simplify(frac):
        return f"${frac}$"

    def gen_question_order_fractions(num_fractions=3):
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

    def gen_six_simplifying_fractions(doc):
        list_of_frac = []
        for index in range(6):
            numerator = random.randint(1, 12)
            denominator = random.randint(2, 12)
            multiplier = random.randint(2, 12)
            frac = helper.gen_fraction(numerator*multiplier, denominator*multiplier)
            list_of_frac.append(gen_question_simplify(frac))

        doc.add("Simplifying the following fractions leaving your answer in their simplest form:")
        doc.add(r"\begin{table}[h!]")
        doc.add(r"\centering")
        doc.add(r"\begin{tabular}{c c c}")
        doc.add(r"\hspace{2cm} & \hspace{6cm} & \hspace{4cm}\\")
        doc.add(rf"a) {list_of_frac[0]} & b) {list_of_frac[1]} & c) {list_of_frac[2]}\\ \\")
        doc.add(rf"d) {list_of_frac[3]} & e) {list_of_frac[4]} & f) {list_of_frac[5]}\\ \\")
        doc.add(r"\end{tabular}")
        doc.add(r"\end{table}")
        doc.add(r"\newline")


    def gen_three_ordering_fractions(doc, n1=3, n2=3, n3=3):
        q1 = gen_question_order_fractions(n1)
        q2 = gen_question_order_fractions(n2)
        q3 = gen_question_order_fractions(n3)
        doc.add("Order the following lists of fractions from smallest to largest:")
        doc.add(r"\begin{table}[h!]")
        doc.add(r"\centering")
        doc.add(r"\begin{tabular}{c}")
        doc.add(r"\hspace{4cm}\\")
        doc.add(rf"a) {q1}\\ \\")
        doc.add(rf"b) {q2}\\ \\")
        doc.add(rf"c) {q3}\\ \\")
        doc.add(r"\end{tabular}")
        doc.add(r"\end{table}")
        doc.add(r"\newline")



    def gen_eight_questions(doc):
        # two adding questions
        q1 = gen_question_adding(gen_fraction(gen_rnd_int_text(1, 10), gen_rnd_int_text(1, 10)),
                                gen_fraction(gen_rnd_int_text(1, 10), gen_rnd_int_text(1, 10)))
        q2 = gen_question_adding(gen_fraction(gen_rnd_int_text(-10, 10), gen_rnd_int_text(-10, 10)),
                                gen_fraction(gen_rnd_int_text(-10, 10), gen_rnd_int_text(1, 10)))

        # two substracting questions
        q3 = gen_question_subtracting(gen_fraction(gen_rnd_int_text(1, 10), gen_rnd_int_text(1, 10)),
                                gen_fraction(gen_rnd_int_text(1, 10), gen_rnd_int_text(1, 10)))
        q4 = gen_question_subtracting(gen_fraction(gen_rnd_int_text(-10, 10), gen_rnd_int_text(-10, 10)),
                                gen_fraction(gen_rnd_int_text(-10, 10), gen_rnd_int_text(1, 10)))

        # two multiplying questions
        q5 = gen_question_multiplying(gen_fraction(gen_rnd_int_text(1, 10), gen_rnd_int_text(1, 10)),
                                gen_fraction(gen_rnd_int_text(1, 10), gen_rnd_int_text(1, 10)))
        q6 = gen_question_multiplying(gen_fraction(gen_rnd_int_text(-10, 10), gen_rnd_int_text(-10, 10)),
                                gen_fraction(gen_rnd_int_text(-10, 10), gen_rnd_int_text(1, 10)))

        # two dividing questions
        q7 = gen_question_dividing(gen_fraction(gen_rnd_int_text(1, 10), gen_rnd_int_text(1, 10)),
                                    gen_fraction(gen_rnd_int_text(1, 10), gen_rnd_int_text(1, 10)))
        q8 = gen_question_dividing(gen_fraction(gen_rnd_int_text(-10, 10), gen_rnd_int_text(-10, 10)),
                                    gen_fraction(gen_rnd_int_text(-10, 10), gen_rnd_int_text(1, 10)))

        doc.add("Simplifying the following expression leaving your answer in their simplest form:")
        doc.add(r"\begin{table}[h!]")
        doc.add(r"\centering")
        doc.add(r"\begin{tabular}{c c c c}")
        doc.add(r"\hspace{4cm} & \hspace{4cm} & \hspace{4cm} & \hspace{4cm}\\")
        doc.add(rf"a) {q1} & b) {q2} & c) {q3} & d) {q4} \\ \\")
        doc.add(rf"e) {q5} & f) {q6} & g) {q7} & h) {q8} \\ \\")
        doc.add(r"\end{tabular}")
        doc.add(r"\end{table}")
        doc.add(r"\newline")


