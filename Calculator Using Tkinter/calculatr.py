from tkinter import *

def click(event):
	global entval
	text=event.widget.cget("text")
	
	if text=="=":
		if entval.get().isdigit():
			value=int(entval.get())
		else:
			try:
				value=eval(ent.get())
			except Exception as e:
				print(e)
				value==error		
		entval.set(value)
		ent.update()

	elif text== "C":
		entval.set("")
		ent.update()


	else:
		entval.set(entval.get() + text)
		ent.update()		

	print(text)

root=Tk()
root.title("Calculator")
root.geometry("280x400")
root.minsize(280,400)
root.maxsize(280,400)
root.config(background="seashell3")
root.wm_iconbitmap("cal1.ico.ico")

entval=StringVar()
entval.set("")
ent=Entry(root,textvariable=entval,width=100,font="calibre 22 bold")
ent.pack(pady=20,padx=10,ipadx=10)

f=Frame(root,bg="lightskyblue4",borderwidth=5)


l=Button(f,text="7",font="comicsansms 20 bold",padx=2,pady=2,bg="light grey")
l.pack(side=LEFT,padx=5,pady=5)
l.bind("<Button-1> ",click)

l=Button(f,text="8",font="comicsansms 20 bold",padx=1,pady=2,bg="light grey")
l.pack(side=LEFT,padx=5,pady=5)
l.bind("<Button-1> ",click)

l=Button(f,text="9",font="comicsansms 20 bold",padx=2,pady=2,bg="light grey")
l.pack(side=LEFT,padx=5,pady=5)
l.bind("<Button-1> ",click)

l=Button(f,text="/",font="comicsansms 20 bold",padx=2,pady=2,bg="light grey")
l.pack(side=LEFT,padx=5,pady=5)
l.bind("<Button-1> ",click)


f.pack()

f=Frame(root,bg="lightskyblue4",borderwidth=5)

l=Button(f,text="4",font="comicsansms 20 bold",padx=1,pady=2,bg="light grey")
l.pack(side=LEFT,padx=5,pady=5)
l.bind("<Button-1> ",click)

l=Button(f,text="5",font="comicsansms 20 bold",padx=1,pady=2,bg="light grey")
l.pack(side=LEFT,padx=5,pady=5)
l.bind("<Button-1> ",click)

l=Button(f,text="6",font="comicsansms 20 bold",padx=1,pady=2,bg="light grey")
l.pack(side=LEFT,padx=5,pady=5)
l.bind("<Button-1> ",click)

l=Button(f,text="*",font="comicsansms 20 bold",padx=2,pady=2,bg="light grey")
l.pack(side=LEFT,padx=5,pady=5)
l.bind("<Button-1> ",click)


f.pack()

f=Frame(root,bg="lightskyblue4",borderwidth=5)


l=Button(f,text="1",font="comicsansms 20 bold",padx=2,pady=2,bg="light grey")
l.pack(side=LEFT,padx=5,pady=5)
l.bind("<Button-1> ",click)

l=Button(f,text="2",font="comicsansms 20 bold",padx=2,pady=2,bg="light grey")
l.pack(side=LEFT,padx=5,pady=5)
l.bind("<Button-1> ",click)

l=Button(f,text="3",font="comicsansms 20 bold",padx=1,pady=2,bg="light grey")
l.pack(side=LEFT,padx=5,pady=5)
l.bind("<Button-1> ",click)

l=Button(f,text="-",font="comicsansms 20 bold",padx=2,pady=2,bg="light grey")
l.pack(side=LEFT,padx=5,pady=5)
l.bind("<Button-1> ",click)

f.pack()

f=Frame(root,bg="lightskyblue4",borderwidth=5)


l=Button(f,text="C",font="comicsansms 20",padx=0,pady=2,bg="grey")
l.pack(side=LEFT,padx=5,pady=5)
l.bind("<Button-1> ",click)

l=Button(f,text="0",font="comicsansms 20 bold",padx=0,pady=2,bg="light grey")
l.pack(side=LEFT,padx=5,pady=5)
l.bind("<Button-1> ",click)

l=Button(f,text="=",font="comicsansms 20 bold",padx=1,pady=2,bg="light grey")
l.pack(side=LEFT,padx=5,pady=5)
l.bind("<Button-1> ",click)

l=Button(f,text="+",font="comicsansms 20 bold",padx=1,pady=2,bg="light grey")
l.pack(side=LEFT,padx=5,pady=5)
l.bind("<Button-1> ",click)

f.pack()

root.mainloop()