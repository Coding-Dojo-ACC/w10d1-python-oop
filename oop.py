class Zoo:
    def __init__(self, name, location, animalTypes, hours, ticket):
        self.name = name
        self.location = location
        self.animalTypes = animalTypes
        self.hours = hours
        self.ticket = ticket
        self.animals = []
        self.shops = []
        self.parking = ""

    def welcome(self):
        print(f"Welcome to the {self.name}!")
    
    def welcoming(self):
        print(f"Welcome to the {self.name}! Our hours of operation are {self.hours} and ticket prices are ${self.ticket}.  We are located in {self.location}, and we have {self.animalTypes} animal types located on the property.")
        if self.parking:
            print(f"We have the following parking options available:  {self.parking}")
        # print("Welcome to the {}! Out hours of operation are {} and ticket prices are ${}.  We are located in {} and have {} animal types located on the property.".format(self.name, self.hours, self.ticket, self.location, self.animalTypes))
    
    def addAnimal(self, species):
        self.animals.append(species)

    def addShops(self, shopName):
        self.shops.append(shopName)

    def addParking(self, zooParking):
        self.parking = zooParking

    def types(self):
        print(f"Here are our different types of animals: {self.animals}")

    def businesses(self):
        print(f"Here is a list of the different shops on site: {self.shops}")

ninja = Zoo("Ninja Zoo", "H-town, TX", 5, "9-5pm M-F 9-9pm Sat", 15)
ninja.addParking("50 dedicated parking spots")

ninja.welcome()
ninja.welcoming()

ninja.addAnimal("Giraffes")
ninja.addAnimal("Tigers")
ninja.addAnimal("Zebras")
ninja.addAnimal("Bears")
ninja.addAnimal("Horses")

ninja.addShops("Ninja Gifts")
ninja.addShops("Dojo Souvenirs")

ninja.types()
ninja.businesses()

berwick = Zoo("Berwick Zoo", "Berwick, PA", 3, "9-5 M/W/F", 10)

berwick.addParking("Street Parking only")

berwick.welcoming()

berwick.addAnimal("Cats")
berwick.addAnimal("Dogs")
berwick.addAnimal("Horses")

berwick.types()