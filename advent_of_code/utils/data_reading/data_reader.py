class DataReader:
    def __init__(self):
        self.file_data: [str] = None

    def read_file(self, file: str):
        with open(file, 'r') as f:
            self.file_data = f.readlines()

    def get_data(self, file):
        self.read_file(file)
        return self.file_data