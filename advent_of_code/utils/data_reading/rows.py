from advent_of_code.utils.data_reading.data_reader import DataReader


class Rows(DataReader):
    def __init__(self):
        super(Rows, self).__init__()

    def get_data(self, file, convertor):
        self.read_file(file)
        data = []
        for line in self.file_data:
            data.append(convertor(line.strip()))
        return data
