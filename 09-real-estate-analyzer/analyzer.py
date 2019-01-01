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


<<<<<<< HEAD
=======
class Averager:
    def __init__(self):
        self.current_value = 0
        self.point_counter = 0
        self.max = None
        self.min = None

    def count(self):
        return self.point_counter

    def sum(self):
        return self.current_value * self.point_counter

    def __add__(self, other):
        current_sum = self.current_value * self.point_counter + float(other)
        self.point_counter += 1
        self.current_value = current_sum / self.point_counter
        self.max = self.max if self.max and self.max > other else other
        self.min = self.min if self.min and self.min < other else other
        return self

    def __str__(self):
        return str(self.current_value)

    def __float__(self):
        return float(self.current_value)


>>>>>>> abad0c2981ab58bb7e47a62f0d33ba8f114210c9
class Analyzer:
    def __init__(self, csv_path):
        self.path = csv_path
        self.max = 0
        self.max_record = None
        self.min = maxsize
        self.min_record = None
        self.averages = {
            'price': Averager(),
            'beds': Averager(),
            'baths': Averager(),
        }
        self.two_bed_averages = {
            'price': Averager(),
            'beds': Averager(),
            'baths': Averager(),
        }
        self.load()
        self.max = 0
        self.max_record = None
        self.min = maxsize
        self.min_record = None
        self.averages = defaultdict(int)
        self.two_bed_averages = defaultdict(int)

    def load(self):
        # do something more elegant for average calculations
        with open(self.path, 'r', encoding='utf-8') as fin:
            reader = DictReader(fin)
            for row in reader:
                p = Purchase.create_from_dict(row)
                self.averages['price'] += p.price
                self.averages['beds'] += p.beds
                self.averages['baths'] += p.baths
                if self.averages['price'].max == p.price:
                    self.max_record = row
                if self.averages['price'].min == p.price:
                    self.min_record = row
                if p.beds == 2:
                    self.two_bed_averages['price'] += p.price
                    self.two_bed_averages['beds'] += p.beds
                    self.two_bed_averages['baths'] += p.baths

    def print_headers(self):
        print('Header: ' + ', '.join(self.max_record.keys()))

    def print_most_expensive(self):
        print('Most expensive: {}-beds, {}-baths, {} for ${:,} in {}'.format(self.max_record['beds'], self.max_record['baths'], self.max_record['type'], int(self.max_record['price']), self.max_record['city']))

    def print_least_expensive(self):
        print('Least expensive: {}-beds, {}-baths, {} for ${:,} in {}'.format(self.min_record['beds'], self.min_record['baths'], self.min_record['type'], int(self.min_record['price']), self.min_record['city']))

    def print_most_average(self):
        print('Average: ${:,.2f}, {:,.1f} bed, {:,.1f} bath'.format(float(self.averages['price']), float(self.averages['beds']), float(self.averages['baths'])))

    def print_most_average_two_bedroom(self):
        if len(self.two_bed_averages):
            print('Average 2-bedroom: ${:,.2f}, {:,.1f} bed, {:.1f} bath'.format(round(float(self.two_bed_averages['price']), 2), float(self.two_bed_averages['beds']), float(self.two_bed_averages['baths'])))
