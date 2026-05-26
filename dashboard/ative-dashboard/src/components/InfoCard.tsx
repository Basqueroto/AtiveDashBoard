import styles from './InfoCard.module.css'

export default function InfoCard({title, value, subtitle, isMoney}: {title: string, value: number, subtitle: string, isMoney: boolean}) {
    return (
        <div className={styles.container}>
            <div className={styles.infoCardTitle}>
                <p>{title}</p>
            </div>
            <div className={styles.infoCardValue}>
                <p>{isMoney ? `$${value.toFixed(2)}` : value}</p>
            </div>
            <div className={styles.infoCardSubtitle}>
                <p>{subtitle}</p>
            </div>
        </div>
    )
}