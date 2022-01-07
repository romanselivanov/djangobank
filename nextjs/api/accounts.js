import api from "./index"

export const list = () => api.get(`accounts/`);
