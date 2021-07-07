from django.views.generic.base import View
from rest_framework.permissions import AllowAny
from rest_framework_swagger.views import get_swagger_view
from rest_framework import viewsets
from django.core.serializers import serialize
from django.http import HttpResponse
from owner.serializer import InvoiceSerializer
from owner.models import Invoices
from payapp.settings import INVOICE_SECRET
from cryptography.fernet import Fernet


schema_view = get_swagger_view(title='PayApp API')


# ViewSets define the view behavior.
class ProcessInvoiceView(viewsets.ModelViewSet):
    """
    Method to process the customer link. If the link is valid 
    then return the customer details to process the split otherwise 
    return the exception message
    """
    permission_classes = [AllowAny]
    queryset = Invoices.objects.all()
    serializer_class = InvoiceSerializer
    
    def get_queryset(request, format=None):
        try:
            invoice_data = request.request.parser_context.get("kwargs")
            invoice_ref = invoice_data.get("invoice_ref")
            # use the same secret key to decode the link that we used to
            # encode the key while generating url
            fkey = Fernet((str(INVOICE_SECRET)).encode('utf-8'))
            decrypted = fkey.decrypt(str(invoice_ref).encode('utf-8'))
            # get the invoice id from the decrypted message and process the
            # invoice
            invoice_id =  str(decrypted.decode('utf-8'))
            instance = Invoices.objects.filter(pk=invoice_id).all()
            return instance
        except:
            raise Exception("unable to find the linked invoice")
   