# A simple python program to check whether a year is a leap year or not

year = 2025
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year "is a leap year ")
else:
    print(year "is not a leap year")


#python program to check whethera letter is vowel or consonant

letter ="A"
if  (letter == 'a' or letter == 'e'or letter =="i" or letter == "o" or letter =="u" or letter == "A" or letter == "E" or letter == "I" or letter =="O" or letter =="U" ):
    print("vowel")
else :
    print("consonant")