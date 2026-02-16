import {configureStore} from '@reduxjs/toolkit'
import sharedSlice from '../shared/slices/sharedSlice'
import alertsSlice from '../shared/slices/alerts/alertsSlice';

export const store = configureStore ({
   reducer: {
     // Add your slice reducers here
     shared: sharedSlice,
     alerts: alertsSlice
   }
})
export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;