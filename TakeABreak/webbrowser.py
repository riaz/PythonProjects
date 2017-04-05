from xml.etree.ElementTree import *
from subprocess import call

class webbrowser:
	"""A simple class with a open function, that opens your default browser from the settings.xml file """

	"""
	Instructions:

	1. Get the default browser from the settings.xml file of this project
	2. Use the system command to open the link from the

	"""
	def __init__(self):
		pass

	def open(self,address):
		
	        """ start of url retrieval step  """
        	xmldoc  = parse("settings.xml").getroot()
        	browser = xmldoc.find('browser') 
        	bname   = browser.find('name') .text
		bpath   = browser.find('path').text
		bflags  = browser.find('flags').text
		bflgop  = browser.find('flgop').text
        	""" end of url retrieval step """
		
		flag = ''.join([ bflgop,  bflags])
		
		print ''.join( ["Opening",  bname])
		
		#The actual call to open the browser
		call([bpath, flag, address])
