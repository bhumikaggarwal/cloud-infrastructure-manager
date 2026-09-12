#we are creating here our base class
#Abstract classes

from abc import ABC, abstractmethod

class CloudResource(ABC):

    def __init__(self,name,region):
        self._name = name
        self._region=region

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if value:
            self._name = value
        else:
            raise ValueError("Name cannot be empty")

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self,value):
        if value:
            self._region = value
        else:
            raise ValueError("Region cannot be empty")


    @abstractmethod
    def start(self):
        pass


    @abstractmethod
    def describe(self):
       print(f"Resource: {self.name} is in region: {self.region}")

    @abstractmethod
    def stop(self):
        pass


