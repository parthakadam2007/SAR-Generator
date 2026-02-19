import { Routes, Route } from "react-router-dom";
import './App.css'

// ------------------------- Importing Pages ------------------ //
import PageList from './shared/components/sidebar/PageList';
import AlertsInbox from './features/sidebarservices/alert/pages/AlertsInbox';
import SarGenerator from './features/sidebarservices/sargenerator/pages/SarGenerator';
import CaseInvestigation from "./features/sidebarservices/CaseInvestigation";
import AuditReplay from "./features/sidebarservices/AuditReplay";

function App() {
  return (
    <>
        <Routes>
          <Route path="/" element={<PageList />} />
          <Route path="/alert-inbox" element={<AlertsInbox />} />
          <Route path="/case-investigation" element={<CaseInvestigation />} />
          <Route path="/case-investigation/:alertId" element={<CaseInvestigation />} />
          <Route path="/sar-editor" element={<SarGenerator />} /> 
          <Route path="/audit-replay" element={<AuditReplay />} />  
        </Routes>
    </>
  )
}

export default App
