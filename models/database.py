from models.resource import CloudResource

class Database(CloudResource):
    def __init__(self,name,region,engine,version,storage):
        super().__init__(name,region)
        self.engine = engine
        self.version = version
        self.storage = storage

    def describe(self):
       super().describe()
       print(f"Database Engine: {self.engine}, Version: {self.version}, Storage: {self.storage}GB")

    def start(self):
        print(f"Starting database resource: {self.name}")

    def stop(self):
        print(f"Stopping database resource: {self.name}")