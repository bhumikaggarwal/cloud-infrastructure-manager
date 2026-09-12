from models.resource import CloudResource

class Network(CloudResource):
    def __init__(self,name,region,VPC,subnet):
        super().__init__(name,region)
        self._VPC = VPC
        self._subnet = subnet

    @property
    def VPC(self):
        return self._VPC

    @VPC.setter
    def VPC(self,value):
        if value:
            self._VPC = value
        else:
            raise ValueError("VPC cannot be empty")

    @property
    def subnet(self):
        return self._subnet

    @subnet.setter
    def subnet(self,value):
        if value:
            self._subnet = value
        else:
            raise ValueError("Subnet cannot be empty")

    def describe(self):
     super().describe()
     print(f"VPC: {self.VPC}, Subnet: {self.subnet}")

    def start(self):
        print(f"Starting network resource: {self.name}")

    def stop(self):
        print(f"Stopping network resource: {self.name}")