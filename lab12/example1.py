import math
class Cylinder:
  def __init__(self,radius,height):
    self.radius=radius
    self.height=height
  
  def set_radius(self,radius):
    if radius>0:
      self.radius=radius
    else:
      print("Invalid input")
  def set_height(self,height):
    if height>0:
      self.height=height
    else:
      print("Invalid input")
  def get_radius(self):
    print(self.radius)
  def get_height(self):
    print(self.height)
  def calc_area(self):
    return 2*math.pi*self.radius**2+2*math.pi*self.radius*self.height
  def calc_volume(self):
    return math.pi*self.radius**2*self.height
x=Cylinder(3,5)
print(x.calc_volume())