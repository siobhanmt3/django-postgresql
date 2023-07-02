from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from inventory import views

urlpatterns = [
    path("create/", csrf_exempt(views.create), name="create"),
    path("list/", views.list, name="list"),
    path("get/<int:id>", views.get, name="get"),
    path("update/<int:id>", csrf_exempt(views.update), name="update"),
     path("delete/<int:id>", csrf_exempt(views.delete), name="delete"),

]