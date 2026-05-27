import requests  # Certifique-se de ter instalado: pip install requests

class Connection:
    def __init__(self, symbol="SOLUSDT", interval="1m"):
        self.symbol = symbol
        self.interval = interval  # '1m' = 1 minuto, '1h' = 1 hora, etc.
        self.prices = []

    def fetch_market_data(self):
        """Busca o histórico recente do ativo para alimentar as médias móveis"""
        # Endpoint público da Binance para Klines (dados de velas/candlesticks)
        url = f"https://api.binance.com/api/v3/klines?symbol={self.symbol}&interval={self.interval}&limit=50"
        
        try:
            response = requests.get(url, timeout=10)
            data = response.json()
            
            # O índice 4 na resposta da Binance é o preço de FECHAMENTO (Close price) da vela
            self.prices = [float(candle[4]) for candle in data]
            return True
        except Exception as e:
            print(f"❌ Erro de conexão com a API: {e}")
            return False

    def get_current_price(self):
        """Retorna o preço mais recente coletado"""
        if self.prices:
            return self.prices[-1]
        return None

    def calculate_moving_averages(self):
        """Calcula as médias móveis de 7 e 40 ciclos"""
        if len(self.prices) < 40:
            print("⚠️ Dados insuficientes para calcular a média de 40 ciclos.")
            return None, None
        
        # Pega os últimos 7 e 40 preços do nosso histórico
        ma_fast = sum(self.prices[-7:]) / 7
        ma_slow = sum(self.prices[-40:]) / 40
        
        return ma_fast, ma_slow