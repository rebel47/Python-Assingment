# # Question 1
# def sum_list(items):
#     sum_numbers = 0
#     for x in items:
#         sum_numbers += x
#     return sum_numbers
# print(sum_list([16,9,-18]))

# # Question 2
# def multiply(numbers):  
#     total = 1
#     for x in numbers:
#         total *= x  
#     return total  
# print(multiply((8, 12, 3, -1, 7)))

# # Question 3
# def smallest_num_in_list( list ):
#     min = list[ 0 ]
#     for a in list:
#         if a < min:
#             min = a
#     return min
# print(smallest_num_in_list([1, 13, -7, 0]))

# # Question 4
# def max_num_in_list( list ):
#     max = list[ 0 ]
#     for a in list:
#         if a > max:
#             max = a
#     return max
# print(max_num_in_list([1, 13, -7, 0]))

# # Question 5
# def second_largest(numbers):
#   if (len(numbers)<2):
#     return
#   if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):
#     return
#   dup_items = set()
#   uniq_items = []
#   for x in numbers:
#     if x not in dup_items:
#       uniq_items.append(x)
#       dup_items.add(x)
#   uniq_items.sort()    
#   return  uniq_items[-2]   
# print(second_largest([1,2,3,4,4]))
# print(second_largest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
# print(second_largest([2,2]))
# print(second_largest([7]))

# # Question 6
# def LargestFunc(list1, N):
# 	new_list = []
# 	for i in range(0, N):
# 		max1 = 0
# 		for j in range(len(list1)):
# 			if list1[j] > max1:
# 				max1 = list1[j]
			
# 		list1.remove(max1)
# 		new_list.append(max1)
# 	print("Largest numbers = ",new_list)

# my_list = [12, 61, 41, 85, 40, 13, 77, 65, 100]
# N = 4
# LargestFunc(my_list, N)

# # Question 7
# def even(num_list):
#    for num in num_list:
#          if num % 2 == 0:
#             print(num, end=' ')

# even([18, 10, 29, 53, 32])

# # Question 8
# def even(num_list):
#    for num in num_list:
# 	         if num % 2 != 0:
#             print(num, end=' ')

# even([18, 10, 29, 53, 32])

# # Question 9
# list1 = [[], [], 'Shahequa', [], 'Red', 'Data', [1,2], 'Blue', [], []]
# print("Original list:")
# print(list1)
# print("\nAfter deleting the empty lists from the said lists of lists")
# list2 = [x for x in list1 if x]
# print(list2)

# # Question 10
# original_list = [73, 22, 89, 23, 64]
# new_list = list(original_list)
# print(original_list)
# print(new_list)

# # Question 11
# count = ['a', 1, 'a', 4, 3, 2, 'a'].count('a')
# print(count)
