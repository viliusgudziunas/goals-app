import React, { useEffect, useState } from 'react';
import axios from 'axios';

import './styles/UserStatus.css';

const UserStatus = () => {
  const [id, setId] = useState(null);
  const [email, setEmail] = useState('');
  const [active, setActive] = useState('');
  const [admin, setAdmin] = useState('');

  useEffect(() => {
    const options = {
      url: `${process.env.REACT_APP_USERS_SERVICE_URL}/auth/status`,
      method: 'get',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${window.localStorage.authToken}`
      }
    };
    axios(options)
      .then(res => {
        setId(res.data.data.id);
        setEmail(res.data.data.email);
        setActive(String(res.data.data.active));
        setAdmin(String(res.data.data.admin));
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  return (
    <div className='container'>
      <br />
      <h1>User Status</h1>
      <hr />
      <div className='row'>
        <div className='list-group'>
          <div className='list-group-item'>
            <strong>{'User ID: '}</strong>
            {id}
          </div>
          <div className='list-group-item'>
            <strong>{'Email: '}</strong>
            {email}
          </div>
          <div className='list-group-item'>
            <strong>{'Active: '}</strong>
            {active}
          </div>
          <div className='list-group-item'>
            <strong>{'Admin: '}</strong>
            {admin}
          </div>
        </div>
      </div>
    </div>
  );
};

export default UserStatus;
