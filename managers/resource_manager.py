from models.compute import Compute
from models.storage import Storage
from models.network import Network
from models.database import Database


class ResourceManager:
    """Manage cloud resources in one place."""

    def __init__(self, resources=None):
        self.resources = []
        if resources is not None:
            self.add_resources(resources)

    def add_resource(self, resource):
        self.resources.append(resource)

    def add_resources(self, *resources):
        for item in resources:
            if isinstance(item, list):
                for resource in item:
                    self.add_resource(resource)
            else:
                self.add_resource(item)

    def remove_resource(self, resource):
        if resource in self.resources:
            self.resources.remove(resource)

    def start_all(self):
        for resource in self.resources:
            resource.start()

    def describe_all(self):
        for resource in self.resources:
            resource.describe()

    @staticmethod
    def sample_resources():
        compute = Compute("AppServer", "us-east-1", 8, 32)


        storage = Storage("AppStorage", "us-east-1", 500, "SSD")

        network = Network("AppNetwork", "us-east-1", "vpc-123456", "subnet-654321")


        database = Database("AppDatabase", "us-east-1", "PostgreSQL", "13.3", 500)

        return [compute, storage, network, database]


# Example usage:
manager = ResourceManager()
manager.add_resources(ResourceManager.sample_resources())
manager.describe_all()
manager.start_all()
