from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get("access_token") 
        if not token:
            return None  

        validated_token = self.get_validated_token(token)
        user = self.get_user(validated_token)

        if user is None:
            raise AuthenticationFailed("User not found")

        return (user, validated_token)
