import React, {useState} from "react";
import {Link} from "react-router-dom";
import {useDispatch, useSelector} from "react-redux"
import {updatesidebarStatus} from "../../slices/sharedSlice";
import { useNavigate } from "react-router-dom";
// import { useLocation } from "react-router-dom";

interface RootState {
    shared: {
        sidebarStatus: {
            activePage: string;
        };
    };
} 

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
     {item_name: 'Dashboard', navigate: '/dashboard'},
     {item_name: 'Alert Inbox', navigate: '/alert-inbox'},
     {item_name: 'Case Investigation', navigate: '/case-investigation'},
     {item_name: 'SAR Editor', navigate: '/sar-editor'},
     {item_name: 'Audit Replay', navigate: '/audit-replay'}
   ]
   return (
      <div className="w-70 p-2 flex flex-col justify-end h-[89vh] overflow-y-hidden" style={{ transition: 'width 0.1s'}}>
            <div className="flex-grow">
                {pageList.map((item) => (
                    <div
                        key={item.item_name}
                        onClick={() => item.item_name && handleItemSelection(item.item_name)}
                        className={`
                            flex items-center gap-4 p-3 px-4 cursor-pointer mb-4 rounded-2xl
                            transition-colors duration-200 ease-in-out 
                            ${activePage === item.item_name
                                ? 'bg-gray-200 text-blue-500 font-medium'
                                : 'text-gray-700 hover:bg-gray-100 hover:text-gray-700'
                            }
                        `}
                    >
                        <img
                            // src={item.item_img}
                            className={`w-6 h-6 flex items-center justify-center ${activePage === item.item_name ? 'filter brightness-0 invert' : ''}`}
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
                            className={`w-6 h-6`}
                        />
                        <span className="text-sm md:text-base hover:text-blue-700">Settings</span>   
                    </div>
              
            
            <div className="mt-auto mb-[10px]">
            </div>
            </div>           
        </div>
   )
};

export default PageList