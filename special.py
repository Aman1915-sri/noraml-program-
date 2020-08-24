special=["@","-","&"]
word="gnu-linux is rule the world now"
kj=[]
for i in word:
	if i in special:
		pass
	else:
		kj.append(i)
print("".join(kj))