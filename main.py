from student import Student
from readfile import mergeStudentData, parseFiles

##TODO: Make a method that, for each element in the 2D array from readFile.py, constructs a student object and call the str() method on it
        #each of these strings is to be written to the output file, output.txt.
        
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

    except FileNotFoundError:
        print("Missing the required files")
    
    except NameError:
        print("Missing required method")
        
def stringToFile(student,outFile):
    if(len(student) == 4):
        data = str(Student(student[0], student[1] , student[2] , student[3])) + "\n"
        outFile.write(data)
main()