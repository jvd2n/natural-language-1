import React, { useState } from 'react';
import './Login.css';
import { Button } from '@material-ui/core';
// import { InputSharp, SettingsInputSvideo } from '@material-ui/icons';
import { userLogin } from 'api/index';
import { useHistory } from 'react-router'

const Login = () => {
  const history = useHistory()

  const [loginInfo, setLoginInfo] = useState({
    username: '',
    password: ''
  })

  const { username, password } = loginInfo

  const handleChange = e => {
    const { name, value } = e.target
    setLoginInfo({
      ...loginInfo,
      [name]: value
    })
    console.log(`${name} : ${value}`)
    // alert(`키: ${name}, 밸류: ${value}`)
  }

  const handleSubmit = e => {
    e.preventDefault()
    alert(`전송클릭: ${JSON.stringify({...loginInfo})}`)
    userLogin({...loginInfo})
    .then((res) => {
      console.log(res)
      alert(`${res.data.username}님, 로그인 되었습니다.`)
    })
    .catch(err => {
      alert(`로그인 실패 : ${err}`)
    })
  }


  return(<>
    <h2>Login Form</h2>
    <div className="login">
      <form  onSubmit={handleSubmit} method="GET" name="LoginForm">
        <div className="imgcontainer">
          {/* <img src="https://www.w3schools.com/howto/img_avatar2.png" style={{width:'300px'}} alt="Avatar" className="avatar"/> */}
        </div>

        <div className="container">
          <label laberFor="username"><b>Username</b></label>
          <input type="text" placeholder="Enter Username" name="username" value={username} onChange={handleChange}/>

          <label laberFor="password"><b>Password</b></label>
          <input type="password" placeholder="Enter Password" name="password" value={password} onChange={handleChange}/>
          
          <Button type="submit">Login</Button>
          <label>
            <input type="checkbox" checked="checked" name="remember"/> Remember me
          </label>
        </div>

        <div className="container2" style={{backgroundColor:"#f1f1f1"}}>
          <Button type="button" className="cancelbtn">Cancel</Button>
          <span class="psw">Forgot <a href="/home">password?</a></span>
        </div>
      </form>
    </div>
  </>)
}

export default Login