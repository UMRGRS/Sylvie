from rest_framework import serializers

from .models import CompanyUser, Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ['id']
        
class CompanyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyUser
        fields = ['id', 'username', 'password', 'company']
        read_only_fields = ['id', 'company']