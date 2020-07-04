from reportlab.platypus import SimpleDocTemplate,Paragraph,Table,TableStyle
from reportlab.lib import colors
def show():	
	import webbrowser
	import sqlite3
	a=0
	con=sqlite3.connect('feemanager.db')
	obj=con.cursor()
	obj.execute("SELECT * FROM feerate")
	sh=obj.fetchall()
	pdf=SimpleDocTemplate("feerate.pdf",title="feerate")
	flow_obj=[]
	td=[["Class","BF","UF","SF","SEF","SG","SciF","Fine","PhEdu","Lib","Exam","Fur","Cult","mag","Icard"]]
	for row in sh:
		data=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14])
		td.append(data)
	table=Table(td)
	ts=TableStyle([("GRID",(0,0),(-1,-1),3,colors.black),
               ("BACKGROUND",(0,0),(-1,0),colors.white)])
	table.setStyle(ts)
	flow_obj.append(table)
	pdf.build(flow_obj)	
	webbrowser.open_new(r'feerate.pdf')
	