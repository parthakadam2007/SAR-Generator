// import { StrictMode } from 'react'
// import React from "react"
// import ReactDOM from "react-dom/client"
// import './index.css'
// import App from './App.tsx'
// import { createRoot } from 'react-dom/client'
// import { Provider } from "react-redux"
// import { store } from "./app/store"

// createRoot(document.getElementById('root')!).render(
//     <React.StrictMode>
//     <Provider store={store}>
//       <App />
//     </Provider>
//   </React.StrictMode>,
// )

import React from "react"
import ReactDOM from "react-dom/client"
import App from "./App.tsx"
import { Provider } from "react-redux"
import { store } from "./app/store.ts"
import { BrowserRouter } from "react-router-dom"

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <Provider store={store}>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </Provider>
  </React.StrictMode>
)
