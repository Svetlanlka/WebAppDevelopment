from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
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
    c = Computer.objects.get(pk=id)
    c.delete()
    return redirect(reverse('index'))
  except Computer.DoesNotExist:
    return HttpResponseNotFound("Computer not found")

def os_add(request, id):
  computer = Computer.objects.get(pk=id)

  if request.method == "POST":
    os = OperatingSystem()
    os.name = request.POST.get("name")
    os.publication_year = request.POST.get("publication_year")
    os.computer = computer
    os.save()
  else:
    if request.method == 'GET':
      return render(request, "computer.html")

  return HttpResponseRedirect("/")

def os_delete(request, id):
  try:
    os = OperatingSystem.objects.get(pk=id)
    os.delete()
    return HttpResponseRedirect("/")
  except Computer.DoesNotExist:
    return HttpResponseNotFound("OperatingSystem not found")

def os_edit(request, id):
  try:
    os = OperatingSystem.objects.get(pk=id)

    if request.method == "POST":
      os.name = request.POST.get("name")
      os.publication_year = request.POST.get("publication_year")
      os.save()
      return HttpResponseRedirect("/")
    else:
      return render(request, "os_edit.html", {"os_edit": os})

  except Computer.DoesNotExist:
    return HttpResponseNotFound("Computer not found")

def report(request):
    operating_systems = OperatingSystem.objects.all()
    computers = Computer.objects.all()

    operating_systems_join_computers = [{'operating_systems': o, 'computers': c}
      for c in computers
      for o in operating_systems
      if o.computer.id == c.id
    ]

    return render(request, 'report.html', {'r': operating_systems_join_computers, 'oss': operating_systems, 'computers': computers})