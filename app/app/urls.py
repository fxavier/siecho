from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('', include('core.urls', namespace='core')),
    path('api/v1/assistencia-tecnica/', include('assistencia_tecnica.urls')),
    path('api/v1/si-stock/', include('si_stock.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
