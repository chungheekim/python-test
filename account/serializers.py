from rest_framework import serializers

from account.models import Account
from bike.models import Bike


class AccountsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ['name', 'email', 'password']


class CreateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['name', 'email', 'password', 'date_of_birth']

    def create(self, validated_data):
        account = Account(name=validated_data.get('name'),
                          email=validated_data.get('email'),
                          password=validated_data.get('password'),
                          date_of_birth=validated_data.get('date_of_birth'))
        account.save()
        return account
