import { useEffect, useState } from 'react';
import styles from './PrecosAtualizados.module.css';

// Mudamos o nome da interface para refletir que representa o estado atual do bot
interface BotActualStatus {
    nome: string;
    ativo: string;
    preco_atual: number;
    ma_rapida: number;
    ma_lenta: number;
    sinal: string;
}

export default function PrecosAtualizados() {
    // Agora o estado começa como null (pois o Python envia UM objeto {} e não uma lista [])
    const [botData, setBotData] = useState<BotActualStatus | null>(null);

    async function getData() {
        try {
            const response = await fetch('http://localhost:8000/trades/actual/', {
                method: 'GET', 
                headers: {
                    'Content-Type': 'application/json', 
                }
            });
                
            if (!response.ok) {
                throw new Error('Erro na requisição');
            }
            const data: BotActualStatus = await response.json();
            setBotData(data); 
            console.log('Dados atuais recebidos:', data);
        } catch (error) {
            console.error('Error fetching actual data:', error);
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
                <p>Preços em tempo real</p>
            </div>
            <div className={styles.table}>
                <div className={styles.header}>
                    <div className={styles.ativo}>
                        <p>Ativo</p>
                    </div>
                    <div className={styles.infos}>
                        <p>Preço</p>
                        <p>Variação rápida</p>
                        <p>Variação lenta</p>
                        <p>Sinal</p>
                    </div>  
                </div>
                <div className={styles.rowInfo}>
                    {/* Se botData for null (ainda não carregou), exibe aviso. Caso contrário, joga na tela sem usar .map() */}
                    {!botData ? (
                        <div className={styles.rowData}>
                            <p>Aguardando resposta do bot...</p>
                        </div>
                    ) : (
                        <div className={styles.rowData}>
                            <p>{botData.ativo}</p>
                            <p>R$ {Number(botData.preco_atual).toFixed(2)}</p>
                            <p>{Number(botData.ma_rapida).toFixed(2)}</p>
                            <p>{Number(botData.ma_lenta).toFixed(2)}</p>
                            <p style={{ color: botData.sinal === 'C' ? '#4caf50' : '#f44336', fontWeight: 'bold' }}>
                                {botData.sinal === 'C' ? 'COMPRA' : 'VENDA'}
                            </p>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
}