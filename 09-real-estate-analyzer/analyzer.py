from csv import DictReader
from collections import defaultdict
from sys import maxsize


class Analyzer:
    path = ''
    info = []
    max = 0
    max_record = None
    min = maxsize
    min_record = None
    averages = defaultdict(int)
    two_bed_averages = defaultdict(int)

    def __init__(self, csv_path):
        self.path = csv_path
        self.load()

    def load(self):
        # I managed to poop this out in like 10 mins, it works but sucks
        # todo: make this suck less
        # 1. use a something better than a dict of strings
        # 2. drop self.info as soon as analysis is complete... or never use it at all... counter + sums should suffice
        with open(self.path, 'r', encoding='utf-8') as fin:
            reader = DictReader(fin)
            two_bed_count = 0
            for row in reader:
                if self.max < int(row['price']):
                    self.max = max(self.max, int(row['price']))
                    self.max_record = row
                if self.min > int(row['price']):
                    self.min = min(self.min, int(row['price']))
                    self.min_record = row
                self.averages['price'] += int(row['price'])
                self.averages['beds'] += int(row['beds'])
                self.averages['baths'] += int(row['baths'])
                if int(row['beds']) == 2:
                    self.two_bed_averages['price'] += int(row['price'])
                    self.two_bed_averages['beds'] += int(row['beds'])
                    self.two_bed_averages['baths'] += int(row['baths'])
                    two_bed_count += 1
                self.info.append(row)

            self.averages['price'] = round(self.averages['price'] / len(self.info))
            self.averages['beds'] = round(self.averages['beds'] / len(self.info), 1)
            self.averages['baths'] = round(self.averages['baths'] / len(self.info), 1)
            if two_bed_count > 0:
                self.two_bed_averages['price'] = round(self.two_bed_averages['price'] / two_bed_count)
                self.two_bed_averages['beds'] = round(self.two_bed_averages['beds'] / two_bed_count, 1)
                self.two_bed_averages['baths'] = round(self.two_bed_averages['baths'] / two_bed_count, 1)

    def print_headers(self):
        print('Header: ' + ', '.join(self.info[0].keys()))

    def print_most_expensive(self):
        print('Most expensive: {}-beds, {}-baths, {} for ${:,} in {}'.format(self.max_record['beds'], self.max_record['baths'], self.max_record['type'], int(self.max_record['price']), self.max_record['city']))

    def print_least_expensive(self):
        print('Least expensive: {}-beds, {}-baths, {} for ${:,} in {}'.format(self.min_record['beds'], self.min_record['baths'], self.min_record['type'], int(self.min_record['price']), self.min_record['city']))

    def print_most_average(self):
        print('Average: ${:,}, {} bed, {} bath'.format(self.averages['price'], self.averages['beds'], self.averages['baths']))

    def print_most_average_two_bedroom(self):
        if len(self.two_bed_averages):
            print('Average 2-bedroom: ${:,}, {} bed, {} bath'.format(self.two_bed_averages['price'], self.two_bed_averages['beds'], self.two_bed_averages['baths']))
