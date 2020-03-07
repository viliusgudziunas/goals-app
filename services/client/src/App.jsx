import React from 'react';
import { Switch, Route } from 'react-router-dom';

import NavBar from './components/NavBar';
import Admin from './components/Admin';
import About from './components/About';
import UserStatus from './components/UserStatus';
import Form from './components/Form';
import Logout from './components/Logout';

import { GlobalProvider } from './context/GlobalState';

const App = () => {
  return (
    <GlobalProvider>
      <NavBar title='Goals App' />
      <Switch>
        <Route exact path='/' component={Admin} />
        <Route exact path='/about' component={About} />
        <Route exact path='/status' component={UserStatus} />
        <Route
          exact
          path='/register'
          render={() => <Form formType='Register' />}
        />
        <Route exact path='/login' render={() => <Form formType='Login' />} />
        <Route exact path='/logout' component={Logout} />
      </Switch>
    </GlobalProvider>
  );
};

export default App;
