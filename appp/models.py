from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Worker(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='workers/')

    def __str__(self):
        return self.name

class Menu(models.Model):
    image = models.ImageField(upload_to='menu/')
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'Menu item by {self.worker.name} in {self.category.name}'
