'''
rows =5
num = rows
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(num, end=' ')
    print("\r")
''' 

def pattern(n):  
	for i in range(n,-1, -1):  
		for j in range(0, i+1): 
			print("* ",end="") 
		print("\r") 
if __name__ == '__main__':
	n = 5
	pattern(n) 
