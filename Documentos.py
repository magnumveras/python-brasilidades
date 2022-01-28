from Cnpj import Cnpj
from Cpf import Cpf
import string


class Documento:

    @staticmethod
    def cria_documento(doc):
        doc = ''.join(filter(str.isdigit, str(doc)))
        if len(doc) == 11:
            return Cpf(doc)
        elif len(doc) == 14:
            return Cnpj(doc)
        else:
            raise ValueError("Quantidade de dígitos incorreta!")

    """"
    def onlynumber(self, texto) -> str:
        
        Remove todos os caracteres que não são números
        Informa uma string e retorna somente os números dela

        :param texto: String a ser analisada
        :return: String somente com números
        
        if (texto is None) or (str(texto) == ''):
            return ''
        return ''.join(filter(str.isdigit, str(texto)))
    """