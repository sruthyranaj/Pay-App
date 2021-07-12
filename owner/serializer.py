from rest_framework import serializers
from payapp.settings import APP_BASE_URL
from .models import Invoices

# Serializers define the API representation.


class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Invoices
        fields = ['id', 'invoice_number', 'client_name', 'client_email', 'project_name',
                  'amount', 'created_at', 'link', 'status', 'created_by']
        # No need to input from the frontend
        read_only_fields = ['link', 'status']

    def save(self, **kwargs):
        """
        Method to create invoice and create the link. Update the link
        in the customer model
        """
        kwargs["created_by"] = self.fields["created_by"].get_default()
        ins = super().save(**kwargs)
        ins.link = '{base_url}/customers/{path}'.format(
            base_url=APP_BASE_URL, path=ins.invoice_number)
        ins.save()
