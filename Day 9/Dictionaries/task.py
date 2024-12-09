# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }



student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = {}
for grade in student_scores:
    if student_scores[grade] >= 91:
        student_grades[grade] = "Outstanding"

    elif student_scores[grade] >= 81:
        student_grades [grade] = "Exceeds Expectations"
    elif student_scores[grade] >= 71:
        student_grades[grade] = "Acceptable"
    else:
        student_grades[grade] = "Fail"
print(student_grades)







