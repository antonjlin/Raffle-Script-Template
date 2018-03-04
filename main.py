import requests
import time
import threading
from utils import*
import random
import proxymanager

numEntries = 0

class Entry(threading.Thread):
	def __init__(self,):
		threading.Thread.__init__(self)

	def run(self):
		return True
		#or
		return False


for i in range(0,numEntries):
	t = Entry()
	t.start()
	time.sleep(0.5)
