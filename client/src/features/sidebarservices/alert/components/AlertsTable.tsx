import type { Alert } from "../../../../shared/slices/alerts/alertsTypes";
import RiskBadge from "./RiskBadge";

interface Props {
  alerts: Alert[];
}

export default function AlertsTable({ alerts }: Props) {
  return (
    <div className="bg-white rounded-2xl p-6">
      {/* Header */}
      <div className="flex items-center justify-between mb-6">
        <div className="flex items-center gap-3">
          <h2 className="text-2xl font-bold text-gray-900">Alerts</h2>
          <span className="px-3 py-1 bg-blue-100 text-blue-800 text-xs font-medium rounded-full">
            {alerts.length} alerts
          </span>
        </div>
        <button className="px-4 py-2 bg-blue-600 text-white text-sm font-medium rounded-lg hover:bg-blue-700 transition-colors">
          New Alert
        </button>
      </div>

      {/* Filters & Search */}
      <div className="flex flex-wrap items-center gap-3 mb-6 p-4 bg-gray-50 rounded-xl">
        <div className="relative flex-1 min-w-[200px] max-w-md">
          <input
            type="text"
            placeholder="Search by Customer Name"
            className="w-full pl-10 pr-4 py-2.5 bg-white border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-sm"
          />
          <svg className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
        </div>
        <select className="px-4 py-2.5 bg-white border border-gray-200 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent">
          <option>All</option>
          <option>Transaction Monitoring</option>
          <option>Sanctions Hit</option>
          <option>PEP Check</option>
          <option>High-Value Transfer</option>
        </select>
        <select className="px-4 py-2.5 bg-white border border-gray-200 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent">
          <option>Last 7 Days</option>
          <option>Last 30 Days</option>
          <option>Last 90 Days</option>
        </select>
        <select className="px-4 py-2.5 bg-white border border-gray-200 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent">
          <option>All</option>
          <option>Under Review</option>
          <option>Resolved</option>
          <option>Under Investigation</option>
        </select>
      </div>

      {/* Table */}
      <div className="overflow-x-auto rounded-xl border border-gray-200">
        <table className="w-full">
          <thead className="bg-gray-50 text-gray-500 text-xs font-medium uppercase tracking-wider">
            <tr>
              <th className="px-6 py-4 text-left">Alert ID</th>
              <th className="px-6 py-4 text-left">Customer Name</th>
              <th className="px-6 py-4 text-left">Alert Type</th>
              <th className="px-6 py-4 text-left">Risk Score</th>
              <th className="px-6 py-4 text-left">Location</th>
              <th className="px-6 py-4 text-left">Status</th>
              <th className="px-6 py-4 text-left">Days</th>
              <th className="px-6 py-4 text-center">Actions</th>
            </tr>
          </thead>

          <tbody className="divide-y divide-gray-200">
            {alerts.length === 0 ? (
              <tr>
                <td colSpan={8} className="px-6 py-12 text-center text-gray-500">
                  No alerts available
                </td>
              </tr>
            ) : (
              alerts.map((alert, index) => (
                <tr
                  key={alert.id}
                  className="hover:bg-gray-50 transition-colors group"
                >
                  <td className="px-6 py-4 font-mono text-sm font-medium text-gray-900">
                    {alert.id}
                  </td>
                  <td className="px-6 py-4 text-sm text-gray-900">
                    {alert.customerName}
                  </td>
                  <td className="px-6 py-4 text-sm text-gray-900">
                    {alert.alertType}
                  </td>
                  <td className="px-6 py-4">
                    <RiskBadge risk={alert.riskScore} />
                  </td>
                  <td className="px-6 py-4 text-sm text-gray-900">
                    {alert.location}
                  </td>
                  <td className="px-6 py-4">
                    {/* <span className={`inline-flex px-3 py-1 text-xs font-medium rounded-full ${
                      alert.status === 'Under Review' ? 'bg-yellow-100 text-yellow-800' :
                      alert.status === 'Resolved' ? 'bg-green-100 text-green-800' :
                      'bg-blue-100 text-blue-800'
                    }`}>
                      {alert.status}
                    </span> */}
                  </td>
                  <td className="px-6 py-4 text-sm text-gray-500">
                    3
                  </td>
                  <td className="px-6 py-4 text-center">
                    <button className="text-blue-600 hover:text-blue-900 text-sm font-medium group-hover:underline transition-colors">
                      Investigate
                    </button>
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>

      {/* Pagination */}
      {alerts.length > 0 && (
        <div className="flex items-center justify-between mt-6 px-4 sm:px-6">
          <div className="text-sm text-gray-700">
            Showing <span className="font-medium">1</span> to <span className="font-medium">5</span> of{' '}
            <span className="font-medium">{alerts.length}</span> results
          </div>
          <div className="flex space-x-2">
            <button className="w-10 h-10 bg-white border border-gray-200 rounded-lg flex items-center justify-center text-gray-500 hover:bg-gray-50 transition-colors">
              <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
              </svg>
            </button>
            <button className="w-10 h-10 bg-white border border-gray-200 rounded-lg flex items-center justify-center text-gray-500 hover:bg-gray-50 transition-colors">
              <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
              </svg>
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
