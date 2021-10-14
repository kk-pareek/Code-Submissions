n = int(input("Enter your number from 1 to n: "))

# Find factorial of n

factorial = 1
for i in range(n, 0, -1):
    factorial = factorial*i
print("Factorial of n: ",factorial)

# _________________________________________________
# Find sum of all even nums from 1 to n
# as there is no mention if n is included or not
# in this code I included n in sum if n is even

even_num = []
for i in range(n):
    if (i+1)%2 ==0:
        even_num.append(i+1)

sum_even = 0
for num in even_num:
    sum_even += num

print('Sum of even numbers: ', sum_even)

# _________________________________________________
# Find sum of all the prime numbers from 1 to n
# as there is no mention if n is included or not
# in this code I included n in sum if n is even

prime_num = []

for i in range(2,n):
    if (i+1)%2 != 0 and (i+1)%3 !=0:
        prime_num.append(i+1)

sum_prime = 0
for prime in prime_num:
    sum_prime += prime

print("List of prime numbers between 1 and n: ", prime_num)
print("Sum of prime numbers between 1 and n: ", sum_prime)
