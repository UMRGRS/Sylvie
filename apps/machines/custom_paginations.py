from rest_framework import pagination

class MachinesPagination(pagination.PageNumberPagination):
    page_size = 5