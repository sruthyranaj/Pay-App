from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from owner.views import schema_view
from django.conf.urls import url
from django.contrib import admin
from owner.views import InvoiceViewSet
# Serializers define the API representation.



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register("invoices", InvoiceViewSet)

urlpatterns = [
    url('^$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))
]
