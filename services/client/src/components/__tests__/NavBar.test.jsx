import React from 'react';
import { shallow } from 'enzyme';
import { MemoryRouter as Router } from 'react-router-dom';

import NavBar from '../NavBar';

const title = 'Test';
const theLinks = [
  { index: 0, endpoint: '/', link: 'Home' },
  { index: 1, endpoint: '/about', link: 'About' },
  { index: 2, endpoint: '/register', link: 'Register' },
  { index: 3, endpoint: '/login', link: 'Log In' }
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

  it('should have two navs', () => {
    expect(wrapper.find('.navbar-nav').length).toBe(2);
  });

  const links = wrapper.find('Link');
  it('should have four links', () => {
    expect(links.length).toBe(4);
  });

  theLinks.forEach(linkInfo => {
    it(`should have a link to ${linkInfo.link}`, () => {
      expect(links.get(linkInfo.index).props.to).toBe(linkInfo.endpoint);
      expect(links.get(linkInfo.index).props.children).toBe(linkInfo.link);
    });
  });
});
