num1 = int(input('Enter the first number'))
num2 = int(input('Enter the second number'))
operator = input('Enter the operator (+ or -):')

if operator == '+':
       print(f'The result is:{num1 + num2}')
elif operator == '-':
       print(f'The result is: {num1 - num2}')
else:
       print('Unknown operator. Please use + or -')

test_scores = [45, 23, 89, 78, 98, 55, 74, 87, 95, 75]
test_scores.sort()
print(test_scores)


for i in range (10, 60, 10):
    print(i)
print("And we're done!")

number = 10

while number < 61:
   print(number)
   number += 10
print ("And we're done!")
