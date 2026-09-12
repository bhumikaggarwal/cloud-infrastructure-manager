#we are creating here our base class
#Abstract classes

from abc import ABC, abstractmethod

class CloudResource(ABC):

    def __init__(self,name,region):
        self.name = name
        self.region=region

    #here i made this method abstract because i want to force the subclasses(inherited classes) to implement it
    @abstractmethod
    def start(self):
        pass

    #Instance method
    @abstractmethod
    def describe(self):
       print(f"Resource: {self.name} is in region: {self.region}")

    @abstractmethod
    def stop(self):
        pass


