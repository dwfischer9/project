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

    inFile.close()
    studentRecords = mergeStudentData(studentNamesandID,studentData)
    print(studentRecords)
def mergeStudentData(studentNamesandId, studentData):
    for i in range(len(studentNamesandId) -1): ## Appends names to corresponding values from the file that did not have names associated with them
        for j in range(len(studentData) - 1):
            if(studentData[j][0] == studentData[i][0] and i != j):
                studentData[j].append(studentData[i][1])
                studentData[j].append(studentData[i][2])
            if(studentNamesandId[i][0] == studentData[j][0]):
                studentData[j].append(studentNamesandId[i][1])
            ## at this point, studentData has all of the data we need, however, some elements only have
            # partial data on a student. A proper entry has six parts to it, so we trim out
            # any entries less than 6 in length
    for ele in list(studentData):
        if len(ele) < 6:
            studentData.remove(ele)
## now , we have a 2d array in the format of: 
# [int studentID, String course1, String testScores1, String name, String course2, string testScores2 ]
    return studentData
parseFiles()