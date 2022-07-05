import csv
import os

class Data:
    __directory = ''

    def __init__(self, directory):
        self.__directory = directory

    def get_data(self):
        data = []
        filenames = []
        # iterate over files in
        # that directory
        for filename in os.listdir(self.__directory):

            f = os.path.join(self.__directory, filename)
            # checking if it is a file
            if os.path.isfile(f):
                file = open(f, 'r')
                tmp = list(csv.reader(file))
                tmp = tmp[1:]

                data.append(tmp)
                filenames.append(filename)
        return data, filenames
