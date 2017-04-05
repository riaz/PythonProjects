from   webbrowser import *
import time

""" From the file webbrowser import * """

if __name__ == '__main__':
	print "==== Initializing Take-A-Break Program ===="
	
	while True:
		time.sleep(2*60*60)
		address = "https://www.youtube.com/watch?v=EQXzW61ozzI"
		x = webbrowser()
		x.open(address)
	
	
	
