from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Users.models import User
from Users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self, request):
        data = {key: value for key, value in self.request.query_params.items() if key not in [
            'page']}

        return self.queryset.filter(**data)

    def list(self, request, *args, **kwargs):
        # item_user_ownwer = Clases.objects.filter(owner_user=self.request.user)
        item = self.get_queryset(request)
        page = self.paginate_queryset(item)
        if page:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(item, many=True)
        return Response(serializer.data)