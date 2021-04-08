class PhotoDatabase:
    def __init__(self, photoName, dateTaken):
        self.photoName = photoName
        self.dateTaken = dateTaken
        self.photoOptions = []
        self.event = ""
        self.categories = []

    def newPhoto(self):
        (print(f"{self.photoName} has been added to the database"))
    
    def addCamera(self, cameraType ):
        self.photoOptions.append(cameraType)
    
    def addLocation(self, locationTaken ):
        self.photoOptions.append(locationTaken)
    
    def addEventName(self, eventName):
        self.event = eventName


    def addPhotoCategory(self, photoCategory):
        self.categories.append(photoCategory)


    def photoInfo(self):
        if self.photoOptions:
            print(f"{self.photoName} was taken {self.dateTaken}, additional photo information is as follows {self.photoOptions}")
        else:
            print(f"{self.photoName} was taken {self.dateTaken}, no additional photo information was added")

    def eventCategories(self):
        if self.addPhotoCategory:
            if self.event:
                print(f"{self.photoName}, was taken at the following event {self.event}, and has the following categories {self.categories}")
        else:
            print(f"{self.photoName} is not part of any categories or events")


# adding new Photos
headShot = PhotoDatabase("Melissa's Professional photo", "4/8/21")
ann01 = PhotoDatabase("Family Shot", "4/8/21")
ann02 = PhotoDatabase("Grandkids", "4/8/21")


# Adding other information
headShot.addCamera("Nikon")
headShot.addLocation("Melissa's Studio")

ann01.addLocation("High School")
ann02.addLocation("High School")

ann01.addEventName("Shannon's Graduation")
ann01.addPhotoCategory("Graduation")
ann01.addPhotoCategory("People")

ann02.addEventName("Shannon's Graduation")
ann02.addPhotoCategory("Graduation")
ann02.addPhotoCategory("People")


# Accessing information
headShot.newPhoto()
headShot.photoInfo()
headShot.eventCategories()

ann01.photoInfo()
ann01.eventCategories()
ann02.photoInfo()
ann02.eventCategories()


