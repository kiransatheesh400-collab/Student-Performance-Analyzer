import numpy as np

marks=np.random.randint(0,101,100)

# Statistics Calculation
average_marks=marks.mean()
median_mark=np.median(marks)
highest_mark=marks.max()
lowest_mark=marks.min()
variance=marks.var()
standard_deviation=marks.std()

# Students Performance Analysis
passed_students=marks[marks>39]
failed_students=marks[marks<=39]
above_avg_students=marks[marks>=average_marks]
below_avg_students=marks[marks<average_marks]
pass_percentage=(len(passed_students)/len(marks))*100
# Normalizing marks
normalized_marks=((marks-marks.min())/(marks.max()-marks.min()))

# Grade Calculation
"""Grading System:
90-100  → A
80-89   → B
70-79   → C
40-69   → D
0-39    → F"""

A_grade_students=marks[(marks>=90) & (marks<=100)]
B_grade_students=marks[(marks>=80) & (marks<90)]
C_grade_students=marks[(marks>=70) & (marks<80)]
D_grade_students=marks[(marks>=40) & (marks<70)]
F_grade_students=marks[marks<=39]
sorted_marks=np.sort(marks)
top5_marks=sorted_marks[-1:-6:-1]

# Displaying Report
print(f"Students Marks List \n{marks}")
print(f"Average Mark= {average_marks}")
print(f"Median Mark= {median_mark}")
print(f"Highest Mark= {highest_mark}")
print(f"Lowest Mark= {lowest_mark}")
print(f"Variance of Marks Data= {variance}")
print(f"Standard Deviation of Marks Data= {standard_deviation}")
print(f"Passed Students marks list= {passed_students}")
print(f"Failed Students marks list= {failed_students}")
print(f"Above Average Students marks list= {above_avg_students}")
print(f"Below Average Students marks list= {below_avg_students}")
print(f"Pass Percentage is {pass_percentage}%")
print(f"Normalized Marks List= {normalized_marks}")
print(f"\n Students Grading")
print(f"{"A":<5}{"B":<5}{"C":<5}{"D":<5}{"F":<5}")
print(f"{len(A_grade_students):<5}{len(B_grade_students):<5}{len(C_grade_students):<5}{len(D_grade_students):<5}{len(F_grade_students):<5}")
print(f"\nTop 5 marks= {top5_marks}")