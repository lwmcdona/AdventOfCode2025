class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_lines(self):
        """Reads all lines from the file and returns them as a list."""
        try:
            with open(self.file_path, 'r') as f:
                return [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found.")
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
