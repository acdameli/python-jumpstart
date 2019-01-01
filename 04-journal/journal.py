import os


class Journal:
    def __init__(self, name):
        self.path = os.path.abspath(os.path.join('journals', name + '.jrn'))
        self.load()

    def list(self):
        """
        Lists all the entries in the journal
        """
        print(f'Your {len(self.text)} journal entries')
        for i, val in enumerate(self.text):
            val = val.rstrip('\n')
            print(f'{i+1}) {val}')

    def load(self):
        """
        This method loads the journal from the disk
        """
        print(f'... loading journal from {self.path} ...')
        try:
            fin = open(self.path, 'r')
        except FileNotFoundError:
            self.text = []
            return

        with fin:
            self.text = fin.readlines()

        print(f'... loaded {len(self.text)} entries ...')
        fin.close()

    def add(self, entry):
        """
        Adds a new entry to the journal in memory
        :param entry: The string to be added as a journal entry
        """
        self.text.append(entry + '\n')

    def save(self):
        """
        Saves the journal back to disk.
        """
        print(f'... saving to {self.path} ...')
        with open(self.path, 'w') as fout:
            fout.writelines(self.text)
        print('... save complete ...')

