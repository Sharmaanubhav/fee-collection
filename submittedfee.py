from reportlab.platypus import SimpleDocTemplate,Paragraph,Table,TableStyle
from reportlab.lib import colors
def show():	
	import webbrowser
	import sqlite3
	a=0
	con=sqlite3.connect('feemanager.db')
	obj=con.cursor()
	obj.execute("SELECT * FROM feereg")
	data=obj.fetchall()
	pdf=SimpleDocTemplate("submittedfee.pdf",title="submitted fee")
	flow_obj=[]
	q=0
	td=[["ReceiptNo","Date","AdNo","Class","Name","BF","UF","SF","SEF","SG","SciF","Fine","PhEdu","Lib","Exam","Fur","Cult","mag","Icard","Total"]]
	for row in data:
		k=[row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]]
		td.append(k)
	table=Table(td)	
	#ts=TableStyle([("GRID",(0,0),(-1,-1),3,colors.black),
	#			("BACKGROUND",(0,0),(-1,0),colors.white)])
	#table.setStyle(ts)
	flow_obj.append(table)
	pdf.build(flow_obj)
	webbrowser.open_new(r'submitteffee.pdf')