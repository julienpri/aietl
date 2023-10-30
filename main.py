
import logging

# Setting up logging configuration
logging.basicConfig(filename='etl_log.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

from data_handlers import HiveDataHandler, CSVFileDataHandler, TrinoDataHandler
from monitoring import Monitoring

def execute_etl():
    with open("input.json", 'r') as f:
        config = json.load(f)
    
    monitor = Monitoring()
    
    for step in config["ingestionSteps"]:
        logging.info(f"Starting the handling for {step['readerType']}")
        
        # Initialize the data handler
        handler_class = globals()[step["readerType"]]
        handler = handler_class(**step["handlerOptions"])

        # Handle the data
        data = handler.handle_data()

        # Log the action in monitoring and standard log
        message = f"Handled data using {step['readerType']}"
        monitor.add_message(message)
        logging.info(message)

    # At the end, write all messages
    monitor.write_messages()

# Test execution using input.json
if __name__ == "__main__":
    logging.info("Starting ETL execution")
    execute_etl()
    logging.info("Completed ETL execution")
