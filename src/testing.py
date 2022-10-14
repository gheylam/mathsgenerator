from math_generator import fractions_percentages_decimals as fpd 

if __name__ == "__main__":
    gen = fpd.Frac_Perc_Deci_Generator("hello")
    print("test #1 ")
    for i in range(10):
        print(gen.gen_q_fraction_to_decimal_3dp())
    
    print("test #2")
    for i in range(10):
        print(gen.gen_q_percentage_to_fraction())