from users.models import User

def validate_token(token):
    try:
        User.objects.get(
            token = token
        )
        return True

    except Exception:
         return False
    