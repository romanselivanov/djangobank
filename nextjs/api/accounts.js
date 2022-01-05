import { apiNonCache } from "./index"

export const list = () => apiNonCache.get(`accounts/`);
