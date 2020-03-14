import React, { useState, useEffect, useContext } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';

import { GlobalContext } from '../context/GlobalState';

const Form = ({ formType }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const clearForm = () => {
    setEmail('');
    setPassword('');
  };

  useEffect(() => {
    clearForm();
  }, [formType]);

  const { authenticate } = useContext(GlobalContext);
  const handleFormSubmit = e => {
    e.preventDefault();
    const data = { email, password };
    axios
      .post(
        `${
          process.env.REACT_APP_USERS_SERVICE_URL
        }/auth/${formType.toLowerCase()}`,
        data
      )
      .then(res => {
        clearForm();
        window.localStorage.setItem('authToken', res.data.auth_token);
        authenticate();
      })
      .catch(err => {
        console.log(err);
      });
  };

  return (
    <div className='container'>
      <br />
      {formType === 'Login' && <h1>Log In</h1>}
      {formType === 'Register' && <h1>Register</h1>}
      <hr />
      <div className='row'>
        <form className='col-md-4' onSubmit={handleFormSubmit}>
          <div className='form-group'>
            <input
              name='email'
              type='email'
              className='form-control'
              placeholder='Enter an email address'
              id='formEmail'
              value={email}
              onChange={e => setEmail(e.target.value)}
              required
              minLength='6'
            />
          </div>
          <div className='form-group'>
            <input
              name='password'
              type='password'
              className='form-control'
              placeholder='Enter a password'
              id='formPassword'
              value={password}
              onChange={e => setPassword(e.target.value)}
              required
              minLength='4'
            />
          </div>
          <button type='submit' className='btn btn-success btn-block'>
            Submit
          </button>
        </form>
      </div>
    </div>
  );
};

Form.propTypes = {
  formType: PropTypes.string.isRequired
};

export default Form;
