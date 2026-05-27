from rest_framework import serializers
from .models import Coin, Trade

class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = "__all__"

class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = "__all__"