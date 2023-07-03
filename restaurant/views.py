from django.shortcuts import render
from .models import MenuItem,Booking
from .serializers import MenuItemSerializer,BookingSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,DestroyAPIView

# Create your views here.
def index(request):
     return render(request, 'index.html', {})

class MenuItemView(ListCreateAPIView):
     queryset=MenuItem.objects.all()
     serializer_class=MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateAPIView,DestroyAPIView):
     queryset=MenuItem.objects.all()
     serializer_class=MenuItemSerializer

class BookingViewSet(ModelViewSet):
     queryset=Booking.objects.all()
     serializer_class=BookingSerializer
