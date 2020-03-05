import React, { useState } from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';

const NavBar = ({ title }) => {
  const [collapsed, setCollapsed] = useState(true);

  return (
    <nav className='navbar navbar-expand-lg navbar-dark bg-dark'>
      <div className='container'>
        <span className='navbar-brand'>{title}</span>
        <button
          aria-controls='responsive-navbar-nav'
          type='button'
          aria-label='Toggle navigation'
          className={collapsed ? 'navbar-toggler collapsed' : 'navbar-toggler'}
          onClick={() => setCollapsed(!collapsed)}
        >
          <span className='navbar-toggler-icon' />
        </button>
        <div
          className={
            collapsed
              ? 'navbar-collapse collapse'
              : 'navbar-collapse collapse show'
          }
        >
          <div className='mr-auto navbar-nav'>
            <Link to='/' data-rb-event-key='/' className='nav-link'>
              Home
            </Link>
            <Link to='/about' data-rb-event-key='/about' className='nav-link'>
              About
            </Link>
            <Link to='/status' data-rb-event-key='/status' className='nav-link'>
              User Status
            </Link>
          </div>
          <div className='navbar-nav'>
            <Link
              className='nav-link'
              to='/register'
              data-rb-event-key='/register'
            >
              Register
            </Link>
            <Link className='nav-link' to='/login' data-rb-event-key='/login'>
              Log In
            </Link>
            <Link className='nav-link' to='/logout' data-rb-event-key='/logout'>
              Log Out
            </Link>
          </div>
        </div>
      </div>
    </nav>
  );
};

NavBar.propTypes = {
  title: PropTypes.string.isRequired
};

export default NavBar;
