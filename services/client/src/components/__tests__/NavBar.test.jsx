import React from 'react';
import { shallow } from 'enzyme';
import { MemoryRouter as Router } from 'react-router-dom';

import NavBar from '../NavBar';

const title = 'Test';
const firstLinks = [
  { index: 0, endpoint: '/', link: 'Home' },
  { index: 1, endpoint: '/about', link: 'About' },
  { index: 2, endpoint: '/status', link: 'User Status' }
];
const secondLinks = [
  { index: 0, endpoint: '/register', link: 'Register' },
  { index: 1, endpoint: '/login', link: 'Log In' },
  { index: 2, endpoint: '/logout', link: 'Log Out' }
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

  const navs = wrapper.find('.navbar-nav');
  it('should have two navs', () => {
    expect(navs.length).toBe(2);
  });

  const firstNav = navs.get(0);
  firstLinks.forEach(linkInfo => {
    it(`should have ${linkInfo.endpoint} link on the right, pointing to ${linkInfo.link}`, () => {
      expect(firstNav.props.children[linkInfo.index].props.children).toBe(
        linkInfo.link
      );
      expect(firstNav.props.children[linkInfo.index].props.to).toBe(
        linkInfo.endpoint
      );
    });
  });

  const secondNav = navs.get(1);
  secondLinks.forEach(linkInfo => {
    it(`should have ${linkInfo.endpoint} link on the left, pointing to ${linkInfo.link}`, () => {
      expect(secondNav.props.children[linkInfo.index].props.children).toBe(
        linkInfo.link
      );
      expect(secondNav.props.children[linkInfo.index].props.to).toBe(
        linkInfo.endpoint
      );
    });
  });
});
