import re ## importing regex
def parseFiles(fileName1, fileName2):
    #read from the first file, extract student ID, course codes and grades.
    inFile = open(fileName1, 'r')#open file for reading
    lines = inFile.read() # get all text from the file as a string
    studentId = re.findall("\d{9}",lines) #create a list with all student ID's in the input file
    courseCodes = re.findall("[A-Z]{2}\d{3}", lines) #create a list with all course codes in the input file 
    testGrades = re.findall(" \d{2}, \d{2}, \d{2}, \d{2}", lines) #create a list with all test scores in the input fuile
    studentCoursesAndGrades = list()
    for i in range(len(studentId)): #create a 2d array with ID courses and scores.
        studentCoursesAndGrades.append([studentId[i],courseCodes[i],testGrades[i]])
    inFile.close(); #close the input file.


    #read from the second file, extrace student ID and names.
    inFile = open(fileName2, 'r')
    lines = inFile.read()
    studentId2 = re.findall("\d{9}",lines) #create a list with all student ID's in the input file
    studentName = re.findall("[a-zA-Z]+ [a-zA-Z]+",lines)
    studentNamesandID = list()
    for i in range(len(studentId2)): #creates a 2D array with student ID and Names
        studentNamesandID.append([studentId2[i],studentName[i]])
    inFile.close()
    studentRecords = mergeStudentData(studentNamesandID,studentCoursesAndGrades)
    return studentRecords


def mergeStudentData(studentNamesandId, studentData):
    for student in studentNamesandId:
        for data in studentData:
            if(student[0] == data[0]): #if the entries have the same ID
                data.append(student[1]) #append the corresponding name to the student's data

## now , we have a 2d array in the format of: 
# [String name, int studentID, String course1, String testGrades1 String course2, string testGrades2 ]
# test grades are stored as a comma delimited string and must be split and indexed in order to calculate final weighted average
    return studentData