import requests
import bs4
import collections


WeatherReport = collections.namedtuple('WeatherReport', 'cond, temp, scale, loc')


def main():
    print_header()
    event_loop()


def print_header():
    print('------------------------')
    print('   WEATHER CLIENT APP   ')
    print('------------------------')


def event_loop():
    zipCode = 'NOT_EMPTY'
    while zipCode:
        zipCode = input('Enter your zipcode (e.g. 94101): ')
        if zipCode:
            try:
                report = get_details(zipCode)
                print(f'The weather in {report.loc} is {report.temp} {report.scale} and {report.cond}')
            except AttributeError:
                print(f'Sorry, ran into a problem loading the zipcode {zipCode}')


def get_details(zipCode):
    url = f'http://www.wunderground.com/weather-forecast/{zipCode}'
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    loc = loc.strip() if loc else loc
    loc = loc.split('\n')[0].strip()
    condition = soup.find(class_='condition-icon').get_text()
    condition = condition.strip() if condition else condition
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    temp = temp.strip() if temp else temp
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()
    scale = scale.strip() if scale else scale
    return WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)


if __name__ == '__main__':
    main()
