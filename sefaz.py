#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  sefaz.py
#
#  Copyright 2023
#  Autor......: Gustavo Marucci <gustavo@marucciviana.com.br>
#  Data.......: 26/09/2023
#  Descrição..: Retorna o output para o Zabbix mostrar na tela o status do Sefaz CTE e do NFe
#
import sys

from bs4					import BeautifulSoup as bs

from classes.config			import Config
from classes.http			import HTTP
from classes.varglobal		import Global
from classes.status			import Status

class Sefaz(object):

	@staticmethod
	def parseArguments(argv: list):
		'''
		parseArguments
		Verifica se os argumentos passados para esse script são válidos

		# ARG 1: Tipo (CTE|NFE)
		# ARG 2: Autorizador Sefaz (MT|MS|MG|PR|RS|SP|SVRS|SVSP)
		# ARG 3: Disponibilidade

		Os autorizadores e os serviços disponiveis estão configurados no arquivo sefaz.conf

		'''

		# Pelo menos 3 argumentos mandatórios
		if len(argv) > 0 and len(argv) < 4:
			print(Status.error)
			sys.exit(0)

		# Checa os argumentos de acordo com o tipo
		if argv[1].lower() == "cte":
			# Autorizadores
			if argv[2].upper() not in Global.config.cte['autorizadores']:
				print(Status.error)
				sys.exit(0)
			
			# Disponibilidade
			if argv[3].upper() not in Global.config.cte['disponibilidade']:
				print(Status.error)
				sys.exit(0)


		elif argv[1].lower() == "nfe":
			# Autorizadores
			if argv[2].upper() not in Global.config.nfe['autorizadores']:
				print(Status.error)
				sys.exit(0)
			
			# Disponibilidade
			if argv[3].upper() not in Global.config.nfe['disponibilidade']:
				print(Status.error)
				sys.exit(0)

		else:
			# Tipo não suportado
			print(Status.error)
			sys.exit(0)

		return argv[1], argv[2], argv[3], getattr(Global.config, argv[1].lower())['table']
	

	@staticmethod
	def checkAvailability(type: str, authorizer: str, availability: str, table: str):
		'''
		checkAvailability
		Checa no portal a disponibilidade do serviço de acordo com o tipo, autorizador e disponibilidade

		'''
		# Config
		config = getattr(Global.config, type)

		# Extrair a url correspondente da configuracao
		http 	= HTTP()
		try:
			url =	getattr(Global.config, type)['url']
		
		except:
			print(Status.error)
			sys.exit(0)

		# Fazer a chamada no portal do Sefaz
		response = http.get(url)

		# Scraper library
		try:
			scrapper 	= bs(response, "html.parser")
			table 		= scrapper.find('table', class_= table )
			header		= table.find_all('th')
			rows		= table.find_all('tr')
			if not table:
				print(Status.no_data)
				sys.exit(0)

		except:
			print(Status.error)
			sys.exit(0)

		# Procura a linha correspondente ao autorizador
		authIndex = None
		for index, row in enumerate(rows):
			cell = row.find_all('td')
			try:
				if cell[0].text.upper() == authorizer.upper():
					authIndex = index
					break

			except:
				pass
		
		# Procura a coluna correspondente a disponibilidade
		availIndex = None
		for index, col in enumerate(header):
			try:
				if col.text.upper() == config['disponibilidade'][availability.upper()].upper():
					availIndex = index
					break

			except:
				pass
		
		# Sem dados
		if not authIndex:
			print(Status.no_data)
			sys.exit(0)
		
		if not availIndex:
			print(Status.no_data)
			sys.exit(0)

		# Extrair a bolinha
		cellsRow 	= rows[authIndex].find_all('td')
		cell 		= cellsRow[availIndex]
		ball 		= cell.find('img')
		if not ball:
			print(Status.no_data)
			sys.exit(0)

		print(Status.balls[ball['src'].lower()])
		return
		
		

if __name__ == "__main__":
	# Carrega as configs
	Global.config = Config()

	# Verifica os argumentos
	type, authorizers, avalability, table = Sefaz.parseArguments(sys.argv)

	# Checa disponibilidade
	Sefaz.checkAvailability(type, authorizers, avalability, table)
