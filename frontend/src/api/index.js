import axios, { csrfToken } from 'axios';

// axios.defaults.xsrfCookieName = "csrftoken"
// axios.defaults.xsrfHeaderName = "X-CSRFToken";
// axios.defaults.withCredentials = true

const SERVER = 'http://127.0.0.1:8000'

const headers = {
  // "X-CSRFToken": csrfToken,
  'Content-Type': 'application/json'
}

// export const userSignup = signupRequest => axios.post(`${SERVER}/member/signup/`, signupRequest)
export const userSignup = body => axios.post(`${SERVER}/member/signup/`, {headers, body})
// export const userLogin = loginRequest => axios.post(`${SERVER}member/login`, loginRequest)
// export const userLogin = logData => axios.get(`${SERVER}/member/login/${logData.username}`, logData)

export const userLogin = logData => axios.post(`${SERVER}/member/login/`, {headers, logData})

export const postRegister = jsonData => axios.post(`${SERVER}/board/register/`, {headers, jsonData})
