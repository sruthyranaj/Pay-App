from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from django.conf.urls import url, include
import customers
# existing serializer, viewset, router registrations code
...

# Create our schema's view w/ the get_schema_view() helper method. Pass in the proper Renderers for swagger
schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

# Inlcude the schema view in our urls.
urlpatterns = [
    url(r'^', schema_view, name="docs"),
    url(r'^users/', include(customers.urls)),
]