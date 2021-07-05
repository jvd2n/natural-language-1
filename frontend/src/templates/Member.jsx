import React from 'react';
import { MemberMenu as Menu } from '../common';
import './table.style.css';
import { Nav } from 'common'

const Member = ({children}) => (<>
  <Nav/>
  <h1>User</h1>
  <Menu/>
  {children}
</>);

export default Member;