from time import localtime, strftime, sleep
import requests
from bs4 import BeautifulSoup
import os
		
filename = "downloaded_kurs.html"

def kurs_open():
	try:
		with open(filename, "r") as curs_file:
			curs_read=curs_file.read()
			data = eval(curs_read)	
			bezroot=data["root"]
			b=bezroot["item"]
	
			for i in b:
				spisok = i['data']
		
		new_spisok = spisok['currency']
		for dics in new_spisok:
			if dics['code'] == "USD":
				kurs_USD =(dics['buy'],dics["sell"])		
			if dics['code'] == "EUR":
				kurs_EUR =(dics['buy'],dics["sell"])
			if dics['code'] == "CNY":
				kurs_CNY =(dics['buy'],dics["sell"])
			
		kurs_USD= '&emsp;'.join(map(str, kurs_USD))
		kurs_EUR= '&emsp;'.join(map(str, kurs_EUR))
		kurs_CNY= '&emsp;'.join(map(str, kurs_CNY))
		return kurs_USD, kurs_EUR, kurs_CNY
		
	except:		
		kurs_USD="00.00&emsp;00.00"
		kurs_EUR="00.00&emsp;00.00"
		kurs_CNY="00.00&emsp;00.00"
		return kurs_USD, kurs_EUR, kurs_CNY

def main():	
	if __name__ == "__main__":
		main()
		
	
	
		
	
	
