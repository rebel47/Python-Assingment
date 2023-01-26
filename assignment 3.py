#Question 1
num = int(input("Enter a number: "))
if num<0:
    print(f"{num} is Negative number")
elif num>0:
    print(f"{num} is Positive number")
else:
    print(f"{num} is Zero")


# Question 2
num1 = int(input("Enter a number: "))
if num1%2==0:
    print("Even")
else:
    print("Odd")


# Question 3
year = int(input("Enter year: "))
if (year%400)==0 and (year%100)==0:
    print(f"{year} is a leap year")
elif (year%4)==0 and (year%100)!=0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")




# Question 4
num2 = int(input("Enter a number: "))
if num2 > 1:
    for i in range(2,num2):
        if (num2 % i)==0:
            print(f"{num2} is not a prime number")
            break
    else:
        print(f"{num2} is a prime number")
else:
    print(f"{num2} is not a prime number")

# Question 5
for i in range(1,10000):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        print(i)
