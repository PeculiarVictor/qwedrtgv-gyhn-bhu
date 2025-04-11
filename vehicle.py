# create class
class Vehicle:


    # create init method
    def __init__(self, max__speed, mileage):



          # bind the arguments
          self.max__speed = max__speed
          self.mileage = mileage


          # Object creation
modelX = Vehicle(240, 18)


# access the variables inside init method
print("Model Max speed:",modelX.max__speed)
print("Model Mileage:",modelX.mileage)

