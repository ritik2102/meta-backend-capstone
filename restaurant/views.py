from django.shortcuts import render
from .models import MenuItem,Booking
from .serializers import MenuItemSerializer,BookingSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,DestroyAPIView
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponse


# Create your views here.
def index(request):
     return render(request, 'index.html', {})

class MenuItemView(ListCreateAPIView):
     queryset=MenuItem.objects.all()
     serializer_class=MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateAPIView,DestroyAPIView):
     queryset=MenuItem.objects.all()
     serializer_class=MenuItemSerializer

@permission_classes([IsAuthenticated])
class BookingViewSet(ModelViewSet):
     queryset=Booking.objects.all()
     serializer_class=BookingSerializer

@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
     return Response({"message":"This view is protected"})