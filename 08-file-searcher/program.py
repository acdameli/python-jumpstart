import os


def main():
    print_header('File Search App')
    string = input('What string are you looking for? ')
    directory = input('What directory do you want to search? ')
    print()
    print(f'Searching {directory} for {string}')
    print()
    results = search_directory(directory, string)
    for l in results:
        print(l)
    print()
    print(f'{len(results)} total matches.')
    print(f'End of search')


def print_header(string):
    length = len(string) + 20
    print('-' * length)
    print(' ' * 10 + string)
    print('-' * length)


def search_directory(directory, string):
    results = []
    for f in os.scandir(directory):
        if f.is_dir():
            results += search_directory(f, string)
        elif f.is_file():
            try:
                with open(f, 'r') as fin:
                    i = 0
                    for line in fin.readlines():
                        i += 1
                        if line.__contains__(string):
                            results.append(f'{f.name}, line {i}>> {line.rstrip()}')
            except UnicodeDecodeError:
                pass
    return results


if __name__ == '__main__':
    main()
