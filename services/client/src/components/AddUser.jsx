import React, { useState } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';

const AddUser = ({ pingFetchUsers, setPingFetchUsers }) => {
  const [email, setEmail] = useState('');

  const handleFormSubmit = e => {
    e.preventDefault();
    const data = { email };
    axios
      .post(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`, data)
      .then(() => {
        setPingFetchUsers(!pingFetchUsers);
        setEmail('');
      })
      .catch(err => {
        console.log(err);
      });
  };

  return (
    <div className='row'>
      <form className='col-md-4' onSubmit={handleFormSubmit}>
        <div className='form-group'>
          <input
            type='email'
            className='form-control'
            placeholder='Enter an email address'
            id='formEmail'
            value={email}
            onChange={e => setEmail(e.target.value)}
            required
          />
        </div>
        <button type='submit' className='btn btn-success btn-block'>
          Submit
        </button>
      </form>
    </div>
  );
};

AddUser.propTypes = {
  pingFetchUsers: PropTypes.bool.isRequired,
  setPingFetchUsers: PropTypes.func.isRequired
};

export default AddUser;
