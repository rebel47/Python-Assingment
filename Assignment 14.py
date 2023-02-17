# Question 1
class DivisibleBySeven:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        for i in range(self.n+1):
            if i % 7 == 0:
                yield i
divisible_by_seven = DivisibleBySeven(50)
for num in divisible_by_seven:
    print(num)

# Question 2
from collections import defaultdict

input_string = input("Enter a string: ")
words = input_string.split()
word_freq = defaultdict(int)
for word in words:
    word_freq[word] += 1

sorted_word_freq = dict(sorted(word_freq.items()))
for word, freq in sorted_word_freq.items():
    print(f"{word}: {freq}")


# Question 3
class Person:
    def getGender(self):
        pass

class Male(Person):
    def getGender(self):
        print("Male")

class Female(Person):
    def getGender(self):
        print("Female")
person1 = Male()
person1.getGender() 

person2 = Female()
person2.getGender() 

# Question 4
subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]

for subject in subjects:
    for verb in verbs:
        for obj in objects:
            print(f"{subject} {verb} {obj}.")

# Question 5
import gzip

input_string = "hello world!hello world!hello world!hello world!"
compressed_data = gzip.compress(bytes(input_string, 'utf-8'))
print(f"Compressed size: {len(compressed_data)} bytes")

decompressed_data = gzip.decompress(compressed_data)

output_string = str(decompressed_data, 'utf-8')
print(f"Original string: {input_string}")
print(f"Decompressed string: {output_string}")


# Question 6
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
arr = [2, 4, 6, 8, 10, 12]
target = 8
index = binary_search(arr, target)

if index != -1:
    print(f"Found {target} at index {index}")
else:
    print(f"{target} not found in the list")
