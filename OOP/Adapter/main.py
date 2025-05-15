from file_data_source import FileDataSource
from database_data_source import DatabaseDataSource
from database_adapter import DatabaseAdapter

if __name__ == "__main__":

    file_source = FileDataSource("12.txt")
    print("Чтение из файла:")
    print(file_source.read_data())


    database_source = DatabaseDataSource("my_database_connection_string")
    database_adapter = DatabaseAdapter(database_source)
    print("\nЧтение из базы данных:")
    print(database_adapter.read_data())