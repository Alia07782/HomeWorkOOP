from data_source import DataSource
from database_data_source import DatabaseDataSource

class DatabaseAdapter(DataSource):
    def __init__(self, database_source: DatabaseDataSource):
        self.database_source = database_source

    def read_data(self):
        return self.database_source.fetch_data()