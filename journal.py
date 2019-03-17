"""
journal module
"""
import os


def load(name):
    """
    creates and loads new journal

    :param name: name of the journal to load
    :return: journal data populated with file data
    """
    data = []
    file = get_full_path(name)

    if os.path.exists(file):
        with open(file) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return data


def save(name, data):
    file = get_full_path(name)
    print('saving to {}'.format(file))

    with open(file, 'w') as fout:
        for entry in data:
            fout.write(entry + '\n')


def get_full_path(name):
    return os.path.abspath(os.path.join('.', 'journals', name + '.txt'))


def add(entry, journal_data):
    return journal_data.append(entry)

