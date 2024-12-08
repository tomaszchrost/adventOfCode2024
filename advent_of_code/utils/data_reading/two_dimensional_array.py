from advent_of_code.utils.data_reading.data_reader import DataReader


class TwoDimensionalArray(DataReader):
    def __init__(self):
        super(TwoDimensionalArray, self).__init__()

    def get_data(self, file, convertor, spaces = True):
        self.read_file(file)
        data = []
        for line in self.file_data:
            row = []
            split_line = line.strip().split(" ") if spaces else line.strip()
            for character in split_line:
                row.append(convertor(character))
            data.append(row)
        return data
