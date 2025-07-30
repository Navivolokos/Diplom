from settings import *
from time import localtime, strftime, sleep
import requests
from bs4 import BeautifulSoup
import os
import hashlib
import time

url = URL_WEB # Заменить URL на адрес нужной веб-страницы
current_hash = None
filename = "downloaded_kurs.html"

def save_webpage(url, filename):	   
	try:
		response = requests.get(url)
		response.raise_for_status()
		soup = BeautifulSoup(response.content, 'html.parser')
		with open(filename, 'w', encoding='utf-8') as f:
			f.write(soup.prettify())
		print(f"Страница успешно сохранена в {filename}")
	except requests.exceptions.RequestException as e:
		print(f"Ошибка при загрузке страницы: {e}")				
	except Exception as e:
		print(f"Ошибка при сохранении страницы: {e}")

def fetch_content(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.content, 'html.parser')
	return soup.get_text() # Получаем текст страницы для сравнения
	
while True:	
	try:
		requests.get(url)				
		print("web-site доступен")		
		print("Проверка на изменения...")
		content = fetch_content(url)
		new_hash = hashlib.sha256(content.encode('utf-8')).hexdigest()					
		if current_hash is None:
			current_hash = new_hash
			print("Мониторинг начат...")
		elif new_hash != current_hash:
			print("Обнаружены изменения!")
			current_hash = new_hash
#  добавляем сохранение страницы
			save_webpage(url, filename)			
	except requests.exceptions.ConnectionError:
		print("web-site недоступен!!!")
		time.sleep(10)		
	time.sleep(20) # Проверка каждые 20 секунд
		
def main():	
	if __name__ == "__main__":
		main()
		
	
