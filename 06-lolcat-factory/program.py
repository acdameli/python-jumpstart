import requests
import shutil
import subprocess
import os
import platform


def main():
    print_header()
    path = './images'
    print('Contacting cat service for cat pictures...')
    load_cats(path)
    print('Launching output folder in Finder')
    launch_finder(path)


def load_cats(path):
    for i in range(0,10):
        cat_binary = requests.get('http://consuming-python-services-api.azurewebsites.net/cats/random', stream=True).raw
        write_cat(path, f'cat-{i}', cat_binary)


def write_cat(directory, name, cat):
    path = os.path.join(directory, name + '.jpg')
    with open(path, 'wb') as fout:
        shutil.copyfileobj(cat, fout)


def launch_finder(path):
    print('Displaying cats in OS window.')
    if platform.system() == 'Darwin':
        subprocess.call(['open', path])
    elif platform.system() == 'Windows':
        subprocess.call(['explorer', path])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', path])
    else:
        print("We don't support your os: " + platform.system())


def print_header():
    print('-------------------------------')
    print('       Cat Factory App         ')
    print('-------------------------------')
    print()


if __name__ == '__main__':
    main()
