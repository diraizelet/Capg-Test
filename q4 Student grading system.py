#calculate_grade is used to find what grade the student got
def calculate_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 75:
        return 'B'
    elif percentage >= 30:
        return 'C'
    else:
        return 'Fail'
    

# getInput will take the input from the student
def getInput():
    student_name = input("Enter the student's name: ")
    marks = []
    for i in range(1, 6):
        mark = float(input(f"Enter marks for subject {i}: "))
        marks.append(mark)
    return student_name, marks


#convertToPercent will calculate and return the percent 
def convertToPercent(total_marks):
    return (total_marks / 500) * 100

#printOutputs will print all the outputs that are to be displayed
def printOuputs(student_name, total_marks, percentage, grade):
    print(f"Student Name: {student_name}")
    print(f"Total Marks: {total_marks}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

# the main function is resposnsible for calling the functions that perform the actions
if __name__ == "__main__":
    student_name,marks=getInput()
    total_marks = sum(marks)
    percentage=convertToPercent(total_marks)
    grade = calculate_grade(percentage)
    printOuputs(student_name, total_marks, percentage, grade)