from models.resource import CloudResource

class Storage(CloudResource):

    def __init__(self,name,region,capacity,type):
     super().__init__(name,region)
     self.capacity = capacity
     self.type = type

    def describe(self):
        super().describe()
        print(f"Storage Capacity: {self.capacity}GB, Type: {self.type}")


storage1 = Storage("MyStorage", "us-west-2", 1000, "SSD")
storage1.describe()