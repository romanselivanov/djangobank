import axios from 'axios'
import {apiUrl} from '../env'
import {setupCache} from 'axios-cache-adapter'

const cache = setupCache({
    maxAge: 60 * 1000,
    exclude: {
        query: false,
    },
});

export const apiNonCache = axios.create({
    baseURL: apiUrl,
    withCredentials: true
});

const api = axios.create({
    baseURL: apiUrl,
    withCredentials: true,
    adapter: cache.adapter,
})

export default api;
