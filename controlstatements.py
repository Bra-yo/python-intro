temperature =float(input("Enter the current temperature:"))

if temperature > 25 :
    print("It is too hot")
else:
    print("it is too cold")

#A program that returns the smallest number
first = int(input("Enter the first number:"))
second = int(input("Enter the second number:"))
third = int(input("Enter the third number:"))


if first < second and first < third :
    print(first,"is the smallest number")
elif second < first and second < third :
    print(second,"is the smallest number")
else :
    print(third,"is the small number")

num =0
if num == 0 :
    print(num,"is a neutral number")
elif (num % 2) == 0: print(num,"is an even number")
else:print(num,"is an odd number")