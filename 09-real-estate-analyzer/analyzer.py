from csv import DictReader
from collections import defaultdict
from sys import maxsize


class Purchase:
    def __init__(
            self, city, zipcode, state, beds,
            baths, sq__ft, home_type, sale_date, price,
            latitude, longitude):
        self.longitude = longitude
        self.latitude = latitude
        self.price = price
        self.sale_date = sale_date
        self.type = home_type
        self.sq__ft = sq__ft
        self.baths = baths
        self.beds = beds
        self.state = state
        self.zip = zipcode
        self.city = city

    @staticmethod
    def create_from_dict(lookup):
        return Purchase(
            lookup['city'],
            lookup['zip'],
            lookup['state'],
            int(lookup['beds']),
            int(lookup['baths']),
            int(lookup['sq__ft']),
            lookup['type'],
            lookup['sale_date'],
            float(lookup['price']),
            float(lookup['latitude']),
            float(lookup['longitude']))


class Analyzer:
    path = ''
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
        # do something more elegant for average calculations
        with open(self.path, 'r', encoding='utf-8') as fin:
            reader = DictReader(fin)
            two_bed_count = 0
            count = 0
            for row in reader:
                p = Purchase.create_from_dict(row)
                if self.max < p.price:
                    self.max = max(self.max, p.price)
                    self.max_record = row
                if self.min > p.price:
                    self.min = min(self.min, p.price)
                    self.min_record = row
                self.averages['price'] += p.price
                self.averages['beds'] += p.beds
                self.averages['baths'] += p.baths
                count += 1
                if p.beds == 2:
                    self.two_bed_averages['price'] += p.price
                    self.two_bed_averages['beds'] += p.beds
                    self.two_bed_averages['baths'] += p.baths
                    two_bed_count += 1

            self.averages['price'] = round(self.averages['price'] / count)
            self.averages['beds'] = round(self.averages['beds'] / count, 1)
            self.averages['baths'] = round(self.averages['baths'] / count, 1)
            if two_bed_count > 0:
                self.two_bed_averages['price'] = round(self.two_bed_averages['price'] / two_bed_count)
                self.two_bed_averages['beds'] = round(self.two_bed_averages['beds'] / two_bed_count, 1)
                self.two_bed_averages['baths'] = round(self.two_bed_averages['baths'] / two_bed_count, 1)

    def print_headers(self):
        print('Header: ' + ', '.join(self.max_record.keys()))

    def print_most_expensive(self):
        print('Most expensive: {}-beds, {}-baths, {} for ${:,} in {}'.format(self.max_record['beds'], self.max_record['baths'], self.max_record['type'], int(self.max_record['price']), self.max_record['city']))

    def print_least_expensive(self):
        print('Least expensive: {}-beds, {}-baths, {} for ${:,} in {}'.format(self.min_record['beds'], self.min_record['baths'], self.min_record['type'], int(self.min_record['price']), self.min_record['city']))

    def print_most_average(self):
        print('Average: ${:,}, {} bed, {} bath'.format(self.averages['price'], self.averages['beds'], self.averages['baths']))

    def print_most_average_two_bedroom(self):
        if len(self.two_bed_averages):
            print('Average 2-bedroom: ${:,}, {} bed, {} bath'.format(self.two_bed_averages['price'], self.two_bed_averages['beds'], self.two_bed_averages['baths']))
