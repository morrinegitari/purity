#program to check whether a number is prime number or not

num =int(input("Enter a number ;"))
if num > 1 :
    for i in range (2,(num//2)+1):
        if (num % i) == 0:
           print(num,"is not prime number")

        else :
            print(num,"is a prime number")


