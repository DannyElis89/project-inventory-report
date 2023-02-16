import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.endswith("xml"):
            with open(path) as file:
                xml = file.read()
                return xmltodict.parse(xml)["dataset"]["record"]

        raise ValueError("Arquivo inválido")
