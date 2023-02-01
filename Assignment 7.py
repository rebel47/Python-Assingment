# Question 1
arr = [1,2,3,4,5]
print(sum(arr))
# We also find that using loop
sum = 0
for i in arr:
    sum+=i
print(sum)

# Question 2
arr = [11,2,3,4,51,9]
print(max(arr))


# Question 3
def rotate_array1(arry, K, E):  
    temp_1 = []  
    J = 0  
    while (J < E):  
        temp_1.append(arry[J])  
        J = J + 1  
    J = 0  
    while (E < K):  
        arry[J] = arry[E]  
        J = J + 1  
        E = E + 1  
    arry[:] = arry[: J] + temp_1  
    return arry  
   
   
# Driver function to test above function  
arry = [1, 3, 5, 7, 9, 11, 13, 15]  
num = int(input('Enter the number of elements to be rotated: '))
print (f"Array after Rotation by 4 elements is: {rotate_array1(arry, len(arry), num)}", end = ' ')   


# Question 4
arr = [1,2,3,4,5,6,7,8,9,10]
split1 = arr[0:int(len(arr)/2)]
split2 = arr[int(len(arr)/2):]
new_arr = split2 + split1
print(new_arr)

# Question 5
def isMonotonic(A):
	x, y = [], []
	x.extend(A)
	y.extend(A)
	x.sort()
	y.sort(reverse=True)
	if(x == A or y == A):
		return True
	return False

A = [6, 5, 4, 4]
print(isMonotonic(A))
