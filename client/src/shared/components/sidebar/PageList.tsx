import {useDispatch, useSelector} from "react-redux"
import {updatesidebarStatus} from "../../slices/sharedSlice";
import { useNavigate } from "react-router-dom";
import Dashboard from "../../../assets/dashboard1.svg";
import AlertInbox from "../../../assets/alert_inbox.svg";
import CaseInvestigation from "../../../assets/caseinvestigation.svg";
import SarEditor from "../../../assets/sareditor.svg";
import AuditReplay from "../../../assets/audittrail.svg";
import Settings from "../../../assets/settings1.svg";
// import { useLocation } from "react-router-dom";

interface RootState {
    shared: {
        sidebarStatus: {
            activePage: string;
        };
    };
} 

// here the pagelist is hardcoded but in future we can make it dynamic by fetching the data from the server and then rendering the list based on the data received from the server. This will make the application more flexible and scalable as we can easily add or remove pages without changing the codebase. We can also add a loading state while fetching the data from the server to enhance the user experience.
const PageList: React.FC = () => {
   const dispatch = useDispatch();
   const navigate = useNavigate();
   const activePage = useSelector((state: RootState) => state.shared.sidebarStatus.activePage);

    const handleItemSelection = (itemName: string) => {
        const selectedItem = pageList.find(item => item.item_name === itemName);
        if (selectedItem) {
            navigate(selectedItem.navigate);
        }
        dispatch(updatesidebarStatus({ activePage: itemName }));
    };
   const pageList = [
     {item_name: 'Dashboard', item_img: Dashboard, navigate: '/dashboard'},
     {item_name: 'Alert Inbox', item_img: AlertInbox, navigate: '/alert-inbox'},
     {item_name: 'Case Investigation', item_img: CaseInvestigation, navigate: '/case-investigation'},
     {item_name: 'SAR Editor', item_img: SarEditor, navigate: '/sar-editor'},
     {item_name: 'Audit Replay', item_img: AuditReplay, navigate: '/audit-replay'}
   ]
   return (
      <div className="w-78 py-4 flex flex-col justify-end h-[89vh] overflow-y-hidden border-r border-gray-200" style={{ transition: 'width 0.1s'}}>
            <div className="flex-grow">
                {pageList.map((item) => (
                    <div
                        key={item.item_name}
                        onClick={() => item.item_name && handleItemSelection(item.item_name)}
                        className={`
                            flex items-center gap-4 p-3 px-4 cursor-pointer mb-4 rounded-2xl
                            transition-colors duration-200 ease-in-out 
                            ${activePage === item.item_name
                                ?  'hover:bg-gray-100 bg-gray-300/20 text-[#127fde] font-medium'
                                : 'text-gray-700 hover:bg-gray-100 hover:text-gray-700'
                            }
                        `}
                    >
                        <img
                            src={item.item_img}
                            className={`w-6 h-6 flex items-center justify-center ${activePage === item.item_name ? 'filter brightness-150' : ''}`}
                            alt={item.item_name}
                        />
                        <span className="text-sm md:text-base">{item.item_name}</span>
                    </div>
                ))}
            </div>
            <div className=' '>
            <div
                className={`
                          flex items-center gap-5 p-4 rounded-[70px] cursor-pointer mb-2
                           transition-colors duration-200 ease-in-out hover:bg-gray-100  `}
                        >
                        <img 
                            src={Settings}
                            alt="Settings"
                            className={`w-6 h-6`}
                        />
                        <span className="text-sm md:text-base hover:text-blue-700">Settings</span>   
                    </div>
              
            </div>           
        </div>
   )
};

export default PageList