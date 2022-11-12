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
for student in  STUDENT_ANSWER:
    studentMARK =0 # we assume each student got 0
    for index, q in enumerate(REAL_TEST_ANSWER):
        resultCount = 0 # keep track of the point earned for each question
        if((student[index+1].isnumeric())): # CHECKING  IF THE ANSWER IS A NUMBER VALUE. FOR EXAMPLE ONE OF THEM IS "*" in the student answer csv file
            if(int(q[1])==1): # if number of choices is only one then we can just do exact match
                if(int(q[0])==int(student[index+1])): resultCount=resultCount+1
            else:
                for answer in student[index+1]: # go through each answer choice and check if it exist in the student choices
                    if(answer in q[0]):
                        resultCount= resultCount+(float(1)/float(len(q[0]))) # for every correct answer we add the points 
                    else:
                        resultCount= resultCount-(float(1)/float(len(q[0]))) # for every incorrect choice we subtract the points
                    if(resultCount<0): resultCount=0 # we can't have negative points
       # print("question: ", index+1 ,student[0], student[index+1],resultCount, q[0], q[1])  
        studentMARK += resultCount  
        resultCount=0
       
    testResult[str(student[0])] = studentMARK


# write the data back into a csv
with open('student_mark_with_partial.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["StudentID"])
    for key, value in testResult.items():
       writer.writerow([key, value])

