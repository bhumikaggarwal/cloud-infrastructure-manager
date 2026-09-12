from models.resource import CloudResource

class Database(CloudResource):
    def __init__(self,name,region,engine,version,storage):
        super().__init__(name,region)
        self._engine = engine
        self._version = version
        self._storage = storage

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self,value):
        if value:
            self._engine = value
        else:
            raise ValueError("Engine cannot be empty")

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self,value):
        if value:
            self._version = value
        else:
            raise ValueError("Version cannot be empty")

    @property
    def storage(self):
        return self._storage

    @storage.setter
    def storage(self,value):
        if value > 0:
            self._storage = value
        else:
            raise ValueError("Storage must be greater than 0")

    def describe(self):
       super().describe()
       print(f"Database Engine: {self.engine}, Version: {self.version}, Storage: {self.storage}GB")

    def start(self):
        print(f"Starting database resource: {self.name}")

    def stop(self):
        print(f"Stopping database resource: {self.name}")