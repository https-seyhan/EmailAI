import pandas as pd
import os
import psutil
import datetime
import json
import eml_parser

class readFiles:
	name= 'read email files'
	email_details = []

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
		#print(type(text))
		json_data = json.loads(text)
	
		#print(json_data['body'])
		#print(json_data['header'])
		self.get_header(json_data)

	def get_header(self, json_object):
		#print('Date ', json_object['header']['date'], '\n')
		#print('From ', json_object['header']['from'], '\n')
		#print('Received ', json_object['header']['received'], '\n')
		#print('Received Domain', json_object['header']['received_domain'], '\n')
		#print('Received Email', json_object['header']['received_email'], '\n')
		#print('Received Foremail', json_object['header']['received_foremail'], '\n')
		#print('Received IP', json_object['header']['received_ip'], '\n')
		#print('Subject ', json_object['header']['subject'], '\n')
		#print('To ', json_object['header']['to'], '\n')
	
		for item in json_object['header']:
			#print(item)
			#print(item['date'])
			if item == 'received':
				print('Received called')
				#print(len(json_object['header']['received']))
				
				for element in range(len(json_object['header']['received'])):
					print('Received elements ', json_object['header']['received'][element])
					elements = list(json_object['header']['received'][element].items())
					readFiles.email_details.append(elements)



#files = readFiles()
readFiles()
#files
