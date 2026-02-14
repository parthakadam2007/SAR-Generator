import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import { BrowserRouter, Routes, Route } from "react-router-dom";
import PageList from './shared/components/sidebar/PageList'
// import Header from './shared/components/header/Header'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
     <div style={{ display: "flex" }}>
      <PageList />
    </div>
    </>
  )
}

export default App
