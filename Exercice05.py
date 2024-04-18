Student_grade={
    "AMIT":17,
    "ABU":18,
    "SALIM":10,
    "ISMAIL":12,
    "KEKEW":10

}
def ave_student_with_ave_grade(Student_grade):
    ave_grade = 10
    ave_grade_student = None

    for student, grade in Student_grade.items():
        if grade > ave_grade:
            ave_grade = grade
            ave_grade_student = student

    return ave_grade_student, ave_grade
ave_student, ave_grade = ave_student_with_ave_grade(Student_grade)

print(f"The student with the average grade is {ave_student} with a grade of {ave_grade}.")

#...................................................................................
def get_student_with_max_grade(students):
    max_grade = -1
    max_grade_student = None

    for student, grade in students.items():
        if grade > max_grade:
            max_grade = grade
            max_grade_student = student

    return max_grade_student, max_grade


