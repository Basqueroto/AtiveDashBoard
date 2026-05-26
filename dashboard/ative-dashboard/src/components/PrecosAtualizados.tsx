import styles from './PrecosAtualizados.module.css'

export default function PrecosAtualizados() {
    return (
        <div className={styles.container}>
            <div className={styles.title}>
                <p>Precos em tempo real</p>
            </div>
            <div className={styles.table}>
                <div className={styles.header}>
                    <div className={styles.ativo}>
                        <p>Ativo</p>
                    </div>
                    <div className={styles.infos}>
                        <p>Preço</p>
                        <p>Variação rapida</p>
                        <p>Variação lenta</p>
                        <p>sinal</p>
                    </div>  
                </div>
                <div className={styles.rowInfo}>
                    <p>aguardadndo api de resposta</p>
                </div>
            </div>
        </div>
    )
}