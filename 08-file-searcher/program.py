import os


def main():
    print_header('File Search App')
    string = input('What string are you looking for? ').lower()
    directory = input('What directory do you want to search? ')
    print()
    print(f'Searching {directory} for {string}')
    print()
    results = search_directory(directory, string)
    i = 0
    for l in results:
        i += 1
        print(l)
    print()
    print(f'{i} total matches.')
    print(f'End of search')


def print_header(string):
    length = len(string) + 20
    print('-' * length)
    print(' ' * 10 + string)
    print('-' * length)


def search_directory(directory, string):
    for f in os.scandir(directory):
        if f.is_dir():
            yield from search_directory(f, string)
        elif f.is_file():
            try:
                with open(f, 'r', encoding='utf-8') as fin:
                    i = 0
                    for line in fin.readlines():
                        i += 1
                        if line.lower().find(string) >= 0:
                            yield f'{f.name}, line {i}>> {line.rstrip()}'
            except UnicodeDecodeError:
                pass


if __name__ == '__main__':
    main()
