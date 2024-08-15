class TextFileWriter():
    @staticmethod
    def Write(filename: str, text: str, encoding: str = 'utf-8'):
        with open(filename, mode='w', encoding=encoding, newline='') as f:
            f.write(text)
