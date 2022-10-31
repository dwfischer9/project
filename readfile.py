import re
def parseFiles():
    inFile = open('CourseFile.txt', 'r')
    data = inFile.read()
    studentId = re.findall("\d{9}",data) #create a list with all student ID's in the input file
    course = re.findall("[A-Z]{2}\d{3}", data) #create a list with all course codes in the input file 
    scores = re.findall(" \d{2}, \d{2}, \d{2}, \d{2}", data) #create a list with all test scores in the input fuile
    studentData = list()
    for i in range(len(studentId)-1): #create a 2d array with ID courses and scores.
        studentData.append([studentId[i],course[i],scores[i]])
    inFile.close();
    inFile = open('NameFile.txt', 'r')
    data = inFile.read()
    studentId2 = re.findall("\d{9}",data) #create a list with all student ID's in the input file
    studentName = re.findall("[a-zA-Z]+ [a-zA-Z]+",data)
    studentNamesandID = list()
    for i in range(len(studentId2)-1): #creates a 2D array with student ID and Names
        studentNamesandID.append([studentId2[i],studentName[i]])
    print(studentNamesandID)
    inFile.close()
###def mergeStudentData(studentNamesandId, studentData):
    ###print(studen)
parseFiles()