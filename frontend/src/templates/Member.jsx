import React from 'react';
import { MemberMenu as Menu } from '../common';
import './table.style.css';

const Member = ({children}) => (<>
  <h1>User</h1>
  <Menu/>
  {children}
</>);

export default Member;