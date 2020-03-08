import React from 'react';
import { Link } from 'react-router-dom';

const NotAllowed = () => {
  return (
    <div className='container'>
      <br />
      <h1>Not Allowed</h1>
      <hr />
      <p>
        You must be logged in to view this. Click <Link to='/login'>here</Link>{' '}
        to log back in.
      </p>
    </div>
  );
};

export default NotAllowed;
