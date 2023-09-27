# -*- coding: utf-8 -*-
#
#  http.py
#
#  Copyright 2023
#  Autor......: Gustavo Marucci <gustavo@marucciviana.com.br>
#  Data.......: 26/09/2023
#  Descrição..: Acesso a HTTP
#
import  aiohttp
import  asyncio
import	socket
import 	sys
from    classes.varglobal		import Global
from 	classes.status			import Status

class HTTP:
	
	def get(self, url, headers = None):
		'''
		get
		Method that executes the asyncronous get
		
		'''
		if not url:
			print(Status.url_not_found)
			sys.exit(0)
		
		if not headers:
			response = asyncio.run(self._requestGET(url))
		else:
			response = asyncio.run(self._requestGET(url, headers))

		return response
	

	async def  _requestGET(self, url, headers = None):
		'''
		_requestGET
		Privte Method that executes the GET
		
		'''
		defaultHeaders = {
			'User-Agent': 		f'SefazScraper/{Global.config.version}'
		}

		connector = aiohttp.TCPConnector(
			verify_ssl		= False, 
			use_dns_cache 	= False,
			family			= socket.AF_INET
		)

		if not headers:
			headers = defaultHeaders

		async with aiohttp.ClientSession( 
			connector	= connector,
		) as session:
			try:
				response 		= await session.get(url, headers=headers)
				response_text 	= await response.text()
				return response_text
		
			except:
				print(Status.fail_http)
				sys.exit(0)

		



	