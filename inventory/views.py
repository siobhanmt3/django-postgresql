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
        return JsonResponse(
            data,
            status=201,
        )

    else:
        return JsonResponse(
            {"message": "Method not allowed"},
            status=405,
        )


def list(request):
    if request.method == "GET":
        response = [
            {
                "id": inventory.id,
                "name": inventory.name,
                "price": inventory.price,
                "category": inventory.category,
                "identifier": inventory.identifier,
            }
            for inventory in Inventory.objects.all()
        ]
        return JsonResponse({"data": response}, status=200)

    else:
        return JsonResponse(
            {"message": "Method not allowed"},
            status=405,
        )


def get(request, id: int):
    if request.method == "GET":
        try:
            response = Inventory.objects.get(pk=id)

            return JsonResponse(
                {
                    "id": response.id,
                    "name": response.name,
                    "price": response.price,
                    "category": response.category,
                    "identifier": response.identifier,
                },
                status=200,
            )

        except Inventory.DoesNotExist:
            return JsonResponse(
                {
                    "message": f"Object with id {id} does not exists",
                },
                status=404,
            )

        except Exception:
            return JsonResponse(
                {
                    "message": "Internal Server Error",
                },
                status=500,
            )

    else:
        return JsonResponse(
            {"message": "Method not allowed"},
            status=405,
        )


def update(request, id: int):
    data = json.loads(request.body)

    if request.method == "PUT":

        try:
            object_to_update = Inventory.objects.get(pk=id)

            object_to_update.name = data["name"]
            object_to_update.price = data["price"]
            object_to_update.category = data["category"]
            object_to_update.identifier = data["identifier"]

            object_to_update.save()

            return JsonResponse(
                {
                    "id": object_to_update.id,
                    "name": object_to_update.name,
                    "price": object_to_update.price,
                    "category": object_to_update.category,
                    "identifier": object_to_update.identifier,
                },
                status=200,
            )

        except Inventory.DoesNotExist:
            return JsonResponse(
                {
                    "message": f"Object with id {id} does not exists",
                },
                status=404,
            )

        except Exception:
            return JsonResponse(
                {
                    "message": "Internal Server Error",
                },
                status=500,
            )

    else:
        return JsonResponse(
            {"message": "Method not allowed"},
            status=405,
        )
    
def delete(request, id: int):

    if request.method == "DELETE":

        try:
            Inventory.objects.get(pk=id).delete()
            return JsonResponse(
                {
                    "message": "OK"
                },
                status=200,
            )
        except Inventory.DoesNotExist:
            return JsonResponse(
                {
                    "message": f"Object with id {id} does not exists",
                },
                status=404,
            )
        except Exception:
            return JsonResponse(
                {
                    "message": "Internal Server Error",
                },
                status=500,
            )

    else:
        return JsonResponse(
            {"message": "Method not allowed"},
            status=405,
        )
