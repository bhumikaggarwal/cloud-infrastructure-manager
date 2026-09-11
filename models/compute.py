from models.resource import CloudResource


class Compute(CloudResource):
    def __init__(self,name,region,cpu,memory):
     super().__init__(name,region)
     self.cpu = cpu
     self.memory = memory


    def describe(self):
        super().describe()
        print(f"CPU: {self.cpu} cores, Memory: {self.memory}GB")

    def start(self):
        print(f"Starting compute resource: {self.name}")


class Server(Compute):
    def __init__(self,name,region,cpu,memory,os):
        super().__init__(name,region,cpu,memory)
        self.os = os

    def describe(self):
        super().describe()
        print(f"Operating System: {self.os}")

    # def start(self):
    #     print(f"Server {self.name} is starting...")