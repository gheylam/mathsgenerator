from maths_generator.tsz_latex_generator import *
from maths_generator.fractions import *
from maths_generator.power_rules import *
from maths_generator.negative_numbers import *

doc = Doc('./year8_output/year8_weekly_assessment_neg_frac_pow.tex')
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
gen_section_power_rules(doc)

doc.add(r"\end{document}")

