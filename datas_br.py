from datetime import datetime, timedelta

class Datas_Br:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def mes_cadastro(self):
        meses_ano = [
            "Janeiro", "Fevereiro", "Março",
            "Abril", "Maio", "Junho", "Julho",
            "Agosto", "Setembro", "Outubro",
            "Novembro","Dezembro"
        ]

        return meses_ano[self.momento_cadastro.month - 1]

    def dias_semana(self):
        dias_semana = ["Segunda-Feira", "Terça-Feira", "Quarta-Feira"
                        "Quinta-Feira", "Sexta-Feira", "Sábado", "Domingo"]
        return dias_semana[self.momento_cadastro.weekday()]

    def data_formatada(self):
        return self.momento_cadastro.strftime("%d/%m/%Y")

    def data_cadastro(self):
        return (datetime.today() + timedelta(days=30, weeks=2, hours=8)) - self.momento_cadastro

    def __str__(self):
        return self.data_formatada()