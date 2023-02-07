# Question 1

X = [[7,12,1],
    [5,4,6],
    [7 ,8,1]]
Y = [[6,8,4,2],
    [5,4,3,0],
    [7,4,3,11]]
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(X)):
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)

# Question 2

X = [[7,12,1],
    [5,4,6],
    [7 ,8,1]]
Y = [[6,8,4,2],
    [5,4,3,0],
    [7,4,3,11]]
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

for i in range(len(X)):
   for j in range(len(Y[0])):
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)

# Question 3

X = [[1,4],
    [2 ,5],
    [3 ,6]]

result = [[0,0,0],
         [0,0,0]]

for i in range(len(X)):
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)

# Question 4
my_str = "Hello this Is an Example With cased letters"
words = [word.lower() for word in my_str.split()]
words.sort()
print("The sorted words are:")
for word in words:
   print(word)

# Question 5
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_string = "Hello!!!, he said ---and went."
noPunct = ""
for char in my_string:
   if char not in punctuations:
       noPunct = noPunct + char
print(noPunct)
