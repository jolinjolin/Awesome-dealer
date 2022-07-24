from django.db import models
from django.utils.timezone import now

class CarMake(models.Model):
    name = models.CharField(null=False, max_length=100, default='Toyota')
    description = models.CharField(max_length=1000)

    def __str__(self):
        return "Name: " + self.name

class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    id = models.IntegerField(default=1,primary_key=True)
    name = models.CharField(max_length=100)
    year = models.DateField()
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    CROSSOVER = 'Crossover'
    VAN = 'Van'
    TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (CROSSOVER, 'Crossover'),
        (VAN, 'Van')
    ]
    type = models.CharField(
        null=False,
        max_length=100,
        choices=TYPES,
        default=SEDAN
    )

    def __str__(self):
        return "Name: " + self.name

class CarDealer:

    def __init__(self, address, city, id, lat, long, st, zip, full_name):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
       
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long

        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

        # Full name
        self.full_name = full_name

    def __str__(self):
        return "Dealer name: " + self.full_name


class DealerReview:

    def __init__(self, dealership, name, purchase, review):
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        self.purchase_date = ""
        self.purchase_make = ""
        self.purchase_model = ""
        self.purchase_year = ""
        self.sentiment = ""
        self.id = ""

    def __str__(self):
        return "Review: " + self.review
