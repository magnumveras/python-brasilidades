from validate_docbr import CPF


class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.valida_cpf(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF Inválido!")

    def valida_cpf(self, documento):
        if len(documento) == 11:
            validator = CPF()
            return validator.validate(documento)
        else:
            raise ValueError("Quantidade de digitos inválida!")

    def formata_cpf(self):
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
        return self.formata_cpf()