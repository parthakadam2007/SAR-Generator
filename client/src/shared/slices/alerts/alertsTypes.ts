export type RiskLevel = "High" | "Medium" | "Low";
export type AlertStatus = "Pending Review" | "Under Investigation" | "Resolved";

export interface Alert {
  id: string;
  customerName: string;
  alertType: string;
  riskScore: RiskLevel;
  location: string;
  status: AlertStatus;
}
