# -*- coding: utf-8 -*-
#
#  status.py
#
#  Copyright 2023
#  Autor......: Gustavo Marucci <gustavo@marucciviana.com.br>
#  Data.......: 26/09/2023
#  Descrição..: Lista de retorno
#

class Status(object):
	'''
	Status
	Objeto de retorno para o Zabbix
	O Zabbix espera o retorno com um número inteiro
		
	'''
	offline			= 0			# Serviço está offline
	online			= 1			# Serviço está online
	unavailable		= 2			# 
	no_data			= 5			# O site não retornou a disponibilidade
	error			= 500		# Argumentos não suportados
	invalid_conf	= 501		# Arquivo de configuração inválido
	url_not_found	= 502		# Não foi configurada uma url para esse tipo
	fail_http		= 400		# Portal Sefaz retornou erro
	timeout_http	= 408		# Portal Sefaz não respondeu
	
	balls			= {
		"imagens/bola_verde_p.png": 	online,
        "imagens/bola_amarela_p.png": 	unavailable,
        "imagens/bola_vermelho_p.png": 	offline
	}