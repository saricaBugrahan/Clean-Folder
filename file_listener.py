import os
from file_type import file_type
import time
class file_listener:

    def __init__(self,**kwargs):
        self.location = kwargs["location"]
        self.period_of_listen = kwargs["period_of_listen"]
        self.logger = kwargs["logger"]
        self.current_files = os.listdir(self.location) 
        self.desired_locations = kwargs["desired_locations"]
        self.create_new_folders = kwargs["create_new_folders"]
    
    def listen(self):
        while True:
            periodically_checked_files = os.listdir(self.location)
            new_files = [file for file in periodically_checked_files if file not in self.current_files]
            
            for file in new_files:
                checked_file = file_type(filename=file,logger=self.logger,desired_locations=self.desired_locations,base_location=self.location)

                #Controls whether the created file is dir or file.    
                if checked_file.type == "folder":
                    self.logger.log("New folder found: "+file,level='info')
                    if checked_file.desired_location is not None:
                        self.logger.log("Moving folder: "+file+" to "+checked_file.get_desired_location(),level='info')
                        os.rename(os.path.join(self.location,checked_file.filename),os.path.join(self.location,checked_file.desired_location,checked_file.filename))
                    else:
                        self.logger.log("Sending to the 'Others' folder, desired location not found in folder:"+checked_file.filename,level='warning')
                        os.rename(os.path.join(self.location,checked_file.filename),os.path.join(self.location,"others",checked_file.filename))
                else:
                    self.logger.log("New file found: "+file,level='info')
                    if checked_file.desired_location is not None:
                        #Controls the for desired location found but not created
                        if not os.path.exists(os.path.join(self.location,checked_file.desired_location)):
                            self.logger.log("Creating folder: "+checked_file.desired_location,level='info')
                            os.makedirs(os.path.join(self.location,checked_file.desired_location))
                        #Controls the for desired location found and created
                        else:
                            self.logger.log("Moving file: "+file+" to "+checked_file.get_desired_location(),level='info')
                            renamed_file = checked_file.get_renamed_file()                        
                            os.rename(os.path.join(self.location,checked_file.filename),os.path.join(self.location,checked_file.desired_location,renamed_file))
                    else:
                        self.logger.log("Sending to the 'others' folder, desired location not found in folder:"+self.filename,level='warning')
                        os.rename(os.path.join(self.location,checked_file.filename),os.path.join(self.location,"others",checked_file.filename))
            
            self.current_files = periodically_checked_files        
            time.sleep(self.period_of_listen)