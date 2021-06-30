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
      <li><Link to='/user-delete'>User Delete</Link></li>
    </ol>
  </nav>
);

export const ItemMenu = () => (
  <nav>
    <ol>
      <li><Link to='/item-list'>Item List</Link></li>
      <li><Link to='/item-register'>Item Register</Link></li>
      <li><Link to='/item-retreive'>Item Read</Link></li>
      <li><Link to='/item-detail'>Item Detail</Link></li>
      <li><Link to='/item-update'>Item Update</Link></li>
      <li><Link to='/item-delete'>Item Delete</Link></li>
    </ol>
  </nav>
);

export const BlogMenu = () => (
  <nav>
    <ol>
      <li><Link to='/post-list'>Blog List</Link></li>
      <li><Link to='/post-register'>Blog Write</Link></li>
      <li><Link to='/post-retrieve'>Blog Read</Link></li>
      <li><Link to='/post-update'>Blog Update</Link></li>
      <li><Link to='/post-delete'>Blog Delete</Link></li>
    </ol>
  </nav>
);

export const ArticleMenu = () => (
  <nav>
    <ol>
      <li><Link to='/article-list'>Article List</Link></li>
      <li><Link to='/article-write'>Article Write</Link></li>
      <li><Link to='/article-read'>Article Read</Link></li>
      <li><Link to='/articel-delete'>Article Delete</Link></li>
    </ol>
  </nav>
);

export const PostMenu = () => (
  <nav>
    <ol>
      <li><Link to='/post-list'>Board List</Link></li>
      <li><Link to='/post-register'>Board Write</Link></li>
      <li><Link to='/post-retrieve'>Board Read</Link></li>
      <li><Link to='/post-update'>Board Update</Link></li>
      <li><Link to='/post-delete'>Board Delete</Link></li>
    </ol>
  </nav>
);