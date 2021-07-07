from rest_framework.permissions import IsAuthenticated
from rest_framework_swagger.views import get_swagger_view
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializer import InvoiceSerializer
from .models import Invoices

schema_view = get_swagger_view(title='PayApp API')


# ViewSets define the view behavior.
class InvoiceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Invoices.objects.all()
    serializer_class = InvoiceSerializer

    def post(self, request, format=None):
        serializer = InvoiceSerializer(data=request.data)
        request.data['user'] = request.user.id

        if serializer.is_valid():
            serializer = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
