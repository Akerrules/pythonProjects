import csv


STUDENT_ANSWER = []
testResult = {}
with open('test.csv', newline='') as csvfile:
    data = csv.reader(csvfile, data=' ', quotechar='|')
    count =0
    for row in data:
        if(count>0):
            STUDENT_ANSWER.append(row[0].split(","))
        count = count+1
        

REAL_TEST_ANSWER = []
with open('testanswer.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in data:
        REAL_TEST_ANSWER.append(row[0].split(","))


resultCount = 0
for student in  STUDENT_ANSWER:
    studentMARK =0

    for index, q in enumerate(REAL_TEST_ANSWER):
        for answer in q[1]:
           if(answer in student[index+1]):
                resultCount= resultCount+1
       #print("question: ", index+1 ,student[0], student[index+1],resultCount/len(q[1]), q[1])  
        studentMARK += resultCount/len(q[1])  
        resultCount=0
       
    testResult[str(student[0])] = studentMARK



with open('student_mark_with_partial.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["StudentID"])
    for key, value in testResult.items():
       writer.writerow([key, value])

print(testResult.items())
