from django.shortcuts import render

from .models import Vacation

# Create your views here.
def homepage(request):
    return render(request, "homepage/homepage.html", {
        "vacations": Vacation.objects.all
    })

def vacation(request, vacation_id):
    vacation = Vacation.objects.get(pk=vacation_id)
    return render(request, "homepage/vacations.html", {
        "vacation": vacation
    })

# def tropical_options(request):
#     return render(request, "homepage/vacation_options.html", {
#         "vacations": Vacation.objects.filter(destination_type="Tropical")
#     })

def tropical_options(request):
    return render(request, "homepage/Tropical-Options.html", {
        "vacations": Vacation.objects.filter(destination_type="Tropical")
    })

def historical_options(request):
    return render(request, "homepage/Historical-Options.html", {
        "vacations": Vacation.objects.filter(destination_type="Historical")
    })

def winter_options(request):
    return render(request, "homepage/Winter-Options.html", {
        "vacations": Vacation.objects.filter(destination_type="Winter")
    })

def algarve(request):
    return render(request, "homepage/algarve.html", {
        "vacations": Vacation.objects.filter(destination_type="Tropical")
    })

def borabora(request):
    return render(request, "homepage/borabora.html", {
        "vacations": Vacation.objects.filter(destination_type="Tropical")
    })

def maui(request):
    return render(request, "homepage/maui.html", {
        "vacations": Vacation.objects.filter(destination_type="Tropical")
    })

def boulder(request):
    return render(request, "homepage/boulder.html", {
        "vacations": Vacation.objects.filter(destination_type="Winter")
    })

def reykjavik(request):
    return render(request, "homepage/reykjavik.html", {
        "vacations": Vacation.objects.filter(destination_type="Winter")
    })

def anchorage(request):
    return render(request, "homepage/anchorage.html", {
        "vacations": Vacation.objects.filter(destination_type="Winter")
    })

def siberia(request):
    return render(request, "homepage/siberia.html", {
        "vacations": Vacation.objects.filter(destination_type="Winter")
    })

def newyork(request):
    return render(request, "homepage/newyork.html", {
        "vacations": Vacation.objects.filter(destination_type="Historical")
    })

def machupicchu(request):
    return render(request, "homepage/machupicchu.html", {
        "vacations": Vacation.objects.filter(destination_type="Historical")
    })