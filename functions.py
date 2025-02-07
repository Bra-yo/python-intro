#Built-in functions (also called standard library functions
y = max(67,43,89,76,66,13)
print(f"The maximum value is {y}")

z = min(34,356,56,45,13,46,679,678,89)
print(f"The minimum value is {z}")

#User-defined functions

def name():
   print("Brian")

name() #calling a function

def product():
    x = 10
    y =30
    print(x*y)

product()

#Parameters/variable and Arguments/value assigned to a variable
def Add(a,b):
    print(a+b)
Add(4,4)


def employee(Name,Gender,Position,Salary,Age):
    print(Name,Gender,Position,Salary,Age)

employee("Brian","Male","Manager",900000,67)
employee("Albert","Male","Chairperson",760000,87)
employee("Glory","Female","Manager",4780000,57)
employee("Moses","Male","Treasure",255000,36)
employee("Becca","Female","works manager",567000,23)
employee("Mary","Female","Director",289000,39)
employee("Fifi","Famale","Secretary",345000,97)