import os

class file_type:
    def __init__(self,**kwargs):
        self.filename = kwargs["filename"]
        self.logger = kwargs["logger"]
        self.extensions = kwargs["extensions"]
        self.is_directory = os.path.isdir(self.filename+self.filename)
        self.desired_locations = kwargs["desired_locations"]
        self.desired_location = self.get_desired_location()
        if self.is_directory:
            self.type = "folder"
            self.extension_group = None
        else:
            self.type = kwargs["filename"].split(".")[1]
            self.extension_group = self.get_extension_type()
        

    def __str__(self):
        return self.filename

    def get_extension_type(self):
        for extension_group in self.extensions:
            if self.type in self.extensions[extension_group]:
                return extension_group
        self.logger.log("Extension type not found in folder: "+self.filename,level='warning')
        return None

    def get_desired_location(self):
        for desired_location in self.desired_locations:
            if desired_location in self.filename:
                return desired_location

        self.logger.log("Sending to the 'Others' folder, desired location not found in folder:"+self.filename,level='warning')
        return None

    def get_renamed_file(self):
        split_filename = self.filename.split(".")[-2].split(self.desired_location)
        for name in split_filename:
            if name != self.desired_location and name != "":
                return name+"."+self.type    
        return None