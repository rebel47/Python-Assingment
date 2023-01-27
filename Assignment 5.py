# Question 1
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

def cal_LCM(a,b):
    if a>b:
        greater = a
    else:
        greater = b
    while True:
        if ((greater%a)==0) and ((greater%b)==0):
            lcm = greater
            break
        greater +=1
    return lcm
print(f"L.C.M of {num1} and {num2} is: {cal_LCM(num1, num2)}")


# Question 2
num1 = int(input("Enter a num1: "))
num2 = int(input("Enter a num2: "))

def cal_HCF(a,b):
    if a>b:
        smaller = b
    else:
        smaller = a
    for i in range(1, smaller+1):
        if ((a%i)==0) and ((b%i)==0):
            hcf = i
    return hcf

print(f"H.C.F of {num1} and {num2} is {cal_HCF(num1,num2)}")


# Question 3
num = int(input("Enter Decimal number: "))

print(f"Binary value of decimal {num} is : {bin(num)}")
print(f"Octal value of decimal {num} is : {oct(num)}")
print(f"Hexadecimal value of decimal {num} is : {hex(num)}")


# Question 4
char = input("Enter a character: ")
print(f"The ASCII value of {char} is : {ord(char)}")


# Question 5
num1 = int(input("Enter the first value: "))
num2 = int(input("Enter the second value: "))

print(f"Addition of {num1}+{num2} = {num1+num2}")
print(f"Substraction of {num1}-{num2} = {num1-num2}")
print(f"Multiplication of {num1}*{num2} = {num1*num2}")
print(f"Division of {num1}/{num2} = {num1/num2}")