
# # # # Python Paradigmas

# # # # This code demonstrates different programming paradigms in Python, 
# # # # including procedural, object-oriented, and functional programming.

# # # # Imperative Programming 

# # # # userValue = int(input("Enter a number: "))
# # # # userSecondValue = int(input("Enter another number: "))

# # # # if userValue > 0 or userSecondValue > 200:
# # # #     print("The number is positive.")
# # # # elif userValue == 0:
# # # #     print("The number is zero.")
# # # # else:
# # # #     print("The number is not positive.")

# # # a= ""

# # # if [] == "":
# # #     print("Welcome!") 
# # # else:
# # #     print("Goodbye!")

# # # numbers = [1, 2, 3,[4, 5, 6]]
# # # numbers1 = numbers.copy()

# # # numbers1.append(4)
# # # numbers1[3].append(7)

# # # print(numbers) 
# # # print(numbers1)

# # # Deep copy



# # import copy

# # numbers = [1, 2, 3,[4, 5, 6]]
# # numbers2 = copy.deepcopy(numbers)

# # numbers2.append(4)
# # numbers2[3].append(7)


# # print(numbers)
# # print(numbers2)

# # Procedural Programming
# # result = 0
# # def calculate_area(length, width):
# #     result = length * width
# #     return result


# # defResult =  calculate_area(5, 10)
# # print("Area of rectangle:", result)
# # print("Area of rectangle:", defResult)


# # Recrusive Function

# # def factorial(n):
# #     if n == 0:
# #         return 1
# #     else:
# #         return n * factorial(n - 1)
    
# # factorialResult = factorial(5)

# # 5 * factorial(4) * 4 *factorial(3) * 3 * factorial(2) * 2 * factorial(1) * 1

# # print("Factorial of 5:", factorialResult)

# # Anonymous Function (Lambda Function)

# # lambdaFunction = lambda x: x * 2

# # print("Lambda Function Result:", lambdaFunction(5))

# def sum(a, b = 0):
#     return a + b

# sumResult = sum(5)

# print("Sum Result:", sumResult)

# Functional Programming

numbers = [1, 2, 3, 4, 5]

# Using map to square each number in the list

squared_numbers = list(map(lambda x: x ** 2, numbers))

print("Squared Numbers:", squared_numbers)

# Using filter to get even numbers from the list

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even Numbers:", even_numbers)

# Using reduce to calculate the product of all numbers in the list

import functools

product = functools.reduce(lambda x, y: x * y, numbers)

print("Product of Numbers:", product)