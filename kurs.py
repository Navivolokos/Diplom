import requests
from bs4 import BeautifulSoup

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

url = "http://obuchenie.forabank.ru/index.cgi?mid=4&ajob=json3002&id=788"
filename = "downloaded_kurs.html"
save_webpage(url, filename)
