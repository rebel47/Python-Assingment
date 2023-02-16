# Question 1
dict1 = {'A' : [1, 3, 5, 4],
         'B' : [4, 6, 8, 10],
         'C' : [6, 12, 4 ,8],
         'D' : [5, 7, 2]}

print("The original dictionary is : " ,dict1)
res = list(sorted({ele for val in dict1.values() for ele in val}))  
print("The unique values list is : " , res) 

# Question 2
dict={ 'x':455, 'y':223, 'z':300, 'p':908 }
print("Dictionary: ", dict)
print("Sum of all items: ",sum(dict.values()))

# Question 3
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

print(dict_1 | dict_2)

# Question 4
from itertools import product

my_dict = {'month_num' : [1, 2, 3, 4, 5, 6], 'name_of_month' : ['Jan', 'Feb', 'March', 'Apr', 'May', 'June']}

print("The dictionary is : ")
print(my_dict)

my_result = dict(zip(my_dict['month_num'], my_dict['name_of_month']))

print("The flattened dictionary is: ")
print(my_result)

# Question 5
from collections import OrderedDict
dic1 = OrderedDict([('A', '100'), ('B', '200'), ('C', '300')])
insrt = OrderedDict([("D", '400')])
  
final = OrderedDict(list(insrt.items()) + list(dic1.items()))
  
# print result
print ("Resultant Dictionary :")
print(final)

# Question 6
from collections import OrderedDict 
def checkOrder(string, pattern): 
    dict1 = OrderedDict.fromkeys(string) 
    ptr = 0
    for key,value in dict1.items(): 
        if (key == pattern[ptr]): 
            ptr = ptr + 1
        if (ptr == (len(pattern))): 
            return 'True'
    return 'False'

string = 'Syed Mohammad Ayaz Alam'
pattern = 'sye'
print (checkOrder(string,pattern))

string2= 'Data Analyst'
pattern2= 'Dls'
print (checkOrder(string2,pattern2)) 

# Question 7
#Sorting by Key
color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}

for key in sorted(color_dict):
    print("%s: %s" % (key, color_dict[key]))