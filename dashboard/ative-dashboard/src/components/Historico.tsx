import styles from './Historico.module.css'
import { useState, useEffect } from 'react';

interface Trade {
    id: number; 
    hora: string;
    ativo: string;
    preco: number;
    qtd: number;
    sinal: string;
}

export default function Historico() {
    const [trades, setTrades] = useState<Trade[]>([]);
    async function getData() {
        try {
            const response = await fetch('http://localhost:8000/trades/history/', {
                method: 'GET', 
                headers: {
                    'Content-Type': 'application/json', 
                }
            });
            
            if (!response.ok) {
                throw new Error('Erro na requisição');
            }
            const data: Trade[] = await response.json();
            setTrades(data); 
            console.log('Dados históricos recebidos:', data);
        } catch (error) {
            console.error('Error fetching historical data:', error);
        } 
    }

    useEffect(() => {
        getData();

        const intervalo = setInterval(() => {
            getData();
        }, 5000);

        return () => clearInterval(intervalo);
    }, []); 

    return (
        <div className={styles.container}>
            <div className={styles.title}>
                <p>Historico de ordens</p>
            </div>
            <div className={styles.table}>
                <div className={styles.header}>
                    <p>hora</p>
                    <p>ativo</p>
                    <p>preco</p>
                    <p>Qtd</p>
                    <p>Sinal</p>
                </div>
                <div className={styles.rowInfo}>
                    {trades.length === 0 ? (
                        <div className={styles.rowData}>
                            <p>Nenhuma ordem encontrada.</p>
                        </div>
                    ) : (
                        trades.map((trade) => (
                            <div key={trade.id} className={styles.rowData}>
                                <p>{trade.hora}</p>
                                <p>{trade.ativo}</p>
                                <p>R$ {Number(trade.preco).toFixed(2)}</p>
                                <p>{trade.qtd}</p>
                                {/* Um toque de estilo baseado no sinal (opcional) */}
                                <p style={{ color: trade.sinal === 'C' ? '#4caf50' : '#f44336', fontWeight: 'bold' }}>
                                    {trade.sinal === 'C' ? 'COMPRA' : 'VENDA'}
                                </p>
                            </div>
                        ))
                    )}
                </div>
            </div>
        </div>
    )
}