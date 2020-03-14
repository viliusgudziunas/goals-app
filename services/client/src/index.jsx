import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router } from 'react-router-dom';

import { GlobalProvider } from './context/GlobalState';

import App from './App';

ReactDOM.render(
  <GlobalProvider>
    <Router>
      <App />
    </Router>
  </GlobalProvider>,
  document.getElementById('root')
);
