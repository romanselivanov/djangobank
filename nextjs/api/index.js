import axios from 'axios'
import {apiUrl} from '../env'

export const apiNonCache = axios.create({
    baseURL: apiUrl,
    withCredentials: true
});
