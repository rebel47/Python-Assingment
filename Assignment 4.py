# Question 1
num = int(input("Enter a number: "))
fact = 1

if num<0:
    print(f"Factorial of {num} doest not exist.")
elif num==0:
    print(f"Factorial of {num} is 1.")
else:
    for i in range(1,num+1):
        fact = fact*i
    print(f"Factorial of {num} is {fact}")


# Question 2
num = int(input('Enter a number: '))
for i in range(1,11):
    print(f"{num}x{i}={num*i}")

# Question 3
num = int(input('Enter a number: '))
a = 0
b = 1
c =0 
for i in range(1,num+1):
    print(a,end=",")
    c = a+b
    a = b
    b = c
    


# Question 4
num = input('Enter a number: ')
sum = 0
for i in num:
    sum = sum+(int(i)**3)
if int(num)==sum:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")



# Question 5
num = int(input('Enter a number: '))
sum = 0
for i in range(1,num+1):
    sum += i

print(sum)