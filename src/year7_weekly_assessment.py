from math_generator import *

doc = tsz_latex_generator.Doc('f:/Development/Maths_Generator/output/weekly_assessments/year7_output/year7_weekly_assessment_week06.tex')
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


negative_numbers.gen_section_negative_numbers(doc)

fraction_gen = fractions.Fraction_Generator(doc)
fraction_gen.gen_three_ordering_fractions()
fraction_gen.gen_eight_questions()
operators.gen_section_operators(doc)
rounding_and_approximation.gen_section_rounding(doc)


doc.add(r"\end{document}")
