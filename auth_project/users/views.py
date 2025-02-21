from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import JsonResponse

User = get_user_model()
@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    
    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already taken"}, status=400)

    user = User.objects.create_user(username=username, email=email, password=password)
    return Response({"message": "User registered successfully!"})

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response({"error": "Username and password are required"}, status=400)
    
    user = authenticate(username=username, password=password)
    
    if user is None:
        return Response({"error": "Invalid credentials"}, status=400)

    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token) 
    print(f"Access token: {access_token}")
    response = JsonResponse({"message": "Login successful"})
    response.set_cookie(
        key="access_token",
        value=str(refresh.access_token),
        httponly=True,
        samesite="None",
        secure=True, 
        max_age=6
    )
    return response


@api_view(['POST'])
def logout(request):
    response = Response({"message": "Logged out"})
    response.delete_cookie("access_token")
    return response


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_details(request):
    user = request.user  
    
    if not user:
        return Response({"error": "No user found"}, status=401)
    
    return Response({"username": user.username})

