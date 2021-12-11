#!/usr/bin/env python3

#Python libraries
import requests
import json
import re
from random import randint
import os.path
import time
import smtplib
from email.mime.text import MIMEText

#Configure your personnel email account and the receiver account
#From
email = '' #To complete
password = '' #To complete

#To
receiver = '' #To complete

#Choose a working directory path
pathDirectory = os.path.dirname(os.path.realpath(__file__))

#Color setup
class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

def printAscii():
	"""
	ASCII Art
	"""
	print("""
______         _      ___  ___            _ _             
| ___ \       | |     |  \/  |           (_) |            
| |_/ /_ _ ___| |_ ___| .  . | ___  _ __  _| |_ ___  _ __ 
|  __/ _` / __| __/ _ \ |\/| |/ _ \| '_ \| | __/ _ \| '__|
| | | (_| \__ \ ||  __/ |  | | (_) | | | | | || (_) | |   
\_|  \__,_|___/\__\___\_|  |_/\___/|_| |_|_|\__\___/|_|   
                                                                                                                 												  
	""")

def checkPastebinAPIStatut():
	"""
	This function check Pastebin API statut access : allowed / not allowed
	"""
	requestPastebinAPI = requests.get('https://scrape.pastebin.com/api_scraping.php')
	if requestPastebinAPI.status_code == 200:
		print(f"IP Access  : Your IP address is {bcolors.OKGREEN}allowed{bcolors.ENDC} to connect to the Pastebin.com API")
	else:
		print(f"IP Access  : Your IP address is {bcolors.FAIL}not allowed{bcolors.ENDC} to connect to the Pastebin.com API")
		print("Please visit this webpage: https://pastebin.com/doc_scraping_api ")
		print("Then, enter the IP address of your machine in section: 'Your Account & Whitelisted IP'")
		exit()

def pastebinRequest():
	#Create daily directory
	todayDate = time.strftime("%d-%m-%y")
	directory = todayDate 
	if not os.path.exists(directory):
   		os.makedirs(directory)
	directory = pathDirectory + "/" + todayDate 

	#Pastebin request
	jsonResponse = requests.get("https://scrape.pastebin.com/api_scraping.php").json()
	for element in jsonResponse:
		scrape_url = element["scrape_url"]
		key = element["key"] 
		request = requests.get(scrape_url)
		download = request.text
		filename = (str(key)+".txt")
		if os.path.isfile(filename) is True:
			pass
		else:
			savepath = directory + "/"
			savedPastePath = os.path.join(savepath, filename)
			print(savedPastePath)
			with open(savedPastePath, "w") as savedPasteFile:
				savedPasteFile.write(download)
			
			#Wordlist check
			with open("wordlist.txt", "r") as fd:
			    lines = fd.read().splitlines()
			
			with open(savedPastePath, "r") as readPaste:
				readfile = readPaste.read()
			
			#Sending Email alert if match			
			for line in lines:
				if line in readfile: 
					subject = 'PASTEBIN ALERT'
					pastebinURL = re.findall("/([A-Za-z0-9]{8}).txt", str(savedPastePath))
					textMessage = "This is an automatic email alert.\n We actually monitoring Pastebin and we have found a word in you wordlist (" + str(line) + ").\n You can visit the Pastebin webpage here: https://pastebin.com/" + str(''.join(pastebinURL))
					message = MIMEText(textMessage)
					message['From'] = email
					message['To'] = receiver
					message['Subject'] = subject
					try:
					    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
					    server.ehlo()
					    server.login(email, password )
					    server.sendmail(email, receiver, message.as_string())
					    server.close()

					    print('Email sent!')
					except Exception as e:
					    print(e)
					    print('Something went wrong...')

	print("Sleeping time between 60-100 seconds")
	time.sleep(randint(60,100))

# Entry point of the script
def main():
	printAscii()
	checkPastebinAPIStatut()
	pastebinRequest()
	while True:
		pastebinRequest()

if __name__ == '__main__':
	main()
