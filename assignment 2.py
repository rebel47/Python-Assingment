#Question 1
km = int(input("Enter KM: "))
mile = km/1.609
print(mile)


# Question 2
celsius = int(input("Enter Celsius: "))
fahrenheit = ((celsius)*9/5)+32
print(fahrenheit)


# Question 3
import calendar

year = int(input("Enter year: "))
month = int(input("Enter a month 1-12: "))

calendar = calendar.month(year, month)
print(calendar)


#Question 4
import cmath
# ax**2+bx+c=0
a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

# Calculate the discriminant
d = (b**2)-(4*a*c)
# Finding two solutions
solution_1 = (-b-cmath.sqrt(d))/(2*a)
solution_2 = (-b+cmath.sqrt(d))/(2*a)

print(f"The solutions are {solution_1} and {solution_2}")


# Question 5
a = 5
b = 10
print(f"Original Value of a:{a} and b:{b}")

a,b=b,a
print(f"Values of after swapping a:{a} and b{b}")