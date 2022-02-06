from validate_docbr import CPF


class Cpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF Inválido!")

    def valida(self, documento):
            validator = CPF()
            return validator.validate(documento)

    def formata(self):
        cpf = CPF()
        return cpf.mask(self.cpf)
        """fatia_um = self.cpf[:3]
        fatia_dois = self.cpf[3:6]
        fatia_tres = self.cpf[6:9]
        fatia_quatro = self.cpf[9:]

        return("{}.{}.{}-{}".format(fatia_um,
                                    fatia_dois,
                                    fatia_tres,
                                    fatia_quatro))
        """

    def __str__(self):
        return self.formata()

