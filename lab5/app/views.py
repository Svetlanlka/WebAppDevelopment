from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from datetime import date
from app.models import DonutsSet, Donut
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import DonutsSetForm


def index(request):
  sets = DonutsSet.objects.all()

  return render(request, 'index.html', {
      'donuts_sets': sets,
  })

def set(request, id):
  set = DonutsSet.objects.get(pk=id)
  donuts = set.fk_donuts.all()

  context = {'set': set, 'donuts': donuts}
  return render(request, 'set.html', context)

def set_add(request):
  try:
    if request.method == "POST":
      form = DonutsSetForm(request.POST, files=request.FILES)
      if form.is_valid():
        form.save()
        return redirect(reverse('index'))
    else:
      if request.method == 'GET':
        form = DonutsSetForm()
        return render(request, "set_add.html", {"form": form})
    return redirect(reverse('index'))
  except:
    return redirect(request.META.get('HTTP_REFERER'))

def set_edit(request, id):
  try:
    set = DonutsSet.objects.get(pk=id)

    if request.method == "POST":
      set.name = request.POST.get("name")
      set.info = request.POST.get("info")
      set.picture = request.POST.get("picture")
      set.save()
      form = DonutsSetForm(request.POST, files=request.FILES, instance=set)
      if form.is_valid():
        form.save()
        return redirect(reverse('index'))
      else:
        return redirect(request.META.get('HTTP_REFERER'))
    else:
      form = DonutsSetForm(instance=set)
      return render(request, "set_edit.html", {"form": form, 'set': set})
  except DonutsSet.DoesNotExist:
    return HttpResponseNotFound("Donuts set not found")

def set_delete(request, id):
  try:
    set = DonutsSet.objects.get(pk=id)
    set.delete()
    return redirect(reverse('index'))
  except DonutsSet.DoesNotExist:
    return HttpResponseNotFound("Donuts set not found")

def donut_add(request, id):
  set = DonutsSet.objects.get(pk=id)

  if request.method == "POST":
    donut = Donut()
    donut.name = request.POST.get("name")
    donut.info = request.POST.get("info")
    donut.cost = request.POST.get("cost")
    donut.picture = request.POST.get("picture")
    donut.save()
    set.fk_donuts.add(donut)
    set.save()    

  return redirect(request.META.get('HTTP_REFERER'))

def donut_delete(request, id):
  try:
    d = Donut.objects.get(pk=id)
    d.delete()
    return redirect(request.META.get('HTTP_REFERER'))
  except Donut.DoesNotExist:
    return HttpResponseNotFound("Donut not found")

def donut_edit(request, id):
  try:
    donut = Donut.objects.get(pk=id)

    if request.method == "POST":
      donut.name = request.POST.get("name")
      donut.info = request.POST.get("info")
      donut.cost = request.POST.get("cost")
      donut.picture = request.POST.get("picture")
      try:
        donut.save()
        return redirect(reverse('index'))
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
      except:
        return redirect(request.META.get('HTTP_REFERER'))
    else:
      return render(request, "donut_edit.html", {"donut": donut})
  except Donut.DoesNotExist:
    return HttpResponseNotFound("Donut not found")