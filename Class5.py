class vehicle:
  wheel = 4
  def __init__(self):
    self.car = "BUGGATI"
    self.speed = 1000
c1 = vehicle()
c1.car = "FERRARI"
c2 = vehicle()
vehicle.wheel = 8
print(c1.car,c1.speed,c1.wheel)
print(c2.car,c2.speed,c2.wheel)



