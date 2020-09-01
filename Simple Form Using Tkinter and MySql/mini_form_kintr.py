from tkinter import *
import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='1234',database='db1')
cur=mydb.cursor()




def getval():
	tabl="INSERT INTO form(name,email,gender,college,place,pin) VALUES(%s,%s,%s,%s,%s,%s)"
	dat=(nameval.get(),emailval.get(),genderval.get(),collegeval.get(),placeval.get(),pinval.get())
	cur.execute(tabl,dat)
	mydb.commit()
	print("Working fine..")

root=Tk()
root.title("Mini Form")
root.geometry("544x350")

Label(root,text="Please Fill the Form",font="comicsansms 13 bold",pady=15).grid(row=0,column=5)

name=Label(root,text="Name :")
email=Label(root,text="E-mail :")
gender=Label(root,text="Gender :")
college=Label(root,text="college :")
place=Label(root,text="place :")
pin=Label(root,text="pin :")

name.grid(row=1,column=2,padx=2,pady=2)
email.grid(row=2,column=2,padx=2,pady=2)
gender.grid(row=3,column=2,padx=2,pady=2)
college.grid(row=4,column=2,padx=2,pady=2)
place.grid(row=5,column=2,padx=2,pady=2)
pin.grid(row=6,column=2,padx=2,pady=2)

nameval=StringVar()
emailval=StringVar()
genderval=StringVar()
collegeval=StringVar()
placeval=StringVar()
pinval=StringVar()
submitt=IntVar()


nameentry=Entry(root,textvariable=nameval)
emailentry=Entry(root,textvariable=emailval)
genderentry=Entry(root,textvariable=genderval)
collegeentry=Entry(root,textvariable=collegeval)
placeentry=Entry(root,textvariable=placeval)
pinentry=Entry(root,textvariable=pinval)

nameentry.grid(row=1,column=3)
emailentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
collegeentry.grid(row=4,column=3)
placeentry.grid(row=5,column=3)
pinentry.grid(row=6,column=3)

Checkbutton(root,text="i want to submit",variable=submitt).grid(row=7,column=3)
Button(text="sumit Form",command=getval).grid(row=8,column=3)

root.mainloop()