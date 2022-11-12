from math_generator import *

doc = tsz_latex_generator.Doc(
    'f:/Development/Maths_Generator/output/weekly_assessments/year9_output/year9_weekly_assessment_week10.tex')
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

# Generate the questions 
algebra_simplifying_gen = algebra_simplifying.AlgebraSimplifyGenerator(doc)
algebra_simplifying_gen.gen_batch_linear()
algebra_simplifying_gen.gen_batch_non_linear()

algebra_expanding_gen = algebra_expanding.AlgebraExpandingGenerator(doc)
algebra_expanding_gen.gen_batch_single_brackets()
algebra_expanding_gen.gen_batch_double_brackets()

algebra_factorising_gen = algebra_factorising.AlgebraFactorisingGenerator(doc)
algebra_factorising_gen.gen_batch_simple_factorising()
algebra_factorising_gen.gen_batch_factorising()

doc.add(r"\end{document}")
print("[LOG] Generated year9 weekly assessment.")
