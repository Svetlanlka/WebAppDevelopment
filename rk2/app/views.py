from django.http.response import JsonResponse
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
  try:
    if request.method == "POST":
      form = ComputerForm(request.POST, files=request.FILES)
      if form.is_valid():
        form.save()
        return redirect(reverse('index'))
    else:
      if request.method == 'GET':
        form = ComputerForm()
        return render(request, "computer_add.html", {"form": form})
    return redirect(reverse('index'))
  except:
    return redirect(request.META.get('HTTP_REFERER'))

def computer_edit(request, id):
  try:
    computer = Computer.objects.get(pk=id)

    if request.method == "POST":
      computer.name = request.POST.get("name")
      computer.cost = request.POST.get("cost")
      computer.photo = request.POST.get("photo")
      computer.save()
      form = ComputerForm(request.POST, files=request.FILES, instance=computer)
      if form.is_valid():
        form.save()
        return redirect(reverse('index'))
      else:
        return redirect(request.META.get('HTTP_REFERER'))
    else:
      form = ComputerForm(instance=computer)
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
    print(os)
    os.save()

  return redirect(request.META.get('HTTP_REFERER'))

def os_delete(request, id):
  try:
    os = OperatingSystem.objects.get(pk=id)
    os.delete()
    return redirect(request.META.get('HTTP_REFERER'))
  except Computer.DoesNotExist:
    return HttpResponseNotFound("OperatingSystem not found")

def os_edit(request, id):
  try:
    os = OperatingSystem.objects.get(pk=id)

    if request.method == "POST":
      os.name = request.POST.get("name")
      os.publication_year = request.POST.get("publication_year")
      try:
        os.save()
        return redirect(reverse('index'))
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
      except:
        return redirect(request.META.get('HTTP_REFERER'))
    else:
      return render(request, "os_edit.html", {"os": os})
  except Computer.DoesNotExist:
    return HttpResponseNotFound("Operation System not found")

def report(request):
  operating_systems = OperatingSystem.objects.all()
  computers = Computer.objects.all()

  operating_systems_join_computers = [{'operating_systems': o, 'computers': c}
    for c in computers
    for o in operating_systems
    if o.computer.id == c.id
  ]

  computer_sum_count_dict = {}
  for os_computers_row in operating_systems_join_computers:
    computer_name = os_computers_row['computers'].name
    # os_publication_year = os_computers_row['operating_systems'].publication_year
    os_name = os_computers_row['operating_systems'].name

    if computer_name in computer_sum_count_dict:
      computer_sum_count_dict[computer_name].append(os_name)
    else:
      computer_sum_count_dict[computer_name] = [os_name,]
  
  for c in computers:
    if c not in computer_sum_count_dict:
      computer_sum_count_dict[c] = ['Нет операционных систем']

  return render(request, 'report.html', {'os_comp': computer_sum_count_dict})