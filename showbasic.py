from reportlab.platypus import SimpleDocTemplate,Paragraph,Table,TableStyle
from reportlab.lib import colors
def show():	
	import webbrowser
	import sqlite3
	a=0
	con=sqlite3.connect('feemanager.db')
	obj=con.cursor()
	obj.execute("SELECT * FROM basicinfo")
	sh=obj.fetchall()
	pdf=SimpleDocTemplate("basicinfo.pdf",title="basicinfo")
	flow_obj=[]
	td=[["AdNo","NAME","FNAME","MNAME","ADDRESS","DOA"]]
	for row in sh:
		data=[row[0],row[1],row[2],row[3],row[4],row[5]]
		td.append(data)
	table=Table(td)
	ts=TableStyle([("GRID",(0,0),(-1,-1),3,colors.black),
               ("BACKGROUND",(0,0),(-1,0),colors.white)])
	table.setStyle(ts)
	flow_obj.append(table)
	pdf.build(flow_obj)
	webbrowser.open_new(r'basicinfo.pdf')
