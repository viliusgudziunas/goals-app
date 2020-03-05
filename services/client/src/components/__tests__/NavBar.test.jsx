import React from 'react';
import { shallow } from 'enzyme';
import { MemoryRouter as Router } from 'react-router-dom';

import NavBar from '../NavBar';

const title = 'Test';
const firstLinks = [
  [0, '/', 'Home'],
  [1, '/about', 'About'],
  [2, '/status', 'User Status']
];
const secondLinks = [
  [0, '/register', 'Register'],
  [1, '/login', 'Log In'],
  [2, '/logout', 'Log Out']
];

describe('<NavBar />', () => {
  it('should match the snapshot', () => {
    const wrapper = shallow(
      <Router location='/'>
        <NavBar title={title} />
      </Router>
    );
    expect(wrapper.html()).toMatchSnapshot();
  });

  const wrapper = shallow(<NavBar title={title} />);
  it('should have a title', () => {
    expect(wrapper.find('span').get(0).props.children).toBe(title);
  });

  const firstNav = wrapper.find('.navbar-nav').get(0);
  test.each(firstLinks, (index, endpoint, link) => {
    it(`should have ${link} link on the right, pointing to ${endpoint}`, () => {
      expect(firstNav.props.children[index].props.children).toBe(link);
      expect(firstNav.props.children[index].props.to).toBe(endpoint);
    });
  });

  const secondNav = wrapper.find('.navbar-nav').get(1);
  test.each(secondLinks, (index, endpoint, link) => {
    it(`should have ${link} link on the left, pointing to ${endpoint}`, () => {
      expect(secondNav.props.children[index].props.children).toBe(link);
      expect(secondNav.props.children[index].props.to).toBe(endpoint);
    });
  });
});
