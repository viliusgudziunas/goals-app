import React from 'react';
import { Switch, Route } from 'react-router-dom';

import Admin from './components/Admin';
import About from './components/About';
import NavBar from './components/NavBar';
import Form from './components/Form';

const App = () => {
  return (
    <>
      <NavBar title='Goals App' />
      <Switch>
        <Route exact path='/' component={Admin} />
        <Route exact path='/about' component={About} />
        <Route
          exact
          path='/register'
          render={() => <Form formType='Register' />}
        />
        <Route exact path='/login' render={() => <Form formType='Login' />} />
      </Switch>
    </>
  );
};

export default App;
