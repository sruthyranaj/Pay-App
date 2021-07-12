from rest_framework.permissions import AllowAny
from rest_framework_swagger.views import get_swagger_view
from rest_framework import viewsets
from owner.serializer import InvoiceSerializer
from owner.models import Invoices


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
            instance = Invoices.objects.filter(
                invoice_number=invoice_ref, status=True).all()
            return instance
        except:
            return []
