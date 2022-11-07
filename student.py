from readfile import parseFiles
class Student:
    # [String name, int studentID, String course1, String testGrades1 String course2, string testGrades2 ]
    def __init__(self, name, studentID, course1, testGrades1, course2, testGrades2):
        self.name = name
        self.studentID = studentID
        self.course1 = course1
        self.testGrades1 = testGrades1
        self.course2 = course2
        self.testGrades2 = testGrades2
##TODO: create method that converts string of grades into integers and calculates final weighted grade
##TODO: create toString method that takes all information and formats it as requested by the assignment. Should be formatted as: studentID, name, course1, final grade1, 
      #  and studentID, name, course2, finalGrade2 on a separate line.
##TODO: implement getter methods. these will be used in main.py
    def __str__(self):
        return 0
        
       
    def getName(self):
        return self.name
    def getStudentID(self):
        return 0
    def getCourse1(self):
        return 0
    def getTestGrades1(self):
        return 0
    def getCourse2(self):
        return 0
    def getTestGrades2(self):
        return 0
    
    ##each test weighs 20% and the final exam weighs 40%. The final grade is calculated with
    ##the following: (test,1,2,3) 3x20% + (final exam) 40% = 100%.
    def calcFinalGrade1(self):
        
        return 0
    def calcFinalGrade2(self):
        return 0
print(parseFiles())