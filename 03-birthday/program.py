import datetime


def print_header():
    print('--------------------------------')
    print('        BIRTHDAY APP            ')
    print('--------------------------------')


def get_birthday():
    def get_number(question, min, max):
        num = None;
        while not num or num < min or num > max:
            try:
                num = int(input(question))
                if num < min or num > max:
                    print(f'Your value must be between {min} and {max} inclusive.')
            except ValueError:
                print('Sorry that was not a valid number')
        return num

    year = get_number('What year were you born [YYYY]? ', 1900, 2018)
    month = get_number('What month were you born [MM]? ', 1, 12)
    day = get_number('What day were you born [DD]? ', 1, 31)
    return datetime.date(year, month, day)


def compute_days_between_dates(original, target):
    this_year = datetime.date(target.year, original.month, original.day)
    dt = this_year - target
    return dt.days


def print_birthday_information(days):
    if days < 0:
        print('You had your birthday {} days ago this year.'.format(-days))
    elif days > 0:
        print('Your birthday is in {} days!'.format(days))
    else:
        print('Happy birthday!')


def main():
    print_header()
    bday = get_birthday()
    today = datetime.date.today()
    days = compute_days_between_dates(bday, today)
    print_birthday_information(days)


main()
