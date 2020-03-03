import React from 'react';
import { Switch, Route } from 'react-router-dom';

import Admin from './components/Admin';
import About from './components/About';
import NavBar from './components/NavBar';

const App = () => {
  return (
    <>
      <NavBar title='Goals App' />
      <Switch>
        <Route exact path='/' component={Admin} />
        <Route exact path='/about' component={About} />
      </Switch>
    </>
  );
};

export default App;
