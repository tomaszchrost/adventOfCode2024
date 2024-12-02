from advent_of_code.utils.data_reading.data_reader import DataReader


class TwoVerticalArrays(DataReader):
    def __init__(self):
        super(TwoVerticalArrays, self).__init__()

    def get_data(self, file):
        self.read_file(file)
        data = [[], []]
        for line in self.file_data:
            first_value, *_, last_value = line.split()
            data[0].append(int(first_value))
            data[1].append(int(last_value))
        return data
