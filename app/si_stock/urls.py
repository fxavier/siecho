from django.urls import path, include
from rest_framework.routers import DefaultRouter

from si_stock import views

router = DefaultRouter()
router.register('provincias', views.ProvinciaViewSet)
router.register('sectores', views.SectorViewSet)
router.register('instrumentos', views.InstrumentoViewSet)
# router.register('instrumentos/<int:pk>', views.InstrumentoViewSet)
router.register('requisicoes', views.RequisicaoViewSet)
# router.register('requisicoes/<str:pk>/', views.RequisicaoViewSet)
router.register('entradas', views.EntradaViewSet)
# router.register('entradas/<int:pk>/', views.EntradaViewSet)
router.register('aprovacoes', views.AprovacaoViewSet)
router.register('resumo', views.ResumoViewSet)
router.register('resumo_visualizacoes', views.ResumoVisualizacaoViewSet)



app_name = 'si_stock'

urlpatterns = [
    path('', include(router.urls)),
    # path('requisicoes/<int:pk>/', views.RequisicaoDetailView.as_view()),
    # path('requisicoes/<int:pk>/update/', views.RequisicaoDetailView.as_view()),
]