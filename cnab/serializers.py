from rest_framework import serializers

from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
    
    def create(self, validated_data: dict):
        transation = Transaction.objects.create(**validated_data)
        return transation