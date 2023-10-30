class file_type:
    def __init__(self,**kwargs):
        self.filename = kwargs["filename"]
        self.type = kwargs["filename"].split('.')[-1]
        self.logger = kwargs["logger"]

    def __str__(self):
        return self.filename

    def choose_content(self,content_type):
        for type in self.content_types:
            if type == content_type:
                return type
        self.logger.log("Content type not found in folder: "+self.filename,level='warning')
        return None


    def choose_subfolder(self,subfolder_type):
        for subfolder in self.subfolder_types:
            if subfolders in subfolder_type:
                return subfolder        
        self.logger.log("Subfolder type not found in folder: "+self.filename,level='warning')
        return None