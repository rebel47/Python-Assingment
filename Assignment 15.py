# # Question 1
# def divisible_by_5_and_7(n):
#     for i in range(n+1):
#         if i % 5 == 0 and i % 7 == 0:
#             yield i
# n = int(input("Enter a value for n: "))
# divisible_nums = divisible_by_5_and_7(n)
# print(", ".join(str(num) for num in divisible_nums))

# # Question 2
# def even_numbers(n):
#     for i in range(n+1):
#         if i % 2 == 0:
#             yield i

# n = int(input("Enter a value for n: "))
# even_nums = even_numbers(n)
# print(", ".join(str(num) for num in even_nums))

# # Question 3
# n = int(input("Enter a value for n: "))
# fib_sequence = [0, 1] + [fib_sequence[i-1] + fib_sequence[i-2] for i in range(2, n+1)]
# print(", ".join(str(num) for num in fib_sequence))

# # Question 4
# def extract_username(email):
#     username, domain = email.split("@")

#     return username

# email = "ayazalam@inueron.ai"
# username = extract_username(email)
# print(username)

# # Question 5
# class Shape:
#     def area(self):
#         print("The area of the shape is 0 by default.")

# class Square(Shape):
#     def __init__(self, length):
#         self.length = length
    
#     def area(self):
#         area = self.length ** 2
#         print(f"The area of the square is {area}.")

# s = Shape()
# s.area()

# sq = Square(5)
# sq.area()

from ast import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        nums_sorted = sorted(nums)
        n = len(nums_sorted)
        low_score = abs(nums_sorted[0] - nums_sorted[2])
        high_score = abs(nums_sorted[n-3] - nums_sorted[n-1])
        score1 = low_score + high_score
        low_score = abs(nums_sorted[n-4] - nums_sorted[n-2])
        high_score = abs(nums_sorted[0] - nums_sorted[2])
        score2 = low_score + high_score
        low_score = abs(nums_sorted[1] - nums_sorted[n-1])
        high_score = abs(nums_sorted[0] - nums_sorted[n-3])
        score3 = low_score + high_score

        return min(score1, score2, score3)
    

def handle_queries(nums1, nums2, queries):
    result = []
    
    for query in queries:
        q_type, l, r = query
        
        if q_type == 1:
            for i in range(l, r+1):
                nums1[i] = 1 - nums1[i]
                
        elif q_type == 2:
            for i in range(len(nums1)):
                nums2[i] += nums1[i] * l
        
        else:
            result.append(sum(nums2))
            
    return result






        





nums = [1,4,7,8,5]
ab = Solution()
a = ab.minDifference(nums)
print(a)