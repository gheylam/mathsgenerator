from tsz_latex_generator import *
from power_rules import *
from negative_numbers import *
from fractions import *
from standard_form import *
from surds import *
from prime_factors_hcf_lcm import * 

doc = Doc('./weekly_assessments/year8_output/year8_weekly_assessment.tex')
doc.erase()

doc.add(r"\documentclass[12pt]{article}")
doc.add_geometry(['a4paper', 'top=40mm', 'left=20mm', 'right=20mm'])
doc.add(r"\usepackage[utf8]{inputenc}")
doc.add(r"\usepackage{fancyhdr}")

doc.add(r"\begin{document}")

doc.add(r"\pagestyle{fancy}")
doc.add(r"\fancyhead[L]{\textbf{Name:}}")
doc.add(r"\fancyhead[C]{\textbf{Date:\hspace{2cm}}}")
doc.add(r"\fancyhead[R]{\textbf{Mark:\hspace{2cm}}}")
doc.add(r"\fancyfoot{} ")


gen_section_negative_numbers(doc)
gen_section_fractions(doc)
doc.add_newpage()
gen_section_power_rules(doc)
doc.add_newpage()
gen_section_standard_form(doc)
doc.add_newpage()
gen_section_prime_HCF_LCM(doc)

doc.add(r"\end{document}")
print("[LOG] Generated year8 weekly assessment.")
