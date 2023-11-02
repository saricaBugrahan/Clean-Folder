import os
from file_type import file_type
import time
class file_listener:

    def __init__(self,**kwargs):
        self.location = kwargs["location"]
        self.extensions = kwargs["extensions"]
        self.period_of_listen = kwargs["period_of_listen"]
        self.logger = kwargs["logger"]
        self.current_files = os.listdir(self.location) 
        self.desired_locations = kwargs["desired_locations"]
    
    def listen(self):
        while True:
            periodically_checked_files = os.listdir(self.location)
            new_files = [file for file in periodically_checked_files if file not in self.current_files]
            
            for file in new_files:
                checked_file = file_type(filename=file,logger=self.logger,extensions=self.extensions,desired_locations=self.desired_locations)

                if checked_file.type == "folder":
                    self.logger.log("New folder found: "+file,level='info')
                    
                else:
                    self.logger.log("New file found: "+file,level='info')
                    if checked_file.desired_location is not None:
                        if not os.path.exists(os.path.join(self.location,checked_file.desired_location)):
                            self.logger.log("Creating folder: "+checked_file.desired_location,level='info')
                            os.makedirs(os.path.join(self.location,checked_file.desired_location))
                        
                        else:

                            self.logger.log("Moving file: "+file+" to "+checked_file.get_desired_location(),level='info')
                            renamed_file = checked_file.get_renamed_file()
                            self.logger.log("Renaming file: "+file+" to "+renamed_file,level='info')                        
                            os.rename(os.path.join(self.location,checked_file.filename),os.path.join(self.location,checked_file.desired_location,renamed_file))
            
            
            self.current_files = periodically_checked_files        
            time.sleep(self.period_of_listen)