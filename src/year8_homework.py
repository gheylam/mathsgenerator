from math_generator import *
import os
print(os.curdir)
doc = tsz_latex_generator.Doc("F:\\Development\\Maths_Generator\\output\\homework\\year8_output\\year8_homework_week06.tex")
doc.erase()

doc.add(r"\documentclass[12pt]{article}")
doc.add_geometry(['a4paper', 'top=40mm', 'left=20mm', 'right=20mm'])
doc.add(r"\usepackage[utf8]{inputenc}")
doc.add(r"\usepackage{fancyhdr}")

doc.add(r"\begin{document}")
doc.add(r"\pagestyle{fancy}")
doc.add(r"\fancyhead[L]{\textbf{Name:} \\ \textbf{Fractions homework}}")
doc.add(r"\fancyhead[C]{\textbf{Date:\hspace{2cm}} \\}")
doc.add(r"\fancyhead[R]{\textbf{Mark:\hspace{2cm}} \\}")
doc.add(r"\fancyfoot{} ")

fpd_gen = fractions_percentages_decimals.Frac_Perc_Deci_Generator(doc)
fpd_gen.gen_batch_fraction_conversion()
fpd_gen.gen_batch_percentage_conversion()
fpd_gen.gen_batch_fraction_and_percentage_operators()
interest_rate_gen = interest_rates.Interest_Rate_Generator(doc)
interest_rate_gen.gen_batch_interest_rates()

doc.add_newpage()
rounding_and_approximation.gen_section_rounding(doc)



doc.add(r"\end{document}")
print("Generated")