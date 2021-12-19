from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from datetime import date
from app.models import OperatingSystem, Computer
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ComputerForm

def index(request):
  computers = Computer.objects.all()

  return render(request, 'index.html', {
      'computers': computers,
  })

def computer(request, id):
  c = Computer.objects.get(pk=id)
  operating_systems = OperatingSystem.objects.filter(computer=c)

  context = {'computer': c, 'operating_systems': operating_systems}
  return render(request, 'computer.html', context)

def computer_add(request):
  if request.method == "POST":
    c = Computer()
    c.name = request.POST.get("name")
    c.cost = request.POST.get("cost")
    c.photo = request.POST.get("photo")
    c.save()
  else:
    if request.method == 'GET':
      form = ComputerForm()
      return render(request, "computer_add.html", {"form": form})
  return redirect(reverse('index'))

def computer_edit(request, id):
  try:
    computer = Computer.objects.get(pk=id)

    if request.method == "POST":
      computer.name = request.POST.get("name")
      computer.cost = request.POST.get("cost")
      computer.photo = request.POST.get("photo")
      computer.save()
      return redirect(reverse('index'))
    else:
      form = ComputerForm(instance=computer, files=request.FILES)
      return render(request, "computer_edit.html", {"form": form, 'computer': computer})
  except Computer.DoesNotExist:
    return HttpResponseNotFound("Computer not found")

def computer_delete(request, id):
  try:
    c = Computer.objects.get(id=id)
    c.delete()
    return redirect(reverse('index'))
  except Computer.DoesNotExist:
    return HttpResponseNotFound("Computer not found")