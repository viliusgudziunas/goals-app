import React from 'react';
import { shallow } from 'enzyme';
import { MemoryRouter as Router } from 'react-router-dom';

import NotAllowed from '../NotAllowed';

describe('<NotAllowed />', () => {
  it('should match the snapshot', () => {
    const wrapper = shallow(
      <Router location='/'>
        <NotAllowed />
      </Router>
    );
    expect(wrapper.html()).toMatchSnapshot();
  });

  const wrapper = shallow(<NotAllowed />);
  it('should have a header', () => {
    expect(wrapper.find('h1').length).toBe(1);
    expect(wrapper.find('h1').text()).toBe('Not Allowed');
  });

  it('should have a not allowed message', () => {
    expect(wrapper.find('p').length).toBe(1);
    expect(wrapper.find('p').text()).toContain(
      'You must be logged in to view this.'
    );
  });

  it('should have a link to login page', () => {
    expect(wrapper.find('Link').length).toBe(1);
    expect(wrapper.find('Link').prop('to')).toBe('/login');
  });
});
