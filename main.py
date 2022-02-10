#from Cpf import Cpf
#from Cnpj import Cnpj
from Documentos import Documento
import re
from TelefonesBr import TelefonesBr
from datetime import datetime, timedelta

novo_cpf = Documento.cria_documento("23013646829")
print(novo_cpf)

novo_cnpj = Documento.cria_documento("49.009.546/0001-00")
print(novo_cnpj)


#Expressões regulares
padrao = "[0-9][a-z]{2}[0-9]"
texto = "123 1ac2 1cc aa1"
resposta = re.search(padrao, texto)
print(resposta.group())


padrao= "\w{1,20}[\W]*\w{1,20}@\w{2,20}.\w{2,3}[.]*[\w{2,3}]*"
texto = "teste.teste23@gmail.com sgsdfsdfsdfsdfgsdgsd"
resposta = re.search(padrao, texto)
print(resposta.group())

#+xxx(xx)xxxxx-xxxx
telefone = "(11)992409317"
telefone_testa = TelefonesBr(telefone)
print(telefone_testa)

#Utilização da Classe DateTime
print(datetime.today())


from datas_br import Datas_Br
cadastro = Datas_Br()
print(cadastro.momento_cadastro)
print(cadastro.dias_semana())
print(cadastro.mes_cadastro())
print(cadastro)
print(cadastro.data_cadastro())

from acesso_cep import BuscaEndereco

cep = "01001000"
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)

import requests

#r = requests.get("https://viacep.com.br/ws/01001000/json/")
#print(r)

a = objeto_cep.acessa_via_cep()
print(type(a))
print(dir(a))

Bairro, Cidade, Estado = objeto_cep.acessa_via_cep()
print(Bairro, Cidade, Estado)






