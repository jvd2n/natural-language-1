import React from 'react';
import { Link } from 'react-router-dom';
import './Nav.css'

const Nav = () => (<>
  <nav>
    <ol>
      <li><Link to='/home'>Home</Link></li>
      <li><Link to='/counter'>Counter</Link></li>
      <li><Link to='/todos'>Todos</Link></li>
      <li><Link to='/user'>User</Link></li>
      <li><Link to='/item'>Item</Link></li>
    </ol>
  </nav>
</>);

export default Nav;