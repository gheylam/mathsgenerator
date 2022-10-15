'''
Created by: Tsz Hey Lam 
Created on: 13.10.2022 

Class for generating questions related fractions, percentages and decimals.
'''
from . import numbers_fractions_operators as helper 
import random 
import numpy as np 

class Frac_Perc_Deci_Generator:
    def __init__(self, doc):
        self.doc = doc
        doc.add_section("Fractions, Percentages and Decimals")

    def gen_q_fraction_to_percentage_easy(self):
        divisor_of_100 = [1, 2, 5, 10, 20, 25, 50]
        numerator = helper.gen_rnd_int_text(1, 100)
        denominator = int(100 / random.choice(divisor_of_100))
        fraction = helper.gen_fraction(numerator, denominator)
        return f"${fraction}$"
    
    def gen_q_fraction_to_decimal_3dp(self):
        '''
        These will be fractions that can be easily divided to be 1 to 3 decimal places.
        '''
        found = False
        numerator = 0 
        denominator = 0
        while(found == False):
            numerator = random.randint(1, 20)
            denominator = random.randint(10, 50)
            result = numerator / denominator
    
            found_1_place = helper.check_decimal_place(result, 1)
            found_2_place = helper.check_decimal_place(result, 2)
            found_3_place = helper.check_decimal_place(result, 3)
            if found_1_place or found_2_place or found_3_place:
                if result < 1: 
                    found = True
                    print(str(result))

        fraction = helper.gen_fraction(numerator, denominator)
        return f"${fraction}$"

    def gen_q_percentage_to_fraction(self):
        num = random.randint(1, 100)
        random_val = random.random()
        if random_val < 0.2:
            percentage = num / 10
        elif random_val >= 0.2 and random_val < 0.9:
            percentage = num 
        else:
            percentage = num * 10
        return f"${percentage}\%$"

    def gen_q_percentage_operators(self, percentage_scalar=-1):
        num = random.randint(1, 100) * 10
        if percentage_scalar == -1:
            percentage = random.randint(1, 99)
        else:
            percentage = random.randint(1, 9) * percentage_scalar
    
        return f"${percentage}\%$ of ${num}$"
    
    def gen_q_fraction_operators(self): 
        numerator = random.randint(1, 20)
        denominator = random.randint(1, 10)
        number = denominator * random.randint(1, 10)
        fraction = helper.gen_fraction(numerator, denominator)
        return f"${fraction}$ of ${number}$"
    

    def gen_batch_fraction_conversion(self):
        '''
        Generate 6 questions, 3 fractions to percentages, 3 fractions to decimals 
        '''
        q1 = self.gen_q_fraction_to_percentage_easy()
        q2 = self.gen_q_fraction_to_percentage_easy()
        q3 = self.gen_q_fraction_to_percentage_easy()
        q4 = self.gen_q_fraction_to_decimal_3dp()
        q5 = self.gen_q_fraction_to_decimal_3dp()
        q6 = self.gen_q_fraction_to_decimal_3dp()
        
        self.doc.add("Convert the following fractions into percentages and then convert them to decimal:")
        self.doc.add(r"\begin{table}[h!]")
        self.doc.add(r"\centering")
        self.doc.add(r"\begin{tabular}{c c c}")
        self.doc.add(r"\hspace{2cm} & \hspace{6cm} & \hspace{4cm}\\")
        self.doc.add(rf"a) {q1} & b) {q2} & c) {q3}\\ \\")
        self.doc.add(r"\end{tabular}")
        self.doc.add(r"\end{table}")
        self.doc.add(r"\newline")

        self.doc.add("Convert the following fractions into decimals:")
        self.doc.add(r"\begin{table}[h!]")
        self.doc.add(r"\centering")
        self.doc.add(r"\begin{tabular}{c c c}")
        self.doc.add(r"\hspace{2cm} & \hspace{6cm} & \hspace{4cm}\\")
        self.doc.add(rf"a) {q4} & b) {q5} & c) {q6}\\ \\")
        self.doc.add(r"\end{tabular}")
        self.doc.add(r"\end{table}")
        self.doc.add(r"\newline")

        return 

    def gen_batch_percentage_conversion(self):
        '''
        Generate 3 questions, 3 percentage to fractions and decimal 
        '''
        q1 = self.gen_q_percentage_to_fraction()
        q2 = self.gen_q_percentage_to_fraction()
        q3 = self.gen_q_percentage_to_fraction()

        self.doc.add("Convert the following percentages into fractions and then decimals:")
        self.doc.add(r"\begin{table}[h!]")
        self.doc.add(r"\centering")
        self.doc.add(r"\begin{tabular}{c c c}")
        self.doc.add(r"\hspace{2cm} & \hspace{6cm} & \hspace{4cm}\\")
        self.doc.add(rf"a) {q1} & b) {q2} & c) {q3}\\ \\")
        self.doc.add(r"\end{tabular}")
        self.doc.add(r"\end{table}")
        self.doc.add(r"\newline")
        return 

    def gen_batch_fraction_and_percentage_operators(self): 
        '''
        Generate 6 questions, 3 percentage operator questions, 3 fraction operator questions 
        '''
        q1 = self.gen_q_percentage_operators()
        q2 = self.gen_q_percentage_operators()
        q3 = self.gen_q_percentage_operators()

        q4 = self.gen_q_fraction_operators()
        q5 = self.gen_q_fraction_operators()
        q6 = self.gen_q_fraction_operators()

        self.doc.add("Work out the value of the following expressions :")
        self.doc.add(r"\begin{table}[h!]")
        self.doc.add(r"\centering")
        self.doc.add(r"\begin{tabular}{c c c}")
        self.doc.add(r"\hspace{2cm} & \hspace{6cm} & \hspace{4cm}\\")
        self.doc.add(rf"a) {q1} & b) {q2} & c) {q3}\\ \\")
        self.doc.add(rf"d) {q4} & e) {q5} & f) {q6}\\ \\")
        self.doc.add(r"\end{tabular}")
        self.doc.add(r"\end{table}")
        self.doc.add(r"\newline")
        return 
