from file_listener import file_listener
from logger import logger
import json


if __name__ == "__main__":
    #Read the json file and create the logger
    configuration_file = json.load(open("conf.json")) 
    if configuration_file is None:
        raise Exception("Configuration file not found")


    """
    LOGGER CONSTANTS
    """
    
    log_file = configuration_file["logger"]["log_file"]
    timezone = configuration_file["logger"]["timezone"]
    
    
    """
    FILE LISTENER CONSTANTS
    """
    
    folder_to_be_listen = configuration_file["folder"]["folder_to_be_listen"]
    period_of_listen    = configuration_file["folder"]["period_of_listen"]  


    logger = logger(log_file=log_file,timezone=timezone)



    listener = file_listener(location=folder_to_be_listen,period_of_listen=5,logger=logger)
    listener.listen()