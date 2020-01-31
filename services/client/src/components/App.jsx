import React, { useState, useEffect } from 'react';
import axios from 'axios';
import UsersList from './UsersList';
import AddUser from './AddUser';

const App = () => {
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
      <div className='row'>
        <div className='column'>
          <UsersList users={users} />
        </div>
      </div>
    </div>
  );
};

export default App;
