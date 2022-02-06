#from Cpf import Cpf
#from Cnpj import Cnpj
from Documentos import Documento
import re
from TelefonesBr import TelefonesBr

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


telefone = "5566514685142"
telefone_objeto = TelefonesBr(telefone)