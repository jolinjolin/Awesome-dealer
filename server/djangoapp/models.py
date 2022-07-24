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

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
