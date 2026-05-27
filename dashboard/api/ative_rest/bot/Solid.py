from .Trigger import Trigger
from .Wallet import Wallet
from .Connection import Connection

class Solid:
    def __init__(self, wallet: Wallet, trigger: Trigger, connection: Connection, lucro_alvo_pct=1.5):
        self.wallet = wallet
        self.trigger = trigger
        self.connection = connection
        self.lucro_alvo_pct = lucro_alvo_pct  # 🔥 Configura a meta de lucro em % (ex: 1.5%)

    def run_cycle(self):
        print(f"\n🔄 Atualizando ciclo para {self.connection.symbol}...")
        
        # 1. Busca os dados reais do mercado através da Connection
        if not self.connection.fetch_market_data():
            return  # Se falhar a conexão, pula este ciclo

        current_price = self.connection.get_current_price()
        ma_fast, ma_slow = self.connection.calculate_moving_averages()
        
        if current_price is None or ma_fast is None or ma_slow is None:
            print("⚠️ Aguardando carregamento completo de indicadores da API...")
            return

        print(f"Preço Atual: ${current_price:.2f} | Média Rápida (7): {ma_fast:.2f} | Média Lenta (40): {ma_slow:.2f}")
        

        # 2. NOVO: Se o robô já está comprado, verifica primeiro se bateu a meta de lucro no topo
        if self.wallet.positions > 0:
            preco_compra = self.wallet.last_buy_price
            lucro_atual = ((current_price - preco_compra) / preco_compra) * 100
            print(f"📈 Progresso do Trade: {lucro_atual:.2f}% / Meta Alvo: {self.lucro_alvo_pct}%")
            
            if lucro_atual >= self.lucro_alvo_pct:
                print(f"🎯 META ATINGIDA no topo! Lucro de {lucro_atual:.2f}%. Executando venda imediata.")
                self.wallet.execute_trade("VENDER", current_price)
                return  # Finaliza o ciclo com o lucro garantido

        # 3. Caso não tenha atingido a meta (ou não esteja posicionado), segue as regras do Trigger
        signal = self.trigger.evaluate(ma_fast, ma_slow)
        print(f"Sinal do Trigger: {signal}")

        if signal == "COMPRAR" and self.wallet.positions == 0:
            self.wallet.execute_trade("COMPRAR", current_price)
        elif signal == "VENDER" and self.wallet.positions > 0:
            print("⚠️ Saída antecipada: Média móvel cruzou para baixo antes da meta de lucro.")
            self.wallet.execute_trade("VENDER", current_price)
        else:
            print("⏳ Condição mantida. Nenhuma ordem disparada.")
        
        return "Solana", "SOLUSDT", current_price, ma_fast, ma_slow, signal