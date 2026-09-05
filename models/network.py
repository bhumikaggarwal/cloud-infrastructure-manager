from models.resource import CloudResource

class Network(CloudResource):
    def __init__(self,name,region,VPC,subnet):
        super().__init__(name,region)
        self.VPC = VPC
        self.subnet = subnet

    def describe(self):
     super().describe()
     print(f"VPC: {self.VPC}, Subnet: {self.subnet}")

Network1 = Network("MyNetwork", "eu-central-1", "vpc-123456", "subnet-654321")
Network1.describe()