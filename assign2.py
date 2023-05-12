# 2. write a program for the school registry.

marks = int(input(" Enter total marks got by the student out of 600 :"))
out_of_marks = max(0,600)
print("out_of_marks",out_of_marks)
percent_marks = int((marks / out_of_marks) * 100)
print("percent_marks",percent_marks)
if percent_marks < 100:
    if percent_marks <= 35:
        print("FAIL")
    elif  percent_marks <= 50:
        print("Passed in third class")
    elif  percent_marks <= 60:
        print("passed in second class")
    elif  percent_marks <= 85:
        print("passed in First Class")
    elif  percent_marks <= 100:
        print("Distinction")
    else:
        print("Invalid")
else:
    print("Invalid")
