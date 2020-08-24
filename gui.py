from tkinter import*   
top=Tk()
top.title("AMAN")
top.geometry("300x200+10+20")
'''
lbl=Label(top,text="countries...")
#lbl.pack()
listbox=Listbox(top)
listbox.insert(1,"india")
lbl.pack()
listbox.pack()
'''
'''
name = Label(top, text = "Name").place(x = 30,y = 50)  
  
email = Label(top, text = "Email").place(x = 30, y = 90)  
  
password = Label(top, text = "Password").place(x = 30, y = 130)

e1 = Entry(top).place(x = 80, y = 50)  
  
  
e2 = Entry(top).place(x = 80, y = 90)  
  
  
e3 = Entry(top).place(x = 95, y = 130)
checkvar1=IntVar()
checkb=Checkbutton(top,text="python",variable=checkvar1,onvalue=1,offvalue=0,height=2,width=10)
checkb.pack()
'''
def messagebox():
	print("THANK YOU","Registration Successful")

name = Label(top, text = "Name").place(x = 30,y = 50)  
  
email = Label(top, text = "Email").place(x = 30, y = 90)  
  
password = Label(top, text = "Password").place(x = 30, y = 130)


e1 = Entry(top).place(x = 80, y = 50)  
  
  
e2 = Entry(top).place(x = 80, y = 90)  
  
  
e3 = Entry(top).place(x = 95, y = 130)
checkvar1=IntVar()
checkb=Checkbutton(top,text="python",variable=checkvar1,onvalue=1,offvalue=0,height=2,width=10)
checkb.pack()
'''
if __name__ == '__main__':
	messagebox()
'''    
b=Button(top,text="SUBMIT",command=messagebox,fg="red",bg="yellow",pady=10)

b.pack(side=BOTTOM)
top.mainloop()
