from tkinter import *
from datetime import datetime
from tkinter import messagebox
def enter():
	root=Tk()
	root.wm_title('NEW STUDENT')
	root.geometry("1000x500")
	Label(root,text="ENTER DATA FOR NEW STUDENT",font=30).place(x=400,y=0)
	Name=Entry(root,width=50,bd=5)
	Name.place(x=400,y=50)
	FName=Entry(root,width=50,bd=5)
	FName.place(x=400,y=100)
	MName=Entry(root,width=50,bd=5)
	MName.place(x=400,y=150)
	Address=Entry(root,width=50,bd=5)
	Address.place(x=400,y=200)
	Nam_e=Label(root,text="NAME")
	Nam_e.place(x=350,y=50)
	F_Name=Label(root,text="FNAME")
	F_Name.place(x=350,y=100)
	M_Name=Label(root,text="MNAME")
	M_Name.place(x=350,y=150)
	A_ddress=Label(root,text="Address")
	A_ddress.place(x=350,y=200)
	def sub():
		import sqlite3
		con=sqlite3.connect('feemanager.db')
		obj=con.cursor()
		obj2=con.cursor()
		nam=Name.get()
		fnam=FName.get()
		mnam=MName.get()
		dd=Address.get()
		y=datetime.date(datetime.now())
		obj2.execute("SELECT MAX(AdNo) AS x FROM basicinfo")	
		res=obj2.fetchall()
		for i in res:
			x=i[0]
		if x is None:
			x=0
		obj.execute("INSERT INTO basicinfo VALUES ('%d','%s','%s','%s','%s','%s')"%(x+1,nam,fnam,mnam,dd,y))
		con.commit()
		con.close()
		Name.delete(0,END)
		FName.delete(0,END)
		MName.delete(0,END)
		Address.delete(0,END)
		c="Your AdNo is :"
		d=x+1
		e=c+str(d)
		messagebox.showinfo("ADNO",e)
	subm=Button(root,text="Submit",command=sub)
	subm.place(x=400,y=250)	
	root.mainloop()