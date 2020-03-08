import React, { useEffect, useContext } from 'react';
import { Link } from 'react-router-dom';

import { GlobalContext } from '../context/GlobalState';

const Logout = () => {
  const { logout } = useContext(GlobalContext);

  useEffect(() => {
    window.localStorage.clear();
    logout();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <div className='container'>
      <br />
      <h1>Logged Out</h1>
      <hr />
      <p>
        You are now logged out. Click <Link to='/login'>here</Link> to log back
        in.
      </p>
    </div>
  );
};

export default Logout;
