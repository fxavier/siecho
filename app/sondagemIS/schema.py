import graphene 
from graphene_django import DjangoObjectType
from sondagemIS.models import Intervencao, Inquerito, FaixaEtaria, ServicoPrevencao, ServicoCuidadosTratamento, SectorClinico
from assistencia_tecnica.models import Provincia, Distrito, UnidadeSanitaria

class ProvinciaType(DjangoObjectType):
    class Meta:
        model = Provincia
        
class DistritoType(DjangoObjectType):
    class Meta:
        model = Distrito
        
class UnidadeSanitariaType(DjangoObjectType):
    class Meta:
        model = UnidadeSanitaria
        
class IntervencaoType(DjangoObjectType):
    class Meta:
        model = Intervencao
        
class FaixaEtariaType(DjangoObjectType):
    class Meta:
        model = FaixaEtaria
        
class InqueritoType(DjangoObjectType):
    class Meta:
        model = Inquerito
        
class ServicoPrevencaoType(DjangoObjectType):
    class Meta:
        model = ServicoPrevencao
        
class ServicoCuidadosTratamentoType(DjangoObjectType):
    class Meta:
        model = ServicoCuidadosTratamento
        
class SectorClinicoType(DjangoObjectType):
    class Meta:
        model = SectorClinico