from tkinter import *
from tkinter import messagebox
def dlt():
	roo=Tk()
	roo.wm_title('UPDATE FEE')
	roo.geometry("1000x500")
	import sqlite3 
	con=sqlite3.connect('feemanager.db')
	obj2=con.cursor()
	Label(roo,text="UPDATE DATA OF FEERATE",font=25,fg="blue").place(relx=0.39,rely=0)
	CLASS=Entry(roo,width=30,bd=5)
	CLASS.place(x=510,y=95)
	CLASs=Label(roo,text="CLASS TO UPDATE")
	CLASs.place(x=400,y=100)
	def sub():
		ad=int(CLASS.get())
		CLASS.delete(0,END)
		import sqlite3
		con=sqlite3.connect('feemanager.db')
		obj=con.cursor()
		obj.execute("SELECT CLASS FROM feerate")
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
			roo=Tk()
			root.wm_title('FEE UPDATION')
			roo.geometry("1000x700")
			a=Label(roo,text="ENTER DATA",fg="blue",font=20)
			a.place(x=500,y=0)
			BF=Entry(roo,width=50,bd=5)
			BF.place(x=400,y=30)
			UF=Entry(roo,width=50,bd=5)
			UF.place(x=400,y=65)
			SF=Entry(roo,width=50,bd=5)
			SF.place(x=400,y=100)
			SEF=Entry(roo,width=50,bd=5)
			SEF.place(x=400,y=135)
			SG=Entry(roo,width=50,bd=5)
			SG.place(x=400,y=170)
			SCIF=Entry(roo,width=50,bd=5)
			SCIF.place(x=400,y=205)
			FINE=Entry(roo,width=50,bd=5)
			FINE.place(x=400,y=240)
			PHEDU=Entry(roo,width=50,bd=5)
			PHEDU.place(x=400,y=275)
			LIB=Entry(roo,width=50,bd=5)
			LIB.place(x=400,y=310)
			EXAM=Entry(roo,width=50,bd=5)
			EXAM.place(x=400,y=345)
			FUR=Entry(roo,width=50,bd=5)
			FUR.place(x=400,y=380)
			CULT=Entry(roo,width=50,bd=5)
			CULT.place(x=400,y=415)
			MAG=Entry(roo,width=50,bd=5)
			MAG.place(x=400,y=450)
			ICARD=Entry(roo,width=50,bd=5)
			ICARD.place(x=400,y=485)
			B_F=Label(roo,text="BUILDING FUND")
			B_F.place(x=300,y=30)
			U_F=Label(roo,text="UNION FUND   ")
			U_F.place(x=300,y=65)
			S_F=Label(roo,text="SPORTS FUND  ")
			S_F.place(x=300,y=100)
			SE_F=Label(roo,text="SPORT EQ FUND")
			SE_F.place(x=300,y=135)
			S_G=Label(roo,text="SCOUT & GUIDE")
			S_G.place(x=300,y=170)
			SCI_F=Label(roo,text="SCIE. FUND")
			SCI_F.place(x=300,y=205)
			FIN_E=Label(roo,text="FINE FUND")
			FIN_E.place(x=300,y=240)
			PHED_U=Label(roo,text="PHYSICAL FUND")
			PHED_U.place(x=300,y=275)
			LIB_=Label(roo,text="LIB FUND")
			LIB_.place(x=300,y=310)
			EXAM_=Label(roo,text="EXAM FUND")
			EXAM_.place(x=300,y=345)
			FUR_=Label(roo,text="FURNITURE FUND")
			FUR_.place(x=300,y=380)
			CULT_=Label(roo,text="CULTURAL FUND")
			CULT_.place(x=300,y=415)
			MAG_=Label(roo,text="MAGAZINE FUND")
			MAG_.place(x=300,y=450)
			ICARD_=Label(roo,text="ICARD FUND")
			ICARD_.place(x=300,y=485)	
			def k():	
				nam=int(BF.get()),int(UF.get()),int(SF.get()),int(SEF.get()),int(SG.get()),int(SCIF.get()),int(FINE.get()),int(PHEDU.get()),int(LIB.get()),int(EXAM.get()),int(FUR.get()),int(CULT.get()),int(MAG.get()),int(ICARD.get())
				BF.delete(0,END)
				UF.delete(0,END)
				SF.delete(0,END)
				SEF.delete(0,END)
				SG.delete(0,END)
				SCIF.delete(0,END)
				FINE.delete(0,END)
				PHEDU.delete(0,END)
				LIB.delete(0,END)
				EXAM.delete(0,END)
				FUR.delete(0,END)
				CULT.delete(0,END)
				MAG.delete(0,END)
				ICARD.delete(0,END)
				obj.execute("UPDATE feerate SET BF=%d,UF=%d,SF=%d,SEF=%d,SG=%d,SciF=%d,Fine=%d,PhEdu=%d,Lib=%d,Exam=%d,Fur=%d,Cult=%d,mag=%d,Icard=%d WHERE Class IN (%d)"%(nam[0],nam[1],nam[2],nam[3],nam[4],nam[5],nam[6],nam[7],nam[8],nam[9],nam[10],nam[11],nam[12],nam[13],ad))
				con.commit()
				messagebox.showinfo("INFO","DATA UPDATED")
				con.close()
			button=Button(roo,text="UPDATE",command=k,padx=10,pady=5).place(x=500,y=550)
			roo.mainloop()
		else:
			messagebox.showinfo("INFO","NO DATA TO UPDATE")
	botton=Button(roo,text="UPDATE",command=sub,padx=10,pady=5).place(x=450,y=200,anchor=CENTER)
	roo.mainloop()