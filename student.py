from readfile import parseFiles
import re
from person import Person
class Student(Person):
    # [String name, int studentID, String course, String testGrades]
    def __init__(self, studentID, course, testGrades,name):
        self.name = name
        self.studentID = studentID
        self.course = course
        self.testGrades = testGrades
    def __str__(self):
        return str("{0:15}{1:20}{2:15}{3:5}".format(self.getStudentID(),self.getName(),self.getCourse(),self.calcFinalGrade())) 
    def getName(self):
        assert len(self.name) <= 20, "Name must be less than 20 characters"
        return self.name
    def getStudentID(self):
        #Must be 9 characters long
        assert len(self.studentID) == 9, "Student ID number invalid";
        return self.studentID
    def getCourse(self):
        #Must be 5 characters long
        assert len(self.course) == 5, "Course code invalid";
        return self.course
    
    def getTestGrades(self):
        return self.testGrades
    
    ##each test weighs 20% and the final exam weighs 40%. The final grade is calculated with
    ##the following: (test,1,2,3) 3x20% + (final exam) 40% = 100%.
    def calcFinalGrade(self):
        grades = re.split('[,.!?\\-]',self.getTestGrades())  ## split test grades on multiple delimiters
        finalGrade = round((.20 * int(grades[0])) + (.20 * int(grades[1])) + 
        (.20 * int(grades[2])) + (.40 * int(grades[3])),1)
        if(finalGrade < 0):
            finalGrade = 0 # final grade cannot be negative, so we set it to zero
        return finalGrade
