import React, { useState } from 'react';
import { Button } from '@material-ui/core';
import './Signup.css';
// import { InputSharp, SettingsInputSvideo } from '@material-ui/icons';
import { userSignup, userLogin } from 'api/index';
import { useHistory } from 'react-router'

const Signup = () => {
  const history = useHistory()

  const [userInfo, setUserInfo] = useState({
    username: '',
    password: '',
    name: '',
    email: ''
  })

  const { username, password, name, email } = userInfo

  const handleChange = e => {
    const { name, value } = e.target
    setUserInfo({
      ...userInfo,
      [name]: value
    })
    // console.log(...userInfo)
    console.log(e)
    console.log(`${name} : ${value}`)
    // alert(`키: ${name}, 밸류: ${value}`)
  }

  const handleSubmit = e => {
    e.preventDefault()
    alert(`전송클릭: ${JSON.stringify({...userInfo})}`)
    const signupRequest = {...userInfo}
    userSignup(signupRequest)
    .then(res => {
      alert(`회원가입 성공 : ${res.data.result}`)
      // history.push('login')
    })
    .catch(err => {
      alert(`회원가입 실패 : ${err}`)
    })

    const loginRequest = {...userInfo}
    userLogin(loginRequest)
    .then()
    .catch()
  }

  const handleClick = e => {
    e.preventDefault()
    alert(`click btn`)
  }

  // const onChange = e => {
  //   const { name, value } = e.target
  //   const nextInputs = {
  //     ...userInfo,
  //     [name]: value,
  //   }
  //   setUserInfo(nextInputs)
  // }

  return(<>
  <div className="Signup">
    <form onSubmit={handleSubmit} method="get" style={{border:"1px solid #ccc"}} name="SignupForm">
      <div class="container">
        <h1>Sign Up</h1>
        <p>Please fill in this form to create an account.</p>
        <hr/>

        <label for="username"><b>ID</b></label>
        <input type="text" placeholder="Enter ID" onChange={handleChange} name="username" value={username} />
        <br/>
        <label for="psw"><b>Password</b></label>
        <input type="password" placeholder="Enter Password" onChange={handleChange} name="password" value={password} />
        <br/>
        {/* <label for="psw-repeat"><b>Repeat Password</b></label>
        <input type="password" placeholder="Repeat Password" onChange={handleChange} name="psw-repeat" value={psw} />
        <br/> */}
        <label for="username"><b>Name</b></label>
        <input type="text" placeholder="Enter name" onChange={handleChange} name="name" value={name} />
        <br/>
        <label for="email"><b>Email</b></label>
        <input type="text" placeholder="Enter Email" onChange={handleChange} name="email" value={email} />
        <br/>
        {/* <label>
          <input type="checkbox" checked="checked" name="remember" style={{marginBottom:"15px"}}/> Remember me
        </label>--------------------------------------------------- */}
        
        <p>By creating an account you agree to our <a href="/home" style={{color:"dodgerblue"}}>Terms & Privacy</a>.</p>

        <div class="clearfix">
          <Button type="submit" class="signupbtn">Sign Up</Button>
          <Button type="button" class="cancelbtn" onClick={handleClick}>Cancel</Button>
        </div>
      </div>
    </form>
  </div>
  </>)
}

export default Signup