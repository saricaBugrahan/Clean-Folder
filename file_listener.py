import os
from file_type import file_type
import time
class file_listener:

    def __init__(self,**kwargs):
        self.location = kwargs["location"]
        self.period_of_listen = kwargs["period_of_listen"]
        self.logger = kwargs["logger"]
        self.current_files = os.listdir(self.location) 
    def listen(self):
        while True:
            files = os.listdir(self.location)
            new_files = [file for file in files if file not in self.current_files]

            for file in new_files:
                checked_file = file_type(filename=file,logger=self.logger)
                if checked_file.type == None:
                    self.logger.log("File type not found in folder: "+self.location,level='warning')
                    continue

                #TODO: File gelme durumu burada handle edilecek
                if os.path.isfile(self.location+file):
                    self.logger.log("New generated is a file: "+self.location+file,level='warning')
                else:
                    self.logger.log("New generated is a folder: "+self.location+file,level='info')
                
                #content_type = checked_file.choose_content(content_type=checked_file.type)    
                
            


            time.sleep(self.period_of_listen)