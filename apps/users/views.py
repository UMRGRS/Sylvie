from django.shortcuts import get_object_or_404
from knox.views import LoginView as KnoxLoginView

from rest_framework.authentication import BasicAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .serializers import CompanySerializer, CompanyUserSerializer, CompanyUserProfileSerializer

from .models import Company, CompanyUser

# Views marked as Admin are for inner use and should not be expose yet

# Company views
class AdminCreateCompany(APIView):
    serializer_class = CompanySerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    
    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminGetUpdateDeleteCompany(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = Company.objects.all()

# Users views
class AdminCreateUser(APIView):
    serializer_class = CompanyUser
    permission_classes = [IsAdminUser, IsAuthenticated]
    def post(self, request):
        serializer = CompanyUserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            response_data = serializer.data
            response_data.pop('password', None)
            return Response(response_data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AdminGetUpdateDeleteUser(generics.DestroyAPIView):
    permission_classes = [IsAdminUser, IsAuthenticated]
    serializer_class = CompanyUserSerializer
    queryset = CompanyUser.objects.all()
    
    def getUser(self, pk):
        user = get_object_or_404(CompanyUser, pk=pk)
        return user
    
    def setPassword(self, user, password):
        user.set_password(password)
        user.save()
    
    def patch(self, request, pk):
        user = self.getUser(pk)
        if 'password' in request.data:
            request.data._mutable = True
            self.setPassword(user, request.data.pop('password', None)[0])
            request.data._mutable = False
        serializer = CompanyUserSerializer(user, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            response_data = serializer.data
            response_data.pop('password', None)
            return Response(response_data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetCurrentUser(APIView):
    def get(self, request):
        user = request.user
        serializer = CompanyUserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Knox view for getting token via basic auth
class LoginView(KnoxLoginView):
    authentication_classes = [BasicAuthentication]