
from connectors import IConnector
from mock_dataframe import MockDataFrame

class IDataHandler(IConnector):
    """Interface for handling data - both extraction and writing."""
    
    def handle_data(self, data: MockDataFrame = None) -> MockDataFrame:
        pass

class HiveDataHandler(IDataHandler):
    """Handler for interacting with Hive."""
    
    def connect(self):
        # Logic for connecting to Hive
        pass

    def handle_data(self, data: MockDataFrame = None) -> MockDataFrame:
        # Placeholder logic for reading from or writing to Hive
        return MockDataFrame()

class CSVFileDataHandler(IDataHandler):
    """Handler for interacting with CSV files."""
    
    def __init__(self, file_path):
        self.file_path = file_path

    def connect(self):
        # Logic for connecting to a CSV file
        pass

    def handle_data(self, data: MockDataFrame = None) -> MockDataFrame:
        # Placeholder logic for reading from or writing to the CSV file
        return MockDataFrame()

class TrinoDataHandler(IDataHandler):
    """Handler for interacting with Trino."""
    
    def connect(self):
        # Logic for connecting to Trino
        pass

    def handle_data(self, data: MockDataFrame = None) -> MockDataFrame:
        # Placeholder logic for reading from or writing to Trino
        return MockDataFrame()
