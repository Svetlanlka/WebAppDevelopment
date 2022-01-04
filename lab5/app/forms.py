from django import forms

from django.db import models
from .models import DonutsSet

class DonutsSetForm(forms.ModelForm):
  # picture = forms.ImageField(required=True, label='Choose new photo', widget=forms.FileInput(), upload_to='computers/', default="default-computer.jpg")

  def __init__(self, *args, **kwargs):
    super(DonutsSetForm, self).__init__(*args, **kwargs)

  def save(self, *args, **kwargs):
      set = super().save(*args, **kwargs)
      set.save()

      return set

  class Meta:
      model = DonutsSet
      fields = ('name', 'info', 'picture')