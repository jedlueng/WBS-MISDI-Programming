"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""


#Jedlueng 5 November 2021 

ip = int(input('Please input prime number'))
prime = []

for num in range(1, ip):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           prime.append(num)

print('This is prime list')
print(prime)

'''Output :
I am running a program
('10001 prime number is', 104759)
Done!
'''