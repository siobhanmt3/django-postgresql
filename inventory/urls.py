from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from inventory import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", csrf_exempt(views.create), name="create"),
    path("list/", csrf_exempt(views.list), name="list"),

]