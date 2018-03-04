from datetime import datetime
from termcolor import colored
import colorama
colorama.init()

## normal logging function - time and text
def log(text):
	print("[{}] - {}".format(stamp(), text))

## colored logging function - time and text in color
def cLog(value, color):
	text = colored(value, color)
	print('[{}] - {}'.format(stamp(), text))

def taskLog(tasknum,text):
	print("[Task {}] - [{}] - {}".format(str(tasknum),stamp(), text))

## colored logging function - time and text in color
def taskCLog(tasknum,value, color):
	text = colored(value, color)
	print('[Task {}] - [{}] - {}'.format(str(tasknum),stamp(), text))
## colored printing function - text in color
def cPrint(value, color):
	text = colored(value, color)
	print(text)

## used to get the time wrapped in square brackets
def stamp():
    timestamp = str(datetime.now().strftime("%H:%M:%S.%f")[:-3])
    return timestamp

## just fetches the time (no square brackets)
def rawStamp():
	timestamp = datetime.now().strftime("%H:%M:%S")
	return timestamp


def generateEmails(username, domain):
	email = ""
	username_length = len(username)
	combinations = pow(2, username_length - 1)
	padding = "{0:0" + str(username_length - 1) + "b}"
	for i in range(0, combinations):
		bin = padding.format(i)
		full_email = ""
		for j in range(0, username_length - 1):
			full_email += (username[j]);
			if bin[j] == "1":
				full_email += "."
		full_email += (username[j + 1])
		email = full_email + '@' + domain
		global emails
		emails.append(email)
		print(emails)