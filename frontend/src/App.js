import React from 'react';
import { Redirect, Route, BrowserRouter as Router, Link } from "react-router-dom";
import { Login, Signup, UserDetail, UserList, UserEdit } from 'user/index'
import { Nav } from 'common'
import { Home, User, Item, Blog, Stock } from 'templates'
// import { Counter } from 'counter'
// import { Provider } from 'react-redux';
// import { combineReducers, createStore } from 'redux';
// import { Schedule } from 'todos/containers';

// const rootReducer = combineReducers({todoReducer});

const App = () => {
  return (<div>
    <Router>
      <Nav/>
      {/* <nav style={{width: '500px', margin: '0 auto'}}>
        <ol>
          <li><Link to='/home'>Home</Link></li>
          <li><Link to='/user'>User</Link></li>
          <li><Link to='/item'>Item</Link></li>
          <li><Link to='/blog'>Blog</Link></li>
          <li><Link to='/stock'>Stock</Link></li>
        </ol>
      </nav> */}
      <Route exact path='/home' component={Home}/>
      <Redirect exact from={'/'} to={'/home'}/>
      <Route exact path='/user' component={User}/>
      <Route exact path='/item' component={Item}/>
      <Route exact path='/blog' component={Blog}/>
      <Route exact path='/stock' component={Stock}/>
      <Route exact path='/login-form' component={Login}/>
      <Route exact path='/signup-form' component={Signup}/>
      <Route exact path='/user-detail' component={UserDetail}/>
      <Route exact path='/user-edit' component={UserEdit}/>
      <Route exact path='/user-list' component={UserList}/>
    </Router>
  </div>)
}

export default App