# Question 1
def word_k(k, s):    
    word = s.split(" ")
    for x in word:
        if len(x)>k:
          print(x)
k = 5
s ="Hello welcome to the world of illusions"
word_k(k, s)

# Question 2
def remove_char(s, i):
    a = s[ : i]
    b = s[i + 1: ]

    return a+b

string = "Ever-lasting"
i = 5
print(remove_char(string,i-1))

# Question 3
def split_string(string):
    list_string = string.split(' ')
    return list_string

def join_string(list_string):
    string = '-'.join(list_string)
    return string

string = 'Hello welcome to the world of illusions'
list_string = split_string(string)
print("After Splitting: ",list_string)
res_string = join_string(list_string)
print("After Joining: ",res_string)

# Question 4
def check(string) :
    b = set(string)
    s = {'0', '1'}
    if s == b or b == {'0'} or b == {'1'}:
        print("Binary String")
    else :
        print("Non Binary String")
  
s1= "00110101"
check(s1)
s2 = "1010100200111"
check(s2)

# Question 5
def uncommon(s1,s2):
  s1=s1.split()
  s2=s2.split()
  k=set(s1).symmetric_difference(set(s2))
  return k

a = "berry mango cherry"
b = "berry peach cherry"
print(list(uncommon(a,b)))

# Question 6
string = "ShahequaModabbera"
duplicates = []
for char in string:
    if string.count(char) > 1:
       if char not in duplicates:
          duplicates.append(char)
print(*duplicates)

# Question 7
import re

def check_string(my_string):

   regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
   if(regex.search(my_string) == None):
      print("String does not contain any special characters.")
   else:
      print("String contains special character.")

my_string = "Shahequa_Modabbera"
print("The string is :")
print(my_string)
check_string(my_string)