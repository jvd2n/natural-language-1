import axios, { csrfToken } from 'axios';

// axios.defaults.xsrfCookieName = "csrftoken"
// axios.defaults.xsrfHeaderName = "X-CSRFToken";
// axios.defaults.withCredentials = true

const SERVER = 'http://127.0.0.1:8000'

// const headers = {
//   "X-CSRFToken": csrfToken
// }

export const userSignup = signupRequest => axios.post(
  `${SERVER}/member/signup/`, signupRequest)
// export const userLogin = loginRequest => axios.post(`${SERVER}member/login`, loginRequest)