import styles from './Historico.module.css'

export default function Historico() {
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
                    <p>aguardadndo api de resposta</p> 
                </div>
            </div>
        </div>
    )
}