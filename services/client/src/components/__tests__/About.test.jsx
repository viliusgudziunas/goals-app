import React from 'react';
import { shallow } from 'enzyme';

import About from '../About';

describe('<About />', () => {
  const wrapper = shallow(<About />);
  it('should match the snapshot', () => {
    expect(wrapper.html()).toMatchSnapshot();
  });

  it('should have a header', () => {
    expect(wrapper.find('h1').length).toBe(1);
    expect(wrapper.find('h1').text()).toBe('About');
  });

  it('should have a paragraph', () => {
    expect(wrapper.find('p').length).toBe(1);
    expect(wrapper.find('p').text()).toBe('Add something relevant here');
  });
});
