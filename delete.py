from tkinter import *
from tkinter import messagebox
def dlt():
	root=Tk()
	root.wm_title('DELETE DATA')
	import sqlite3 
	con=sqlite3.connect('feemanager.db')
	obj2=con.cursor()
	root.geometry("1000x500")
	Label(root,text="DELETE DATA FROM BASIC INFO AND FEE REG",font=20).place(x=350,y=0)
	AD=Entry(root,width=40,bd=5)
	AD.place(x=450,y=100)
	ad_=Label(root,text="Addmissin NO")
	ad_.place(x=350,y=100)
	def sub():
		ad=int(AD.get())
		AD.delete(0,END)
		import sqlite3
		con=sqlite3.connect('feemanager.db')
		obj=con.cursor()
		obj.execute("SELECT AdNo FROM basicinfo")
		f=obj.fetchall()
		k=0
		for i in f:
			for j in i:
				k=j
				if(k==ad):
					break
			if(k==ad):
				break
			else:
				k=0
		if(ad==k):		
			obj.execute("DELETE FROM basicinfo WHERE AdNo IN (%d)"%(ad))
			con.commit()
			obj.execute("DELETE FROM feereg WHERE AdNo IN (%d)"%(ad))
			con.commit()
			messagebox.showinfo("INFO","DATA DELETED")
			con.close()
		else:
			messagebox.showinfo("INFO","NO DATA TO DEL")
	botton=Button(root,text="DELETE",command=sub,padx=10,pady=5).place(x=430,y=140)
	root.mainloop()