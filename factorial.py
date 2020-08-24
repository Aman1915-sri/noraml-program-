num = int(input("enter a number.."))
factorial =1
if num<0:
	print("its not a factorial")
elif num ==0:
	print("factorial of 0 is 1")
else:
	for i in range(1,num+1):
		factorial=factorial*1
	print("factorial of",num,"is",factorial)