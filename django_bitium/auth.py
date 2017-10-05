from django.conf import settings
from django.contrib.auth.models import User
import jwt


class BitiumBackend(object) :

    def authenticate(self, payload=None) :

        try :
            userdata = jwt.decode(payload, settings.SECRET_KEY)
        except :
            return None

        email = userdata.get('email')

        try :
            user = User.objects.get(email=email)
        except :
            user = User(
                email=email,
                username=str(email.split('@')[0]),
                is_staff=settings.BITIUM_IS_STAFF or False,
                is_active=settings.BITIUM_IS_ACTIVE or True,
                is_superuser=settings.BITIUM_IS_SUPERUSER or False,
            )
            user.save()

        return user



    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


