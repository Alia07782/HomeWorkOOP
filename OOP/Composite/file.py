from file_system_element import FileSystemElement
class File(FileSystemElement):
    def __init__(self, name, size):
        self.name = name
        self.size = size  # Размер в байтах

    def display(self, indent=""):
        print(f"{indent}📄 {self.name} ({self.size} bytes)")

    def get_size(self):
        return self.size