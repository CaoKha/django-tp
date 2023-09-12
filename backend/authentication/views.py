from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class LoginView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {"message": "Welcome to the Social Authentication (Email) page"}
        return Response(content)


# Create your views here.