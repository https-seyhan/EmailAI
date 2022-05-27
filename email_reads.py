import pandas as pd
import os
import psutil
import datetime
import json
import eml_parser

os.chdir('/hAU
ome/saul/kaggle')

class readFiles:
	name= 'read email files'
	email_details = []
	def __init__(self):
		self.email_context = [['', '','', '', '', '']]
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
				#print('Received called')
				#print(len(json_object['header']['received']))
			
				for element in range(len(json_object['header']['received'])):
					#print('Received elements ', json_object['header']['received'][element])
					elements = list(json_object['header']['received'][element].items())
					readFiles.email_details.append(elements)
		#print ('List ', readFiles.email_details[0][0])
		
		for list_recurse in range(len(readFiles.email_details)):
			for list_element in range(len(readFiles.email_details[list_recurse])):
				print('Tuple Size ', len(readFiles.email_details[list_recurse][list_element]))
				tuple_element = 0
				print('List Element Size ', list_element)
				print('List ', readFiles.email_details[list_recurse][list_element])
				print('Type ', type(readFiles.email_details[list_recurse][list_element]))
				while tuple_element < list_element:
					print('tuple_element ', tuple_element)
					print(readFiles.email_details[list_recurse][list_element][tuple_element])
					tuple_element += 1
					




#files = readFiles()
readFiles()
#files
