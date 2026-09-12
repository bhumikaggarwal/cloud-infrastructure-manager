from models.resource import CloudResource


class Compute(CloudResource):
    def __init__(self,name,region,cpu,memory):
     super().__init__(name,region)
     self._cpu = cpu
     self._memory = memory

    @property
    def cpu(self):
        return self._cpu

    @cpu.setter
    def cpu(self,value):
        if value > 0:
            self._cpu = value
        else:
            raise ValueError("CPU cores must be greater than 0")


    @property
    def memory(self):
        return self._memory

    @memory.setter
    def memory(self,value):
        if value > 0:
            self._memory = value
        else:
            raise ValueError("Memory must be greater than 0")

    def describe(self):
        super().describe()
        print(f"CPU: {self.cpu} cores, Memory: {self.memory}GB")

    def start(self):
        print(f"Starting compute resource: {self.name}")

    def stop(self):
        print(f"Stopping compute resource: {self.name}")


class Server(Compute):
    def __init__(self,name,region,cpu,memory,os):
        super().__init__(name,region,cpu,memory)
        self.os = os

    def describe(self):
        super().describe()
        print(f"Operating System: {self.os}")

    def start(self):
        print(f"Server {self.name} is starting...")

    def stop(self):
        print(f"Stopping server: {self.name}")