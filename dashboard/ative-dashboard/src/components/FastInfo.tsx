import InfoCard from "./InfoCard";
import styles from './FastInfo.module.css'

export default function FastInfo() {
    return (
        <div className={styles.container}>
            <InfoCard title="Revenue" value={5000} subtitle="Last month revenue" isMoney={true}/>
            <InfoCard title="Users" value={200} subtitle="Active users" isMoney={false}/>
            <InfoCard title="Orders" value={150} subtitle="Total orders" isMoney={false}/>
            <InfoCard title="Orders" value={150} subtitle="Total orders" isMoney={false}/>
        </div>
    )
}