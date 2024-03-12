from rest_framework import serializers

from account.models import Account, AccountManager
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
        manager = AccountManager()
        obj = manager.create_user(email=validated_data.get('email'),
                                  password=validated_data.get('password'),
                                  date_of_birth = validated_data.get('date_of_birth'),
                                  name = validated_data.get('name'))
        return obj
