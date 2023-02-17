# Question 1
def divisible_by_5_and_7(n):
    for i in range(n+1):
        if i % 5 == 0 and i % 7 == 0:
            yield i
n = int(input("Enter a value for n: "))
divisible_nums = divisible_by_5_and_7(n)
print(", ".join(str(num) for num in divisible_nums))

# Question 2
def even_numbers(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a value for n: "))
even_nums = even_numbers(n)
print(", ".join(str(num) for num in even_nums))

# Question 3
n = int(input("Enter a value for n: "))
fib_sequence = [0, 1] + [fib_sequence[i-1] + fib_sequence[i-2] for i in range(2, n+1)]
print(", ".join(str(num) for num in fib_sequence))

# Question 4
def extract_username(email):
    username, domain = email.split("@")

    return username

email = "ayazalam@inueron.ai"
username = extract_username(email)
print(username)

# Question 5
class Shape:
    def area(self):
        print("The area of the shape is 0 by default.")

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        area = self.length ** 2
        print(f"The area of the square is {area}.")

s = Shape()
s.area()

sq = Square(5)
sq.area()
