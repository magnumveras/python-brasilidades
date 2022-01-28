#from Cpf import Cpf
#from Cnpj import Cnpj
from Documentos import Documento

novo_cpf = Documento.cria_documento("23013646829")
print(novo_cpf)

novo_cnpj = Documento.cria_documento("49.009.546/0001-00")
print(novo_cnpj)