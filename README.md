
# Script para integrar no Zabbix o monitoramento da Sefaz

Esse script em python consulta a Sefaz e transmite ao agente do Zabbix um status code para fazer o monitoramento desses serviços


## Autores

- [@gusmarucci](https://github.com/gusmarucci)


## Deploy

Para fazer o deploy desse script, depois de ter o Zabbix instalado e configurado, salve os arquivos desse repositorio em /usr/lib/zabbix/externalscripts

Certifique que seu possui todas dependencias:
```bash
apt install python3 python3-pip
```

Na pasta /usr/lib/zabbix/externalscripts execute:
```bash
pip3 install -r requeriments.txt
```

Forneça permissão de execução ao script com o comando:

```bash
chmod +x sefaz.py
```

## Configuração

Salve o arquivo user_parameters_sefaz.conf na pasta /etc/zabbix/zabbix_agentd.d/

```bash
  cp user_parameters_sefaz.conf /etc/zabbix/zabbix_agentd.d/
```

Reinicie o serviço do agente zabbix

```bash
  cp systemctl restart zabbix_agentd
```
## Zabbix

Os scripts geram os status de cada funcionalidade do Sefaz. Mas para isso precisa-se configurar os templates, os mapa de valores, os triggers

### Mapa de valores

É preciso criar um mapeamento de valor, pois no script ele enviará para o Zabbix apenas os valores inteiros do status, é possivel criar manualmente, ou importar o arquivo zabbix/zabbix_map_value.xml

### Templates

Crie os templates manualmente de acordo com cada script ou importe o arquivo zabbix/zabbix_template_nfe.xml

### Host

#### Guia Host

Depois de importar os templates é necessário a criação de um host:

- Nome do host: Dê um nome para o host
- Interfaces do agente: Coloque o IP localhost (pressupondo que você tenha instalado os scripts no mesmo servidor)

#### Guia Templates

Associe os templates que foi importado ou criado


## Arquivo SEFAZ.CONF

Neste arquivo, o script é configurado para ler as paginas do SEFAZ

### Exemplo do arquivo SEFAZ.CONF

```json
{
	"version":	"0.0.1",

	"nfe": {

		"url": 					"https://www.nfe.fazenda.gov.br/portal/disponibilidade.aspx?versao=0.00&tipoConteudo=P2c98tUpxrI=",
		"table":				"tabelaListagemDados",
		"autorizadores": 		[
									"AM",
									"BA",
									"GO",
									"MG",
									"MS",
									"MT",
									"PE",
									"PR",
									"RS",
									"SP",
									"SVAN",
									"SVRS",
									"SVC-AN",
									"SVC-RS"
		],

		"disponibilidade": 		{

			"AUTORIZACAO":			"Autorização4",
			"RETORNO.AUT":			"Retorno Autorização4",
			"INUTILIZACAO":			"Inutilização4",
			"CONSULTA.PROTOCOLO":	"Consulta Protocolo4",
			"SERVICO":				"Status Serviço4",
			"CONSULTA.CADASTRO":	"Consulta Cadastro4",
			"RECEPCAO.EVENTO":		"Recepção Evento4"

		}
	},

	"cte": {
		"url": 					"https://www.cte.fazenda.gov.br/portal/disponibilidade.aspx?versao=1.00&tipoConteudo=XbSeqxE8pl8=",
		"table":				"tabelaListagemDados",
		"autorizadores": 		[
									"MT",
									"MS",
									"MG",
									"PR",	
									"RS",
									"SP",
									"SVRS",
									"SVSP",
									"AN"

		],

		"disponibilidade": 		{

			"RECEPCAOCTE":				"Recepção",
			"RETORNO.RECEP":			"Retorno Recepção",
			"INUTILIZACAOCTE":			"Inutilização",
			"CONSULTA.PROTOCOLOCTE":	"Consulta Protocolo",
			"RECEPCAOOS":				"RecepçãoOS",
			"SERVICOCTE":				"Status Serviço",
			"RECEPCAO.EVENTO":			"Recepção Evento"

		}
	} 
}
```




