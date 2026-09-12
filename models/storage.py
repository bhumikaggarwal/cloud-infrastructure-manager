from models.resource import CloudResource

class Storage(CloudResource):

    def __init__(self,name,region,capacity,type):
     super().__init__(name,region)
     self.capacity = capacity
     self.type = type

    def describe(self):
        super().describe()
        print(f"Storage Capacity: {self.capacity}GB, Type: {self.type}")


    def start(self):
        print(f"Starting storage resource: {self.name}")

    def stop(self):
        print(f"Stopping storage resource: {self.name}")