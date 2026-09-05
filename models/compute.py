from models.resource import CloudResource


class Compute(CloudResource):
    def __init__(self,name,region,cpu,memory):
     super().__init__(name,region)
     self.cpu = cpu
     self.memory = memory


    def describe(self):
        super().describe()
        print(f"CPU: {self.cpu} cores, Memory: {self.memory}GB")


class Server(Compute):
    def __init__(self,name,region,cpu,memory,os):
        super().__init__(name,region,cpu,memory)
        self.os = os

    def describe(self):
        super().describe()
        print(f"Operating System: {self.os}")

Server1 = Server("MyServer", "us-east-1", 8, 32, "Ubuntu 20.04")
Server1.describe()