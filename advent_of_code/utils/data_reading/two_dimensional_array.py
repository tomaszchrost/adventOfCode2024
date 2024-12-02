from advent_of_code.utils.data_reading.data_reader import DataReader


class TwoDimensionalArray(DataReader):
    def __init__(self):
        super(TwoDimensionalArray, self).__init__()

    def get_data(self, file, convertor):
        self.read_file(file)
        data = []
        for line in self.file_data:
            row = []
            for character in line.strip().split(" "):
                row.append(convertor(character))
            data.append(row)
        return data
