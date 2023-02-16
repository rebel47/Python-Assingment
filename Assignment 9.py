# Question 1
def is_disarium(num):
    temp = 0
    for i in range(len(str(num))):
        temp += int(str(num)[i]) ** (i + 1)
    return temp == num

num = int(input("Enter a number: "))

if is_disarium(num):
    print(f"{num} is a Disarium Number")
else:
    print(f"{num} is not a Disarim Number")

# Question 2
def check_disarium(number):    
  no_digits = 0
  num = number  
  while(num != 0):
    no_digits = no_digits + 1
    num = num//10

  remainder = 0
  disarium_num = 0    
  while(number > 0):
    remainder = number % 10
    disarium_num = disarium_num + (remainder**no_digits)
    number = number//10
    no_digits = no_digits - 1
  return disarium_num

print("DISARIUM NUMBERS WITHIN RANGE({1},{100}) ARE -")
for i in range(1,101):    
  if check_disarium(i) == i:
    print(i,end=" ")

# Question 3
def is_Happy_num(n):
  past = set()
  while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in past:
            return False
        past.add(n)
  return True
print(is_Happy_num(7))
print(is_Happy_num(932))
print(is_Happy_num(6))
# Question 4
def check_happy(number):
  remainder = 0
  happy_num = 0;    
  while(number > 0):    
    remainder = number%10;    
    happy_num = happy_num + (remainder*remainder);    
    number = number//10;
  return happy_num;

lower = int(1)
upper = int(100)
print("HAPPY NUMBERS WITHIN RANGE({},{}) ARE -".format(lower,upper))
for i in range(lower,upper+1):
  happy_num = i
  while(happy_num != 1 and happy_num != 4):
    happy_num = check_happy(happy_num)
  if(happy_num == 1):
    print(i,end=" ")
# Question 5
Number = int(input("Enter a Number = "))
Sum = 0
rem = 0

Temp = Number
while Temp > 0:
    rem = Temp % 10
    Sum = Sum + rem
    Temp = Temp // 10

print("The Sum of the Digits = %d" %Sum)

if Number % Sum == 0:
    print("\n%d is a Harshad Number." %Number)
else:
    print("%d is Not a Harshad Number." %Number)
# Question 6
def checkPronic(Number):
    i = 0
    flag = 0
    while i <= Number:
        if Number == i * (i + 1):
            flag = 1
            break
        i = i + 1
    return flag

minPro = int(1)
maxPro = int(100)

print("\nThe List of Pronic Numbers from {} and {}".format(minPro, maxPro)) 
for i in range(minPro, maxPro):
    if(checkPronic(i) == 1):
        print(i, end = '   ')
