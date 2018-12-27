import requests


def main():
    print_header('Movie Search App')
    while True:
        search = input('Enter search text: ')
        if not search:
            break

        try:
            results = search_movies(search)
            print(f'{len(results["hits"])} found')
            for r in results['hits']:
                print(f"{r['year']} - {r['title']}")
        except ConnectionError:
            print('A network error occurred')
        except Exception as e:
            print(f'An unexpected error occurred {e}')


def print_header(string):
    print('-' * (20 + len(string)))
    print(' ' * 10 + string)
    print('-' * (20 + len(string)))


def search_movies(string):
    return requests.get(f'http://movie_service.talkpython.fm/api/search/{string}').json()


if __name__ == '__main__':
    main()