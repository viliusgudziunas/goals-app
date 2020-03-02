import React from 'react';
import { Switch, Route } from 'react-router-dom';

import Admin from './Admin';
import About from './About';

const App = () => {
  return (
    <Switch>
      <Route exact path='/' component={Admin} />
      <Route exact path='/about' component={About} />
    </Switch>
  );
};

export default App;
