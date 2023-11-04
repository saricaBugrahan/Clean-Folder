import os

class file_type:
    def __init__(self,**kwargs):
        self.filename = kwargs["filename"]
        self.logger = kwargs["logger"]
        self.base_location = kwargs["base_location"]
        self.is_directory = os.path.isdir(self.base_location+self.filename)
        self.desired_locations = kwargs["desired_locations"]
        self.desired_location = self.get_desired_location()
        if self.is_directory:
            self.type = "folder"
        else:
            self.type = kwargs["filename"].split(".")[1]

    def __str__(self):
        return self.filename

    def get_desired_location(self):
        for desired_location in self.desired_locations:
            if desired_location in self.filename:
                return desired_location
        return None

    def get_renamed_file(self):
        split_filename = self.filename.split(".")[-2].split(self.desired_location)
        for name in split_filename:
            if name != self.desired_location and name != "":
                return name+"."+self.type    
        return None