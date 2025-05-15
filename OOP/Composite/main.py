from file import File
from directory import Directory

def main():
    root = Directory("root")
    home = Directory("home")
    user = Directory("user")

    file1 = File("file1.txt", 100)
    file2 = File("file2.txt", 200)
    file3 = File("file3.txt", 300)

    root.add(home)
    home.add(user)
    user.add(file1)
    user.add(file2)
    root.add(file3)

    print("Структура файловой системы:")
    root.display()

    print(f"\nОбщий размер: {root.get_size()} байт")

if __name__ == "__main__":
    main()