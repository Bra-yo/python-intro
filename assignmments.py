#A program to check whether a year is a leap year or not

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) :
    print(f"{year} is a leap year. ")
else: print(f"{year} is not a leap year. ")


#A program to check whether a letter is a consonant or a vowel

letter =str(input("Enter a letter: "))
if letter == ("a","e","i","o","u"):
    print(f" letter '{letter}' is a vowel!")
else:
    print(f"The letter '{letter}' is a consonant!")