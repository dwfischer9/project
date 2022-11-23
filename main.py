from student import Student
from readfile import mergeStudentData, parseFiles

##TODO: Make a method that, for each element in the 2D array from readFile.py, constructs a student object and call the str() method on it
        #each of these strings is to be written to the output file, output.txt.

FILENAME1 = "CourseFile.txt"
FILENAME2 = "NameFile.txt"
OUTFILE = "output.txt"

def main():
    fileName1 = FILENAME1
    fileName2 = FILENAME2
    outFile = open(OUTFILE,"w")
    studentData = parseFiles(fileName1, fileName2)
    outFile.write("Student ID     Student Name      Course Code      Final Grade\n----------------------------------------------------------------\n")
    for e in studentData:
        stringToFile(e,outFile)
    outFile.close()

def stringToFile(student,outFile):
    data = str(Student(student[0], student[1] , student[2] , student[3])) + "\n"
    outFile.write(data)
main()