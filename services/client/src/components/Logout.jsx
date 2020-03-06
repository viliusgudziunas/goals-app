import React, { useEffect, useContext } from 'react';
import { Link } from 'react-router-dom';

import { GlobalContext } from '../context/GlobalState';

const Logout = () => {
  const { logout } = useContext(GlobalContext);
  const logoutUser = () => {
    window.localStorage.clear();
    logout();
  };

  useEffect(() => {
    logoutUser();
  }, []);

  return (
    <div className='container'>
      <br />
      <p>
        You are now logged out. Click <Link to='/login'>here</Link> to log back
        in
      </p>
    </div>
  );
};

export default Logout;
