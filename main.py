from student import Student
from readfile import mergeStudentData, parseFiles

#main handles the input files, completes the student object and handles any exceptions

def main():
    try:
        fileName1 = "CourseFile.txt"
        fileName2 = "NameFile.txt"
        outFile = open("output.txt","w");
        studentData = parseFiles(fileName1, fileName2)
        
        outFile.write("Student ID      Student Name      Course Code      Final Grade\n ----------------------------------------------------------------\n")
        for e in studentData:
            stringToFile(e,outFile)
        outFile.close()

    #in case a required input file not found, return error
    except FileNotFoundError:
        print("Missing the required files")
    
    #in case a required method not found, return error
    except NameError:
        print("Missing required method")
        
#method handling writing file output to text file titled output.txt

def stringToFile(student,outFile):
    if(len(student) == 4):
        data = str(Student(student[0], student[1] , student[2] , student[3])) + "\n"
        outFile.write(data)
main()
