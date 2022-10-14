import random

def gen_rnd_int_text(low_bound, high_bound):
    rnd_num = random.randint(low_bound, high_bound)
    if rnd_num < 0:
        rnd_num = f"-{abs(rnd_num)}"
    text_arr = ["{", f"{rnd_num}", "}"]
    return ''.join(text_arr)

def convert_num_to_str(num):
    txt = ['{', f"{num}", '}']
    return ''.join(txt)

def gen_rnd_choice_text(list):
    text_arr = ["{", f"{random.choice(list)}", "}"]
    return ''.join(text_arr)

def gen_prime_less_than_ten():
    primes = [2, 3, 5, 7]
    return random.choice(primes)

def gen_prime_less_than_twenty():
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    return random.choice(primes)

def gen_rootable_number(small=False):
    if small==False:
        rootable_number = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]
    else:
        rootable_number = [4, 9, 16, 25]

    return random.choice(rootable_number)


def gen_fraction(numerator, denominator):
    fact_arr = [r"\frac{", f"{numerator}", "}{", f"{denominator}", "}"]
    return ''.join(fact_arr)

def gen_add_expr(term1, term2):
    return f"{term1} + {term2}"

def gen_sub_expr(term1, term2):
    return f"{term1} - {term2}"

def gen_mul_expr(term1, term2):
    mul_expr_arr = [f"{term1}", r"\times", f"{term2}"]
    return ''.join(mul_expr_arr)

def gen_div_expr(term1, term2):
    div_expr_arr = [f"{term1}", r"\div", f"{term2}"]
    return ''.join(div_expr_arr)

def gen_term_pow(base, pow):
    return f"{base}^{pow}"

def gen_term_sqrt(num, scalar=1):
    if scalar == 1:
        term = ['$', r'\sqrt{', f"{num}", '}$']
    else:
        term = ['$', f"{scalar}", r'\sqrt{', f"{num}", '}$']
    return ''.join(term)

def check_decimal_place(num, places):
    str_num = str(num)
    str_num_split = str_num.split('.')
    if len(str_num_split[-1]) == places:
        return True 
    else:
        return False 