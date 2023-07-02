import json
import hashlib
import secrets

from django.http import JsonResponse
from users.models import User


def create(request):
    if request.method == "POST":
        data = json.loads(request.body)
        User.objects.create(
            email = data["email"],
            password = hashlib.sha512(data["password"].encode()).hexdigest(),
            token = secrets.token_hex(16),
        )
        return JsonResponse(
            {"message": "user successfully created"},
            status = 201,
        )

    else:
        return JsonResponse(
            {"message": "Method not allowed"},
            status = 405,
        )

def login(request):
    if request.method == "POST":
        data = json.loads(request.body)

        try:
            user = User.objects.get(
                email = data["email"],
                password = hashlib.sha512(data["password"].encode()).hexdigest(),
            )

            return JsonResponse(
                {"token": user.token},
                status = 200,
            )

        except User.DoesNotExist:
            return JsonResponse(
                {"message": "email or password is incorrect"},
                status=401,
            )
    
        except Exception:
            return JsonResponse(
                {"message": "Internal Server Error"},
                status = 500,
            )

        return JsonResponse(
            {"message": "test"},
            status = 200,
        )

    else:
        return JsonResponse(
            {"message": "Method not allowed"},
            status = 405,
        )