'''
i = 0
while(i<=10):
    print(i)
    i += 1

lst = [i for i in zip(*[iter(range(1,101))]*10)]

for i in lst:
    for j in i:
        print(j, end=" ")
    print()



 def solution_01(n):
    index = 0
    row = ''
    while index <=n:
        index+=1
        row += ' '+str(index) 
        if index%10 == 0:
            print row
            row = ''
if __name__ == '__main__':
	('
	solution_01')
'''

# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1