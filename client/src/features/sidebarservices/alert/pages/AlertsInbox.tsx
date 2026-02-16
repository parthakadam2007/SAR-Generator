import { useEffect } from "react";
import { useAppDispatch, useAppSelector } from "../../../../app/hooks";
import { fetchAlerts } from "../../../../shared/slices/alerts/alertsSlice";
import AlertsTable from "../components/AlertsTable";
import PageList from "../../../../shared/components/sidebar/PageList";

export default function AlertsInbox() {
  const dispatch = useAppDispatch();
  const { alerts, loading } = useAppSelector((state) => state.alerts);

  useEffect(() => {
    dispatch(fetchAlerts());
  }, [dispatch]);

  if (loading) return <p className="p-8">Loading alerts...</p>;

  return (
    <div className="py-4 flex gap-6">
      <PageList />
      <div className="bg-blue-50 w-full rounded-lg p-8">
      <AlertsTable alerts={alerts} />
      </div>
      {/* console.log("Redux alerts state:", alerts); */}
    </div>
  );
}
