# -*- coding: utf-8 -*-
#
#  config.py
#
#  Copyright 2023
#  Autor......: Gustavo Marucci <gustavo@marucciviana.com.br>
#  Data.......: 26/09/2023
#  Descrição..: Arquivo de configuração do script
#
import os
import json
import sys

from classes.status				import Status

class Config:
	version = None
	url 	= None
	cte		= dict()
	nfe		= dict()

	def __init__(self):
		'''
		Constructor
		
		'''
		try:
			config_file = os.path.dirname(os.path.abspath(__file__))
			config_file = os.path.join(config_file, '..')
			config_file = os.path.join(config_file, "sefaz.conf")

			with open(config_file, "r", encoding='utf-8') as conf:
				data = json.loads(conf.read())

			for d in data:
				try:
					setattr(self, d, data[d])
				except:
					pass
		except:
			print(Status.invalid_conf)
			sys.exit(0)
