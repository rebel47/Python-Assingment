### Problem 1: Stuttering Function

def stutter(word):
    stuttered_word = f"{word[:2]}... {word[:2]}... {word}?"
    return stuttered_word

# Test examples
print(stutter('incredible'))  # Output: 'in... in... incredible?'
print(stutter('enthusiastic'))  # Output: 'en... en... enthusiastic?'
print(stutter('outstanding'))  # Output: 'ou... ou... outstanding?'


### Problem 2: Convert Radians to Degrees

import math

def radians_to_degrees(radians):
    degrees = radians * (180 / math.pi)
    return round(degrees, 1)

# Test example
print(radians_to_degrees(1))  # Output: 57.3
print(radians_to_degrees(math.pi))  # Output: 180.0


### Problem 3: Curzon Number

def is_curzon_number(num):
    power_part = 2**num + 1
    multiply_part = 2*num + 1
    return power_part % multiply_part == 0

# Test examples
print(is_curzon_number(5))  # Output: True
print(is_curzon_number(10))  # Output: False
print(is_curzon_number(14))  # Output: True


### Problem 4: Area of a Hexagon

import math

def area_of_hexagon(side_length):
    area = (3 * math.sqrt(3) / 2) * side_length**2
    return round(area, 2)

# Test examples
print(area_of_hexagon(1))  # Output: 2.6
print(area_of_hexagon(2))  # Output: 10.39
print(area_of_hexagon(3))  # Output: 23.38

### Problem 5: Decimal to Binary Conversion

def decimal_to_binary(decimal_str):
    decimal_number = int(decimal_str)
    binary_number = bin(decimal_number)[2:]  # Remove the '0b' prefix
    return binary_number

# Test examples
print(decimal_to_binary('10'))  # Output: '1010'
print(decimal_to_binary('255'))  # Output: '11111111'
print(decimal_to_binary('128'))  # Output: '10000000'


