def getInput():
    while True:

     try:
        grade = int(input("enter grade number "))
        if 0 <= grade <= 100:
            return grade
        print('score should be between 1 1nd 100!\n')

     except:
            print("invalid input")
        

def determine_grade(grade):

    if(grade >= 70 ) & (grade <= 100):
        return 'A'
    elif(grade >= 60) & (grade <= 69):
        return 'B'
    elif(grade >= 50) & (grade <= 59):
        return 'C'
    elif(grade >= 45) & (grade <= 49):
        return 'D'
    elif(grade >= 40) & (grade <= 45):
         return 'E'
    elif(grade >= 0) & (grade <= 39):
        return 'F'
    else:
        return 'no value entered'
grade= getInput()
#determine_grade(grade)
print(determine_grade(grade))  
def readScore(filepath):
    '''
    create another file that contain the student names and their grades
    '''
    student_score = open(filepath)
    for score in file:
        gradeScore(grade)
    
    open('stuednt_grade.txt','w')
    return 