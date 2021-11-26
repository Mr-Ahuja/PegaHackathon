from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Movie, VaccinesRegistered, Vaccines
from .serializers import *

from .pagination import CustomPagination
from .filters import MovieFilter

class ListCreateVaccineRegisteredAPIView(ListCreateAPIView):
    serializer_class = VaccinesRegisteredSerializer
    queryset = VaccinesRegistered.objects.all()
    #permission_classes = [IsAuthenticated]
    filter_fields = (
        'username',
    )

class ListCreateVaccineAPIView(ListCreateAPIView):
    serializer_class = VaccinesSerializer
    queryset = Vaccines.objects.all()
    #permission_classes = [IsAuthenticated]


class ListCreateBookingDetailsAPIView(ListCreateAPIView):
    serializer_class = BookingDetailsSerializer
    queryset = BookingDetails.objects.all()

class ListCreateHealthProviderAPIView(ListCreateAPIView):
    serializer_class = HealthProviderSerializer
    queryset = HealthProvider.objects.all()
    filter_fields = (
        'vid','driveDate',
    )