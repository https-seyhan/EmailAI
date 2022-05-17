import pandas as pd
import os
import psutil
import datetime
import json
import eml_parser
#read email context
class readFiles:
	name= 'read email files'
	print('Read Files')
	def __init__(self):
		
		#print(psutil.virtual_memory())
		print('Virtual Memory Percent ', psutil.virtual_memory().percent)
		print(psutil)
		self.read_eml_file()


	def read_eml_file(self):
		with open('sample_file.eml', 'rb') as email:
  			raw_email = email.read()
		ep = eml_parser.EmlParser()
		parsed_eml = ep.decode_email_bytes(raw_email)
		print(json.dumps(parsed_eml))



#files = readFiles()
readFiles()
#files
