from rest_framework import serializers

from .models import CompanyUser, Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ['id']
        
class CompanyUserSerializer(serializers.ModelSerializer):
        
    def create(self, validated_data):
        return CompanyUser.objects.create_standard_user(**validated_data)
    
    class Meta:
        model = CompanyUser
        fields = ['id', 'username', 'password', 'company']
        read_only_fields = ['id']
        extra_kwargs = {'company': {'required': True}}
        
class CompanyUserProfileSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = CompanyUser
        fields = ['id', 'username', 'company']
        read_only_fields = ['id', 'company']
    