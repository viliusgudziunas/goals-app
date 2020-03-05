import React, { useState } from 'react';
import PropTypes from 'prop-types';

const Form = ({ formType }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleFormSubmit = e => {
    e.preventDefault();
    console.log(email);
    console.log(password);
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
            />
          </div>
          <div className='form-group'>
            <input
              name='passowrd'
              type='password'
              className='form-control'
              placeholder='Enter a password'
              id='formPassword'
              value={password}
              onChange={e => setPassword(e.target.value)}
              required
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
