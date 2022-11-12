import csv

#variable declaration
STUDENT_ANSWER = []
testResult = {}

#read the the the student answer file please replace the 'test.csv" with the correct file name according to your document
with open('test.csv', newline='') as csvfile:
    TestData = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in TestData:
            STUDENT_ANSWER.append(row[0].split(","))
        
#Gather the ANSWER KEY and load the the db of dataset. PLEASE CHOOSE A VALID FILE NAME AND MAKE SURE IT EXIST 
REAL_TEST_ANSWER = []
with open('testanswer.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in data:
        REAL_TEST_ANSWER.append(row[0].split(","))

#calculate partial marks for each student
resultCount = 0
for student in  STUDENT_ANSWER:
    studentMARK =0

    for index, q in enumerate(REAL_TEST_ANSWER):
        for answer in q[1]: # go through each answer choice and check if it exist in the student choices
           if(answer in student[index+1]):
                resultCount= resultCount+1
       #print("question: ", index+1 ,student[0], student[index+1],resultCount/len(q[1]), q[1])  
        studentMARK += resultCount/len(q[1])  
        resultCount=0
       
    testResult[str(student[0])] = studentMARK


# write the data back into a csv
with open('student_mark_with_partial.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["StudentID"])
    for key, value in testResult.items():
       writer.writerow([key, value])

