from rest_framework import serializers
from si_stock.models import Provincia, Sector, Instrumento, Entrada, Requisicao, Aprovacao, Resumo, ResumoVisualizacao

class ProvinciaSerializer(serializers.ModelSerializer):
      
    class Meta:
        model = Provincia
        fields = ['id', 'nome']
        read_only_fields = ('id',)
        
class SectorSerializer(serializers.ModelSerializer):
    instrumentos = serializers.StringRelatedField(many=True, read_only=True)
    provincia = serializers.PrimaryKeyRelatedField(queryset=Provincia.objects.all())
    
    
    class Meta:
        model = Sector
        fields = ['id', 'provincia', 'nome','instrumentos']
        read_only_fields = ('id',)
        
    def get_provincia(self, instance):
        provincia = instance.provincia
        serializer = ProvinciaSerializer(provincia, many=False)
        return serializer.data
        
        
class InstrumentoSerializer(serializers.ModelSerializer):
    provincia = serializers.PrimaryKeyRelatedField(queryset=Provincia.objects.all())
    sector = serializers.PrimaryKeyRelatedField(queryset=Sector.objects.all())
   
    
    class Meta:
        model = Instrumento
        fields = ['id', 'nome', 'stock', 'ano', 'quantidade_necessaria', 'provincia', 'sector']
        read_only_fields = ('id',)
   
        

class EntradaSerializer(serializers.ModelSerializer):
    provincia = serializers.PrimaryKeyRelatedField(queryset=Provincia.objects.all())
    sector = serializers.PrimaryKeyRelatedField(queryset=Sector.objects.all())
    instrumento = serializers.PrimaryKeyRelatedField(queryset=Instrumento.objects.all())
    
    class Meta:
        model = Entrada
        fields = ['id', 'data_entrada', 'fornecedor', 'quantidade', 'instrumento', 'provincia', 'sector', 'feito_em']
        read_only_fields = ('id',)
        
        
        
        
class RequisicaoSerializer(serializers.ModelSerializer):
    provincia = serializers.PrimaryKeyRelatedField(queryset=Provincia.objects.all())
    sector = serializers.PrimaryKeyRelatedField(queryset=Sector.objects.all())
    instrumento = serializers.PrimaryKeyRelatedField(queryset=Instrumento.objects.all())
    
    class Meta:
        model = Requisicao
        fields = ['id', 'data_requisicao', 'provincia', 'sector', 'instrumento', 'quantidade', 'feito_por', 'feito_em', 'status_requisicao']
        read_only_fields = ('id',)
        
class AprovacaoSerializer(serializers.ModelSerializer):
    requisicao = serializers.PrimaryKeyRelatedField(queryset=Requisicao.objects.all())
    
    class Meta:
        model = Aprovacao
        fields = ['id', 'requisicao', 'tipo_aprovacao', 'comentario', 'feito_por', 'feito_em']
        read_only_fields = ('id',)
        
        
class ResumoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Resumo
        fields = '__all__'
        read_only_fields = ('id',)
        
class ResumoVisualizacaoSerializer(serializers.ModelSerializer):
     class Meta:
         model = ResumoVisualizacao
         fields ='__all__'
         read_only_fields = ('id',)
         