import React, { useState } from 'react';
import { Button } from '@material-ui/core';
import './PostWrite.css';
// import { InputSharp, SettingsInputSvideo } from '@material-ui/icons';
import { postRegister } from 'api/index';
import { useHistory } from 'react-router'

const PostWrite = () => {

  const [postInfo, setPostInfo] = useState({
    title: '',
    content: ''
  })

  const { title, content } = postInfo

  const handleChange = e => {
    const { name, value } = e.target
    setPostInfo({
      ...postInfo,
      [name]: value
    })
    // console.log(...userInfo)
    console.log(e)
    console.log(`${name} : ${value}`)
    // alert(`키: ${name}, 밸류: ${value}`)
  }

  const handleSubmit = e => {
    e.preventDefault()
    alert(`전송클릭: ${JSON.stringify({...postInfo})}`)
    // const signupRequest = {...userInfo}
    // userSignup(signupRequest)
    postRegister({...postInfo})
    .then((res) => {
      alert(`${res.data.title}이 업로드 되었습니다.`)
      // history.push('login')
    })
    .catch(err => {
      alert(`게시글 쓰기 실패 : ${err}`)
    })
  }

  return(<>
  <div className="PostWrite">
    <form onSubmit={handleSubmit} method="POST" style={{border:"1px solid #ccc"}} name="PostWriteForm">
      <div class="container">
        <h1>Post Write</h1>
        <p>Please fill in this form to create a post.</p>
        <hr/>

        <label for="title"><b>Title</b></label>
        <input type="text" placeholder="Enter Title" onChange={handleChange} name="title" value={title} />
        <br/>
        <label for="content"><b>Content</b></label>
        <textarea name="content" cols="40" rows="10" placeholder="Enter Content" onChange={handleChange} value={content} />
        <br/>

        <div class="clearfix">
          <Button type="submit" class="signupbtn">Write</Button>
          <Button type="button" class="cancelbtn">Cancel</Button>
        </div>
      </div>
    </form>
  </div>
  </>)
}

export default PostWrite