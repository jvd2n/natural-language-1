import React from 'react';
import './Login.css';

const Login = () => {
  return(<>
    <h2>Login Form</h2>
    <div className="login">
      <form action="/" method="post">
        <div className="imgcontainer">
          <img src="https://www.w3schools.com/howto/img_avatar2.png" style={{width:'300px'}} alt="Avatar" className="avatar"/>
        </div>

        <div className="container">
          <label laberFor="uname"><b>Username</b></label>
          <input type="text" placeholder="Enter Username" name="uname" required/>

          <label laberFor="psw"><b>Password</b></label>
          <input type="password" placeholder="Enter Password" name="psw" required/>
          
          <button type="submit">Login</button>
          <label>
            <input type="checkbox" checked="checked" name="remember"/> Remember me
          </label>
        </div>

        <div className="container2" style={{backgroundColor:"#f1f1f1"}}>
          <button type="button" className="cancelbtn">Cancel</button>
          <span class="psw">Forgot <a href="/home">password?</a></span>
        </div>
      </form>
    </div>
  </>)
}

export default Login