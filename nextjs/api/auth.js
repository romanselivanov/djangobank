import { apiNonCache } from "./index"

const BASE_URL = 'auth'

export const login = (username, password) => {
    return apiNonCache.post(`${BASE_URL}/login/`, {username, password})
}

export const logout = () => {
    return apiNonCache.post(`${BASE_URL}/logout/`)
}

export const passwordReset = (email) => {
    return apiNonCache.post(`${BASE_URL}/password/reset/`, {email: email})
}

export const passwordResetConfirm = (uid, token, new_password1, new_password2) => {
    return apiNonCache.post(`${BASE_URL}/password/reset/confirm/`, {uid, token, new_password1, new_password2})
}

export const passwordChange = (new_password1, new_password2) => {
    return apiNonCache.post(`${BASE_URL}/password/change/`, {new_password1, new_password2})
}