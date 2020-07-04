from tkinter import *
import newstd
import submitfee
import showbasic	
import addfee
import delete
import showfeestruct
import updatefee
import submittedfee
def show1():
	root=Tk()
	root.wm_title('STUDENT DATA')
	root.geometry("1000x500")
	Label(root,text="STUDENS INFO AND FEE SUBMISSION & VIEW BASIC INFO",font=50).place(x=200,y=0)
	mybutton=Button(root,text="NEW ENTERY   ",command=newstd.enter,padx=30,pady=5)
	button2=Button(root,text="  SUBMIT FEE ",command=submitfee.fee,padx=30,pady=5)	
	button3=Button(root,text="BASIC INFO   ",command=showbasic.show,padx=30,pady=5)
	button8=Button(root,text="SUBMITTED FEE",command=submittedfee.show,padx=30,pady=5)
	mybutton.place(x=200,y=60)
	button2.place(x=600,y=60)
	button3.place(x=200,y=180)
	button8.place(x=600,y=180)
	root,mainloop()
def show2():
	root=Tk()
	root.wm_title('OFFICE USE')
	root.geometry("1000x500")
	Label(root,text="UPDATE FEE STRUCTURE OR ADD NEW FEE STRUCTURE",font=50).place(x=200,y=0)
	button5=Button(root,text="ADD FEE INFO  ",command=addfee.feestruc,padx=30,pady=5)
	button6=Button(root,text="DEL FERG&INFO ",command=delete.dlt,padx=30,pady=5)
	button7=Button(root,text="UPDATE FEERATE",command=updatefee.dlt,padx=30,pady=5)
	button4=Button(root,text="  FEE STRUCT  ",command=showfeestruct.show,padx=30,pady=5)
	button5.place(x=200,y=60)
	button6.place(x=600,y=60)
	button7.place(x=200,y=180)
	button4.place(x=600,y=180)
	root.mainloop()
