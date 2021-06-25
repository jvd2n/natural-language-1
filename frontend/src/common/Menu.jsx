import React from 'react';
import { Link } from 'react-router-dom'

export const UserMenu = () => (
  <nav>
    <ol>
      <li><Link to='/signup-form'>Sign Up</Link></li>
      <li><Link to='/login-form'>Login</Link></li>
      <li><Link to='/user-list'>User List</Link></li>
      <li><Link to='/user-detail'>User Detail</Link></li>
      <li><Link to='/user-modify'>User Modify</Link></li>
      <li><Link to='/user-remove'>User Remove</Link></li>
    </ol>
  </nav>
);

export const ItemMenu = () => (
  <nav>
    <ol>
      <li><Link to='/item-list'>Item List</Link></li>
      <li><Link to='/item-register'>Item Register</Link></li>
      <li><Link to='/item-detail'>Item Detail</Link></li>
      <li><Link to='/item-remove'>Item Remove</Link></li>
    </ol>
  </nav>
);

export const ArticleMenu = () => (
  <nav>
    <ol>
      <li><Link to='/article-list'>Article List</Link></li>
      <li><Link to='/article-write'>Article Write</Link></li>
      <li><Link to='/article-read'>Articel Read</Link></li>
      <li><Link to='/articel-remove'>Article Remove</Link></li>
    </ol>
  </nav>
);
