import time
import sys

from Trigger import Trigger
from Wallet import Wallet
from Solid import Solid
from Connection import Connection

if __name__ == "__main__":
    # Inicializando os módulos para Solana
    minha_conexao = Connection(symbol="SOLUSDT", interval="1m") 
    minha_carteira = Wallet(initial_balance=1000.0) 
    meu_trigger = Trigger()
    
    # Instancia o Solid passando nossa carteira, gatilho e conexão ativa
    robo_solid = Solid(wallet=minha_carteira, trigger=meu_trigger, connection=minha_conexao, lucro_alvo_pct=1.5)

    print("🚀 Robô Solid iniciado. Pressione CTRL+C a qualquer momento para interromper.")

    try:
        # Loop contínuo de varredura de mercado
        while True: 
            robo_solid.run_cycle()
            time.sleep(30)  # Varre a API a cada 30 segundos
            
    except KeyboardInterrupt:
        print("\n\n🛑 [INTERRUPÇÃO] Você acionou a parada manual do Robô Solid.")
        print("Escolha uma ação para finalizar:")
        print("[ 1 ] 🚨 BOTAO DE PÂNICO: Vender tudo a preço de mercado e encerrar")
        print("[ 2 ] 🚪 APENAS ENCERRAR: Fechar o bot mantendo as posições atuais")
        
        opcao = input("Digite a opção desejada (1 ou 2): ").strip()
        
        if opcao == "1":
            print("\n🔄 Executando Botão de Pânico... Buscando preço atualizado para venda...")
            if minha_conexao.fetch_market_data():
                preco_atual = minha_conexao.get_current_price()
                if minha_carteira.positions > 0:
                    minha_carteira.execute_trade("VENDER", preco_atual)
                else:
                    print("⚠️ Você não possui posições abertas para vender.")
            else:
                print("❌ Falha ao conectar na API para realizar a venda de emergência.")
        
        elif opcao == "2":
            print("\n🚪 Encerrando o bot sem mexer nas posições do mercado.")
        else:
            print("\n⚠️ Opção inválida reconhecida. Por segurança, nenhuma ordem foi enviada.")

        # Exibe os relatórios consolidados gerados pela Wallet
        minha_carteira.get_trade_history()
        minha_carteira.get_performance_summary()
        print("\n🤖 Robô Solid desligado com sucesso.")

    except Exception as e:
        print(f"\n💥 [ERRO CRÍTICO INESPERADO]: {e}")
        print("O robô encontrou uma falha no código ou na execução e precisou parar.")
        minha_carteira.get_trade_history()
        minha_carteira.get_performance_summary()
        sys.exit(1)