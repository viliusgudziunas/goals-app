import React from 'react';
import { Switch, Route } from 'react-router-dom';

import NavBar from './components/NavBar';
import UsersList from './components/UsersList';
import About from './components/About';
import UserStatusPage from './pages/UserStatusPage';
import RegisterPage from './pages/RegisterPage';
import LoginPage from './pages/LoginPage';
import Logout from './components/Logout';

import { GlobalProvider } from './context/GlobalState';

const App = () => {
  return (
    <GlobalProvider>
      <NavBar title='Goals App' />
      <Switch>
        <Route exact path='/' component={UsersList} />
        <Route exact path='/about' component={About} />
        <Route exact path='/status' component={UserStatusPage} />
        <Route exact path='/register' component={RegisterPage} />
        <Route exact path='/login' component={LoginPage} />
        <Route exact path='/logout' component={Logout} />
      </Switch>
    </GlobalProvider>
  );
};

export default App;
