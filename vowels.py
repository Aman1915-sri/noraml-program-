#Write the program to print vowels and consonant letters from "gnulinux"
#Vowels variables
Vowels=[
#defining empty lists
vowles1 = []
conatants = []
#giving input
string11 = "gnulinux"
#sepearating constants from vowels
for i in string11:
	if i in Vowels:
		vowles1.append(i)
	else:
		constants.append(i)
#Printing results
print("Constants : ")
print(constants)
print("vowels : ")
print(vowles1)