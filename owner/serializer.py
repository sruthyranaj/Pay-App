import os
from rest_framework import serializers
from .models import Invoices
from cryptography.fernet import Fernet
from payapp.settings import INVOICE_SECRET
# Serializers define the API representation.
class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Invoices
        fields = ['id', 'client_name', 'client_email', 'project_name', 'amount', 'created_at', 'created_by']
    
    def save(self, **kwargs):
        """Include default for read_only `user` field"""
        kwargs["created_by"] = self.fields["created_by"].get_default()
        ins = super().save(**kwargs)
        fkey = Fernet((str(INVOICE_SECRET)).encode('utf-8'))
        encrypted = fkey.encrypt(str(ins.id).encode('utf-8'))
        print("encrypted", str(ins.id))
        b = Fernet((str(INVOICE_SECRET)).encode('utf-8'))
        decoded_slogan = b.decrypt(encrypted)
        print("decoded_slogan", decoded_slogan)
        encrypted = encrypted.decode('utf-8')
        ins.link=f'https://customers/{encrypted}'
        ins.save()