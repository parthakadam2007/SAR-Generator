import { useEffect } from "react";
import { useAppDispatch, useAppSelector } from "../../../../app/hooks";
import { fetchAlerts } from "../../../../shared/slices/alerts/alertsSlice";
import AlertsTable from "../components/AlertsTable";
import PageList from "../../../../shared/components/sidebar/PageList";
import Header from "../../../../shared/components/header/Header";

export default function AlertsInbox() {
  const dispatch = useAppDispatch();
  const { alerts, loading } = useAppSelector((state) => state.alerts);

  useEffect(() => {
    dispatch(fetchAlerts());
  }, [dispatch]);

  if (loading) return <p className="p-8">Loading alerts...</p>;

  return (
    <>
    <Header />
    <div className="flex">
      <PageList />
      <div className="w-full p-4 bg-blue-300/20 h-[89vh] overflow-y-auto">
      <AlertsTable alerts={alerts} />
      </div>
      {/* console.log("Redux alerts state:", alerts); */}
    </div>
    </>
  );
}
