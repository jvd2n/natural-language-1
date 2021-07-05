import React from 'react';
import { ItemMenu as Menu } from '../common';
import './table.style.css';
import { Nav } from 'common'

const Item = ({children}) => (<>
  <Nav/>
  <h1>Item</h1>
  <Menu/>
  {children}
</>);

export default Item;