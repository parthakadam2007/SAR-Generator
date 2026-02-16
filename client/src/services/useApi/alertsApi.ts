import type { Alert } from "../../shared/slices/alerts/alertsTypes";

export const fetchAlertsApi = async (): Promise<Alert[]> => {
  // simulate backend delay
  await new Promise((res) => setTimeout(res, 8));

  return [
    {
      id: "ALRT-00123",
      customerName: "Eleanor Rigby",
      alertType: "Transaction Monitoring",
      riskScore: "High",
      location: "London, UK",
      status: "Pending Review",
    },
    {
      id: "ALRT-00124",
      customerName: "Arthur Morgan",
      alertType: "Sanction Hit",
      riskScore: "High",
      location: "New York, USA",
      status: "Under Investigation",
    },
    {
      id: "ALRT-00125",
      customerName: "Lara Croft",
      alertType: "AML Typology",
      riskScore: "Medium",
      location: "Cairo, Egypt",
      status: "Pending Review",
    },
    {
      id: "ALRT-00126",
      customerName: "Marcus Aurelius",
      alertType: "PEP Check",
      riskScore: "Low",
      location: "Rome, Italy",
      status: "Resolved",
    },
    {
      id: "ALRT-00127",
      customerName: "Ada Lovelace",
      alertType: "High-Value Transfer",
      riskScore: "Medium",
      location: "Berlin, Germany",
      status: "Under Investigation",
    },
  ];
};
