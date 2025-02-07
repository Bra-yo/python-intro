firstname = str(input("Enter your First name : "))
lastname = str(input("Enter Your Last name: "))

print(f"Dear {firstname} {lastname} you have successfully registered")
Age = int(input("Enter your age :"))
if Age < 18 :
    print(f"Dear {firstname} {lastname} you are not allowed to enter this site!!! Not for Children under 18")
else:
 print(f"Dear {firstname} {lastname},you're {Age} years old")