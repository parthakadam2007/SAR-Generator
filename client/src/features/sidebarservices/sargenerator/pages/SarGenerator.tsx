import PageList from "../../../../shared/components/sidebar/PageList";
import Header from "../../../../shared/components/header/Header";

const sarData = {
   executiveSummary: `Rakesh Patel, a retail shop owner from Ahmedabad, conducted rapid high-value transactions totaling INR 3,00,000 on 10-Feb-2026. Funds were received and immediately routed through intermediary accounts before being transferred internationally to Hong Kong. The activity triggered critical AML alerts and is inconsistent with the customer's profile and declared income.`,
   customerProfile: `Customer Name: Rakesh Patel
    Customer ID: CUST991200
    DOB: 21-Feb-1988
    PAN: ZXCVB1234Q
    Occupation: Retail Shop Owner
    Declared Annual Income: INR 4,20,000
    Risk Category: Medium

    Account: Savings XXXX5521 (Opened 11-Apr-2017)
    Average Monthly Credit: INR 90,000
    Average Monthly Balance: INR 65,000
    Usual Activity: Small retail deposits`,

    suspiciousActivity: `On 10-Feb-2026, Rakesh Patel's account received three large deposits of INR 1,00,000 each within a span of 2 hours. These funds were then rapidly transferred to two different accounts (XXXX1234 and XXXX5678) before being sent internationally to Hong Kong. The transactions were flagged by the AML system due to their size, frequency, and the use of multiple intermediary accounts, which is inconsistent with the customer's typical banking behavior and declared income.`,
    regulatoryRationale: `The transactions conducted by Rakesh Patel exhibit several red flags indicative of potential money laundering activities. The rapid succession of high-value deposits followed by immediate transfers to intermediary accounts and subsequent international remittances to Hong Kong are inconsistent with the customer's declared income and typical banking patterns. Such behavior raises concerns about the legitimacy of the funds and potential attempts to obscure their origin, warranting further investigation and reporting under AML regulations.`,
    conclusion: `Given the significant discrepancies between Rakesh Patel's declared income and the nature of the transactions, along with the use of multiple intermediary accounts and international transfers, there is a strong indication of potential money laundering. It is recommended that this case be escalated for further investigation to determine the legitimacy of the funds and to ensure compliance with AML regulations.`
}
const Section = ({ title, value }: { title: string, value?: string }) => (
  <div className="mb-8">
    <div className="flex items-center gap-3 mb-2 pb-3 border-gray-200">
      <h3 className="text-lg font-semibold text-gray-900">{title}</h3>
      <span className="px-2.5 py-1 bg-gray-100 text-gray-700 text-xs font-medium rounded-full">
        Draft
      </span>
    </div>
    <textarea
      className="w-full border border-gray-200 rounded-lg p-4 h-32 resize-none bg-white/50 hover:bg-white focus:bg-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-sm leading-relaxed placeholder-gray-400 transition-all duration-200"
      placeholder={`Write ${title.toLowerCase()}...`}
      defaultValue={value}
    />
  </div>
);

const SarGenerator = () => {
  return (
    <>
    <Header />
    <div className="flex">
      <PageList />
      <div className="w-full px-8 py-8 bg-blue-300/20 h-[89vh] overflow-y-auto">
        {/* HEADER */}
        <div className="mb-8">
          <div className="flex items-start justify-between mb-4">
            <div>
              <div className="flex items-center gap-3 mb-2">
                <div>
                  <h4 className="text-3xl font-bold bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent">
                    SAR Generator Editor
                  </h4>
                  <p className="text-gray-500 mt-1 max-w-2xl">
                    Utilize AI-generated content to draft and refine Suspicious Activity
                    Reports, ensuring accuracy and compliance.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div className="flex flex-wrap gap-3 mb-8 justify-end">
          <button className="px-6 py-3 bg-white border border-gray-300 rounded-2xl text-sm font-medium text-gray-900 transition-all duration-200 flex items-center gap-2">
            <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
            Regenerate Draft
          </button>
          <button className="px-6 py-3 bg-white border border-gray-300 rounded-2xl text-sm font-medium text-gray-900  transition-all duration-200 flex items-center gap-2">
            <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
            </svg>
            Highlight Evidence
          </button>
          <button className="px-6 py-3 bg-white border border-gray-200 rounded-2xl text-sm font-medium text-gray-900  hover:bg-gray-50 transition-all duration-200 flex items-center gap-2">
            <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
            </svg>
            Save Draft
          </button>
          <button className="px-8 py-3 bg-gradient-to-r from-blue-600 to-blue-700 text-white rounded-2xl text-sm font-semibold hover:from-blue-700 hover:to-blue-800 transition-all duration-200 flex items-center gap-2">
            <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
            </svg>
            Submit for Approval
          </button>
        </div>

        <div className="bg-white rounded-xl border border-gray-200 p-8">
          <div className="flex items-center justify-between mb-8 pb-6 border-b border-gray-100">
            <div className="flex items-center gap-3">
              <div>
                <h2 className="text-2xl font-bold text-gray-900">
                  Suspicious Activity Report Draft
                </h2>
                <p className="text-gray-500 mt-1">
                  Review and edit the AI-generated content before submission.
                </p>
              </div>
            </div>
            <div className="flex items-center gap-2 text-sm text-gray-500">
              <span>Auto-saved 2min ago</span>
              <div className="w-px h-4 bg-gray-200" />
              <span>Word count: 0</span>
            </div>
          </div>

          <Section title="Executive Summary" value={sarData.executiveSummary} />
          <Section title="Customer Profile" value={sarData.customerProfile}  />
          <Section title="Suspicious Activity" value={sarData.suspiciousActivity} />
          <Section title="Regulatory Rationale" value={sarData.regulatoryRationale} />
          <Section title="Conclusion" value={sarData.conclusion} />
        </div>
      </div>
    </div>
    </>
  );
};

export default SarGenerator;
