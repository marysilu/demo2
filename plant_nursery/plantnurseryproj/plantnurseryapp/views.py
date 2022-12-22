from django.shortcuts import render, HttpResponse, redirect
from .models import Plants
from .forms import PlantForm


# Create your views here.
def home(request):
    plant = Plants.objects.all()  # fetching all details from database
    context = {'plant': plant}
    return render(request, 'home.html', context)


def detail(request, plant_id):
    plant = Plants.objects.get(id=plant_id)
    return render(request, 'detail.html', {'plant': plant})
    # return HttpResponse("This Plant is %s" % plant_id)


def add(request):
    if request.method == "POST":
        pcod = request.POST.get('cod')
        pname = request.POST.get('name')
        pcat = request.POST.get('type')
        rate = request.POST.get('rate')
        img = request.FILES['img']
        plant = Plants(pcod=pcod, pname=pname, pcat=pcat, rate=rate, img=img)
        plant.save()
        return redirect('/')
    return render(request, 'add.html')


def update(request, plant_id):
    plant = Plants.objects.get(id=plant_id)
    form = PlantForm(request.POST or None, request.FILES, instance=plant)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'plant': plant})


def delete(request, plant_id):
    if request.method=='POST':
        plant = Plants.objects.get(id=plant_id)
        plant.delete()
        return redirect('/')
    return render(request,'delete.html')
