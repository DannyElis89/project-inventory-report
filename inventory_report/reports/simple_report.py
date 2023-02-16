class ReportFilter:
    @classmethod
    def data_de_fabricacao(cls, report):
        lista_datas = []
        for date in report:
            lista_datas.append(date['data_de_fabricacao'])
        return min(lista_datas)

    @classmethod
    def data_de_validade(cls, report):
        lista_datas = []
        for date in report:
            lista_datas.append(date['data_de_validade'])
        return min(lista_datas)

    @classmethod
    def nome_da_empresa(cls, report):
        all_companies = []
        for company in report:
            all_companies.append(company['nome_da_empresa'])
        return max(all_companies, key=all_companies.count)


class SimpleReport:
    @classmethod
    def generate(cls, report):
        oldest_fabrication = ReportFilter.data_de_fabricacao(report)
        closest_expiration = ReportFilter.data_de_validade(report)
        company = ReportFilter.nome_da_empresa(report)

        return (
            f'Data de fabricação mais antiga: {oldest_fabrication}\n'
            f'Data de validade mais próxima: {closest_expiration}\n'
            f'Empresa com mais produtos: {company}'
        )
