from time import sleep, localtime, strftime
import os 
from kurs import kurs_open
from flask import Flask
import time
from livereload import Server

app = Flask(__name__)

@app.route('/')
def index():
	with open("timer.py" , "r") as c_t:
		file_time=c_t.read()
		
	#times=strftime("%d-%m-%Y %H:%M", localtime())
	
	#cur_date =  .today().strftime('%d-%m-%Y')
	USD, EUR, CNY = kurs_open()	
	kurs_end = (f' Курсы обмена валют: {USD}, {EUR}, {CNY}')
	return f"""
	<html>
		<head>
			<title>Курсы обмена</title>
		</head>
		<body>	
		<h1> </h1>
		<p>	</p>
		<p>	</p>
		<div align="center">
			<hr size=7px width=1800px color=white>
			 <b><p style="font-size: 60px;><span style="color:black;">{file_time} &emsp;&emsp;&emsp;</span><font color="red"> КУРСЫ ОБМЕНА ВАЛЮТ</p></font></b> 
			<hr size=7px width=1800px color="#FF0000">
			<hr size=7px width=1800px color=white>
			<b><p style="font-size: 45px;><span style="color:black;">&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;ПОКУПКА</span><span style="color:black;">&emsp;&emsp;&emsp;&emsp;ПРОДАЖА&emsp; </span></p></b>
			<hr size=7px width=1800px color=white>
			<hr size=7px width=1800px color=white>
			
			<div style="font-size: 120px;">
			<b><p style="line-height: 48px;">$ &emsp;&emsp; <font color="red">{USD}</font></p></b>
			<b><p style="line-height: 48px;">€ &emsp;&emsp; <font color="red">{EUR}</font></p></b>			
			<b><p style="line-height: 48px;">¥ &emsp;&emsp; <font color="red">{CNY}</font></p></b> 
	
			</div>
			</div>			
		</body>
		</html>"""

if __name__ == "__main__":
	
	server = Server(app.wsgi_app)
	server.serve(host='0.0.0.0', port='5501')
	app.run(host='0.0.0.0', port='5500', debug=True)
	









