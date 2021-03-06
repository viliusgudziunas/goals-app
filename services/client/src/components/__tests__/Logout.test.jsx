import React from 'react';
import { shallow } from 'enzyme';
import { MemoryRouter as Router } from 'react-router-dom';

import Logout from '../Logout';

describe('<Logout />', () => {
  it('should match the snapshot', () => {
    const wrapper = shallow(
      <Router location='/'>
        <Logout />
      </Router>
    );
    expect(wrapper.html()).toMatchSnapshot();
  });

  const wrapper = shallow(<Logout />);
  it('should have a header', () => {
    expect(wrapper.find('h1').length).toBe(1);
    expect(wrapper.find('h1').text()).toBe('Logged Out');
  });

  it('should have a logged out message', () => {
    expect(wrapper.find('p').length).toBe(1);
    expect(wrapper.find('p').text()).toContain('You are now logged out.');
  });

  it('should have a link to login page', () => {
    expect(wrapper.find('Link').length).toBe(1);
    expect(wrapper.find('Link').prop('to')).toBe('/login');
  });
});
