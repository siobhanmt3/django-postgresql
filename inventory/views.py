from django.http import HttpResponse, JsonResponse
import json
from inventory.models import Inventory
from inventory.utils.auth import validate_token


def create(request):
    if request.method == "POST":

        token_is_valid = validate_token(request.headers["X-Token"])

        if not token_is_valid:
            return JsonResponse(
                {
                    "message": "Invalid token"
                }, status = 401
            )
        
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

        token_is_valid = validate_token(request.headers["X-Token"])

        if not token_is_valid:
            return JsonResponse(
                {
                    "message": "Invalid token"
                }, status = 401
            )
        
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

        token_is_valid = validate_token(request.headers["X-Token"])

        if not token_is_valid:
            return JsonResponse(
                {
                    "message": "Invalid token"
                }, status = 401
            )
        
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

        token_is_valid = validate_token(request.headers["X-Token"])

        if not token_is_valid:
            return JsonResponse(
                {
                    "message": "Invalid token"
                }, status = 401
            )
        
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

        token_is_valid = validate_token(request.headers["X-Token"])

        if not token_is_valid:
            return JsonResponse(
                {
                    "message": "Invalid token"
                }, status = 401
            )

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
