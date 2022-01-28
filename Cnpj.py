from validate_docbr import CNPJ


class Cnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido!")

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def formata(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self):
        return self.formata()
