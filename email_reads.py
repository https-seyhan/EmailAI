import pandas as pd
import os
import psutil
import datetime
import json
import eml_parser

class readFiles:
	name= 'read email files'
	print('Read Files')


	def __init__(self):
		self.read_eml_file()


	def read_eml_file(self):
		with open('sample_file.eml', 'rb') as email:
  			raw_email = email.read()
		ep = eml_parser.EmlParser()
		parsed_eml = ep.decode_email_bytes(raw_email)
		#print(json.dumps(parsed_eml))
		self.get_information(json.dumps(parsed_eml, indent=4, sort_keys=True, default=str))
		
	
	def get_information(self, text):
		#print('Email Text ', text)
		print(type(text))
		json_data = json.loads(text)
		
		
		#for item in json_data:
		#	print( "Item ", item)
		
		#print(json_data['body'])
		#print(json_data['header'])
		self.get_header(json_data)
		

	def get_header(self, json_object):
		print('Date ', json_object['header']['date'])
		print('From ', json_object['header']['from'])
		
		for item in json_object['header']:
			print(item)
			#print(item['date'])



#files = readFiles()
readFiles()
#files
