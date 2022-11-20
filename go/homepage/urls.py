from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("<int:vacation_id>", views.vacation, name="vacation"),
    path("tropical_options", views.tropical_options, name="tropical_options"),
    path("historical_options", views.historical_options, name="historical_options"),
    path("winter_options", views.winter_options, name="winter_options")



]