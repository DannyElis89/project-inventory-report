import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    pass
    if len(sys.argv) < 3:
        return print("Verifique os argumentos", file=sys.stderr)
    else:
        format = sys.argv[1].rsplit(".", 1)[-1]
        xy = sys.argv[2]

        if format == 'xml':
            data = InventoryRefactor(XmlImporter).import_data(sys.argv[1], xy)
            return sys.stdout.write(data)

        if format == 'json':
            data = InventoryRefactor(JsonImporter).import_data(sys.argv[1], xy)
            return sys.stdout.write(data)

        if format == 'csv':
            data = InventoryRefactor(CsvImporter).import_data(sys.argv[1], xy)
            return sys.stdout.write(data)


if __name__ == "__main__":
    main()
