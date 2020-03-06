import React, { createContext, useReducer } from 'react';
import PropTypes from 'prop-types';

import AppReducer from './AppReducer';

const initialState = {
  authenticated: false
};

export const GlobalContext = createContext(initialState);

export const GlobalProvider = ({ children }) => {
  const [state, dispatch] = useReducer(AppReducer, initialState);

  function authenticate() {
    dispatch({
      type: 'AUTHENTICATE'
    });
  }

  function logout() {
    dispatch({
      type: 'LOGOUT'
    });
  }

  return (
    <GlobalContext.Provider
      value={{ authenticated: state.authenticated, authenticate, logout }}
    >
      {children}
    </GlobalContext.Provider>
  );
};

GlobalProvider.propTypes = {
  children: PropTypes.node.isRequired
};
