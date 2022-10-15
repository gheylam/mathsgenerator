'''
Created on: 14.10.2022
Created by: Tsz Hey Lam 

Class for generating interest rate related questions.
'''
import random 
from . import numbers_fractions_operators as helper 

class Interest_Rate_Generator:
    def __init__(self, doc):
        self.doc = doc 
        doc.add_section("Interest Rates")

    def gen_q_static_interest_rate(self, ir=-1, sv=-1, period=-1):
        if ir == -1: 
            interest_rate = random.randint(1, 10)
        else: 
            interest_rate = ir
        if sv == -1:
            starting_value = random.randint(1, 10) * 1000 + random.randint(0, 10) * 100
        else:
            starting_value = sv 
        if period == -1:
            num_years = random.randint(1, 5)
        else:
            num_years = period
        q = f"With a starting value of £${starting_value}$ and annual static interest rate of ${interest_rate}$\%, how much will I have after ${num_years}$ years?"
        return q

    def gen_q_compound_interest_rate(self, ir=-1, sv=-1, period=-1):
        if ir == -1: 
            interest_rate = random.randint(1, 10)
        else: 
            interest_rate = ir
        if sv == -1:
            starting_value = random.randint(1, 10) * 1000 
        else:
            starting_value = sv 
        if period == -1:
            num_years = random.randint(2, 3)
        else:
            num_years = period
        q = f"With a starting value of £${starting_value}$ and annual compound interest rate of ${interest_rate}$\%, how much will I have after ${num_years}$ years?" 
        return q

    def gen_batch_interest_rates(self):
        q1 = self.gen_q_static_interest_rate()
        q2 = self.gen_q_compound_interest_rate()
        self.doc.add("a) " + q1)
        self.doc.add("b) " + q2)
