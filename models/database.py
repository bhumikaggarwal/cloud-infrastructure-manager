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

database1 = Database("MyDatabase", "ap-southeast-1", "PostgreSQL", "13.3", 500)
database1.describe()