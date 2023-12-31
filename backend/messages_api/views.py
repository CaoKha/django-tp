from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Message

# from messages_api.models import Message


class PublicMessageApiView(APIView):
    def get(self, request, format=None):
        message = Message()
        public_message = message.create("public")
        public_message.save()
        return Response(public_message.text)


class ProtectedMessageApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        message = Message()
        accessToken = request.data.get('access_token')
        protected_message = message.create(accessToken)
        protected_message.save()
        return Response(request.data.get('access_token'))


class AdminMessageApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        messages = "admin"
        return Response(messages)
