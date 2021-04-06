class Garden:
    def __init__(self, gardenName, gardenLocation, sunLevel, gardenSize):
        self.gardenName = gardenName
        self.gardenLocation = gardenLocation
        self.sunLevel = sunLevel
        self.gardenSize = gardenSize
        self.plants = []
        self.tours = ""


    def gardenInfo(self):
        print(f"{self.gardenName} is located in {self.gardenLocation}.  {self.gardenName} is {self.gardenSize}sq/ft and is in the sun {self.sunLevel}% of the day")

    def addPlants(self, plantName):
        self.plants.append(plantName)

    def inventory(self):
        if self.plants:
            print(f"{self.gardenName} currently has the following plants for you to look and learn about {self.plants}")
        else:
            print(f"{self.gardenName} is currently still being added to and does not have any plants at this time.")

    def addTours(self, toursAvail):
        self.tours = toursAvail

    def tourInfo(self):
        if self.tours:
            print(f"{self.gardenName} currently has {self.tours} upon request.  Please call for more information")
        else:
            print(f"{self.gardenName} currently does not offer tours")



irish = Garden("Irish Gardens", "Berwick, PA", 50, 64)
botanical = Garden("Hawaii Botanical Gardens", "Honolulu, HI", 100, 90)

irish.addPlants("Tulips")
irish.addPlants("Roses")

botanical.addTours("3 different types of tours available")

irish.gardenInfo()
botanical.gardenInfo()

irish.inventory()
botanical.inventory()

irish.tourInfo()
botanical.tourInfo()