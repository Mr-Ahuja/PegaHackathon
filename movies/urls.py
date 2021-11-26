from django.urls import path
from . import views


urlpatterns = [
    path('booking/', views.ListCreateBookingDetailsAPIView.as_view(), name='get_post_booking'),
    path('healthprovider/', views.ListCreateHealthProviderAPIView.as_view(), name='get_post_healthprovider'),
    path('vaccinesregistered/', views.ListCreateVaccineRegisteredAPIView.as_view(), name='get_post_vaccines_registered'),
    path('vaccines/', views.ListCreateVaccineAPIView.as_view(), name='get_post_vaccines'),
    # path('', views.ListCreateMovieAPIView.as_view(), name='get_post_movies'),
    # path('<int:pk>/', views.RetrieveUpdateDestroyMovieAPIView.as_view(), name='get_delete_update_movie'),
]