import React, { useState, useEffect } from 'react';
import axios from 'axios';

import UsersList from './UsersList';
import AddUser from './AddUser';

const Admin = () => {
  const [users, setUsers] = useState([]);
  const [pingFetchUsers, setPingFetchUsers] = useState(true);

  useEffect(() => {
    axios
      .get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
      .then(res => {
        setUsers(res.data.data);
      })
      .catch(err => {
        console.log(err);
      });
  }, [pingFetchUsers]);

  return (
    <div className='container'>
      <br />
      <h1>All Users</h1>
      <hr />
      <AddUser
        pingFetchUsers={pingFetchUsers}
        setPingFetchUsers={setPingFetchUsers}
      />
      <hr />
      <UsersList users={users} />
    </div>
  );
};

export default Admin;
