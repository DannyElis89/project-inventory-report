import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.endswith("json"):
            with open(path) as file:
                return json.load(file)

        raise ValueError("Arquivo inválido")
