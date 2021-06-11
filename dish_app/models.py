from django.db import models


class Ingredient(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.title

class Dish(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='dishes/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    description = models.TextField()
    ingredient = models.ManyToManyField(Ingredient)

    class Meta:
        ordering = ['price']

    def __str__(self):
        return self.title

class DayOfWeek(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)

class MenuForWeek(models.Model):
    day_of_week = models.ForeignKey(DayOfWeek, on_delete=models.CASCADE, related_name='menu')
    breakfast = models.CharField(max_length=200)
    lunch = models.CharField(max_length=200)
    dinner = models.CharField(max_length=200)




