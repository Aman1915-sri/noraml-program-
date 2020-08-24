year= int(input("enter year here...."))


if(year%4==0 and year%100!=0 or year%400==0):
	print("its leap year!!")
else:
	print("its normal year!!")