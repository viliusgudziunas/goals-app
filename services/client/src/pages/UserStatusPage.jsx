import React, { useContext } from 'react';

import UserStatus from '../components/UserStatus';
import NotAllowed from '../components/NotAllowed';
import { GlobalContext } from '../context/GlobalState';

const UserStatusPage = () => {
  const { authenticated } = useContext(GlobalContext);

  if (authenticated) {
    return <UserStatus />;
  }

  return <NotAllowed />;
};

export default UserStatusPage;
