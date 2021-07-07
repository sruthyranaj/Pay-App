from rest_framework import serializers
from cryptography.fernet import Fernet
from payapp.settings import INVOICE_SECRET, BASE_URL
from .models import Invoices

# Serializers define the API representation.
class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Invoices
        fields = ['id', 'client_name', 'client_email', 'project_name',
                  'amount', 'created_at', 'created_by']

    def save(self, **kwargs):
        """
        Method to create invoice and create the link. Update the link
        in the customer model
        """
        kwargs["created_by"] = self.fields["created_by"].get_default()
        ins = super().save(**kwargs)
        # use invoice secret and invoice id to generate link from the invoice
        fkey = Fernet((str(INVOICE_SECRET)).encode('utf-8'))
        # generate link from the invoice
        encrypted = fkey.encrypt(str(ins.id).encode('utf-8'))
        encrypted = encrypted.decode('utf-8')
        # update invoice with the link
        ins.link = '{base_url}/customers/{path}'.format(
            base_url=BASE_URL, path=encrypted)
        ins.save()
