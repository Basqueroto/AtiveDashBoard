from django.db import models

# Create your models here.
class Trade (models.Model):
    SINAL_CHOICES = [
        ('C', 'Compra'),
        ('V', 'Venda'),
    ]
    id = models.AutoField(primary_key=True)
    hora = models.TimeField(auto_now_add=True, verbose_name="Hora da Operação")
    ativo = models.CharField(max_length=10, verbose_name="Ativo (Ex: PETR4)")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    qtd = models.IntegerField(verbose_name="Quantidade")
    sinal = models.CharField(max_length=1, choices=SINAL_CHOICES, verbose_name="Sinal")

    def __str__(self):
        # Isso faz o Django mostrar o resumo bonitinho no painel de administração
        return f"{self.ativo} | {self.sinal} | Qtd: {self.qtd}"

class Coin (models.Model):
    id = models.AutoField(primary_key=True)
    symbol = models.CharField(max_length=20, verbose_name="Símbolo da Moeda (Ex: BTCUSDT)")
    name = models.CharField(max_length=50, verbose_name="Nome da Moeda (Ex: Bitcoin)")

    def __str__(self):
        return f"{self.name} ({self.symbol})"