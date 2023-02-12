class ReportFilter:
    @classmethod
    def data_de_fabricacao(cls, report):
        lista_data_de_fabricacao = []
        for date in report:
            lista_data_de_fabricacao.append(date['data_de_fabricacao'])

        return min(lista_data_de_fabricacao)

    @classmethod
    def data_de_validade(cls, report):
        lista_data_de_validade = []
        for date in report:
            lista_data_de_validade.append(date['data_de_validade'])

        return min(lista_data_de_validade)

    @classmethod
    def empresa_com_mais_produtos(cls, report):
        todas_empresas = []
        for empresa in report:
            todas_empresas.append(empresa['nome da empresa'])
        return max(todas_empresas, key=todas_empresas.count)


class SimpleReport:
    @classmethod
    def generate(cls, report):
        data_de_fabricacao = ReportFilter.data_de_fabricacao(report)
        data_de_validade = ReportFilter.data_de_validade(report)
        empresa = ReportFilter.empresa_com_mais_produtos(report)

        return (
            f'Data de fabricação mais antiga: {data_de_fabricacao}\n'
            f'Data de validade mais próxima: {data_de_validade}\n'
            f'Empresa com mais produtos: {empresa}'
        )
