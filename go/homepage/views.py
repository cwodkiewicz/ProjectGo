from django.shortcuts import render

from .models import Vacation

# Create your views here.
def homepage(request):
    return render(request, "homepage/homepage.html")

def vacation(request, vacation_id):
    vacation = Vacation.objects.get(pk=vacation_id)
    return render(request, "homepage/vacations.html", {
        "vacation": vacation
    })

def tropical_options(request):
    return render(request, "homepage/vacation_options.html", {
        "vacations": Vacation.objects.filter(destination_type="Tropical")
    })

def historical_options(request):
    return render(request, "homepage/vacation_options.html", {
        "vacations": Vacation.objects.filter(destination_type="Historical")
    })

def winter_options(request):
    return render(request, "homepage/vacation_options.html", {
        "vacations": Vacation.objects.filter(destination_type="Winter")
    })


