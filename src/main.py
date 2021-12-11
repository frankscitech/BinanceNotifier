'''
	:brief: Main code.
	:author: @frankscitech.
'''
# View Deps
import os
from getpass import getpass

# Controller Deps
import time
import keyboard
from threading import Timer
from functools import partial
from binance.client import Client

class Model:
	hot_tag=3
	warm_tag=2
	chill_tag=1
	cold_tag=0
	table={}
	def __init__(self,timestamp):
		self.timestamp=timestamp # seconds
	def conn_client(self):
		self.client=Client(self.api_key, self.api_sec)

class Controller:
	def __init__(self,model,view):
		self.model=model
		self.view=view
	def update_table(self,start):
		# Get the information from binance

		# Format info
		
		# Save info
		model.table=model.client.get_all_tickers()
		view.update(model.table)
	def run(self):
		view.clear()
		view.intromsg()
		model.api_key=view.in_apikey()
		model.api_sec=view.in_apisec()
		model.conn_client()
		interval = Interval(model.timestamp, self.update_table, args=[time.time(),])
		interval.start() 
		while True:
			try:
				time.sleep(0.1)
			except KeyboardInterrupt:
				interval.stop()
				view.byemsg()
				break

# credits @bbengfort
class Interval(object):
    def __init__(self, interval, function, args=[], kwargs={}):
        self.interval = interval
        self.function = partial(function, *args, **kwargs)
        self.running  = False 
        self._timer   = None 
    def __call__(self):
        self.running = False  # mark not running
        self.start()          # reset the timer for the next go 
        self.function()       # call the partial function 
    def start(self):
        if self.running:
            return  
        self._timer = Timer(self.interval, self)
        self._timer.start() 
        self.running = True
    def stop(self):
        if self._timer:
            self._timer.cancel() 
        self.running = False 
        self._timer  = None

class View:
	def __init__(self):
		return
	def update(self,table):
		self.refresh_header()
		for element in table:
			print(element)
	def clear(self):
		os.system('cls' if os.name == 'nt' else 'clear')
	def in_apikey(self):
		return  getpass("Enter API KEY:")
	def in_apisec(self):
		return  getpass("Enter API SECRET:")
	def intromsg(self):
		print('''
		______ _                            _   _       _   _  __ _           
		| ___ (_)                          | \ | |     | | (_)/ _(_)          
		| |_/ /_ _ __   __ _ _ __   ___ ___|  \| | ___ | |_ _| |_ _  ___ _ __ 
		| ___ \ | '_ \ / _` | '_ \ / __/ _ \ . ` |/ _ \| __| |  _| |/ _ \ '__|
		| |_/ / | | | | (_| | | | | (_|  __/ |\  | (_) | |_| | | | |  __/ |   
		\____/|_|_| |_|\__,_|_| |_|\___\___\_| \_/\___/ \__|_|_| |_|\___|_|''',end='\n')
		print("By @frankscitech")
	def refresh_header(self):
		self.clear()
		self.intromsg()
		print("press CTRL+C to stop.\n")
	def byemsg(self):
		print("\n Good Bye ...")

if __name__ == '__main__':
	timestamp=3 #seconds
	view = View()
	model = Model(timestamp)
	controller=Controller(model,view)
	controller.run()
	
