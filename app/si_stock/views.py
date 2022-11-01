from rest_framework import viewsets, mixins, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from si_stock.models import Provincia, Sector, Instrumento, Entrada, Requisicao, Aprovacao, Resumo, ResumoVisualizacao

from si_stock import serializers

def _params_to_int(qs):
        return int(qs)

class ProvinciaViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       viewsets.GenericViewSet):
    queryset = Provincia.objects.all()
    serializer_class = serializers.ProvinciaSerializer
    

    
class SectorViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Sector.objects.all()
    serializer_class = serializers.SectorSerializer
    
    def perform_create(self, serializer):
        serializer.save(provincia=self.request.provincia)
   

class InstrumentoViewSet(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         viewsets.GenericViewSet):
    queryset = Instrumento.objects.all()
    serializer_class = serializers.InstrumentoSerializer
    lookup_field = 'pk'

    
class EntradaViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Entrada.objects.all()
    serializer_class = serializers.EntradaSerializer
    lookup_field = 'pk'
    

class RequisicaoViewSet(viewsets.GenericViewSet, 
                        mixins.ListModelMixin, 
                        mixins.CreateModelMixin, 
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin):
    queryset = Requisicao.objects.all()
    serializer_class = serializers.RequisicaoSerializer
    lookup_field = 'pk'
    
#
      
    

class AprovacaoViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):
    queryset = Aprovacao.objects.all()
    serializer_class = serializers.AprovacaoSerializer
    lookup_field = 'pk'
    
    
class ResumoViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Resumo.objects.raw("select 1 as id, p.nome AS provincia, s.nome AS sector, i.nome AS instrumento, i.stock,"\
                                  "i.quantidade_necessaria AS necessidade,  e.data_entrada, e.quantidade, e.fornecedor,"\
                                  "r.data_requisicao, r.quantidade AS quantidade_requisitada, r.status_requisicao from si_stock_instrumento i" \
                                  " inner join si_stock_sector s on s.id=i.sector_id" \
                                  " inner join si_stock_provincia p on i.provincia_id=p.id" \
                                  " left join si_stock_entrada e on e.instrumento_id=i.id" \
                                  " left join si_stock_requisicao r on r.instrumento_id=i.id"
                                   )
    serializer_class = serializers.ResumoSerializer
    
class ResumoVisualizacaoViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset =  ResumoVisualizacao.objects.raw("select 1 AS id, i.nome AS instrumento, sum(e.quantidade) AS ECHO_MISAU, sum(i.quantidade_necessaria) Necessidade," \
                                               "sum(i.stock) AS  Stock_actual from si_stock_entrada e inner join si_stock_instrumento i on i.id=e.instrumento_id group by i.nome"
                                               )
    
    serializer_class = serializers.ResumoVisualizacaoSerializer
    
