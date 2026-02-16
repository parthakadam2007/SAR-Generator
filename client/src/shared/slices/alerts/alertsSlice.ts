import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { fetchAlertsApi } from "../../../services/useApi/alertsApi";
import type { Alert } from "./alertsTypes";

interface AlertsState {
  alerts: Alert[];
  loading: boolean;
}

const initialState: AlertsState = {
  alerts: [],
  loading: false,
};

export const fetchAlerts = createAsyncThunk(
  "alerts/fetchAlerts",
  async () => await fetchAlertsApi()
);

const alertsSlice = createSlice({
  name: "alerts",
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder.addCase(fetchAlerts.pending, (state) => {
      state.loading = true;
    });
    builder.addCase(fetchAlerts.fulfilled, (state, action) => {
      state.alerts = action.payload;
      state.loading = false;
    });
  },
});

export default alertsSlice.reducer;
