class school:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print("student name",self.name)
    def show_age(self):
        print("student age",self.age)
s1=school("sanju",17)
s2=school("vikram",18)
s3=school("chandan",19)
s4=school("rohan",21)
s5=school("atish",23)
print(getattr(s1,'name'),":",getattr(s1,'age'))
setattr(s2,'name','vikram')
print(getattr(s2,'name'),":",getattr(s2,'age'))
print(hasattr(s1,'6'))
