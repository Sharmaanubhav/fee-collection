from tkinter import *
from tkinter import messagebox
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate,Paragraph,Table,TableStyle
from reportlab.lib import colors
def fee():
	root=Tk()
	root.wm_title('FEE SUBMISSION')
	root.geometry("700x500")
	Label(root,text="FEE SUBMISSION",font=50).place(x=200,y=0) 
	ID=Entry(root,width=30,bd=5)
	ID.place(x=200,y=50)
	CLASS=Entry(root,width=30,bd=5)
	CLASS.place(x=200,y=85)
	AdNo=Label(root,text="AdNo")
	AdNo.place(x=150,y=50)
	Class=Label(root,text="Class")
	Class.place(x=150,y=85)
	def sub():
		import webbrowser
		import sqlite3
		con=sqlite3.connect('feemanager.db')
		obj1=con.cursor()
		id=int(ID.get())
		clas=int(CLASS.get())
		ID.delete(0,END)
		CLASS.delete(0,END)
		z="hello"
		flag=0
		obj1.execute("SELECT Class FROM feerate")
		res2=obj1.fetchall()
		for i in res2:
			for j in i:
				p=j
				if(p==clas):
					break
			if(p==clas):
				break
		obj1.execute("SELECT AdNo FROM basicinfo")
		res=obj1.fetchall()
		x=0		
		for i in res:
			for j in i:
				x=j
				if(x==id):
					break
			if(x==id):
				break
		if(x==id):
			obj1.execute("SELECT Name FROM basicinfo WHERE AdNo IN ('%s')"%(id))
			res2=obj1.fetchall()
			for i in res2:
				z=i[0]
		else:
			messagebox.showwarning("INFO","NO STUDENT WITH THIS ID")
		if(p==clas):
			obj1.execute("SELECT BF,UF,SF,SEF,SG,SciF,Fine,PhEdu,Lib,Exam,Fur,Cult,mag,Icard FROM feerate WHERE Class IN ('%s')"%(clas))
			res1=obj1.fetchall()
		else:
			messagebox.showwarning("INFO","NO DATA OF THIS CLASS")
		obj1.execute("SELECT AdNo FROM feereg")
		add=obj1.fetchall()
		for i in add:
			for j in i:
				if (x==j):
					obj1.execute("SELECT RDate FROM feereg WHERE AdNo IN ('%s')"%(x))
					cd=obj1.fetchall()
					for m in cd:
						for n in m:
							datee=datetime.strptime(n,"%Y-%m-%d")
							p=datee.month
							s=datetime.date(datetime.now())
							b=datetime.strftime(s,"%m")
							q=int(p)
							w=int(b)
					break
			if (x==j and q==w):
				messagebox.showinfo("INFO","Fee allready paid")
				flag=1
				break
		if(flag==0):		
			if(x==id and p==clas):
				obj1.execute("SELECT MAX(RNo) AS x FROM feereg")
				res=obj1.fetchall()
				for i in res:
					k=i[0]
				if k is None:
					k=0
				obj1.execute("SELECT BF FROM feerate WHERE Class IN ('%s')"%(clas))
				bf_=obj1.fetchall()
				for i in bf_:
					for j in i:
						bf=j
				obj1.execute("SELECT UF FROM feerate WHERE Class IN ('%s')"%(clas))
				uf_=obj1.fetchall()
				for i in uf_:
					for j in i:
						uf=j
				obj1.execute("SELECT SF FROM feerate WHERE Class IN ('%s')"%(clas))
				sf_=obj1.fetchall()
				for i in sf_:
					for j in i:
						sf=j
				obj1.execute("SELECT SEF FROM feerate WHERE Class IN ('%s')"%(clas))
				sef_=obj1.fetchall()
				for i in sef_:
					for j in i:
						sef=j
				obj1.execute("SELECT SG FROM feerate WHERE Class IN ('%s')"%(clas))
				sg_=obj1.fetchall()
				for i in sg_:
					for j in i:
						sg=j
				obj1.execute("SELECT SciF FROM feerate WHERE Class IN ('%s')"%(clas))
				scif_=obj1.fetchall()
				for i in scif_:
					for j in i:
						scif=j
				obj1.execute("SELECT Fine FROM feerate WHERE Class IN ('%s')"%(clas))
				fine_=obj1.fetchall()
				for i in fine_:
					for j in i:
						fine=j
				obj1.execute("SELECT PhEdu FROM feerate WHERE Class IN ('%s')"%(clas))
				phedu_=obj1.fetchall()
				for i in phedu_:
					for j in i:
						phedu=j
				obj1.execute("SELECT Lib FROM feerate WHERE Class IN ('%s')"%(clas))
				lib_=obj1.fetchall()
				for i in lib_:
					for j in i:
						lib=j
				obj1.execute("SELECT Exam FROM feerate WHERE Class IN ('%s')"%(clas))
				exam_=obj1.fetchall()
				for i in exam_:
					for j in i:
						exam=j
				obj1.execute("SELECT Fur FROM feerate WHERE Class IN ('%s')"%(clas))
				fur_=obj1.fetchall()
				for i in fur_:
					for j in i:
						fur=j
				obj1.execute("SELECT Cult FROM feerate WHERE Class IN ('%s')"%(clas))
				cult_=obj1.fetchall()
				for i in cult_:
					for j in i:
						cult=j
				obj1.execute("SELECT mag FROM feerate WHERE Class IN ('%s')"%(clas))
				mag_=obj1.fetchall()
				for i in mag_:
					for j in i:
						mag1=j
				obj1.execute("SELECT Icard FROM feerate WHERE Class IN ('%s')"%(clas))
				icard_=obj1.fetchall()
				for i in icard_:
					for j in i:
						icard=j
				total=bf+uf+sf+sg+scif+fine+phedu+lib+exam+fur+cult+mag1+icard
				l=datetime.date(datetime.now())
				obj1.execute("INSERT INTO feereg VALUES ('%d','%s','%d','%d','%s','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d')"%(k+1,l,x,p,z,bf,uf,sf,sef,sg,scif,fine,phedu,lib,exam,fur,cult,mag1,icard,total))
				con.commit()
				tr=[["ReceiptNo        :"],["Date        :"],["AdNo        :"],["Class        :"],["Name        :"],["BF        :"],["UF        :"],["SF        :"],["SEF        :"],["SG        :"],["SciF        :"],["Fine        :"],["PhEdu        :"],["Lib        :"],["Exam        :"],["Fur        :"],["Cult        :"],["mag        :"],["Icard        :"],["Total        :"]]
				obj1.execute("SELECT * FROM feereg WHERE AdNo IN ('%s')"%(id))
				sh=obj1.fetchall()
				con.close()
				pdf=SimpleDocTemplate("reciept01.pdf",title="receipt")
				flow_obj=[]
				q=0
				for row in sh:
					for data in row:	
						tr[q].append(row[q])
						q+=1
				table=Table(tr)
				flow_obj.append(table)
				pdf.build(flow_obj)
				webbrowser.open_new(r'reciept01.pdf')
	subm=Button(root,text="Submit",command=sub)
	subm.place(x=250,y=120)
	root.mainloop()
