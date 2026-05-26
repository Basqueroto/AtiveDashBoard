import './App.css'
import FastInfo from './components/FastInfo'
import Header from './components/Header'
import Historico from './components/Historico'
import PrecosAtualizados from './components/PrecosAtualizados'

function App() {

  return (
    <>
      <Header/>
      <div className="containerBody">
      <FastInfo/>
      <div className="separator">
        <PrecosAtualizados/>
        <Historico/>
      </div>
      </div>
    </>
  )
}

export default App
