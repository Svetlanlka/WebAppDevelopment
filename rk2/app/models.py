from django.db import models
from datetime import datetime, date
from django.utils import timezone

class Computer(models.Model):
  name = models.CharField(max_length=255, default=None)
  photo = models.ImageField(upload_to='', default="default-computer.jpg")
  cost = models.IntegerField(default=0)

  def __str__(self):
      return self.name

  class Meta:
      verbose_name = 'Компьютер'
      verbose_name_plural = 'Компьютеры'

class OperatingSystem(models.Model):
  name = models.CharField(max_length=255, default=None)
  publication_year = models.DateField(default=timezone.now)
  computer = models.ForeignKey('Computer', on_delete=models.CASCADE, default=None) #связь 1 ко многим

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = 'Операционная система'
    verbose_name_plural = 'Операционные системы'
