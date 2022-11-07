import re
def parseFiles():
    #read from the first file, extract student ID, course codes and grades.
    inFile = open('CourseFile.txt', 'r')#open file for reading
    lines = inFile.read() # get all text from the file as a string
    studentId = re.findall("\d{9}",lines) #create a list with all student ID's in the input file
    courseCodes = re.findall("[A-Z]{2}\d{3}", lines) #create a list with all course codes in the input file 
    testGrades = re.findall(" \d{2}, \d{2}, \d{2}, \d{2}", lines) #create a list with all test scores in the input fuile
    studentCoursesAndGrades = list()
    for i in range(len(studentId)-1): #create a 2d array with ID courses and scores.
        studentCoursesAndGrades.append([studentId[i],courseCodes[i],testGrades[i]])
    inFile.close(); #close the input file.

    #read from the second file, extrace student ID and names.
    inFile = open('NameFile.txt', 'r')
    lines = inFile.read()
    studentId2 = re.findall("\d{9}",lines) #create a list with all student ID's in the input file
    studentName = re.findall("[a-zA-Z]+ [a-zA-Z]+",lines)
    studentNamesandID = list()
    for i in range(len(studentId2)-1): #creates a 2D array with student ID and Names
        studentNamesandID.append([studentId2[i],studentName[i]])

    inFile.close()
    studentRecords = mergeStudentData(studentNamesandID,studentCoursesAndGrades)
    return studentRecords


def mergeStudentData(studentNamesandId, studentData):
    for i in range(len(studentNamesandId) -1): ## Appends names to corresponding values from the file that did not have names associated with them
        for j in range(len(studentData) - 1):
            if(studentData[j][0] == studentData[i][0] and i != j):
                studentData[j].append(studentData[i][1])
                studentData[j].append(studentData[i][2])
            if(studentNamesandId[i][0] == studentData[j][0]):
                studentData[j].insert(0,studentNamesandId[i][1])
            ## at this point, studentData has all of the data we need, however, some elements only have
            # partial data on a student. A proper entry has six parts to it, so we trim out
            # any entries less than 6 in length
    for ele in list(studentData):
        if len(ele) < 6:
            studentData.remove(ele)
## now , we have a 2d array in the format of: 
# [String name, int studentID, String course1, String testGrades1 String course2, string testGrades2 ]
# test grades are stored as a comma delimited string and must be split and indexed in order to calculate final weighted average

    return studentData