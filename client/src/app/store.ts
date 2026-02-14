import {configureStore} from '@reduxjs/toolkit'
import sharedSlice from '../shared/slices/sharedSlice'

export const store = configureStore ({
   reducer: {
     // Add your slice reducers here
     shared: sharedSlice
   }
})