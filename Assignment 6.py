# # Question 1
# def fibonacci(n):  
#    if n <= 1:  
#        return n  
#    else:  
#        return(fibonacci(n-1) + fibonacci(n-2))

# num = int(input("Enter a number: "))  
# if num <= 0:  
#    print("Plese enter a positive integer")  
# else:    
#    for i in range(num):  
#        print(fibonacci(i))  


# #Question 2
# def factorial(num):
#     if num==1:
#         return 1
#     else:
#         return (num*factorial(num-1))

# num = int(input("Enter a number: "))
# print(f"Factorial of {num} is {factorial(num)}")


# # Question 3
# height = int(input("Enter your height in cm: "))
# weight = int(input("Enter your weight in kg: "))

# bmi = weight/(height/100)**2
# print(f"Your BMI is {bmi}")


# # Question 4
# import math
# num = int(input("Enter a number: "))
# log = math.log(num)
# print(f"The log of {num} is: {log}")


# Question 5
num = int(input("Enter a number: "))
sum=0
for i in range(1,num+1):
    sum += sum+(i**3)
print(f"The sum of cubes from 1 to {num} is: {sum}")