from django import forms

from django.db import models
from .models import Computer

class ComputerForm(forms.ModelForm):
  # photo = forms.ImageField(required=True, label='Choose new photo', widget=forms.FileInput(), upload_to='computers/', default="default-computer.jpg")

  def __init__(self, *args, **kwargs):
    super(ComputerForm, self).__init__(*args, **kwargs)

  def save(self, *args, **kwargs):
      computer = super().save(*args, **kwargs)
      computer.save()

      return computer

  class Meta:
      model = Computer
      fields = ('name', 'cost', 'photo')