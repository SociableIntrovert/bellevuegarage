class Vehicle():
    """The Vehicle class is a base class for cars and trucks"""
    
    def __init__(self, make, model, color, fuelType, options):
        """Initialize a few fields of the vehicle"""
        self.make = make
        self.model = model
        self.color = color
        self.fuelType = fuelType
        self.options = options
    
    def getMake(self):
        return self.make
    
    def getModel(self):
        return self.model 
    
    def getColor(self):
        return self.color 
    
    def getFuelType(self):
        return self.fuelType
    
    def getOptions(self):
        return self.options

class Car(Vehicle):
    """The Car class extends the vehicle class"""
    def __init__(self, make='Toyota', model='Supra', color='Orange', fuelType='Gasoline', options=[], engineSize='3.0L', numDoors='2'):
        """Initialize the parent class and the child class"""
        Vehicle.__init__(self, make, model, color, fuelType, options)
        self.engineSize = engineSize 
        self.numDoors = numDoors 
    
    def getEngineSize(self):
        return self.engineSize
    
    def getNumDoors(self):
        return self.numDoors

class Pickup(Vehicle):
    """The Pickup class extends the vehicle class"""
    def __init__(self, make='Ford', model='Lightning', color='Red', fuelType='Gasoline', options=[], cabStyle='Standard', bedLength='Long'):
        Vehicle.__init__(self, make, model, color, fuelType, options)
        self.cabStyle = cabStyle
        self.bedLength = bedLength
    
    def getCabStyle(self):
        return self.cabStyle
    
    def getBedLength(self):
        return self.bedLength
