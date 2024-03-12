from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from account.models import Account
from account.serializers import AccountsSerializer, CreateAccountSerializer


# Create your views here.
class AccountsViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer
    permission_classes = [AllowAny]


class SignupViewSet(viewsets.ModelViewSet):
    serializer_class = CreateAccountSerializer
    permission_classes = [AllowAny]
