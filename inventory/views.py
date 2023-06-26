from django.http import HttpResponse, JsonResponse
import json
from inventory.models import Inventory

def index(request):
    return HttpResponse("Hello world!")

def create(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Inventory.objects.create(
            name=data["name"],
            price=data["price"],
            category=data["category"],
            identifier=data["identifier"],
        )
        return HttpResponse("Created")

    else:
        return HttpResponse("Not Allowed")
    
def list(request):
    if request.method == "GET":
        response = [
            {
                "name": inventory.name,
                "price": inventory.price,
                "category": inventory.category,
                "identifier": inventory.identifier,
            }
            for inventory in Inventory.objects.all()
        ]
        return JsonResponse({"data": response}, status=200)

    else:
        return HttpResponse("Not Allowed")