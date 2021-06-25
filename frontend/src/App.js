import React from 'react';
import { Redirect, Route, BrowserRouter as Router } from "react-router-dom";
import { Login, Signup, UserDetail, UserList, UserEdit } from 'user/index'
import { Nav } from 'common'
import { Home, User } from 'templates'
// import { Counter } from 'counter'
// import { Provider } from 'react-redux';
// import { combineReducers, createStore } from 'redux';
// import { Schedule } from 'todos/containers';

// const rootReducer = combineReducers({todoReducer});

const App = () => {
  return (<div>
    <Router>
        <Nav/>
        <Route exact path='/home' component={Home}/>
        <Redirect exact from={'/'} to={'/home'}/>
        <Route exact path='/user' component={User}/>
        <Route exact path='/login-form' component={Login}/>
        <Route exact path='/signup-form' component={Signup}/>
        <Route exact path='/user-detail' component={UserDetail}/>
        <Route exact path='/user-edit' component={UserEdit}/>
        <Route exact path='/user-list' component={UserList}/>
    </Router>
  </div>)
}

export default App