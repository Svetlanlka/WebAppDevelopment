from django.db import models
from datetime import datetime

class Donut(models.Model):
    name = models.CharField(max_length=255, default=None)
    info = models.TextField()
    date = models.DateTimeField()
    cost = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='donuts/', default="donut-default.jpg")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пончик'
        verbose_name_plural = 'Пончики'
