import { useNavigate } from "react-router-dom";
import { FaExclamationTriangle } from "react-icons/fa";
import ArrowUpward from "../../assets/arrow_outward.svg";
import Header from "../../shared/components/header/Header";
import PageList from "../../shared/components/sidebar/PageList";

const transactions = [
  {
    time: "10:50 AM",
    title: "Incoming Transfer from ACC_A",
    amount: "₹5,67,665",
    channel: "NEFT",
    location: "India",
    type: "Deposit",
    suspicious: false,
  },
  {
    time: "10:55 AM",
    title: "Transfer to ACC_B",
    amount: "₹4,57,965",
    channel: "IMPS",
    location: "India",
    type: "Transfer",
    suspicious: false,
  },
  {
    time: "11:00 AM",
    title: "Transfer to ACC_C",
    amount: "₹13,33,299",
    channel: "IMPS",
    location: "India",
    type: "Transfer",
    suspicious: false,
  },
  {
    time: "11:06 AM",
    title: "International Transfer to HK_NODE_8821",
    amount: "₹23,45,678",
    channel: "SWIFT",
    location: "Hong Kong",
    type: "Transfer",
    suspicious: true,
  },
];

const CaseInvestigation = () => {
  const navigate = useNavigate();
  // const { alertId } = useParams();
  return (
    <>
      <Header />
      <div className="flex">
        <PageList />

        <div className="w-full p-4 bg-blue-300/20 p-8 h-[89vh] overflow-y-auto">
          {/* Enhanced Header */}
          <div className="flex justify-between items-center mb-6 pb-8">
            <div className="flex items-center space-x-4">
              <div>
                <h1 className="text-3xl font-bold bg-gradient-to-r from-gray-900 to-slate-700 bg-clip-text text-transparent">
                  Case Investigation
                </h1>
              </div>
            </div>

            <button
              onClick={() => navigate("/sar-editor")}
              className="group relative px-8 py-4 bg-gradient-to-r from-blue-600 to-blue-700 text-white font-semibold rounded-2xl hover:from-blue-700 hover:to-blue-800 transform transition-all duration-300 flex items-center space-x-3"
            > 
             <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
            </svg>
              <span>Checkout SAR Report</span>
            </button>
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
            <div className="lg:col-span-1">
              <div className="bg-white/80  p-8 rounded-xl border border-slate-200/50 top-8">
                <h2 className="text-2xl font-bold text-slate-900 mb-8 flex items-center space-x-3">
                  <span>Customer Profile</span>
                </h2>

                <div className="space-y-6 mb-8">
                  <div className="space-y-2 border-b border-slate-300 pb-4">
                    <h3 className="font-semibold text-slate-800 text-lg flex items-center space-x-2">
                      <span className="w-6 h-6 bg-slate-200 rounded-lg flex items-center justify-center text-sm font-bold">ID</span>
                      Customer Details
                    </h3>
                    <div className="space-y-1 text-sm">
                      <p className="font-bold"><span className="text-slate-600">Name:</span> Rakesh Patel</p>
                      <p className="font-bold"><span className="text-slate-600">Customer ID:</span> CUST991200</p>
                      <p className="font-bold"><span className="text-slate-600">Account:</span> XXXX5521</p>
                      <p className="font-bold"><span className="text-slate-600">Account Age:</span> Apr 2017</p>
                      <p className="font-bold"><span className="text-slate-600">Occupation:</span> Retail Shop Owner</p>
                      <p className="text-emerald-600 font-medium">Ahmedabad, India</p>
                    </div>
                  </div>

                  <div className="p-5 bg-gradient-to-r from-red-50/80 to-orange-50/80 rounded-2xl border-b border-red-200/50">
                    <h3 className="font-semibold text-slate-800 mb-3">Risk Profile</h3>
                    <div className="flex items-center justify-between">
                      <span className="text-red-600 font-bold text-xl">High Risk</span>
                      <div className="w-20 h-2 bg-slate-200 rounded-full overflow-hidden">
                        <div className="w-[70%] h-full bg-gradient-to-r from-red-500 to-orange-500 rounded-full shadow-sm" />
                      </div>
                    </div>
                    <p className="text-sm text-slate-600 mt-1">Score: 70/100</p>
                  </div>

                  <div className="space-y-2">
                    <h3 className="font-semibold text-slate-800">KYC Summary</h3>
                    <p className="text-sm text-slate-600">Last Updated: 10-Jun-2024</p>
                    <p className="font-medium text-emerald-600">Status: Verified</p>
                    <p className="text-sm text-slate-600">Income: ₹4,20,000/year</p>
                  </div>

                  {/* Overview */}
                  <div className="p-5 bg-gradient-to-r from-slate-50 to-blue-50/50 rounded-2xl border border-slate-200/50">
                    <h3 className="font-semibold text-slate-800 mb-4">Transaction Overview</h3>
                    <div className="space-y-2 text-sm">
                      <p>Transactions: <span className="font-bold text-slate-900">4</span></p>
                      <p>Suspicious Volume: <span className="font-bold text-amber-600">₹3,00,000</span></p>
                        <p>Last Transaction: <span className="font-bold text-slate-900">10-Feb-2026</span></p>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div className="lg:col-span-2">
              <div className="bg-white/80 p-8 rounded-xl border border-slate-200/50">
               <div className="flex justify-between border-b border-slate-200">
                <h2 className="text-2xl font-bold text-slate-900 mb-10 flex items-center space-x-3">
                  <span>Transaction Timeline</span>
                </h2>
                <div className="relative flex-1 min-w-[200px] max-w-md">
                <input
                    type="text"
                    placeholder="Search alerts by ID of Customer Name..."
                    className="w-full rounded-xl border border-gray-300 bg-white py-2.5 pl-10 pr-4 text-sm focus:border-transparent focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
                <svg className="absolute left-3 top-5 -translate-y-1/2 w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                </svg>
              </div>
            </div>
                <div className="space-y-8 mb-12 ">
                  {transactions.map((tx, i) => (
                    <div key={i} className="group relative pl-12 pr-8 py-6 rounded-2xl border-b border-slate-200 pb-8">
                      {/* Timeline Dot */}
                      <div className={`absolute left-0 w-5 h-5 border border-gray-600 rounded-full flex items-center justify-center -translate-x-2 transition-all duration-300 group-hover:scale-110 ${tx.suspicious ? 'bg-gradient-to-r from-red-500 to-orange-500 shadow-lg shadow-red-500/25' : 'bg-gray-100 shadow-lg shadow-emerald-500/25'}`}>
                        <img src={ArrowUpward}></img>{/* {tx.suspicious ? <FaExclamationTriangle className="w-4 h-4 text-white" /> : <svg className="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 20 20"><path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" /></svg>} */}
                      </div>

                      <div className="justify-between items-start md:flex">
                        <div className="flex-1 min-w-0">
                          <p className="font-bold text-xl text-slate-900 mb-1 truncate group-hover:text-blue-700 transition-colors">{tx.title}</p>
                          <div className="flex items-center space-x-4 text-sm text-slate-600 mb-2">
                            <span className={`px-3 py-1 rounded-full text-xs font-medium ${tx.suspicious ? 'bg-red-100 text-red-800' : 'bg-emerald-100 text-emerald-800'}`}>
                              {tx.type}
                            </span>
                            <span className="flex items-center space-x-1">
                              <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" /><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" /></svg>
                              <span>{tx.location}</span>
                            </span>
                            <span>{tx.channel}</span>
                          </div>
                        </div>

                        <div className="">
                          <p className={`text-2xl font-bold ${tx.suspicious ? 'text-red-600' : 'text-emerald-600'}`}>
                            {tx.amount}
                          </p>
                          <p className="text-sm text-slate-500 font-medium mt-1">{tx.time}</p>
                        </div>
                      </div>

                      {tx.suspicious && (
                        <div className="mt-4 pt-4 border-t border-red-200/50 flex items-start space-x-3 bg-red-50/50 rounded-xl p-4">
                          <FaExclamationTriangle className="w-5 h-5 text-red-500 mt-0.5 flex-shrink-0" />
                          <p className="text-red-800 font-semibold text-sm leading-relaxed">
                            Suspicious international transfer detected
                          </p>
                        </div>
                      )}
                    </div>
                  ))}
                </div>

                {/* Suspicious Flags */}
                <div className="p-8 rounded-3xl">
                  <h3 className="text-2xl font-bold text-red-800 mb-6 flex items-center space-x-3">
                    <span>Unusual Activity Flags</span>
                  </h3>
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div className="flex items-start space-x-3 p-4 bg-white/50 rounded-2xl transition-all">
                      <div className="w-10 h-10 bg-gradient-to-r from-yellow-400 to-amber-500 rounded-xl flex items-center justify-center flex-shrink-0 mt-0.5">
                        <svg className="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
                        </svg>
                      </div>
                      <p className="text-red-700 font-semibold leading-relaxed">Layering pattern detected</p>
                    </div>
                    <div className="flex items-start space-x-3 p-4 bg-white/50 rounded-2xl transition-all">
                      <div className="w-10 h-10 bg-gradient-to-r from-red-400 to-rose-500 rounded-xl flex items-center justify-center flex-shrink-0 mt-0.5">
                        <svg className="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                        </svg>
                      </div>
                      <p className="text-red-700 font-semibold leading-relaxed">Rapid international transfer</p>
                    </div>
                    <div className="flex items-start space-x-3 p-4 bg-white/50 rounded-2xl transition-all">
                      <div className="w-10 h-10 bg-gradient-to-r from-indigo-400 to-blue-500 rounded-xl flex items-center justify-center flex-shrink-0 mt-0.5">
                        <svg className="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4" />
                        </svg>
                      </div>
                      <p className="text-red-700 font-semibold leading-relaxed">Same-day inflow & outflow</p>
                    </div>
                    <div className="flex items-start space-x-3 p-4 bg-white/50 rounded-2xl transition-all">
                      <div className="w-10 h-10 bg-gradient-to-r from-purple-400 to-pink-500 rounded-xl flex items-center justify-center flex-shrink-0 mt-0.5">
                        <svg className="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                        </svg>
                      </div>
                      <p className="text-red-700 font-semibold leading-relaxed">Amount exceeds income profile</p>
                    </div>
                    <div className="flex items-start space-x-3 p-4 bg-white/50 rounded-2xl transition-all md:col-span-2">
                      <div className="w-10 h-10 bg-gradient-to-r from-emerald-400 to-teal-500 rounded-xl flex items-center justify-center flex-shrink-0 mt-0.5">
                        <svg className="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                        </svg>
                      </div>
                      <p className="text-red-700 font-semibold leading-relaxed">Multiple transactions within 1 hour</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default CaseInvestigation;
