import journal


def header():
    print('---------------------------')
    print('----------journal----------')
    print('---------------------------')


def journal_command():
    print('do things: ')
    command = None
    name = 'default'
    journal_data = journal.load(name)

    while command != 'X':
        command = input('[L]ist entry, [A]dd entry, E[x]it: ').upper().strip()
        if command == 'L':
            list_entry(journal_data)
        elif command == 'A':
            add_entry(journal_data)
        elif command == 'X':
            print('bye')
        else:
            print('command not found')

    journal.save(name, journal_data)


def list_entry(journal_data):
    print('List:')

    for index, entry in enumerate(journal_data):
        print('{}: {}'.format(index, entry))


def add_entry(journal_data):
    entry = input('Add: ')
    journal.add(entry, journal_data)


def main():
    header()
    journal_command()


if __name__ == '__main__':
    main()
