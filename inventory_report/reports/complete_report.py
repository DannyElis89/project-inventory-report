from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompaniesFilter:
    @classmethod
    def companies_counter(cls, report):
        all_companies = []
        for company in report:
            all_companies.append(company['nome_da_empresa'])

        # print(all_companies)
        counter_companies = Counter(all_companies)
        # print(counter_companies)

        return counter_companies

    @classmethod
    def companies_data(cls, report):
        companies_counter = cls.companies_counter(report)
        companies_data = str()

        for company in companies_counter.most_common():
            companies_data += f"- {company[0]}: {company[1]}\n"

        report = (
            "Produtos estocados por empresa:\n"
            f"{companies_data}"
        )
        # print(report)

        return report


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, report):
        complete_report = (
            f"{super().generate(report)}\n"
            f"{CompaniesFilter.companies_data(report)}"
        )
        # print(complete_report)

        return complete_report
