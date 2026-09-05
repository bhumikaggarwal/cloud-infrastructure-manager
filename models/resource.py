#we are creating here our base class

class CloudResource:

    def __init__(self,name,region):
        self.name = name
        self.region=region

    #Instance method
    def describe(self):
       print(f"Resource: {self.name} is in region: {self.region}")


