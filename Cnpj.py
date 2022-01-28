from validate_docbr import CNPJ
import string

class Cnpj:
    def __init__(self, documento):
        documento = self.onlynumber(documento)
        if self.valida_cnpj(documento):
            self.novo_cnpj = documento
        else:
            raise ValueError("CNPJ inválido!")

    def valida_cnpj(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def __str__(self):
        mascara = CNPJ()
        return mascara.mask(self.novo_cnpj)

    def onlynumber(self, texto) -> str:
        """
        Remove todos os caracteres que não são números
        Informa uma string e retorna somente os números dela

        :param texto: String a ser analisada
        :return: String somente com números
        """
        if (texto is None) or (str(texto) == ''):
            return ''
        return ''.join(filter(str.isdigit, str(texto)))