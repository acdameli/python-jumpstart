from journal import Journal


def print_header():
    print('------------------------------------------')
    print('        PERSONAL JOURNAL APP              ')
    print('------------------------------------------')


def query_user():
    cmd = None
    while not cmd:
        cmd = input('What do you want to do? [L]ist, [A]dd, or E[x]it? ').lower().strip('\n')
        if cmd not in ['l', 'a', 'x']:
            print(f'Could not understand "{cmd}"')
            cmd = None
    return cmd


def run_event_loop():
    my_journal = Journal('personal')
    command = query_user()
    while command != 'x':
        if command == 'l':
            my_journal.list()
        elif command == 'a':
            my_journal.add(input('Enter your journal entry:\n'))
        command = query_user()

    my_journal.save()


def main():
    print_header()
    run_event_loop()


if __name__ == '__main__':
    main()
