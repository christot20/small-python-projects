import random
gradePoints = {"A":4,"B":3,"C":2,"D":1,"F":0}
courseList = ["CST 161","Mat 144","ENG 201","PSY 101","HIS 101"]
gradeList = ["A","B","C","D","F"]
creditList = [3,4]


i = 0
print("Course"+"..."+"Credits", "", "Grade", "", "Value Per Course")
totalcreditslist = []
qualitypointslist = []
for y in courseList:
    while i < len(courseList):
        k = random.randint(0, 4)
        letterGrade = gradeList[k]
        gPoints = gradePoints[gradeList[k]]
        creditIndex = random.randint(3, 4)
        valuePerCourse = (creditIndex * gPoints)
        totalcreditslist.append(creditIndex)
        qualitypointslist.append(valuePerCourse)
        print (y+"....", creditIndex, "     ", letterGrade, gPoints, "     ", valuePerCourse)
        i += 1
        if len(totalcreditslist) and len (qualitypointslist) == 5:
            totalCredits = sum(totalcreditslist)
            qualityPoints = sum(qualitypointslist)
            GPA = qualityPoints/totalCredits
            print (" Total Credits earned are:", totalCredits,"\n", "Total quality points earned are:", qualityPoints, "\n", "Your GPA is:", round(GPA,2))
        break



