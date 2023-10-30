from datetime import datetime
class logger:
    def __init__(self, **kwargs):
        self.log_file = kwargs["log_file"]
        self.timezone = kwargs["timezone"]

        if self.log_file is None:
            self.log_file = "clean_folder.log"
            self.timezone = "Europe/Istanbul"

    def log(self, message,level='info'):
        with open(self.log_file, 'a') as f:
            current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S") 
            f.write(f"{current_time} {level.upper()} {message}\n")