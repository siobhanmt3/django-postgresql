from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from users import views

urlpatterns = [
    path("create/", csrf_exempt(views.create), name="create"),
    path("login/", csrf_exempt(views.login), name="login"),
]