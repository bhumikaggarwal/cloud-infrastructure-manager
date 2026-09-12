from models.resource import CloudResource

class Storage(CloudResource):

    def __init__(self,name,region,capacity,type):
     super().__init__(name,region)
     self._capacity = capacity
     self._type = type

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self,value):
        if value > 0:
            self._capacity = value
        else:
            raise ValueError("Capacity must be greater than 0")

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self,value):
        if value:
            self._type = value
        else:
            raise ValueError("Type cannot be empty")

    def describe(self):
        super().describe()
        print(f"Storage Capacity: {self.capacity}GB, Type: {self.type}")


    def start(self):
        print(f"Starting storage resource: {self.name}")

    def stop(self):
        print(f"Stopping storage resource: {self.name}")