from datetime import datetime
from ative_rest.models import Trade

class Wallet:
    def __init__(self, initial_balance=10000.0):
        self.initial_balance = initial_balance  # Guardamos o valor inicial para o resumo
        self.balance = initial_balance
        self.positions = 0.0                    # Quantidade acumulada do ativo
        self.trade_history = []                 # Registro de todas as operações feitas
        self.last_buy_price = 0.0               # 🔥 NOVO: Guarda o preço do último ponto de compra

    def execute_trade(self, action, current_price):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if action == "COMPRAR" and self.balance > 0:
            self.positions = self.balance / current_price
            self.last_buy_price = current_price  # 🔥 Salva o preço onde comprou
            self.balance = 0.0
            
            # Registra a operação de compra
            self.trade_history.append({
                "horario": timestamp,
                "acao": "COMPRA",
                "preco": current_price,
                "unidades": self.positions,
                "saldo_restante": self.balance
            })
            print(f"🛒 COMPRA executada! Preço: ${current_price:.2f} | Comprado: {self.positions:.4f} unidades")

            try:
                Trade.objects.create(
                    ativo="SOLUSDT",         
                    preco=current_price,
                    qtd=int(self.positions),     
                    sinal='V'                
                )
                print("💾 Venda salva no banco de dados com sucesso!")
            except Exception as e:
                print(f"❌ Erro ao salvar venda no banco: {e}")
        
        elif action == "VENDER" and self.positions > 0:
            units_sold = self.positions
            self.balance = self.positions * current_price
            self.positions = 0.0
            self.last_buy_price = 0.0  # 🔥 Zera o preço de compra pois saímos do mercado
            
            # Registra a operação de venda
            self.trade_history.append({
                "horario": timestamp,
                "acao": "VENDA",
                "preco": current_price,
                "unidades": units_sold,
                "saldo_restante": self.balance
            })
            print(f"💰 VENDA executada! Preço: ${current_price:.2f} | Novo Saldo: ${self.balance:.2f}")

            try:
                Trade.objects.create(
                    ativo="SOLUSDT",         
                    preco=current_price,
                    qtd=int(units_sold),     
                    sinal='V'                
                )
                print("💾 Venda salva no banco de dados com sucesso!")
            except Exception as e:
                print(f"❌ Erro ao salvar venda no banco: {e}")
        

    def get_trade_history(self):
        """Retorna o registro completo de todas as operações feitas"""
        print("\n=== HISTÓRICO COMPLETO DE OPERAÇÕES ===")
        if not self.trade_history:
            print("Nenhuma operação realizada ainda.")
            return self.trade_history
            
        for i, trade in enumerate(self.trade_history, 1):
            print(f"[{i}] {trade['horario']} | {trade['acao']} | Preço: ${trade['preco']:.2f} | Qtd: {trade['unidades']:.4f} | Saldo: ${trade['saldo_restante']:.2f}")
        
        return self.trade_history

    def get_performance_summary(self):
        """Retorna um resumo de desempenho de toda a operação do robô"""
        saldo_final_estimado = self.balance
        
        status_atual = "Em Dinheiro (Líquido)"
        if self.positions > 0:
            status_atual = f"Posicionado em Ativo ({self.positions:.4f} unidades)"

        lucro_prejuizo_abs = saldo_final_estimado - self.initial_balance
        lucro_prejuizo_perc = (lucro_prejuizo_abs / self.initial_balance) * 100

        print("\n📊 === RESUMO DE DESEMPENHO EM OPERAÇÃO ===")
        print(f"💰 Saldo Inicial:      ${self.initial_balance:.2f}")
        print(f"💵 Saldo Final Atual:  ${saldo_final_estimado:.2f}")
        print(f"📈 Lucro/Prejuízo ($): ${lucro_prejuizo_abs:.2f}")
        print(f"📉 Lucro/Prejuízo (%): {lucro_prejuizo_perc:.2f}%")
        print(f"🗂️ Total de Trades:    {len(self.trade_history)}")
        print(f"🔄 Status da Carteira: {status_atual}")
        print("===========================================")
        
        return {
            "saldo_inicial": self.initial_balance,
            "saldo_final": saldo_final_estimado,
            "pnl_absolute": lucro_prejuizo_abs,
            "pnl_percentual": lucro_prejuizo_perc,
            "total_trades": len(self.trade_history)
        }