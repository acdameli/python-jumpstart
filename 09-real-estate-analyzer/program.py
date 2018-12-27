from analyzer import Analyzer


def main():
    print_header('Real Estate App')
    analyzer = Analyzer('./data.csv')
    analyzer.print_headers()
    analyzer.print_most_expensive()
    analyzer.print_least_expensive()
    analyzer.print_most_average()
    analyzer.print_most_average_two_bedroom()


def print_header(string):
    print('-' * (20 + len(string)))
    print(' ' * 10 + string)
    print('-' * (20 + len(string)))


if __name__ == '__main__':
    main()
