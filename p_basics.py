from pydantic import BaseModel, Field, EmailStr
"""
pydantic fundamentals
pydantic is a data validation and settings management library for python, based on python type annotations"""
"""
step1:the problem 
a normal dictionary accepts anything.Nobody checks the data type of the values we are storing in the dictionary."""
bad_student={
    "name":"",
    "age":"twenty",
    "marks":110,
    "email":"not an email"
}
#print(bad_student)

"""
step2:the solution i.e. BASEMODEL + TYPE HINTS   wht basemodel does is it checks the data type of the values we are 
storing in the dictionary and if it is not correct then it raises an error
we desc a student once and python checks every student agaoinst it"""
"""class Student(BaseModel):
    name:str
    age:int
    marks:int
s=Student(name="palak",age="20",marks=100) """     #it automates type conversion as well i.e. if we give age as string it will convert it to int automatically
#print(s.name,s.age,s.marks)


"""
step 3-FIELD() Rules
gt=greater than          lt=less than
gt=greater than equal to            lt=less than equal to"""
class RuleStudent(BaseModel):
    name:str=Field(...,min_length=2,max_length=100)   #... means it is a required field
    age:int=Field(...,gt=0,lt=100)
    marks:int=Field(...,ge=0,le=100)   
    course:str="python"
    phone:str|None=None
    s=RuleStudent(name="palak",age=20,marks=100)
    print(s.name,s.age,s.marks,s.course,s.phone)

"""
step4-EMAIL VALIDATION
pydantic has a built in email validator which checks if the email is valid or not
class EmailStudent(BaseModel):
    name:str
    email:EmailStr
    s=EmailStudent(email="palak@example.com")
    #print(s.name,s.email)  """