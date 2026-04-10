#Constructor
class Factory:
  def __init__(self,material,zips,pockets):
    self.material=material
    self.zips=zips
    self.pockets=pockets
  def showdetails(self):
    print(f"Making a bag use of {self.material} material, with {self.zips} Zips and {self.pockets} Pockets")

Reebook=Factory("Lether",3,3)
Nike=Factory("Cotton",4,2)

Nike.showdetails()