import React from "react";
import Barclays from "../../../assets/Barclays-Logo.webp"
import { Bell, Sun, Search } from "lucide-react";

const Header: React.FC = () => {
  return (
    <header className="w-full h-16 bg-white border-b border-gray-200 px-1 flex items-center justify-between">
      
      {/* <div className="flex items-center gap-3">
        <div className="bg-blue-600 text-white p-2 rounded-lg">
          🛡️
        </div>
        <h1 className="text-3xl font-semibold text-blue-600">
          Barclays
        </h1>
      </div> */}
       <div className="flex items-center shrink-0">
      <img src={Barclays} alt="Barclays Logo" className="w-40" />
       </div>

      <div className="w-[40%] relative">
        <Search
          size={18}
          className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400"
        />
        <input
          type="text"
          placeholder="Global search..."
          className="w-lg bg-gray-100 rounded-xl pl-10 pr-4 py-2 outline-none focus:ring-2 focus:ring-blue-400"
        />
      </div>

      {/* RIGHT : Icons */}
      <div className="flex items-center gap-5">
        <Bell className="text-gray-600 cursor-pointer" size={20} />
        <Sun className="text-gray-600 cursor-pointer" size={20} />

        {/* Profile */}
        <img
          src="https://i.pravatar.cc/40"
          alt="profile"
          className="w-9 h-9 rounded-full"
        />
      </div>
    </header>
  );
};

export default Header;
