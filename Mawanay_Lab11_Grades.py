#Variables:
counter = 0
passed = 0
student_number = 1 #student label starting at 1 (student 1)

#Initialization of the grade coder:
numlist = []

#Code for the inputing of grades:
while student_number < 6:
    num = float(input(f"Please enter your grade, student {student_number} (between 40 and 100): "))
    if num < 40 or num > 100:
        print("Invalid input, please enter a grade between 40 and 100.")
    else:
        numlist.append(num)
        student_number += 1 #for identifying the number of the next student
        
    if num >= 75:
        passed += 1
        counter += 1
    else:
        counter += 1
    
    if counter == 5:
        print()
        sumNums = sum (numlist)
        average_grade = sumNums / 5
        average_grade = round(average_grade, 2)
        
        Passing_Percentage = (passed / len(numlist)) * 100
        Passing_Percentage + round(Passing_Percentage, 2)
        
        print("Grade Inputted: " + str(numlist))
        print("Average Grade: " + str(average_grade))
        print("Number of students who passed: " + str(passed))
        print("Percentage of students who passed: " + str(Passing_Percentage) + "%")