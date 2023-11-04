from datetime import datetime
from pytz import timezone
class logger:
    def __init__(self, **kwargs):
        self.log_file = kwargs["log_file"]
        self.timezone = kwargs["timezone"]

        if self.log_file is None:
            self.log_file = "clean_folder.log"

        if self.timezone is None:
            self.timezone = "Europe/Istanbul"    

        self.now_timezone = datetime.now(timezone(self.timezone))

    def log(self, message,level='info'):
        with open(self.log_file, 'a') as f:
            current_time = self.now_timezone.strftime("%d/%m/%Y %H:%M:%S") 
            f.write(f"{current_time} {level.upper()} {message}\n")