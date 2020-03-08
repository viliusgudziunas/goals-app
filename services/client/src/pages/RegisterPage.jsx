import React, { useContext } from 'react';
import { Redirect } from 'react-router-dom';

import Form from '../components/Form';
import { GlobalContext } from '../context/GlobalState';

const RegisterPage = () => {
  const { authenticated } = useContext(GlobalContext);
  if (authenticated) {
    return <Redirect to='/' />;
  }

  return <Form formType='Register' />;
};

export default RegisterPage;
