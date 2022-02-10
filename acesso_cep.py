import requests
class BuscaEndereco:
    def __init__(self, cep):
        if self.cep_valida(cep):
            self.cep = str(cep)
        else:
            raise ValueError("Cep Inválido!")

    def cep_valida(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def formata_cep(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])

    def __str__(self):
        return self.formata_cep()

    def acessa_via_cep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        dados = r.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )