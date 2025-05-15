from file_system_element import FileSystemElement
class Directory(FileSystemElement):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, element: FileSystemElement):
        self.children.append(element)

    def display(self, indent=""):
        print(f"{indent}📁 {self.name}/")
        for child in self.children:
            child.display(indent + "  ")

    def get_size(self):
        total_size = 0
        for child in self.children:
            total_size += child.get_size()
        return total_size