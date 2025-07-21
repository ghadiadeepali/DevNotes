from django.shortcuts import render
from rest_framework.decorators import api_view
from users import serializers
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(["POST"])
def user_registration_view(request):

    if request.method == "POST":
            # check if both passwords match
        password1 = request.data.get("password")
        password2 = request.data.get("password2")
        if password1 != password2:
            return Response({"msg": "Passwords do not match. Please re-enter passwords"},status=status.HTTP_400_BAD_REQUEST )
        serializer = serializers.UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data