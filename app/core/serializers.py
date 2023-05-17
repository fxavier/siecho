from rest_framework import serializers
from core.models import TxCurrCounter


class TxCurrCounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TxCurrCounter
        fields = ['id', 'date', 'hour', 'value']
        read_only_fields = ('id',)
