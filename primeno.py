def prime(n):
	if n<= 1:
		return False
	for i in range(2,n):
		if n % i==0:
			return False

	return True

def showprime(n):
	for i in range(2,n + 1):
		if prime(i):
			print(i,end=" ")

if __name__ == '__main__':
	
	showprime(100)