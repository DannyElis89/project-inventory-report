from xmltodict import parse
from json import load
from csv import reader
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def csv_reader(path):
        with open(path) as file:
            csv_reader = reader(file)
            head, *data = csv_reader

        dict_zip = []
        for row in data:
            dict_zip.append(dict(zip(head, row)))
        # print(dict_zip)

        return dict_zip

    def json_reader(path):
        with open(path) as file:
            json_data = load(file)
            # print(json_data)

        return json_data

    def xml_reader(path):
        with open(path) as file:
            xml_file = file.read()
            parse_xml = parse(xml_file)

        return parse_xml['dataset']['record']

    def report_generator(data, type):
        if type == 'simples':
            return SimpleReport.generate(data)
        if type == 'completo':
            return CompleteReport.generate(data)
        raise ValueError('Unknown type')

    @classmethod
    def import_data(cls, path, type):
        if "csv" in path:
            data_file = cls.csv_reader(path)
        elif "json" in path:
            data_file = cls.json_reader(path)
        elif "xml" in path:
            data_file = cls.xml_reader(path)
        else:
            raise ValueError('Unable to read selected file')

        return cls.report_generator(data_file, type)
