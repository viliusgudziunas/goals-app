import React, { useEffect, useState } from 'react';
import axios from 'axios';

import './styles/UserStatus.css';

const UserStatus = () => {
  const [id, setId] = useState(null);
  const [email, setEmail] = useState('');

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
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  return (
    <>
      <div className='container'>
        <br />
        <h1>User Status</h1>
        <hr />
        <div className='row'>
          <div className='list-group'>
            <div className='list-group-item user-status-list-item'>
              <strong>{'User ID: '}</strong>
              {id}
            </div>
            <div className='list-group-item user-status-list-item'>
              <strong>{'Email: '}</strong>
              {email}
            </div>
          </div>
        </div>
      </div>
      <br />
      <br />
    </>
  );
};

export default UserStatus;
