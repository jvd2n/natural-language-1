import axios, { csrfToken } from 'axios';

// axios.defaults.xsrfCookieName = "csrftoken"
// axios.defaults.xsrfHeaderName = "X-CSRFToken";
// axios.defaults.withCredentials = true

const SERVER = 'http://127.0.0.1:8000/'
const headers = {
  // "X-CSRFToken": csrfToken,
  'Content-Type': 'application/json'
}

// export const userSignup = body => axios.post(`${SERVER}/member/signup/`, {headers, body})
// export const userLogin = logData => axios.post(`${SERVER}/member/login/`, {headers, logData})
// export const postRegister = jsonData => axios.post(`${SERVER}/board/register/`, {headers, jsonData})

/* Board */
export const postDetail = body => axios.post(`${SERVER}api/post/detail`,{headers, body})
export const postDelete = body => axios.post(`${SERVER}api/post/delete`,{headers, body})
export const postList = body => axios.post(`${SERVER}api/post/list`,{headers, body})
export const postModify = body => axios.post(`${SERVER}api/post/modify`,{headers, body})
export const postRegister = body => axios.post(`${SERVER}api/post/register/`,{headers, body})
export const postRetrieve = body => axios.post(`${SERVER}api/post/retrieve`,{headers, body})
/* Common */
/* 공통은 네이밍 컨벤션에서 벗어남 */

/* Item */
export const itemDetail = body => axios.post(`${SERVER}item/detail`,{headers, body})
export const itemDelete = body => axios.post(`${SERVER}item/delete`,{headers, body})
export const itemList = body => axios.post(`${SERVER}item/list`,{headers, body})
export const itemModify = body => axios.post(`${SERVER}item/modify`,{headers, body})
export const itemRegister = body => axios.post(`${SERVER}item/register`,{headers, body})
export const itemRetrieve = body => axios.post(`${SERVER}item/retrieve`,{headers, body})

/* Member */
export const memberDetail = body => axios.post(`${SERVER}api/member/detail`,{headers, body})
export const memberDelete = body => axios.post(`${SERVER}api/member/delete`,{headers, body})
export const memberList = () => axios.get(`${SERVER}api/member/list/`)
export const memberList2 = () => axios.get(`${SERVER}api/member/list/`)
export const memberModify = body => axios.post(`${SERVER}api/member/modify`,{headers, body})
export const memberRegister = body => axios.post(`${SERVER}adm/member/register/`,{headers, body})
export const memberRetrieve = body => axios.post(`${SERVER}api/member/retrieve`,{headers, body})
export const memberLogin = body => axios.post(`${SERVER}api/member/login/`,{headers, body})