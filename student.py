class student:
    count=0
    def __init__(self):
       student.count = student.count + 1
       print("hello")
    def sum(self):
        print("sum wala hello")
s1=student()
s2=student()
s3=student()
s4=student()

s4.sum();
print("the number of student:",student.count)