from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Coin, Trade
from .serializers import TradeSerializer

from ative_rest.bot.Trigger import Trigger
from ative_rest.bot.Wallet import Wallet
from ative_rest.bot.Solid import Solid
from ative_rest.bot.Connection import Connection

# Create your views here.

minha_conexao = Connection(symbol="SOLUSDT", interval="1m") 
minha_carteira = Wallet(initial_balance=1000.0) 
meu_trigger = Trigger()
    
robo_solid = Solid(wallet=minha_carteira, trigger=meu_trigger, connection=minha_conexao, lucro_alvo_pct=1.5)

@api_view(['GET'])
def getTradeList(request):
    if request.method == 'GET':
        trades = Trade.objects.all()
        serializer = TradeSerializer(trades, many=True)
        return Response(serializer.data)
    return Response({"message": "Método não permitido"}, status=400)

@api_view(['GET'])
def getTradeActual(request):
    if request.method == 'GET':
        nome, ativo, preco_atual, ma_rapida, ma_lenta, sinal = robo_solid.run_cycle()

        dados_bot = {
            "nome": nome,
            "ativo": ativo,
            "preco_atual": preco_atual,
            "ma_rapida": ma_rapida,
            "ma_lenta": ma_lenta,
            "sinal": sinal
        }

        return Response(dados_bot, status=200)

    return Response({"message": "Método não permitido"}, status=400)

@api_view(['GET'])
def getnumber_of_trades(request):
    if request.method == 'GET':
        total_trades = Trade.objects.count()
        return Response({"total_trades": total_trades}, status=200)
    return Response({"message": "Método não permitido"}, status=400)

@api_view(['GET'])
def getbalance(request):
    if request.method == 'GET':
        balance = minha_carteira.balance
        return Response({"balance": balance}, status=200)
    return Response({"message": "Método não permitido"}, status=400)

@api_view(['GET'])
def getTokenNumber(request):
    if request.method == 'GET':
        total_coins = Coin.objects.count()
        return Response({"total_coins": total_coins}, status=200)
    return Response({"message": "Método não permitido"}, status=400)