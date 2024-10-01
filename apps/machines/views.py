from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .permissions import IsCompanyAdmin

from .serializers import MachineSerializer, AdminMachineSerializer, DataLogsSerializer

from .models import Machine, DataLogs

# Views marked as Admin- are for inner use and should not be expose yet

class AdminCreateMachine(generics.CreateAPIView):
    permission_classes = [IsAdminUser, IsAuthenticated]
    serializer_class = AdminMachineSerializer
    
class AdminGetUpdateDeleteMachine(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser, IsAuthenticated]
    serializer_class = AdminMachineSerializer
    queryset = Machine.objects.all()
    
class GetMachine(generics.RetrieveAPIView):
    serializer_class = MachineSerializer
    
    def get_queryset(self):
        user_company = self.request.user.company
        return Machine.objects.filter(company=user_company)
    
class UpdateMachine(generics.UpdateAPIView):
    serializer_class = MachineSerializer
    permission_classes = [IsCompanyAdmin, IsAuthenticated]
    
    def get_queryset(self):
        user_company = self.request.user.company
        return Machine.objects.filter(company=user_company)

class DeleteMachine(generics.DestroyAPIView):
    serializer_class = MachineSerializer
    permission_classes = [IsCompanyAdmin, IsAuthenticated]
    
    def get_queryset(self):
        user_company = self.request.user.company
        return Machine.objects.filter(company=user_company)
    
class GetDataLogs(APIView):    
    def get_machine(self, pk):
        machine = get_object_or_404(Machine, pk=pk)
        return machine
    
    def post(self, request, pk):
        if 'start_date' not in request.data or 'end_date' not in request.data:
            return Response({'error': 'start_date and end_date fields are required'},status=status.HTTP_400_BAD_REQUEST)
        
        machine = self.get_machine(pk=pk)
        
        data_logs = DataLogs.objects.filter(machine=machine, time__range=(request.data['start_date'], request.data['end_date']))
        
        if data_logs.count() == 0:
            return Response({'Not found': 'No logs were found for this machine'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DataLogsSerializer(data_logs, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)