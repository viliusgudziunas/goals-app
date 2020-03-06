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
  it('should have a logged out message', () => {
    expect(wrapper.find('p').length).toBe(1);
    expect(wrapper.find('p').get(0).props.children[0]).toContain(
      'You are now logged out.'
    );
  });
});
