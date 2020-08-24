#Write the program to print vowels and consonant letters from "gnulinux"
#Vowels variables
vowels=["a","e","i","o","u"]
#defining empty lists
vowles1 = []
constants = []
#giving input
input1 = "gnulinux"
#sepearating constants from vowels
def Vowels(string11):
	for i in string11:
		if i in vowels:
			vowles1.append(i)
		else:
			 constants.append(i)
#caling funtion
Vowels(input1)
#Printing results
print("Constants : ")
print(constants)
print("vowels : ")
print(vowles1)
