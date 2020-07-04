from tkinter import *
import fee
root=Tk()
root.wm_title('FEE MANAGEMENT')
root.geometry('1000x500+60+50')
Label(root,text="SCHOOOOOOOL NAMMEEEEEEEEEEEEEE",font=50).place(x=300,y=10)
Label(root,text="STUDENTS DATA").place(x=350,y=70)
Button(root,text="CLICK HERE",command=fee.show1,padx=30,pady=10).place(x=450,y=60)
Label(root,text="OFFICE DATA").place(x=350,y=130)
Button(root,text="CLICK HERE",command=fee.show2,padx=30,pady=10).place(x=450,y=120)
Label(root,text="Created by:Anubhav Sharma").place(x=0,y=450)
root.mainloop()