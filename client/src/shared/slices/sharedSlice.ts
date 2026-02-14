import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    sidebarStatus: {
        activePage: "Dashboard",
    }
}

export const sharedSlice = createSlice({
    name: "sharedSlice",
    initialState,
    reducers: {
    //   -------------- Sidebar ---------------
     updatesidebarStatus: (state, action) => {
      state.sidebarStatus.activePage = action.payload.activePage;
     },
    }
});

export const {
    updatesidebarStatus,
} = sharedSlice.actions

export default sharedSlice.reducer;