from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("<int:vacation_id>", views.vacation, name="vacation"),
    path("tropical_options", views.tropical_options, name="tropical_options"),
    path("historical_options", views.historical_options, name="historical_options"),
    path("winter_options", views.winter_options, name="winter_options"),

    path("algarve", views.algarve, name="algarve"),
    path("borabora", views.borabora, name="borabora"),
    path("maui", views.maui, name="maui"),

    path("boulder", views.boulder, name="boulder"),
    path("reykjavik", views.reykjavik, name="reykjavik"),
    path("anchorage", views.anchorage, name="anchorage"),
    path("siberia", views.siberia, name="siberia"),
    # path("banff", views.banff, name="banff")

    path("newyork", views.newyork, name="newyork"),
    path("machupicchu", views.machupicchu, name="machupicchu")



]