import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.endswith("csv"):
            with open(path) as file:
                return list(csv.DictReader(file))

        raise ValueError("Arquivo inválido")
