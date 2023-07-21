from django.db import models
from django.urls import reverse

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

TREND = (
    ('U', 'Unknown'),
    ('I', 'Increasing'),
    ('D', 'Decreasing')
)

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)
    us_canada_population_estimate = models.IntegerField('U.S/Canada Population Estimate')
    population_trend = models.CharField(
        'Population Trend',
        max_length = 1,
        choices = TREND
        )

    def __str__(self):
        return f'{self.name} - {self.breed}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
    

class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )

    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_meal_display()} on {self.date}'
    class Meta:
        ordering = ['-date']