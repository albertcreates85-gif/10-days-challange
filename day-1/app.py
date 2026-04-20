Q1. Even or Odd
Write a program to check if a number is even or odd.

num = int(input('entre your number'))
if num % 2 ==0:
     print('its even')
else:
    print('its not')
    
Q2. Sum of First N Numbers 

Input: n = 5
Output: 15

tsum=0
for i in range(num+1):
    tsum += i
print(tsum)

or 

li =[]
for i in range(num+1):
    li.append(i)

print('your sum is ',sum(li))
 
Multiplication Table

Print table of a number n up to 10.

for i in range(11):
    table = i * num
    print(table)

Q4. Count Digits

Input: n = 12345
Output: 5

lenth = 0
 
while num > 0:
    num = num //10
    lenth += 1

print(lenth)

Q5. Reverse a Number

Input: 1234
Output: 4321

num = 1234
reversed_num = 0

while num > 0:
    remainder = num % 10          # Get the last digit (4)
    reversed_num = (reversed_num * 10) + remainder  # Append it
    num = num // 10               # Remove the last digit from original
    
print(reversed_num)  # Output: 4321

Q6. Palindrome Number

Input: 121 → True
Input: 123 → False

num = 121
original = num
# if not done it will be overright as while function does 
reversed_num = 0

while num > 0:
    remainder = num % 10          # Get the last digit (4)
    reversed_num = (reversed_num * 10) + remainder  # Append it
    num //= 10               # Remove the last digit from original
    
print(reversed_num)

if original == reversed_num:
    print("Palindrome")
else:
    print("Not Palindrome")

Q8. Sum of Digits

Input: 1234
Output: 10

num = 1234
total = 0

while num >0:
    total += num % 10 
    num //= 10 
    
print(total)
    

Q9. Factorial Using Loop
Input: 5 → 120

mul = 1 
num = 6

while num > 0 :
    mul = num * mul
    num -= 1
        
print(mul)

Q10. Count Even & Odd Digits
Input: 123456
Output:
    
even_count = 0
odd_count = 0
num = 12345
remainder = None

while num > 0 :
    remainder = num % 10 
    
    if remainder % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    num //= 10 
print(even_count , odd_count)

Q11. Prime Number Check
Input: 7 → Prime
Input: 8 → Not Prime

num = 5
if num <2:
    print('not a prime ')
else:
    for i in range(2,int(num * 0.5) + 1):
        if num % i == 1 :
            print('prime')
            break
        else:
            print('not prime')

Q12. Fibonacci Series (n terms)
Input: n = 5
Output: 0 1 1 2 3

n = int(input())

a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

Q13. Armstrong Number
Input: 153 → True

👉 1³ + 5³ + 3³ = 153

num = 123
final = 0
remainder = 0

while num >0:
    remainder = num % 10 
    final += remainder ** 3
    num //= 10
    
print(final)

Q14. Pattern Problem
*
**
***

for i in range(5):
        print("*" * i)

Q15. Find Second Largest Number

Input: [10, 20, 4, 45, 99]
Output: 45

arr = list(map(int, input().split()))

first = second = float('-inf')

for num in arr:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print(second)