from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import ProcessInvoiceSerializer


class ProcessInvoiceViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = ProcessInvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

# Create your views here.
