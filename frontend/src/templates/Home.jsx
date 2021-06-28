import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Button } from '@material-ui/core';
// import './Home.css'

const Home = ({children}) => {

//   useEffect(()=>{
//     axios({
//       method: "get",
//       url: "http://127.0.0.1:8000/hello",
//       responseType: "json"
//     }).then(function (response) {
//       alert(response.data.greeting)
//     });
// },[])
  const [connection, setConnection] = useState(false)
  const handleClick = e => {
    e.preventDefault();
    axios({
      method: "get",
      url: "http://127.0.0.1:8000/connection",
      responseType: "json"
    }).then(function (res) {
      // alert(res.data.connection)
      // localStorage.setItem('connection', res.data.connection)
      setConnection(res.data.connection === 'SUCCESS')
    });
  }

  return (<>
    <table className="tab_lay">
      <tr><td><h1>Home</h1></td></tr>
      <tr><td><Button variant="outlined" color="primary" onClick={handleClick}>Server Connection TEST</Button></td></tr>
      <tr><td>{ connection ?
      'Connected':'Not Connected'
      }</td></tr>
    </table>
    {children}
</>)}

export default Home;

// export const Counter = () => {
//   return(<>
//     <h1>Counter</h1>
//   </>)
// }