import Header from "../../shared/components/header/Header";
import PageList from "../../shared/components/sidebar/PageList";


const AuditReplay = () => {
  return (
    <>
    <Header />
    <div className="flex">
      <PageList />
    <div className="w-full p-4 bg-blue-300/20 h-[89vh] overflow-y-auto">audit-replay</div>   
    </div>
    </>
  )
}

export default AuditReplay
