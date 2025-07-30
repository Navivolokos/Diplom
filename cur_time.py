from time import sleep, localtime, strftime
import os 

def main():
	while True:
		os.system('cls')
		with open("timer.py", 'w', encoding='utf-8') as f:
			times=strftime("%d-%m-%Y %H:%M", localtime())
			f.write(times)
		sleep(60)
if __name__ == "__main__":
	main()
	
	
