import { useState, useEffect } from 'react';
import InfoCard from "./InfoCard";
import styles from './FastInfo.module.css';

export default function FastInfo() {
    const [balance, setBalance] = useState<number>(0);
    const [totalTrades, setTotalTrades] = useState<number>(0);
    const [tokenNumber, setTokenNumber] = useState<number>(0);

    async function fetchFastInfo() {
        try {
            const [resBalance, resTrades, resTokens] = await Promise.all([
                fetch('http://localhost:8000/trades/balance/', { method: 'GET' }), 
                fetch('http://localhost:8000/trades/count/', { method: 'GET' }),
                fetch('http://localhost:8000/trades/tokens/', { method: 'GET' })
            ]);

            if (!resBalance.ok || !resTrades.ok || !resTokens.ok) {
                throw new Error('Erro ao buscar um dos endpoints de informação rápida');
            }

            const dataBalance = await resBalance.json();
            const dataTrades = await resTrades.json();
            const dataTokens = await resTokens.json();

            setBalance(dataBalance.balance);
            setTotalTrades(dataTrades.total_trades);
            setTokenNumber(dataTokens.total_coins);

        } catch (error) {
            console.error('Erro no FastInfo:', error);
        }
    }

    useEffect(() => {
        fetchFastInfo(); 

        const intervalo = setInterval(() => {
            fetchFastInfo();
        }, 5000);

        return () => clearInterval(intervalo); 
    }, []);

    return (
        <div className={styles.container}>
            <InfoCard 
                title="Valor salvo" 
                value={balance} 
                subtitle="Dinheiro em carteira" 
                isMoney={true}
            />
            <InfoCard 
                title="Total trades" 
                value={totalTrades} 
                subtitle="trades" 
                isMoney={false}
            />
            <InfoCard 
                title="Token lidos" 
                value={tokenNumber} 
                subtitle="Total tokens vistos" 
                isMoney={false}
            />
        </div>
    );
}