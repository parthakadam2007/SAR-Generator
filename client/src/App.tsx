import { Routes, Route } from "react-router-dom";
import './App.css'

// ------------------------- Importing Pages ------------------ //
import PageList from './shared/components/sidebar/PageList';
import AlertsInbox from './features/sidebarservices/alert/pages/AlertsInbox';
import SarGenerator from './features/sidebarservices/sargenerator/pages/SarGenerator';
function App() {
  return (
    <>
        <Routes>
          <Route path="/" element={<PageList />} />
          <Route path="/alert-inbox" element={<AlertsInbox />} />
          <Route path="/sar-editor" element={<SarGenerator />} /> 
        </Routes>
    </>
  )
}

export default App
