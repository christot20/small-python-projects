import random
aGrades = random.sample(range(50, 100), 7) #list of grades
print ("Here is the list of grades:")
print (aGrades)
examCount = len(aGrades)-1 #amount of exams in the list
print ("The number of exams are", examCount)
final_grade = aGrades[-1] #last grade in the list of grades
print ("The grade of the final test is", final_grade)
def sumgrades():
    totalgrade = sum(aGrades) - aGrades[-1] #total points of the list of grades
    print ("The total points are:", totalgrade)
    testaverage = totalgrade / examCount #average score of the grades
    print ("The test average is:", testaverage)
    final_average = (.6*testaverage) + (.4*final_grade) #the average final of the scores
    print ("The final average is:", final_average)
    #final letter grade program
    grade = final_average
    if grade >= 90:
        print ("Your letter grade is a A with a grade of", grade)
        if final_grade >= 90:
            print ("Your final test grade is an A with a score of", final_grade)
        elif final_grade >= 80:
            print("Your final test grade is a B with a score of", final_grade)
        elif final_grade >= 70:
            print ("Your final test grade is a C with a score of", final_grade)
        elif final_grade >= 60:
            print ("Your final test grade is a D with a score of", final_grade)
        else:
            print("Your final test grade is an F with a score of", final_grade)
    elif grade >= 80:
        print ("Your letter grade is a B with a grade of", grade)
        if final_grade >= 90:
            print("Your final test grade is an A with a score of", final_grade)
        elif final_grade >= 80:
            print("Your final test grade is a B with a score of", final_grade)
        elif final_grade >= 70:
            print("Your final test grade is a C with a score of", final_grade)
        elif final_grade >= 60:
            print("Your final test grade is a D with a score of", final_grade)
        else:
            print("Your final test grade is an F with a score of", final_grade)
    elif grade >= 70:
        print ("Your letter grade is a C with a grade of", grade)
        if final_grade >= 90:
            print("Your final test grade is an A with a score of", final_grade)
        elif final_grade >= 80:
            print("Your final test grade is a B with a score of", final_grade)
        elif final_grade >= 70:
            print("Your final test grade is a C with a score of", final_grade)
        elif final_grade >= 60:
            print("Your final test grade is a D with a score of", final_grade)
        else:
            print("Your final test grade is an F with a score of", final_grade)
    elif grade >= 60:
        print ("Your letter grade is a D with a grade of", grade)
        if final_grade >= 90:
            print("Your final test grade is an A with a score of", final_grade)
        elif final_grade >= 80:
            print("Your final test grade is a B with a score of", final_grade)
        elif final_grade >= 70:
            print("Your final test grade is a C with a score of", final_grade)
        elif final_grade >= 60:
            print("Your final test grade is a D with a score of", final_grade)
        else:
            print("Your final test grade is an F with a score of", final_grade)
    else:
        print ("Your letter grade is an F with a grade of", grade)
        if final_grade >= 90:
            print("Your final test grade is an A with a score of", final_grade)
        elif final_grade >= 80:
            print("Your final test grade is a B with a score of", final_grade)
        elif final_grade >= 70:
            print("Your final test grade is a C with a score of", final_grade)
        elif final_grade >= 60:
            print("Your final test grade is a D with a score of", final_grade)
        else:
            print("Your final test grade is an F with a score of", final_grade)
    return totalgrade, testaverage, final_average
sumgrades()



