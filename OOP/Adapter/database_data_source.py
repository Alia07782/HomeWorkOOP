class DatabaseDataSource:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def fetch_data(self):
        return f"Данные из базы данных по подключению: {self.connection_string}"
